# Saving Literatuurplein.nl to Wayback Machine

The site www.literatuurplein.nl will be phased out from December 2019 onwards. 

To preserve the current content of the site (e.g. for sourcing Wikipedia articles) I submitted a copy to The Wayback Machine (web.archive.org).

I saved the xxx most requested pages (= pages that were requested 30 or more times over the last 5 years) out of a total of xxx pages in the Wayback Machine. 

Steps taken: 

1) I first extracted an [input list of xxx URLs](Input-Literatuurplein_TeArchiverenURLs.txt) from Google Analytics. We did 200/404-checking and further cleaning, ending up with this input of xx URLs

2) I then ran [SaveLiteratuurpleinToWaybackMachine.py](SaveLiteratuurpleinToWaybackMachine.py) to submit these xx URLs to The Wayback Machine. This was not a 100% process, in the end xxx URLs were successfully captured (xx%). 

3) The output of the script was dumped in an 
* [Excel file](Output-Literatuurplein_GearchiveerdeURLs_21112019.xlsx)
* [Text file](Output-Literatuurplein_GearchiveerdeURLs_21112019.txt) (using '^^' as a separator)
