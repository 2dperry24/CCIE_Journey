from netmiko import ConnectHandler
from dotenv import load_dotenv
import time
load_dotenv()


R1 = {
    "host": "10.10.150.11",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}
R2 = {
    "host": "10.10.150.12",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}
R3 = {
    "host": "10.10.150.13",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios"
}
R4 = {
    "host": "10.10.150.14",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios"
}
R5 = {
    "host": "10.10.150.15",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios"
}
R6 = {
    "host": "10.10.150.16",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios"
}
R7 = {
    "host": "10.10.150.17",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios"
}
R8 = {
    "host": "10.10.150.18",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios"
}
R9 = {
    "host": "10.10.150.19",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios"
}
R10 = {
    "host": "10.10.150.20",
    "port": 22,
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios"
}

routers = [R1] #used to test against a single router
routers = [R1,R2,R3,R4,R5,R6,R7,R8,R9,R10]
for index,router in enumerate(routers):
    #print(routers[index]["host"])
    try:
        c = ConnectHandler(**routers[index])
        c.enable()
        c.send_command("terminal length 0", use_textfsm=False)
        response_1 = c.send_command("show ip int br", use_textfsm=False)
        response_2 = c.send_command("show ip protocols", use_textfsm=False)
        c.disconnect()
    except Exception as ex:
        print(ex)
    else:
        print(response_1)
        print("\n\n")
        print(response_2)
    print("--------------------------------------------------")

