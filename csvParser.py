import csv

def csvParser(filename):
    return csv.DictReader(open(filename), delimiter=',')
