#! /usr/bin/env python

import requests, csv, time
MAX_RETRIES = 20

# In : Literaireprijzen.nl URL (Lprijzen) : e.g. http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/161/Mode/ViewAwardYears?AwardName=F.%20Bordewijk-prijs
# Out: URL to Wayback Machine (The Internet Archive - TIA) snapshot: e.g. http://web.archive.org/web/20180706113238/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/161/Mode/ViewAwardYears?AwardName=F.%20Bordewijk-prijs
# Works for html pages in  Literaireprijzen.nl
# This script is certainly not 100% solid & error proof, you might need to tweak it here and there to make it more robust and deal with all sorts of possible errors and time-outs. But hey, it does a mostly decent job!

def read_local_csv(filename):
    # Input=local filepath/filename of csv -- Output=List
    list = []
    response = open(filename, 'r', encoding="utf8")
    sheet = csv.reader(response, delimiter=';')
    for row in sheet:
        if not str(row).startswith('#', 2):  # skip rows in cvs that start with '#'
            list.append(row)
    return list

base_url = 'http://web.archive.org'

urllist = []
urllist=read_local_csv("Input-Lprijzen_TeArchiverenURLs_31102018_werkbestand.txt") # file with 1 to-be-archived Leesplein-URL per line

with open("Output-Lprijzen_TeArchiverenURLs_31102018_werkbestand.txt", "w") as outputfile: # open new versin of outputfile, clear the old version

    errorfile = open('Output-Lprijzen_TeArchiverenURLs_31102018_werkbestand.txt', 'a') # deze file bevat alle LP-urls die in de 1e run niet gearchiveerd konden worden

    for url in urllist:
        time.sleep(5)  # pause for 5 sec, not to overrequest the server. Choose longer times for archiving pdf and doc files, as the archiving software needs more time to read these docs than standard html pages
        outputfile = open('Output-Lprijzen_TeArchiverenURLs_31102018_werkbestand.txt', 'a') # append to existing outputfile
        linenumber = urllist.index(url)+1
        #print(str(url[0]))

        #https://stackoverflow.com/questions/33895739/python-requests-cant-load-any-url-remote-end-closed-connection-without-respo
        url_wbm = base_url + '/save/' + str(url[0])
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
        session.mount('https://', adapter)
        session.mount('http://', adapter)

        r = session.get(url_wbm)  #This line actually saves to URL to the Waybackmachine. All the following lines of code are for administration/display
        print(str(url[0])+ " -- " + str(r.headers))

# r.headers fout die kan voorkomen: {'Server': 'nginx/1.13.11', ...., 'X-Archive-Wayback-Runtime-Error': 'WaybackException: Unexpected Error', 'Set-Cookie': 'JSESSIONID=9EAAD47DBDCB85D0514293D472995036; Path=/; HttpOnly', 'X-App-Server': 'wwwb-app53', 'X-ts': '----'}

# Als deze fout voorkomt en de LvdL-URL daardoor niet gearchiveerd wordt: Schrijf niet gearchiveerde LvdL-url weg naar apart bestand - dat kunnen we dan later als invoer voor een correctierun gebruiken

        if 'X-Archive-Wayback-Runtime-Error' in r.headers:
            errorfile.write(str(url[0]) + "\n")
        else: #r.headers bevat geen Error
            #archive_url ="" #only relevant for pdf and doc
            #archive_url= r.headers['X-Cache-Key']
            # X-Cache-Key for PDF and DOC: httpweb.archive.org/web/20180608110403/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdfNL
            # X-Cache-Key for HTML: httpweb.archive.org/save/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&leefcat=12+&id=6726NL

            #if archive_url.startswith('httpweb.') and archive_url.endswith('NL'):
                #archive_url = "http://"+archive_url[4:-2]
                # for PDF and DOC : http://web.archive.org/web/20180608110403/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdf
                # for HTML: http://web.archive.org/save/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&leefcat=12+&id=6726
            #else: print('Unexpected value of X-Cache-Key in r.headers')

            if r.status_code == requests.codes.ok:
                contenttype = r.headers['Content-Type']
                if "text/html" in contenttype: #html page -- X-Cache-Key is not relevant
                    print(str(linenumber) + "^^^^" + str(url[0])+ "^^^^" + base_url + r.headers['Content-Location']) # the "^^^^" is used a separator between the two URLs. The more traditional separators such as ";" or "," are not reliable enough, as the can occur in URLs.
                    outputfile.write(str(linenumber) + "^^^^" + str(url[0])+ "^^^^" + base_url + r.headers['Content-Location'] + "\n")
                #elif contenttype == "application/pdf": #pdf file
                    #print(str(linenumber) + "^^^^" + str(url[0]) + "^^^^" + archive_url)
                    #outputfile.write(str(linenumber) + "^^^^" + str(url[0]) + "^^^^" + archive_url + "\n")
                #elif contenttype == "application/vnd.openxmlformats-officedocument.wordprocessingml.document": #Word doc(x)
                    #print(str(linenumber) + "^^^^" + str(url[0]) + "^^^^" + archive_url)
                    #outputfile.write(str(linenumber) + "^^^^" + str(url[0]) + "^^^^" + archive_url + "\n")
                else:
                    print("Unknown Content-Type: " + str(contenttype))
            else:
                print('Error in response: ' + str(r.status_code))
        outputfile.close()
        #errorfile.close()

#================= For reference purposes: Files type : html =================

#Typical r.headers snippet for html-page (better: for 'Content-Type': 'text/html;) --> 'Content-Location' is the relevant part
# {
#  'Server': 'nginx/1.13.11',
#  'Date': 'Fri, 06 Jul 2018 11:17:30 GMT',
#  'Content-Type': 'text/html;charset=utf-8',
#  'Transfer-Encoding': 'chunked',
#  'Connection': 'keep-alive',
#  'Content-Location': '/web/20180706111728/https://www.lezenvoordelijst.nl/',
#  'Set-Cookie': 'JSESSIONID=8F5EAB7E09A020A89081BAE740868229; Path=/; HttpOnly',
# .....
#  'X-App-Server': 'wwwb-app14', 'X-ts': '----',
#  'X-location': 'save',
#  'X-Cache-Key': 'httpweb.archive.org/save/https://www.lezenvoordelijst.nl/NL',
#  'X-Page-Cache': 'MISS',
#  'Content-Encoding': 'gzip'
#  }