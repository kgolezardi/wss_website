import csv

with open('speakers-data.csv', 'r', encoding='utf-8') as data_file:
	data = list(csv.reader(data_file, delimiter=',', quotechar='"'))
	with open('single-speaker-page-template.html', 'r', encoding='utf-8') as template_file:
		template = template_file.read()
		n_rows = len(data)
		for i in range(0, n_rows):
			row = data[i]
			output = template
			output = output.replace('Single Speaker Name', row[0])
			output = output.replace('Single Speaker Position', row[1])
			output = output.replace('Single Speaker Photo', row[3])
			output = output.replace('Single Speaker Title', row[4])
			output = output.replace('Single Speaker Abstract', row[5])
			output = output.replace('Single Speaker Bio', row[6])
			with open(row[0].lower().replace(' ', '-') + '.html', 'w', encoding='utf-8') as output_file:
				output_file.write(output)
