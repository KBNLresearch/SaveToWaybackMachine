#! /usr/bin/env python
'''
This improved Wayback Machine Internet Archive archiving script has three modes:
1) It can save a page/document to the Wayback Machine (WBM) of the Internet Archive (IA)
2) It can retrieve the latest/newest archived version of a page from the WBM
3) It can retrieve the oldest/first archived version of a page from the WBM

In : URL of page e.g. https://www.kb.nl/annemarie-mol-geillustreerde-bibliografie
Out: URL to WBM snapshot: e.g. https://web.archive.org/web/DATETIMESTAMP/https://www.kb.nl/annemarie-mol-geillustreerde-bibliografie

The URLs to be processed are read from a .txt file, with 1 URL per line

The scripts uses https://pypi.org/project/waybackpy/ + https://github.com/akamhy/waybackpy/wiki/Python-package-docs

Notes:
02/12/2021:
* When archiving/saving pages (mode 1) : script seem to run rather stable due to improved error handling
* When archiving/saving pages (mode 1): script runs rather slow  (pm 3 minutes for 10 urls), this seems to be due to the
  processing speed of the WBM.
* .... 
'''

import csv, time
import waybackpy
from waybackpy.exceptions import WaybackError

def read_local_csv(filename):
    # Input=local filepath/filename of csv -- Output=List
    list = []
    response = open(filename, 'r', encoding="utf8")
    sheet = csv.reader(response, delimiter=';')
    for row in sheet:
        if not str(row).startswith('#', 2):  # skip rows in cvs that start with '#'
            list.append(row)
    return list
    print(list)

user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
infile="url-inputlist.txt" # list of urls/pages that need archiving
outfile="url-outputlist.txt" # list of archieved urls/pages. Format = inputurl^^^^archivedurl, for example
# https://www.kb.nl/annemarie-mol-geillustreerde-bibliografie^^^^https://web.archive.org/web/20171006113747/https://www.kb.nl/annemarie-mol-geillustreerde-bibliografie
# This output can be easily imported into Excel using the "Data --> Text to columns" function, where the "^" must be used as separator, resulting in a 2-column Excel sheet

urllist = []
urllist=read_local_csv(infile) # file with 1 URL per line

with open(outfile, "w") as outputfile: # open new version of outputfile, clear the old version

    for url in urllist:
        time.sleep(1)  # pause for 1 sec, not to overrequest the server.
# Choose longer times for archiving pdf and doc files, as the archiving software needs more time to read these docs than standard html pages
        outputfile = open(outfile, 'a') # append to existing outputfile
        #linenumber = urllist.index(url)+1
        wayback = waybackpy.Url(url[0], user_agent)

# MODE 1: Code for saving url/page
        try:
            archive = wayback.save()
            print(str(url[0] + "^^^^" + str(archive.archive_url)))
            outputfile.write(str(url[0] + "^^^^" + str(archive.archive_url))+"\n")
        except WaybackError as e:
            print(str(url[0] + "^^^^" + "WaybackError - could not save page to WBM"))
            outputfile.write(str(url[0] + "^^^^" + "WaybackError - could not save page to IA")+"\n")
        except AttributeError as d:
            print(str(url[0] + "^^^^" + "AttributeError - could not save page to IA"))
            outputfile.write(str(url[0] + "^^^^" + "AttributeError - could not save page to WBM")+"\n")

# MODE 2: Code for retrieving latest/newest version of page
#         try:
#             archive = wayback.newest()
#             print(str(url[0] + "^^^^" + str(archive.archive_url)))
#             outputfile.write(str(url[0] + "^^^^" + str(archive.archive_url))+"\n")
#         except WaybackError as e:
#             print(str(url[0] + "^^^^" + "WaybackError - page not archived in WBM"))
#             outputfile.write(str(url[0] + "^^^^" + "WaybackError - page not archived in WBM")+"\n")
#         except AttributeError as d:
#             print(str(url[0] + "^^^^" + "AttributeError - page not archived in WBM"))
#             outputfile.write(str(url[0] + "^^^^" + "AttributeError - page not archived in WBM")+"\n")

# MODE 3: Code for retrieving oldest/first version of url/page 
#         try:
#             archive = wayback.oldest()
#             print(str(url[0] + "^^^^" + str(archive.archive_url)))
#             outputfile.write(str(url[0] + "^^^^" + str(archive.archive_url))+"\n")
#         except WaybackError as e:
#             print(str(url[0] + "^^^^" + "WaybackError - page not archived in WBM"))
#             outputfile.write(str(url[0] + "^^^^" + "WaybackError - page not archived in WBM")+"\n")
#         except AttributeError as d:
#             print(str(url[0] + "^^^^" + "AttributeError - page not archived in WBM"))
#             outputfile.write(str(url[0] + "^^^^" + "AttributeError - page not archived in WBM")+"\n")
    outputfile.close()

