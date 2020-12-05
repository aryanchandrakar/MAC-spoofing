#!/user/bin/env/ python
import subprocess
import optparse
import re

def get_arguments():
    # to handle user input
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change mac address")
    parser.add_option("-m", "--mac", dest="mac", help="new mac address")

    # to take the input arguments,options in variables to access later
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # if options.interface does not hold the value
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.mac:
        # if options.mac does not hold the value
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


def change_mac(inter, macc):
    # unsecure
    # subprocess.call("ifconfig "+interface+" down", shell=True)
    # subprocess.call("ifconfig "+interface+" hw ether "+mac, shell=True)
    # subprocess.call("ifconfig "+interface+" up", shell=True)

    # secure
    subprocess.call(["ifconfig", inter, "down"])
    subprocess.call(["ifconfig", inter, "hw", "ether", macc])
    subprocess.call(["ifconfig", inter, "up"])
    print("[+]Changing MAC address to "+macc)

def get_currentmac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # print(ifconfig_result)

    macadd_serach = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if macadd_serach:
        return macadd_serach.group(0)
    else:
        print("[-]Could not read MAC address!")

options = get_arguments()
current_mac=get_currentmac(options.interface)
print("Current MAC = "+str(current_mac))
change_mac(options.interface, options.mac)
current_mac=get_currentmac(options.interface)
if current_mac==options.mac:
    print("[+]MAC address was successfully changed to "+ current_mac)
else:
    print("[-]MAC did not get change.")
