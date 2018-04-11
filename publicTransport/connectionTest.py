import urllib2
import urllib
from bs4 import BeautifulSoup
 
data = {}
  
data['v1'] = 'li156r53hcghvcrp5n62dvsbp2'
data['v2'] = '7f5f402783cd0a4da01418687c3d32df'
data['pwd'] = 'd41d8cd98f00b204e9800998ecf8427e'
data['cmd'] = 'time_table'
data['prefix'] = 'sch_tt'
data['mobile'] = '0'
data['lcid'] = 'en-US'
data['uid'] = '104897'
data['schedule_index'] = 0
#data['transit_system'] = ""
#data['system_state'] = ""
data['transit_system'] = "Ulster County Area Transit"
data['system_state'] = "New York"
   
url_values = urllib.urlencode(data)
print url_values
    
base_url = "https://rideschedules.com/cgi-bin/ws_get_schedule2.pl"
full_url = base_url + "?" + url_values
     
response = urllib2.urlopen(full_url)
html = response.read()
      
soup = BeautifulSoup(html,'html5lib')
print(soup.prettify())
