# Saving Literatuurplein.nl to Wayback Machine

The site www.literatuurplein.nl will be phased out from December 2019 onwards. 

To preserve the content (per november/december 2019) of the site, e.g. for sourcing Wikipedia articles, I submitted a copy to The Wayback Machine of the Internet Archive (web.archive.org).

I archived

1 The pages under the following menu items
* Nieuws
* Columns
* Interviews
* Literaire prijzen
* Recensies
* Canon
* Excursies
* Poezie
* Literaire adressen

2 All pages that were requested 30 or more times over the last 5 years, 32K pages in all, out of a total of 964K pages that were requested in that time period (extreme long tail distribution)  

The might be overlap between the pages in the first group and thise in the second. 

Steps taken: 

1) I first extracted an [input list of xxx URLs](Input-Literatuurplein_TeArchiverenURLs.txt) from Google Analytics. We did 200/404-checking and further cleaning, ending up with this input of xx URLs

2) I then ran [SaveLiteratuurpleinToWaybackMachine.py](SaveLiteratuurpleinToWaybackMachine.py) to submit these xx URLs to The Wayback Machine. This was not a 100% process, in the end xxx URLs were successfully captured (xx%). 

3) The output of the script was dumped in an 
* [Excel file](Output-Literatuurplein_GearchiveerdeURLs_21112019.xlsx)
* [Text file](Output-Literatuurplein_GearchiveerdeURLs_21112019.txt) (using '^^' as a separator)
