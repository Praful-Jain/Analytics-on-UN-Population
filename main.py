# This main.py file will open the csv file into csv_reader, store the data of ASEAN and Saarc countries
import csv

csv_file = r'population-estimates_csv.csv'

def reader_function(csv_file):
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)
        return data

population_reader = reader_function(csv_file)


ASEAN_Countries = [ 'Thailand' ,	 'Vietnam', 'Indonesia', 'Cambodia', 	 'Brunei', 	 'Myanmar',	 
                   'Malaysia', 	 'Laos', 'Philippines','Singapore']

SAARC_Countries = [ 'Afghanistan', 'Bangladesh', 'Bhutan', 'India' , 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']
