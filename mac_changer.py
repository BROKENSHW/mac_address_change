#!/usr/bin/env python
import defChangeMAC
import defGetArguments
import defGetCurrentMac

options = defGetArguments.get_arguments()

current_mac = defGetCurrentMac.get_current_mac(options.interface)
print(f"[+] Current MAC: {str(current_mac)}")

defChangeMAC.change_mac(options.interface, options.new_mac)

current_mac = defGetCurrentMac.get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f"[+] MAC Address was sucessfully changed to {current_mac} ")
else:
    print(f"[-] MAC Address did not get changed.")