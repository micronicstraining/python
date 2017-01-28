#! /usr/bin/env python3
import sys
import csv
from geopy.geocoders import Nominatim

FILE_NAME = 'FL_insurance_sample.csv'
DELIMITER = ','


def main():
    """ Only step 1 is given as solution. """
    with open(FILE_NAME, newline='') as csv_file:
        geo_locator = Nominatim()
        csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
        for row in csv_reader:
            policy_id, *_, point_latitude, point_longitude, line, construction, point_granularity = row
            print(policy_id, point_latitude, point_longitude)
            try:
                print(geo_locator.reverse(point_latitude + ', ' + point_longitude))
            except:
                print("Unable to get reverse coordinates")

    return 0


if __name__ == '__main__':
    status = 1
    try:
        status = main()
    except RuntimeError:
        status = 2
    sys.exit(status)
