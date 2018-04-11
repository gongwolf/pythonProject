import urllib2
import urllib
from bs4 import BeautifulSoup
import googlemaps

v1 = "";
v2 = "";
pwd = "";
system = "Metro - Los Angeles (Bus)"
state = "New York"
def getTransLineList(SystemId):
    global v1,v2,pwd,system,state
    base_url = "https://rideschedules.com/cgi-bin/get_index_result2.pl"
    data = {}
    data['v1'] = v1
    data['v2'] = v2
    data['pwd'] = pwd 
    data['cmd'] = 'lines'
    data['mobile'] = '0'
    data['lcid'] = 'en-US'
    data['uid'] = SystemId
    data['transit_system'] = system
    data['system_state'] = state
   
    url_values = urllib.urlencode(data)
    full_url = base_url + "?" + url_values
    #print full_url
    response = urllib2.urlopen(full_url)
    html = response.read()

    soup = BeautifulSoup(html,'html5lib')

    linesDiv = soup.find("div", class_="sec").find("div",class_="lines_panel").find_all("div")
    #print len(linesDiv)
    linesList = {}
    for div in linesDiv:
        html_lines = div.find_all("a")
        for line in html_lines:
            href = line.attrs["href"]
            lineId = href[href.find("?")+1:]
            line_abr = str(line.contents[0].contents[0])
            line_name = str(line.contents[1][:-1])
            print line_abr+" : "+ line_name+" "+lineId
            linesList[lineId] = [line_name,line_abr]
    #print soup
    return linesList

def getLineInfo(lineId):
    global v1,v2,pwd
    base_url = "https://rideschedules.com/cgi-bin/ws_get_schedule2.pl"
    data = {}
    data['v1'] = v1
    data['v2'] = v2
    data['pwd'] = pwd 
    data['cmd'] = 'time_table'
    data['prefix'] = 'sch_tt'
    data['mobile'] = '0'
    data['lcid'] = 'en-US'
    data['uid'] = lineId
    data['schedule_index'] = 0
    data['transit_system'] = system
    data['system_state'] = state
   
    url_values = urllib.urlencode(data)
    full_url = base_url + "?" + url_values
    print full_url
    response = urllib2.urlopen(full_url)
    html = response.read()
    
    soup = BeautifulSoup(html,'html5lib')
    print soup
    return 

def getTransSystemList(stateId):
    global v1,v2,pwd
    base_url = "https://rideschedules.com/cgi-bin/get_index_result2.pl"
    data = {}
    data['v1'] = v1
    data['v2'] = v2
    data['pwd'] = pwd 
    data['cmd'] = 'systems'
    #data['prefix'] = 'sch_tt'
    data['mobile'] = '0'
    data['lcid'] = 'en-US'
    data['uid'] = stateId
    #data['schedule_index'] = 1
    data['transit_system'] = "Metro - Los Angeles (Bus)"
    data['system_state'] = "California"
   
    url_values = urllib.urlencode(data)
    full_url = base_url + "?" + url_values
    #print full_url
    response = urllib2.urlopen(full_url)
    html = response.read()
    
    soup = BeautifulSoup(html,'html5lib')
    companyList = soup.select(".index")
    companyList = companyList[0].find_all('li')
    systemList={}
    for list in companyList:
        abr = str(list.contents[0].contents[0])
        #title = str(list.find_all("a")[0].attrs["title"])
        #lineId = str(list.find_all("a")[0].attrs["onclick"].split(",")[1][:-1])
        #print abr +" ## "+title +" ## "+lineId
        attrs = list.find_all("a")[0].attrs
        title = ""
        systemId = ""
        
        if "title" in attrs:
            title = str(attrs["title"])
        systemId = str(attrs["onclick"].split(",")[1][:-1])
        systemList[abr] = [title,systemId]
    return systemList

def getStatesInfo():
    global v1,v2,pwd
    starUrl = "https://rideschedules.com/"
    response = urllib2.urlopen(starUrl)
    starPage_html = response.read()
    soup = BeautifulSoup(starPage_html, 'html5lib')
    v1 = soup.select("#span_v1")[0].string
    v2 = soup.select("#span_v2")[0].string
    pwd = soup.select("#span_pwd")[0].string
 
    regions_list = soup.select("#idx_regions ")
    regions_list =  regions_list[0].find_all("ul",class_="index")[0].find_all("li")
    stateList = {}
    for list in regions_list:
        stateName = str(list.contents[0].contents[0])
        stateId = str(list.find_all("a")[0].attrs["onclick"].split(",")[1][:-1])
        stateList[stateName] = stateId;
    return stateList

stateList = getStatesInfo();
print "v1 : " + v1
print "v2 : " + v2
print "pwd : " + pwd
#print stateList
#print len(stateList)

for statekey in stateList:
    if statekey in ["New York"]:
        print statekey + ":" + stateList[statekey]
        systemList = getTransSystemList(stateList[statekey])
        print len(systemList)
        for syskey in systemList:
            systemId = systemList[syskey][1]
            system_i = systemList[syskey][0]
            state = statekey
            if system_i ==  "":
                system = syskey
            else :
                system = system_i
            
            #print state +": " + system 
            #print syskey +" :"+ systemList[syskey][0] +"---" +systemList[syskey][1] 
            if syskey in ["UCAT"]:
                linesList = getTransLineList(systemId)
                for lineId in linesList:
                    getLineInfo(lineId)
            #    #if systemList[syskey][0] is not "":
            #    #    global state, system
            #    #    state = statekey
            #    #    system = systemList[syskey][0] 
