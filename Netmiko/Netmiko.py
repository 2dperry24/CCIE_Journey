from netmiko import ConnectHandler
#from dotenv import load_dotenv
import time
import os
#load_dotenv()

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


def changeToLoginLocal(inputFile):
    # Need to make sure each router config doesn't lock me out 
    # of my backplane connection issuing a "no login" on the VTY lines. 
    read_file = open(inputFile, 'r')
    copy_file = open("cleanedFile.txt", 'w')
    read_lines = read_file.readlines()

    for line in read_lines:
        if "no login" in line or "No Login" in line or "NO LOGIN" in line:
            copy_file.write("login local")
        else:
            copy_file.write(line)

    copy_file.close()
    read_file.close()









foundation_lab_1_initial_configs = "/home/user/Documents/INE_CCIE_LABS/ine.ccie.rsv5.workbook.initial.configs/advanced.foundation.labs/foundation.lab.1.initial.configs/"
initial_BGP = "/home/user/Documents/INE_CCIE_LABS/ine.ccie.rsv5.workbook.initial.configs/advanced.technology.labs/initial.bgp/"
ebgp_with_R9_to_R10 = "/home/user/Documents/INE_CCIE_LABS/ine.ccie.rsv5.workbook.initial.configs/advanced.technology.labs/ebgp.with.r9.to.r10/"


#routers = [R1,R2] # used to test a couple routers and not all devices
routers = [R1,R2,R3,R4,R5,R6,R7,R8,R9,R10]
routerFiles = ["R1.txt","R2.txt","R3.txt","R4.txt","R5.txt","R6.txt","R7.txt","R8.txt","R9.txt","R10.txt"]
for index,router in enumerate(routers):
    #print(routers[index]["host"])
    try:
        c = ConnectHandler(**routers[index])
        c.enable()
        directoryToUse = initial_BGP
        file_to_send = directoryToUse + routerFiles[index]
        os.chdir(directoryToUse)
        #print(file_to_send)
        changeToLoginLocal(file_to_send)
        c.send_config_from_file(directoryToUse + "cleanedFile.txt")
        time.sleep(3)
        response = c.send_command("show ip int br", use_textfsm=False)
        c.disconnect()
    except Exception as ex:
        print(ex)
    else:
        print(response)
    print("--------------------------------------------------")
        