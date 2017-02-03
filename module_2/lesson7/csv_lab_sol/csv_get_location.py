#! /usr/bin/env python3
import sys
import csv
from geopy.geocoders import Nominatim

FILE_NAME = 'FL_insurance_sample.csv'
DELIMITER = ','
UNKNOWN_ERROR = 1
RUN_TIME_EXCEPTION = 2


def main():
    """ Only step 1 is given as solution. """
    with open(FILE_NAME, newline='') as csv_file:
        geo_locator = Nominatim()
        csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
        for record in csv_reader:
            # is this a better way of unpacking you can think of?
            # Perhaps using a better data structure than just a tuple?
            policy_id, *_, point_latitude, point_longitude, line, construction, point_granularity = record
            # print(policy_id, point_latitude, point_longitude)
            try:
                print(geo_locator.reverse(point_latitude + ', ' + point_longitude))
            except Exception as e:
                print(e)
                print("Unable to get reverse coordinates")

    return 0


if __name__ == '__main__':
    status = UNKNOWN_ERROR
    try:
        status = main()
    except RuntimeError:
        status = RUN_TIME_EXCEPTION
    sys.exit(status)
