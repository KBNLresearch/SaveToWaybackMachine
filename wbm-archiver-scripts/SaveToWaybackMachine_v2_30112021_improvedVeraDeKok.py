#!/usr/bin/python
# -*- coding: utf-8 -*-

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
27/11/2021:
* When archiving/saving pages (mode 1) : script seem to run rather stable due to improved error handling
* When archiving/saving pages (mode 1): script runs rather slow  (pm 3 minutes for 10 urls), this seems to be due to the
  processing speed of the WBM.
* .... 
'''

import csv 
import time
from waybackpy.exceptions import WaybackError
import waybackpy
from numpy import loadtxt



USER_AGENT = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
INFILE="url-inputlist.csv" # list of urls/pages that need archiving
OUTFILE="url-outputlist.csv" # list of archieved urls/pages. 

csvfile =  open(OUTFILE , "w", newline='\n', encoding='utf-8')
spamwriter = csv.writer(csvfile, dialect='excel', delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)


urllist = loadtxt(INFILE, dtype=str, comments="#", delimiter="\n", encoding='utf-8')
for url in urllist:
    time.sleep(1)  # pause for 1 sec, not to overrequest the server.
# Choose longer times for archiving pdf and doc files, as the archiving software needs more time to read these docs than standard html pages
    

    wayback = waybackpy.Url(url, USER_AGENT)

# MODE 1: Code for saving url/page
    try:
        archive = wayback.save()
        print(url,  archive.archive_url)
        spamwriter.writerow([url, archive.archive_url])
    except WaybackError as e:
        print(url,  "WaybackError - could not save page to WBM")
        spamwriter.writerow([url , "WaybackError - could not save page to IA"])
    except AttributeError as d:
        print(url,  "AttributeError - could not save page to IA")
        spamwriter.writerow([url, "AttributeError - could not save page to WBM"])

# MODE 2: Code for retrieving latest/newest version of page
#   try:
#       archive = wayback.newest()
#       print(url,  archive.archive_url)
#       spamwriter.writerow([url,  archive.archive_url)])
#   except WaybackError as e:
#       print(url,  "WaybackError - page not archived in WBM")
#       spamwriter.writerow([url,  "WaybackError - page not archived in WBM"])
#   except AttributeError as d:
#       print(url,  "AttributeError - page not archived in WBM")
#       spamwriter.writerow([url,  "AttributeError - page not archived in WBM"])

# MODE 3: Code for retrieving oldest/first version of url/page 
#  try:
#      archive = wayback.oldest()
#      print(url,  archive.archive_url)))
#      spamwriter.writerow([url,  archive.archive_url])
#  except WaybackError as e:
#      print(url,  "WaybackError - page not archived in WBM")
#      spamwriter.writerow([url,  "WaybackError - page not archived in WBM"])
#  except AttributeError as d:
#      print(url,  "AttributeError - page not archived in WBM")
#      spamwriter.writerow([url,  "AttributeError - page not archived in WBM"])