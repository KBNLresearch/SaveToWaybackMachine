# Saving Literatuurplein.nl to the Wayback Machine

The site www.literatuurplein.nl will be phased out from December 2019 onwards. 

<image src="images/literatuurplein-homepage_04122019.JPG" width="500"/><br clear="all"/>

To preserve the content (per november/december 2019) of the site, e.g. for sourcing Wikipedia articles, I submitted a copy to The Wayback Machine of the Internet Archive (web.archive.org).

I archived

1) Pages under the following menu items
* [Nieuws]() - [Columns]()
* [Interviews]() - [Literaire prijzen]()
* [Recensies]()
* [Canon]() - [Excursies]() - [Poezie]()
* [Literaire adressen]()

2) Pages that were requested 30 or more times over the last 5 years, 32K pages in all, out of a total of 964K pages that were requested in that time period (extreme long tail distribution)  

## Steps taken 
1) to extact urls the pages in the first group, using the [Chrome-plugin](https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn?hl=en) of [Webscraper.io](https://webscraper.io/)

2) to extact urls the pages in the second group, extracted an [input list of xxx URLs](Input-Literatuurplein_TeArchiverenURLs.txt) from Google Analytics. 

3) Combined both url lists and did deduplication to avoid overlap

4) We did 200/404-checking and further cleaning, ending up with this input of xx URLs

5) I then ran [SaveLiteratuurpleinToWaybackMachine.py](SaveLiteratuurpleinToWaybackMachine.py) to submit these xx URLs to The Wayback Machine. This was not a 100% process, in the end xxx URLs were successfully captured (xx%). 

6) Matched the archived urls against the original urls, in Excel files
 [Excel file](Output-Literatuurplein_GearchiveerdeURLs_21112019.xlsx) 

7) Converted Excel to open, Unicode Text format * [Text file](Output-Literatuurplein_GearchiveerdeURLs_21112019.txt) (using '^^' as a separator), so it can be imprted in structured fromat similar to csv into 
