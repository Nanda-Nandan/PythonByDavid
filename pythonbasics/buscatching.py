import urllib.request
import sys
print("command options",sys.argv)#argv contains all the inputs passed through command line
#raise SystemExit(0) to stop the execution explicitily
if len(sys.argv)!=3:
    raise SystemExit('usage pass desired inputs')
routeno=sys.argv[1]
stopid=sys.argv[2]
u=urllib.request.urlopen('http://ctabustracker.com//bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(stopid,routeno))
data=u.read()
from xml.etree.ElementTree import XML
doc=XML(data)
#launch debugger in code
#import pdb;pdb.set_trace()
for pt in doc.findall('.//pt'):
    print(pt.text)

