#!/usr/bin/env python3

import os
import netifaces
import re
import subprocess

# For Output formatting
line_length = 90
separator_01 = "=" * line_length
separator_02 = "-" * line_length


def get_available_interfaces():
    # Get a list of available interfaces with their current MAC addresses
    interfaces = netifaces.interfaces()
    available_interfaces = []
    for interface in interfaces:
        if interface != "lo":
            current_mac = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]["addr"]
            available_interfaces.append((interface, current_mac))
    return available_interfaces


def display_available_interfaces():
    # Display the available interfaces with their current MAC addresses
    print(f"{separator_01} \n")
    print("Available Interfaces:")
    print(separator_02)
    for interface, current_mac in get_available_interfaces():
        print(f"| Interface: {interface}   [{current_mac}]")
    print(f"{separator_02}\n")


def get_selected_interface():
    # Prompt the user to enter a valid interface from the available options
    while True:
        selected_interface = input("Enter Interface: ")
        if selected_interface in [interface[0] for interface in get_available_interfaces()]:
            return selected_interface
        else:
            print(f"| Interface {selected_interface} does not exist. Please enter a valid interface!")
            print(f"| Available: {[interface[0] for interface in get_available_interfaces()]}\n")


def get_new_mac():
    # Prompt the user to enter a valid MAC address
    pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    while True:
        new_mac = input("Enter new MAC: ").lower()
        if re.match(pattern, new_mac):
            return new_mac
        else:
            print("| Invalid MAC!\n")


def change_mac_address(selected_interface, new_mac):
    # Change the MAC address of the selected interface
    subprocess.run(f"ifconfig {selected_interface} down", shell=True)
    subprocess.run(f"ifconfig {selected_interface} hw ether {new_mac}", shell=True)
    subprocess.run(f"ifconfig {selected_interface} up", shell=True)


def main():
    # Check if the user is running the script as root
    if os.getuid() != 0:
        print(separator_01)
        print("!!! This Application Can't run with standard user privileges !!!".center(line_length))
        print("Please try again with root!".center(line_length))
        print(separator_01)
        exit()

    # Description and instructions for the user
    print(separator_01)
    print("MAC Address Changer".center(line_length))
    print("[By SahanEra | https://sahanera.me]".center(line_length))
    print(separator_01)
    print("This application allows you to change the MAC address of a network interface in Linux.\n".center(line_length))
    print("Instructions:".center(line_length))
    print(f"1. Select the interface you want to change the MAC address for from the available options.")
    print(f"2. Enter the new MAC address you want to set.")
    print(f"3. The script will change the MAC address of the selected interface.")
    print(separator_01)

    # Display available interfaces
    display_available_interfaces()

    # Get selected interface from user
    selected_interface = get_selected_interface()

    # Get new MAC address from user
    new_mac = get_new_mac()

    # Change MAC address
    change_mac_address(selected_interface, new_mac)

    # Check status
    changed_mac = netifaces.ifaddresses(selected_interface)[netifaces.AF_LINK][0]["addr"]
    if changed_mac == new_mac:
        print(f"Interface {selected_interface} MAC address changed to {changed_mac}\n")
        print(separator_01)
    else:
        print("Something went wrong! Please try again.\n")
        print(separator_01)
        exit()


if __name__ == "__main__":
    main()
