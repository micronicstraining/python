#! /usr/bin/env python3
# pip3 install geopy


""" How to find address given lattitude longitude GPS coordinates. """
from geopy.geocoders import Nominatim

geolocator = Nominatim()
location = geolocator.reverse("52.509669, 13.376294")

print(location.address)

