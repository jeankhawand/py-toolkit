import xml.etree.ElementTree as ET
import pprint

if __name__ == "__main__":
    # looking for all users emails
    tree = ET.parse('../assets/dataset.xml')
    root = tree.getroot()
    # return all elements
    users = root.findall('./record')
    for user in users:
        pprint.pprint(user.find('email').text)


