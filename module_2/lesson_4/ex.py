#! /usr/bin/env python3
import csv

def main():
    with open('ex.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = csv_file.readline()
        csv_dict = dict()
        for record in csv_reader:
            for item in record:

            csv_dict[(first, last)] = rest
        print(csv_dict)


if __name__ == '__main__':
    main()