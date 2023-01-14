import xml.etree.ElementTree as ET

# parse the xml file
tree = ET.parse('SCD.scd')

# get the root element of the xml file
root = tree.getroot()

# lists to store certain information from the xml file
VLAN_ID = []
APP_ID = []
MAC_ADD = []
IP_ADD = []
TK = []

# print out the "IEDs Configuration Report"
print('-'*50)
print('IEDs CONFIGURATION REPORT')
print('-'*50)

# iterate through each child element of the root
for child in root.iter():
    # check the tag of the child element
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}ConnectedAP':
        print('-'*50)
        print('Technical key:', child.attrib['iedName'])
        TK.append(child.attrib['iedName'])
        print('Access Point Name:', child.attrib['apName'])

        # check if the child element has 'redProt' attribute
        if 'redProt' in child.attrib:
            print('Redundancy Protocol:', child.attrib['redProt'])
        else:
            print('Redundancy Protocol:', 'None')
            print()

    # check the tag and attribute of the child element
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}P':
        if child.attrib['type'] == 'IP':
            print('IP:', child.text)
            IP_ADD.append(child.text)
        if child.attrib['type'] == 'IP-SUBNET':
            print('IP-Subnet:', child.text)
        if child.attrib['type'] == 'IP-GATEWAY':
            print('IP-Gateway:', child.text)
            print()

    # check the tag of the child element
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}GSE':
        print('GCB:', child.attrib['cbName'])
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}MinTime':
        print('GOOSE Min Time:', child.text)
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}MaxTime':
        print('GOOSE Max Time:', child.text)
        print()

    # check the tag of the child element
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}SMV':
        print('SMV:', child.attrib['cbName'])
        print()

    # check the tag and attribute of the child element
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}P':
        if child.attrib['type'] == 'VLAN-ID':
            print('VLAN-ID (HEX):', child.text)
            VLAN_ID.append(child.text)
        if child.attrib['type'] == 'VLAN-PRIORITY':
            print('VLAN-PRIORITY:', child.text)
        if child.attrib['type'] == 'MAC-Address':
            print('MAC-Address:', child.text)
            MAC_ADD.append(child.text)
        if child.attrib['type'] == 'APPID':
            print('APPID:', child.text)
            APP_ID.append(child.text)
            print()
            
# print out the "IEC61850 Repeated Parameters Report"
print('-'*50)
print('IEC61850 REPEATED PARAMETERS REPORT')
print('-'*50)
print()

# print out repeated VLAN-ID values
print('-'*50)
VLAN_ID_COUNT = dict((x,VLAN_ID.count(x)) for x in set(VLAN_ID))
print('VLAN ID','|', 'Repeated')
print('-'*50)
for k, v in VLAN_ID_COUNT.items():
    if v > 1:
        print(k,'|', v)
print()

# print out repeated APPID values
print('-'*50)
APPID_COUNT = dict((x,APP_ID.count(x)) for x in set(APP_ID))
print('APPID', '|', 'Repeated')
print('-'*50)
for k, v in APPID_COUNT.items():
    if v > 1:
        print(k,'|', v)
print()

# print out repeated MAC-Address values
print('-'*50)
MACADD_COUNT = dict((x,MAC_ADD.count(x)) for x in set(MAC_ADD))
print('MAC-Address', '|', 'Repeated')
print('-'*50)
for k, v in MACADD_COUNT.items():
    if v > 1:
        print(k,'|', v)

