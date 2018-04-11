import urllib3
import urllib
import requests
from bs4 import BeautifulSoup
import re
from time import sleep 
import random 

s=requests.Session()
v1 = "";
v2 = "";
pwd = "";
system = "Metro - Los Angeles (Bus)"
state = "New York"


def tras2asc(str):
    #new_str = re.sub(u"(\u2018|\u2013|\u2019|\xf1)", " ",str)
    new_str = str.encode("ascii","ignore")
    return new_str 

def getTransLineList(SystemId):
    global v1,v2,pwd,system,state,s
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
    #response = urllib2.urlopen(full_url)
    html = s.get(full_url).text

    soup = BeautifulSoup(html,'html5lib')

    linesDiv = soup.find("div", class_="sec").find("div",class_="lines_panel").find_all("div")
    #print linesDiv
    linesList = {}
    for div in linesDiv:
        html_lines = div.find_all("a")
        for line in html_lines:
            href = line.attrs["href"]
            lineId = href[href.find("?")+1:]
            
            #print line.contents

            if len(line.contents) > 1 :
                line_name = tras2asc(line.contents[0].contents[0])
                line_desc = tras2asc(line.contents[1][:-1])
            else :
                line_desc = ""
                line_name = tras2asc(line.contents[0].contents[0])
            if line_desc.startswith(" - "):
                line_desc = line_desc[3:]
            if line_name.startswith(" - "):
                line_name = line_name[3:]
            #print lineId +" : "+ line_name+"##"+line_desc
            linesList[lineId] = [line_name,line_desc]
    #print soup
    return linesList

def getLineInfo(lineId):
    global v1,pwd,s
    base_url = "https://rideschedules.com/cgi-bin/ws_get_schedule2.pl"
    data = {}
    data['v1'] = v1
    data['pwd'] = pwd 
    data['cmd'] = 'time_table'
    data['prefix'] = 'sch_tt'
    data['mobile'] = '0'
    data['lcid'] = 'en-US'
    data['uid'] = lineId
    data['schedule_index'] = 0
    data['transit_system'] = system
    data['system_state'] = state
   
    schedule_url = "https://rideschedules.com/schedule.html?"+str(lineId)
    # print schedule_url
    html = s.get(schedule_url).text    
    soup = BeautifulSoup(html,'html5lib')
    v2 = soup.select("#span_v2")[0].string
    stops_info = soup.find_all("script")[1].text
    data['v2'] = v2
    #print v2
    regex = r"(?<=\bsch_stops_n=\").*(?=\")"
    linesInfo = re.search(regex,stops_info).group(0).split("`")[:-1]
    #print linesInfo
    #url_values = urllib.urlencode(data)
    #full_url = base_url + "?" + url_values
    #html = s.get(schedule_url).text    
    #soup = BeautifulSoup(html,'html5lib')
    #print soup
    return linesInfo


def getTransSystemList(stateId):
    global v1,v2,pwd,s
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
    #response = urllib2.urlopen(full_url)
    html = s.get(full_url).text
    
    soup = BeautifulSoup(html,'html5lib')
    companyList = soup.select(".index")
    companyList = companyList[0].find_all('li')
    systemList={}
    for list in companyList:
        abr = tras2asc(list.contents[0].contents[0])
        #title = str(list.find_all("a")[0].attrs["title"])
        #lineId = str(list.find_all("a")[0].attrs["onclick"].split(",")[1][:-1])
        #print abr +" ## "+title +" ## "+lineId
        attrs = list.find_all("a")[0].attrs
        title = ""
        systemId = ""
        
        if "title" in attrs:
            title = tras2asc(attrs["title"])
        systemId = tras2asc(attrs["onclick"].split(",")[1][:-1])
        systemList[systemId] = [title,abr]
    return systemList


def getStatesInfo():
    global v1,v2,pwd,http,s
    starUrl = "https://rideschedules.com/"
    response = s.get(starUrl)
    starPage_html = response.text
    # starPage_html = response.data
    # print response.content
    # print "========================================================"
    # print response.text
    soup = BeautifulSoup(starPage_html, 'html5lib')
    #print soup
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
sleep(random.uniform(0.5,1.5))
print "v1 : " + v1
print "v2 : " + v2
print "pwd : " + pwd
#print stateList
#print len(stateList)

for statekey in stateList:
    if statekey == "New Jersey":
        print "====================================================="
        print statekey + ":" + stateList[statekey]
        systemList = getTransSystemList(stateList[statekey])
        sleep(random.uniform(0.5,1.5))
        print len(systemList)
        for systemId in systemList:
            if systemId == '51021':
                system_abr = systemList[systemId][1]
                system_i  = systemList[systemId][0]
                state = statekey
                if system_i ==  "":
                    system = system_abr
                else :
                    system = system_i
                print "     "+state +": " + system +"  ~~~  "+system_abr+" ~~~ "+system_i+" ~~~ "+systemId
                linesList = getTransLineList(systemId)
                sleep(random.uniform(0.5,1.5))
                print len(linesList)
                for lineId in linesList:
                    linesInfo = getLineInfo(lineId)
                    sleep(random.uniform(1.5,2.5))
                    print "           "+tras2asc(linesList[lineId][0])+" ~~~ "+tras2asc(lineId)
                    for i in linesInfo:
                        print "                           "+ tras2asc(i)
