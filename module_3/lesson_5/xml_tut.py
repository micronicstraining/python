#! /usr/bin/env python3

# Lab: Solve Hacker Rank XML problems

# See https://docs.python.org/3.6/library/xml.etree.elementtree.html for more details

import xml.etree.ElementTree as ET

# This is like the JSON.loads
tree = ET.parse('country.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)


print(root[0][1].text)

# buidling XML
data = ET.Element('data')
country = ET.SubElement(data, 'country')
rank = ET.SubElement(country, 'rank')
year = ET.SubElement(country, 'year')
print(ET.dump(data))

# def xml_dumps(self):
#      pass
# <point>
#   <x>5</x>
#   <y>15</y>
# </point>
# Will go over following details if asked
# - XML in depth overview
# - XSLT overview, XPATH overview