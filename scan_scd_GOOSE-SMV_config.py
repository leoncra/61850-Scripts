### THIS SCRIPT IS USED TO QUICKLY NAVIGATE THROUGH AN ABB SCD FILE AND IDENTIFY POSSIBLE MISTAKES IN THE IEC61850 CONFIGURATION

# INSTRUCTIONS
# Rename the exported .scd file as SCD and put it in the same directory as the script
# Run the script and analyze the results

import xml.etree.ElementTree as ET

tree = ET.parse('SCD.scd')
root = tree.getroot()

VLAN_ID = []
APP_ID = []
MAC_ADD = []
IP_ADD = []
TK = []

print('-'*50)
print('IEDs CONFIGURATION REPORT')
print('-'*50)

for child in root.iter():
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}ConnectedAP':
        print('-'*50)
        print('Technical key:', child.attrib['iedName'])
        TK.append(child.attrib['iedName'])
        print('Access Point Name:', child.attrib['apName'])

        if 'redProt' in child.attrib:
            print('Redundancy Protocol:', child.attrib['redProt'])
        else:
            print('Redundancy Protocol:', 'None')
            print()

    if child.tag == '{http://www.iec.ch/61850/2003/SCL}P':
        if child.attrib['type'] == 'IP':
            print('IP:', child.text)
            IP_ADD.append(child.text)
        if child.attrib['type'] == 'IP-SUBNET':
            print('IP-Subnet:', child.text)
        if child.attrib['type'] == 'IP-GATEWAY':
            print('IP-Gateway:', child.text)
            print()

    if child.tag == '{http://www.iec.ch/61850/2003/SCL}GSE':
        print('GCB:', child.attrib['cbName'])
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}MinTime':
        print('GOOSE Min Time:', child.text)
    if child.tag == '{http://www.iec.ch/61850/2003/SCL}MaxTime':
        print('GOOSE Max Time:', child.text)
        print()

    if child.tag == '{http://www.iec.ch/61850/2003/SCL}SMV':
        print('SMV:', child.attrib['cbName'])
        print()

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
print('-'*50)

print('-'*50)
print('IEC61850 REPEATED PARAMETERS REPORT')
print('-'*50)
print()

print('-'*50)
VLAN_ID_COUNT = dict((x,VLAN_ID.count(x)) for x in set(VLAN_ID))
print('VLAN ID','|', 'Repeated')
print('-'*50)
for k, v in VLAN_ID_COUNT.items():
    if v > 1:
        print(k,'|', v)
print()

print('-'*50)
APPID_COUNT = dict((x,APP_ID.count(x)) for x in set(APP_ID))
print('APPID', '|', 'Repeated')
print('-'*50)
for k, v in APPID_COUNT.items():
    if v > 1:
        print(k,'|', v)
print()

print('-'*50)
MACADD_COUNT = dict((x,MAC_ADD.count(x)) for x in set(MAC_ADD))
print('MAC-ADDRESS','|', 'Repeated')
print('-'*50)
for k, v in MACADD_COUNT.items():
    if v > 1:
        print(k,'|', v)
print()

print('-'*50)
IP_ADD_COUNT = dict((x,IP_ADD.count(x)) for x in set(IP_ADD))
print('IP ADDRESS','|', 'Repeated')
print('-'*50)
for k, v in IP_ADD_COUNT.items():
    if v > 1:
        print(k,'|', v)
print()

print('-'*50)
TK_COUNT = dict((x,TK.count(x)) for x in set(TK))
print('TECHNICAL KEYS','|', 'Repeated')
print('-'*50)
for k, v in TK_COUNT.items():
    if v > 1:
        print(k,'|', v)
print()
