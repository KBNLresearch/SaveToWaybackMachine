# Saving Literatuurplein.nl to the Wayback Machine

The site www.literatuurplein.nl has been phased per 16 December 2019. 

<image src="images/literatuurplein-homepage_04122019.JPG" width="500"/><br clear="all"/>

To preserve its content (e.g. for sourcing Wikipedia articles or Wikidata purposes) I submitted a copy of (the most relevant content of) the site to [The Wayback Machine](https://web.archive.org/) of The Internet Archive during November and December 2019.

## The data
- The urls-combis (orginal and archived) are listed in both xlsx and tsv (tab separed value)
- both the orginla as the archived urls are given
- short description of each file
- no overall file list id provided, you'll need to make that ypourself
- one page can hgave several urls, (show three)
- 200 - file status checked
-Klik (Excel)

Short descriopto per file, type of content

for readability the 
-prefix *literatuurplein-* is omitted
-suffix *(_03122019)*, the datestamp when the file was created, and
-the file extension (*.xlsx* / *.tsv*)
are also omitted 

* *adressenbank* : 
* *boeken* : 
* *canon* : 
* *columns* : 
* *evenementen* : 
* *excursies* : 
* *genres* : 
* *interviews* : 
* *leestips* : 
* *nieuws* : 
* *overige* : 
* *personen-allen* : 
* *personen-namen-datums-plaatsen* : 
* *poezie* : 
* *prijzen* : 
* *prijzen-edities* : 
* *prijzen-totaal* : 
* *recensies* : 
* *themas* : 
* *trefwoorden* : 
* *wereldkaart* : 
* *zoeken* : 

## Process

I actively archived

1) Pages under the following menu items of [www.literatuurplein.nl](https://web.archive.org/web/20191125105524/https://www.literatuurplein.nl/)
* Nieuws - Columns
* Interviews - Literaire prijzen
* Recensies
* Canon - Excursies - Poezie
* Literaire adressen

2) Pages that were requested 30 or more times over the last 5 years. This were 32K pages in total, out of a total of 964K pages that were requested in that time period (extreme long tail distribution)  

3) A dump of the CMS with approx 10K person (mainly authors) (map "Archive")


## Steps taken 
1) to extact urls the pages in the first group, using the [Chrome-plugin](https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn?hl=en) of [Webscraper.io](https://webscraper.io/)

2) to extact urls the pages in the second group, extracted an [input list of xxx URLs](Input-Literatuurplein_TeArchiverenURLs.txt) from Google Analytics. 

3) Combined both url lists and did deduplication to avoid overlap

4) We did 200/404-checking and further cleaning, ending up with this input of xx URLs

5) I then ran [SaveLiteratuurpleinToWaybackMachine.py](SaveLiteratuurpleinToWaybackMachine.py) to submit these xx URLs to The Wayback Machine. This was not a 100% process, in the end xxx URLs were successfully captured (xx%). 

6) Matched the archived urls against the original urls, in Excel files
 [Excel file](Output-Literatuurplein_GearchiveerdeURLs_21112019.xlsx) 

7) Converted Excel to open, Unicode Text format * [Text file](Output-Literatuurplein_GearchiveerdeURLs_21112019.txt) (using '^^' as a separator), so it can be imprted in structured fromat similar to csv into 
