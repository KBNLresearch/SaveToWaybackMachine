import requests, bs4

## http://stackoverflow.com/questions/1726402/in-python-how-do-i-use-urllib-to-see-if-a-website-is-404-or-200

print(" * * * This programs checks if a given URL list (input.txt) haves broken URLs * * *")
print("\tEach line should contain a single url to check")

fh = open ('URLsToCheck.txt' , 'r')
strData = fh.read()
fh.close()

listData = []
for row in strData.split("\n"):
	if row.strip() != '' :
		listData.append(row.strip())
	#print(str(row.strip()))

nCorrect = 0
nBroken = 0

with open('URLsChecked.txt','w') as file:

    for strUrl in listData:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(strUrl, headers=headers)
        if response.status_code == 200:
            nCorrect += 1
            print("%s\t%s" % (response.status_code, strUrl))
            file.write("%s \t%s" % (response.status_code, strUrl)+'\n')
        else:
            nBroken += 1
            print("%s\t%s" % (response.status_code, strUrl))
            file.write("%s\t%s" % (response.status_code, strUrl)+'\n')

    print(" #### %d broken URLs      %d correct URLs    (%d total) " % (nBroken, nCorrect, len(listData) ))

    file.close()