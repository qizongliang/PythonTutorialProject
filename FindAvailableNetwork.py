#Find avaialbe WIFI network
import subprocess

network = subprocess.check_output(['netsh','wlan','show','network'])
decoded_network = network.decode('ascii')
print(decoded_network)
