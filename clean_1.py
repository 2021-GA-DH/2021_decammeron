#!/usr/local/bin/python
# -*- coding: utf-8 -*-


sourcefolder = "D:/development/python/2021_decammeron/original/"
destinationfolder = "D:/development/python/2021_decammeron/clean/"

counter = 1
i = 1

while i < 101:

	inputfile = sourcefolder + "page-" + str(i) + ".html"
	outputfile = destinationfolder + "page-" + str(i) + ".txt"
	print (i, outputfile)	

	recording = 0
	output = ""

	fhand1 = open(inputfile, encoding="utf-8")

	for line in fhand1:
		line = line.strip()

		if 'id="text"' in line:
			recording = 1

		if 'id="footer"' in line:
			recording = 0

		if recording == 1:
			output = output + line + " "

	location1 = 0
	location2 = 0
	location3 = 0
	location4= 0
	location5= 0
	location6= 0

	while (output.find("[Voice")) > 0:
		location1 = (output.find("[Voice"))
		location2 = (output.find("]", location1))
		output = output[:location1] + output[location2+1:]


	while (output.find("<a")) > 0:
		location3 = (output.find("<a"))
		location4 = (output.find("</a>", location3))
		output = output[:location3] + output[location4+4:]

	output = output.replace('</p>', '\n\r\n')

	output = output.replace('  ', ' ')

	count = 0
	while (output.find('<')) >= 0:
		location5 = (output.find('<'))
		location6 = (output.find('>', location5))
		output = output[:location5] + output[location6+1:]

	with open(outputfile, 'w', encoding="utf-8") as file1:
		file1.write(output)
		file1.close

	i +=1
