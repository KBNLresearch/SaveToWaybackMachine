# Saving Literatuurplein.nl to the Wayback Machine

<image src="images/literatuurplein-homepage_04122019.JPG" width="500"/><br clear="all"/>

The site www.literatuurplein.nl has been phased out per 16 December 2019. 

To preserve its content, e.g. for sourcing Wikipedia articles or (Wiki)data purposes, I submitted copies of its most relevant pages to [The Wayback Machine](https://web.archive.org/) (WBM) of The Internet Archive during November and December 2019.

## The data
* Every Excel file contains 4 standard columns:
  - *LiteratuurpleinURL* : URL of the orginal page on literatuurplein.nl
  - *LiteratuurpleinArchiefURL* : WBM URL of the page , starting with *http://web.archive.org/web/*
  - *ArchiefURLStatusCheck-datestamp* : HTTP response status code of the WBM page at the given datestamp, indicating if that page can be requested without issues. Status 200 = OK.
  - *Klik* : Clicking on this will open the archived page in a browser.
* Additionaly, some Excels contain extra columns, including unique IDs, page titles, person names, places or dates.
* For every .xlsx there is a .tsv (tab separated value) in Unicode UTF-8. This can be readily imported/exported to other data formats.
* One page can be available under multiple URLs, e.g. in the file *[literatuurplein-adressenbank_03122019.tsv](literatuurplein-adressenbank_03122019.tsv)* there are three lines for *55	Ambo|Anthos uitgevers, Herengracht 499, Amsterdam	Noord-Holland*, as this page was available under 3 distinct URLs	
  - https://literatuurplein.nl/detail/organisatie/ambo-anthos-uitgevers/55	
  - https://www.literatuurplein.nl/detail/organisatie/ambo-anthos-uitgevers/55
  - https://www.literatuurplein.nl/organisatie.jsp?orgId=55   
  Because I archived URLs, *not* pages, this also means that this page has been archived under three distinct WBM URLs. 
* No overall file list is provided, you'll need to compose that yourself from the individual .xlsx/.tsv files if you need it.

## Short description per file
For readability the 
1. prefix *literatuurplein-* , the  
2. suffix *(_03122019)*, the datestamp when the file was created, anf the
3. file extension (*.xlsx* / *.tsv*)
are omitted from the filenames below

The number behind the filename is the number of URLs captured (= number of rows in the Excel)

* *[adressenbank](literatuurplein-adressenbank_03122019.tsv)* (3.464) : Names and adresses of literary organisations (publishers, book sellers, libraries, reading clubs etc.). Mainly in the Netherlands, sortable by province. Some in Belgium and Europe.
* *[boeken](literatuurplein-boeken_06122019.tsv)* (16.677) : Details (descriptive metadata) about books. No explicit titles of authors provided.
* *[canon](literatuurplein-canon_28112019.tsv)* () : 
* *[columns](literatuurplein-columns_06122019.tsv)* () : 
* *[evenementen](literatuurplein-evenementen_06122019.tsv)* () : 
* *[excursies](literatuurplein-excursies_28112019.tsv)* () : 
* *[genres](literatuurplein-genres_06122019.tsv)* () :
* *[interviews](literatuurplein-interviews_28112019.tsv)* () :
* *[leestips](literatuurplein-leestips_06122019.tsv)* () :
* *[nieuws](literatuurplein-nieuws_06122019.tsv)* () :
* *[overige](literatuurplein-overige_06122019.tsv)* () : 
* *[personen-allen](literatuurplein-personen-allen_19122019.tsv)* () :
* *[personen-namen-datums-plaatsen](literatuurplein-personen-namen-datums-plaatsen_19122019.tsv)* () :
* *[poezie](literatuurplein-poezie_29112019.tsv)* () :
* *[prijzen](literatuurplein-prijzen_06122019.tsv)* () : 
* *[prijzen-edities](literatuurplein-prijzen-edities_06122019.tsv)* () :
* *[prijzen-totaal](literatuurplein-prijzen-totaal_17122019.tsv)* () :
* *[recensies](literatuurplein-recensies_28112019.tsv)* () :
* *[themas](literatuurplein-themas_06122019.tsv)* () :
* *[trefwoorden](literatuurplein-trefwoorden_06122019.tsv)* () :
* *[wereldkaart](literatuurplein-wereldkaart_06122019.tsv)* () : 
* *[zoeken](literatuurplein-zoeken_06122019.tsv)* () : 

Obviously, more Literatuurplein URLs than are listed in these files are (likely to be) available in the WBM. This is because apart from the *active* archiving effort described here, the WMB crawler/archiver has visited the site over its lifetime, thus archiving pages for many years (we could call this *passive* archiving).   

## Data sources
The data to make the above files was obtained from 3 sources:

1) *Most relevant subsites* of [www.literatuurplein.nl](https://web.archive.org/web/20191125105524/https://www.literatuurplein.nl/): Page URLs and page content under the menu items *Nieuws - Columns - Interviews - Literaire prijzen - Recensies - Canon - Excursies - Poezie - Literaire adressen* of  were extracted using webscraping.

2) *Google Analytics*: URLs of pages that were requested 30 or more times over the last 5 years were extracted from Google Analytics. This were 32K URLs in total, out of a total of 964K pages that were requested in that time period (extreme long tail distribution)  

3) *[Data dump](archive/literatuurplein-personen-oorspronkelijk_SophieHam_07112019.csv)* from the Literatuurplein CMS,  containing names, dates of birth & death and places of birth & death of 10.027 persons (mainly authors).


## Steps taken 
1) to extact urls the pages in the first group, using the [Chrome-plugin](https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn?hl=en) of [Webscraper.io](https://webscraper.io/)

2) to extact urls the pages in the second group, extracted an [input list of xxx URLs](Input-Literatuurplein_TeArchiverenURLs.txt) from Google Analytics. 

For instance, from the ID in column 1 (**161934**) we we able to construct a Leesplein URL (https://www.literatuurplein.nl/persdetail?persId=**161934**) which we then sent to the WBM (http://web.archive.org/web/20191204192638/https://www.literatuurplein.nl/persdetail?persId=**161934**). This data dump ended up in *[personen-allen](literatuurplein-personen-allen_19122019.tsv)* and *[personen-namen-datums-plaatsen](literatuurplein-personen-namen-datums-plaatsen_19122019.tsv)* 


3) Combined both url lists and did deduplication to avoid overlap

4) We did 200/404-checking and further cleaning, ending up with this input of xx URLs

5) I then ran [SaveLiteratuurpleinToWaybackMachine.py](SaveLiteratuurpleinToWaybackMachine.py) to submit these xx URLs to The Wayback Machine. This was not a 100% process, in the end xxx URLs were successfully captured (xx%). 

6) Matched the archived urls against the original urls, in Excel files
 [Excel file](Output-Literatuurplein_GearchiveerdeURLs_21112019.xlsx) 

7) Converted Excel to open, Unicode Text format * [Text file](Output-Literatuurplein_GearchiveerdeURLs_21112019.txt) (using '^^' as a separator), so it can be imprted in structured fromat similar to csv into 
