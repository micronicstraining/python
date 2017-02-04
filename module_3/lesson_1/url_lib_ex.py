#! /usr/bin/env python3
"""
This programs outputs the HTML contents of python.org.

This is basically the HTML data that your browser receives from an HTTP request.
HTML/JSON/XML is the data encapsulated by the application layer (HTTP protocol).
It is used for structuring web content presentation.
"""
import urllib.request


def main():
    response = urllib.request.urlopen('http://python.org/')
    html = response.read()
    print(html)


if __name__ == '__main__':
    main()
