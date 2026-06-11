#!/usr/bin/env python3
"""
aiai-pulse extractor — Concept 7: The Machine, Live.

Reads Luna's Daily Reports (HTML) and emits pulse.json + pulse.js containing
ONLY allowlisted numbers, timestamps and fixed labels. No free text from any
report can pass through: every field is produced by a specific regex that
captures digits, or by counting files/emoji, or is a hardcoded label.

Safety layers:
  1. Allowlist schema — there is no code path that copies a sentence.
  2. Deny-scan over the OUTPUT — emails, account-ID shapes, IPs, paths,
     ports, and a configurable name/project list. Any hit -> refuse to write,
     keep the previous good file, exit 1.
  3. Schema version stamped in the output for review.

Run:  python3 extract_pulse.py            (writes pulse.json + pulse.js here)
      python3 extract_pulse.py --dry-run  (prints, writes nothing)
"""
import re, os, sys, json, glob, html, datetime

LUNA_DIR = os.path.expanduser('~/Desktop/Luna Daily Reports')
OUT_DIR  = os.path.dirname(os.path.abspath(__file__))

# ---- deny list: patterns that must NEVER appear in the output ----------------
DENY_PATTERNS = [
    (r'[\w.+-]+@[\w-]+\.\w+',                 'email address'),
    (r'\b[0-9A-F]{6}-[0-9A-F]{6}-[0-9A-F]{6}\b', 'account-id shape'),
    (r'\b(?:\d{1,3}\.){3}\d{1,3}\b',          'IP address'),
    (r'/Users/|/Volumes/|~/',                 'filesystem path'),
    (r'\bport\s*\d+|\b0\.0\.0\.0\b|\blocalhost:\d+', 'network endpoint'),
    (r'LOGIN_ERROR|password|secret|token|api[_-]?key', 'credential-ish term'),
]
# names / projects / vendors that must never leak (extend freely)
DENY_NAMES = ['whitfield', 'shooter', 'tony', 'comit', 'jw golf', 'gcp', 'google cloud',
              'supabase', 'solar', 'beechat', 'beelinks', 'topcon', 'midwich', 'dji',
              'hmrc', 'aviva', 'barclays', 'ionos', 'formspree', 'm4', 'mac mini']

def strip_html(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', t, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

def latest(pattern):
    fs = sorted(glob.glob(os.path.join(LUNA_DIR, pattern)))
    return fs[-1] if fs else None

def grab(pattern, t):
    m = re.search(pattern, t, re.I)
    return int(m.group(1)) if m else None

def build():
    now = datetime.datetime.now()
    pulse = {
        'schema': 'aiai-pulse v1 — allowlisted numbers, timestamps, fixed labels only',
        'generated': now.isoformat(timespec='seconds'),
        'generated_day': now.strftime('%A'),
        'fields': {},
    }

    mb = latest('luna-morning-brief-*.html')
    if mb:
        t = strip_html(mb)
        d = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(mb)).group(1)
        pulse['fields']['brief'] = {
            'date': d,
            'overnight_emails': grab(r'(\d+)\s*Overnight Emails', t),
            'pending_actions':  grab(r'(\d+)\s*Pending Actions', t),
            'critical_items':   grab(r'(\d+)\s*Critical Items', t),
            'active_research':  grab(r'(\d+)\s*Active Research', t),
        }

    er = latest('luna-evening-recap-*.html')
    if er:
        t = strip_html(er)
        d = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(er)).group(1)
        pulse['fields']['recap'] = {
            'date': d,
            'emails_processed': grab(r'(\d+)\s*Emails Processed', t),
            'critical':         grab(r'(\d+)\s*Critical\b', t),
            'action_items':     grab(r'(\d+)\s*Action Items', t),
            'info_low':         grab(r'(\d+)\s*Info / Low', t),
            'wins_logged':      min(12, len(re.findall(r'\b(resolved|fixed|completed|confirmed|deployed)\b', t, re.I))),
        }

    hc = latest('luna-health-check-*.html')
    if hc:
        t = strip_html(hc)
        d = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(hc)).group(1)
        pulse['fields']['health'] = {
            'date': d,
            'checks_green': t.count('✅'),
            'checks_amber': t.count('⚠️'),
            'checks_red':   t.count('🔴'),
        }

    # cadence proof: counts + filing times per report type, last 7 days
    week, by_day = {}, {}
    for f in glob.glob(os.path.join(LUNA_DIR, '*.html')):
        mt = datetime.datetime.fromtimestamp(os.path.getmtime(f))
        if (now - mt).days <= 7:
            kind = re.sub(r'-\d{4}-\d{2}-\d{2}\.html$', '', os.path.basename(f))
            week.setdefault(kind, []).append(mt)
            by_day[mt.strftime('%a')] = by_day.get(mt.strftime('%a'), 0) + 1
    pulse['fields']['filed_last_7_days'] = {
        k: {'count': len(v), 'times': [m.strftime('%a %H:%M') for m in sorted(v)]}
        for k, v in sorted(week.items())
    }
    pulse['fields']['reports_by_day'] = {d: by_day.get(d, 0)
        for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']}
    pulse['fields']['reports_this_week'] = sum(by_day.values())
    return pulse

def deny_scan(out_text):
    hits = []
    for pat, why in DENY_PATTERNS:
        if re.search(pat, out_text, re.I):
            hits.append(why)
    low = out_text.lower()
    hits += [f'denied name: {n}' for n in DENY_NAMES if n in low]
    return hits

def main():
    dry = '--dry-run' in sys.argv
    pulse = build()
    out = json.dumps(pulse, indent=1)
    hits = deny_scan(out)
    if hits:
        sys.stderr.write('REFUSING TO WRITE — deny-scan hits: %s\n' % ', '.join(hits))
        sys.stderr.write('Previous pulse.json (if any) left untouched.\n')
        sys.exit(1)
    print(out)
    print('\ndeny-scan: CLEAN', file=sys.stderr)
    if not dry:
        open(os.path.join(OUT_DIR, 'pulse.json'), 'w').write(out + '\n')
        open(os.path.join(OUT_DIR, 'pulse.js'), 'w').write(
            '/* generated by extract_pulse.py — allowlisted data only */\n'
            'window.AIAI_PULSE = ' + out + ';\n')
        print('wrote pulse.json + pulse.js', file=sys.stderr)

if __name__ == '__main__':
    main()
