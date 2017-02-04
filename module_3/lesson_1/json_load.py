#! /usr/bin/env python3
import json


FILE = 'output_data_model.json'


def main():
    with open(FILE,mode='r') as f:
        json_data = f.read()
        print("JSON data", json_data, type(json_data))

        input('')
        data_model = json.loads(json_data)
        print("Data model")
        print(type(data_model))

        # print out key value pairs
        for k, v in data_model.items():
            print(k)
            print(v)

        # Change John's email
        key = 'John Doe'
        if key in data_model['customerEmail']:
            data_model['customerEmail'][key] = 'john@johndoe.com'
            print('Changed John Does email!')

if __name__ == '__main__':
    main()
