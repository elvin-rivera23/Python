"""

Created by: Elvin Rivera
Date: 11/2/2020

Description: Python practice to use netmiko to connect to IOS Router

"""


import NetmikoConnect

connection = NetmikoConnect.connection(ip="192.168.1.210", device_type="cisco_ios",
                                    username="Elvin", password="Password1")

print(connection.send_command("sh ip int brief"))
connection.disconnect()