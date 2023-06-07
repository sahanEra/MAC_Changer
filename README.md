# MAC Address Changer

This is a Python script that allows you to change the MAC address of a network interface in Linux.

## Description

This script provides a simple command-line interface for changing the MAC address of a network interface in Linux. It uses the `ifconfig` command to bring down the interface, set the new MAC address, and bring the interface back up.

## Features

- Display the available network interfaces along with their current MAC addresses.
- Prompt the user to select an interface and enter a new MAC address.
- Validate the MAC address format.
- Change the MAC address of the selected interface.
- Verify the MAC address has been successfully changed.

## Prerequisites

- Linux OS
- Python 3

## Usage

1. Clone the repository:
```
git clone https://github.com/sahanEra/MAC_Changer.git
```

2. Change into the project directory:
```
cd MAC_Changer
```

3. Add execute permission to the script:
```
chmod +x mac_changer.py
```

4. Run the script with root privileges:
```
sudo ./mac_changer.py
```
**Note:** The script requires root privileges to modify network interface settings.


5. Follow the instructions provided by the script to select an interface and enter a new MAC address.

## Author

- [SahanEra](https://sahanera.me)

## License

This project is licensed under the [MIT License](LICENSE).
