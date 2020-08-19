import requests
import json
from pprint import pprint
import xml.etree.ElementTree as ET

url = "https://endpoints.office.com/endpoints/worldwide?noipv6&ClientRequestId=b10c5ed1-bad1-445f-b386-b919946339a7"
filename = "aliases.xml"
dest_alias_name = "Microsoft_365_Services"

r = requests.get(url)
json_data = json.loads(r.text)

ip_list = []
count = 0
for block in json_data:
    for key, value in block.items():
        if key == "ips":
            for ip in value:
                ip_list.append(ip)

print(str(len(ip_list)))

tree = ET.parse(filename)
root = tree.getroot()
block_exists = False

#Prepare Addresses String
addresses_string = ""
for ip in ip_list:
    addresses_string = addresses_string + ip + " "
addresses_string = addresses_string[:-1]

for alias in root.findall("alias"):
    name = alias.find("name").text
    if name == dest_alias_name:
        block_exists = True
        addresses = alias.find("address")
        addresses.text = addresses_string

        
tree.write(filename)
  

           