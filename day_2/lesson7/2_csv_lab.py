# Lab instructions - Finish this script according to the following instructions
#
# Step 1
# 1) A csv file from: https://support.spatialkey.com/spatialkey-sample-csv-data/ has been downloaded
# 2) Read through this CSV file and from the columns extract the following data:

# 3) policyID,...,point_latitude,point_longitude, line, construction, point_granularity
#    Note: (... means ignore those columns)
#
# 4) get the address of the policy given the lat & long point and print it out to the screen
#    Note: see 1_geo_reverse_ex.py for example of how to do thise
#    Note: Warning, you must add exception handling in case an address is not found or the request times out!


# Step 2 (Homework)
# 1) Take the address and add it as a column to a new CSV file called 'address.FL_insurance_sample.csv'
#    Note: use CSV writer.  Go to https://docs.python.org/3/library/csv.html and read how to use it.
# 2) Save the CSV file and verify the column is present in the new file


#! /usr/bin/env python3
import sys
import csv
from geopy.geocoders import Nominatim

FILE_NAME = 'FL_insurance_sample.csv'
DELIMITER = ','


def main():
    with open(FILE_NAME, newline='') as csv_file:
        geolocator = Nominatim()
        csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
        for row in csv_reader:
            # Note: there is a slightly better way to do the unpacking here.
            # Can you think of a better type of tuple to use?
            policy_id, *_, point_latitude, point_longitude, line, construction, point_granularity = row
            print(policy_id, point_latitude, point_longitude)
            try:
                print(geolocator.reverse(point_latitude + ', ' + point_longitude))
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
