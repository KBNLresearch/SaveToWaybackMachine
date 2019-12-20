# Saving Literatuurplein.nl to the Wayback Machine

<image src="images/literatuurplein-homepage_04122019.JPG" width="500"/><br clear="all"/>

The site www.literatuurplein.nl has been phased out per 16 December 2019. 

To preserve its content, e.g. for sourcing Wikipedia articles or (Wiki)data purposes, I submitted copies of its most relevant pages to [The Wayback Machine](https://web.archive.org/) (WBM) of The Internet Archive during November and December 2019.

## The data
* Every Excel file contains 4 standard columns:
  - *LiteratuurpleinURL* : URL of the orginal page on literatuurplein.nl
  - *LiteratuurpleinArchiefURL* : WBM URL of the page , starting with *http://web.archive.org/web/*
  - *ArchiefURLStatusCheck-datestamp* : HTTP response status code of the WBM page at the given datestamp, indicating if that page can be requested without issues. Status 200 = OK.
  - *Klik* : Clicking on this will open the archived page in a browser
* Additionaly, some Excels contain extra columns, including unique IDs, page titles, person names, places or dates.
* For every .xlsx there is a .tsv (tab separated value) in Unicode UTF-8. This can be readily imported/exported to other data formats.
* One page can be available under multiple URLs, e.g. in the file *[literatuurplein-adressenbank_03122019.tsv](literatuurplein-adressenbank_03122019.tsv)* there are three lines for *55	Ambo|Anthos uitgevers, Herengracht 499, Amsterdam	Noord-Holland*, as this page was available under 3 distinct URLs	
  - https://literatuurplein.nl/detail/organisatie/ambo-anthos-uitgevers/55	
  - https://www.literatuurplein.nl/detail/organisatie/ambo-anthos-uitgevers/55
  - https://www.literatuurplein.nl/organisatie.jsp?orgId=55   
  Because I archived URLs, *not* pages, this also means that this page has been archived under three distinct WBM URLs. 
* No overall file list is provided, you'll need to create that yourself from the individual .xlsx/.tsv files if you need it

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
