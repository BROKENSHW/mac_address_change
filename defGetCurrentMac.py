#!/usr/bin/env python
import subprocess
import re

def get_current_mac(interface):
    # Obtendo a saída do comando
    result_change = subprocess.check_output(["ifconfig", interface])

    # Decodificando a saída dos bytes para uma string
    result_change = result_change.decode('utf-8')

    # Expressão regular para corresponder a um endereço MAC
    pattern = r'[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}'

    # Pesquisa usando a expressão regular
    match = re.search(pattern, result_change)

    if match:
        return match.group()
    else:
        print("Could not read MAC Address")
        pass