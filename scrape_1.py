#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#url https://www.brown.edu/Departments/Italian_Studies/dweb/texts/DecShowText.php?myID=nov0101&lang=eng

import time
import urllib3
http = urllib3.PoolManager()


urlroot = "https://www.brown.edu/Departments/Italian_Studies/dweb/texts/DecShowText.php?myID=nov"
extrabit= "&lang=eng"


# establish URLs to scrape
urlset = []
i = 1

while i < 11:
	book = str(i)

	if i < 10:
		book = "0" + book

	count = 1
	while count < 11:
		story = str(count)

		if count < 10:
			story = "0" + story

		urltarget = urlroot + book + story + extrabit 
		urlset.append (urltarget) 

		print (i, count)
		count += 1

	i +=1

print(urlset)


# step 2 : scrape and save

pagedownload = 0

for url in urlset:
	pagedownload +=1	
	print (pagedownload, url)

	resp = http.request("Get", url)
	webcontent = resp.data.decode('utf-8')
	output = "page-" + str(pagedownload) + ".html"

	with open(output, 'w', encoding="utf-8") as file1:
		file1.write(webcontent)
		file1.close

	time.sleep(10)





