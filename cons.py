import csv
from itertools import groupby
from copy import deepcopy


allyears = set([str(x) for x in range(1980,2016)])

def create_cons_year():
	with open("dtp_incidence-xlsx-output.csv", 'w') as output_csv_file:
		with open("dtp_incidence-xlsx.csv", 'r') as input_csv_file:
			d_reader = csv.DictReader(input_csv_file);
			# Lower the field name case.
			d_reader.fieldnames = [field.strip().lower() for field in d_reader.fieldnames]

			# Prepare the output writer.
			d_writer = csv.DictWriter(output_csv_file, fieldnames=d_reader.fieldnames)
			d_writer.writeheader()

			country_group = []
			allrows = []


			# Start reading each row.
			for i, row in enumerate(d_reader):
				allrows.append(row)
			for k, g in groupby(allrows, lambda x:x['cname']):
				currentrows = list(g)
				years = set()
				for row in currentrows:
					years.add(row['year'])
				diffyear = allyears.difference(years)
				if k == 'Afghanistan':
					print allyears, diffyear
				for y in diffyear: 
					newrow = deepcopy(currentrows[0])
					newrow['year'] = y
					newrow['case'] = '-1'
					d_writer.writerow(newrow)
			d_writer.writerows(allrows)
			
create_cons_year()
