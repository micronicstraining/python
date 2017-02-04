#! /usr/bin/env python3
"""
Look at the URL which shows a JSON data.
The data has the best IT tech jobs in US per city.
Each city has 3 different types of jobs.
Average the results per city and print them out.
"""
import json
from urllib import request
import my_module

# Get JSON contents using urllib (see url_lib_ex.py)
URL = 'http://mysafeinfo.com/api/data?list=us_bestitjobcities2015&format=json'


def avg_sal(sal1, sal2, sal3):

    if sal1 < 90000:
        raise ValueError('Divide by Zero')

    return (sal1+sal2+sal3)/3


def main():
    response = request.urlopen(URL)
    json_data = response.read()
    # load array
    data = json.loads(json_data.decode("utf-8"))
    for item in data:
        avg = avg_sal(
            sal1=item['sal1'],
            sal2=item['sal2'],
            sal3=item['sal3']
        )
        item['avgsal'] = avg
        print(item)

if __name__ == '__main__':
    main()
