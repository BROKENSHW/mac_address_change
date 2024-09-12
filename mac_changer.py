#!/usr/bin/env python
import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()

# Nome da interface de rede
interface = options.interface
# Usuario escolher o novo endereço MAC
new_mac = options.new_mac

# Mostrar a rede e o novo endereço mac que o usuario esta alterando
print(f"[+] Changing MAC Address for {interface} to {new_mac}")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print(f"[+] MAC Change Successful")
