# PPTP Brute-Force Script
```
 █████╗ ██████╗  █████╗ ██████╗  █████╗ ███╗   ██╗ █████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗
███████║██████╔╝███████║██║  ██║███████║██╔██╗ ██║███████║
██╔══██║██╔═══╝ ██╔══██║██║  ██║██╔══██║██║╚██╗██║██╔══██║
██║  ██║██║     ██║  ██║██████╔╝██║  ██║██║ ╚████║██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
https://www.amnafzar.net/
By: @KalhorAlireza
```
## Overview

This Python script automates the process of establishing a PPTP VPN connection using the `rasdial` command on Windows. It allows you to try multiple username and password combinations from a list or a single username to find a working pair. Results of the connection attempts are saved in a specified file.

## Features

- **Automated VPN Connection:** Connect to a PPTP VPN by providing the connection name, username(s), and passwords.
- **Username and Password Lists:** Test multiple username and password combinations by specifying files containing lists of usernames and passwords.
- **Connection Logging:** The results of successful and failed connection attempts are logged to a specified file.
- **VPN Disconnection:** Automatically disconnects from the VPN after a successful connection attempt.

## Requirements

- **Operating System:** Windows (as the script relies on the `rasdial` command, which is native to Windows)
- **Python Version:** Python 3.x

## Usage

### Command-Line Arguments

The script accepts the following arguments:

- `-c` or `--connection` (required): The name of the VPN connection.
- `-u` or `--username` (optional): A single username for the VPN connection. If not provided, you must supply a list of usernames using the `--list` argument.
- `-l` or `--list` (optional): Path to a file containing a list of usernames, one per line. If this is provided, the `--username` argument is ignored.
- `-p` or `--password-file` (required): Path to a file containing a list of passwords, one per line.
- `-o` or `--output` (required): Path to the file where the results of the connection attempts will be saved.

### Example Usage

- **Single Username and Password List:**
```bash
python BruteForcePPTP.py -c "MyVPN" -u "user1" -p "passwords.txt" -o "results.txt"
```
- **Username List and Password List:**
```bash
python BruteForcePPTP.py -c "MyVPN" -l "usernames.txt" -p "passwords.txt" -o "results.txt"
```