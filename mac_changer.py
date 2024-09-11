#!/usr/bin/env python
import subprocess

import subprocess

# Nome da interface de rede
interface = input("Interface: ")
# Usuario escolher o novo endereço MAC
new_mac = input("New MAC Addres:")

# Executar o comando e capturar a saída
result = subprocess.run(
    ["ifconfig", interface],
    stdout=subprocess.PIPE,
    text=True
)

# Encontrar e extrair o endereço MAC
output = result.stdout
for line in output.splitlines():
    if "ether" in line:
        current_mac_address = line.split()[1]
        break

# Exibir o endereço MAC Atual
print(f"[+] Your Current MAC Address: {current_mac_address}")
# Mostrar a rede e o novo endereço mac que o usuario esta alterando
print(f"[+] Changing MAC Address for {interface} to {new_mac}")

subprocess.call(f"sudo -S ifconfig {interface} down", shell=True)
subprocess.call(f"sudo -S ifconfig {interface} hw ether {new_mac}", shell=True)
subprocess.call(f"sudo -S ifconfig {interface} up", shell=True)

print(f"[+] MAC Change Successful")