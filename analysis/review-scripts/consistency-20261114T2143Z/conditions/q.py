import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-ubl-examples/3a42b48a-1edc-5b37-938f-a9af42fda1cf/scratchpad/consistency-20261114T2143Z/conditions')
from lib import *
from lxml import etree
# usage: q.py file xpath [xpath...]
f=sys.argv[1]
t=etree.parse('/home/user/ubl-examples/world/examples/'+f)
for xp in sys.argv[2:]:
    for e in t.getroot().xpath(xp,namespaces=NS):
        print('- `%s:%s` = `%s`'%(f,cpath(t,e),(e.text or '').strip()))
