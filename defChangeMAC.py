#!/usr/bin/env python
import subprocess

#Função para alterar o MAC - altera o mac com base no argumento do user
def change_mac(interface, new_mac):
    print(f"[+] Changing MAC Address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])