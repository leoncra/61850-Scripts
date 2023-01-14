# ABB IEC61850 SCD FILE ANALYZER 

The script uses the xml.etree.ElementTree library to parse an XML file called 'SCD.scd'. The library provides a way to navigate and modify the XML tree structure.

1.First, it imports the xml.etree.ElementTree library as ET
2.Next, it uses the parse() method from the ET library to parse the 'SCD.scd' file and store the result in a variable called 'tree'.
3.It then uses the getroot() method from the 'tree' variable to get the root element of the XML file and store it in a variable called 'root'.
4.After that, it creates some empty lists (VLAN_ID, APP_ID, MAC_ADD, IP_ADD, TK) to store certain information from the XML file
5.Then it uses a for loop to iterate through each child element of the 'root' variable and checks the tag of the child element.
6.If the tag matches certain conditions, it prints out certain information from the child element and stores it in the previously created lists.
7.After that, it prints out the "IEDs Configuration Report" and "IEC61850 Repeated Parameters Report" that displays certain information from the XML file and repeated values for VLAN-ID, APPID and MAC-Address.

To use this script you need to have the SCD.scd file in the same directory as the script and you should change the name of the file in the script to match the name of the file you have.

Please note that this script is only printing out certain information from the XML file and not doing any modifications on the XML file.
