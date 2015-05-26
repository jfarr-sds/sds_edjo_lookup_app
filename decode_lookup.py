import csv

infile = open('raw_lookup.csv', 'rb')
outfile = open('decoded_lookup.csv', 'wb')
reader = csv.reader(infile, delimiter=',', quotechar='"')
writer = csv.writer(outfile)
l = list(reader)
header = l[0]
 
for row in l:
	column = 0
	
	for item in row:
		if column == 0:
			column = column + 1
			continue
		else:
			# print row[0] + header[column] + " " + item 
			writer.writerow( [row[0] + header[column] , item])
			column = column + 1

