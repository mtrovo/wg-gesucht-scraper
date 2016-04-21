import requests
from pyquery import PyQuery as pq
from collections import namedtuple

class Offer(object):
    pass

lastid=''
try:
    with open('lastid.tmp', 'r') as f:
        lastid = f.read().strip()
except:
    pass

resp = requests.get('http://www.wg-gesucht.de/wohnungen-in-Berlin.8.2.0.0.html')
d = pq(resp.text)
trs = d('#table-compact-list tr').not_('.inlistTeaser')[2:]
ids = [tr.attrib['adid'] for tr in trs]

try:
    lastpos = ids.index(lastid)
except:
    lastpos = len(ids)
if lastpos == 0:
    exit(1)
else:
    trs = trs[:lastpos]
    ids = ids[:lastpos]

def parse_tr(tr):
    tds = [td.text_content().strip() for td in e.findall('td')][2:]
    tds.append('http://wg-gesucht.de/' + tr.attrib['adid'])
    return tds

data = [parse_tr(e) for e in trs]
print '\n'.join('\t'.join(e) for e in data).encode('utf-8')
open('lastid.tmp', 'w').write(ids[0])
