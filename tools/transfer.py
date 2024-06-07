import os
import tkinter as tk
from tkinter import filedialog
import paramiko
from scp import SCPClient
import argparse
from getpass import getpass

# Mapping of file extensions to directories
EXTENSION_MAP = {
    '.nes': 'FC',
    '.sfc': 'SFC',
    '.gba': 'GBA',
    '.gb': 'GB',
    '.gbc': 'GBC',
    '.nds': 'NDS',
    # Add more extensions and corresponding directories here
}

# SCP and SSH configuration
REMOTE_PORT = 22
REMOTE_BASE_DIR = '/mnt/mmc/Roms'

def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(server, port, user, password)
    return client

def get_destination_dir(extension):
    return EXTENSION_MAP.get(extension, None)

def main():
    parser = argparse.ArgumentParser(description='Transfer files to a remote host via SCP.')
    parser.add_argument('remote_host', type=str, help='The IP address of the remote host.')
    parser.add_argument('-u', '--username', type=str, default='root', help='The SSH username.')
    args = parser.parse_args()

    # Retrieve the remote host and username from command-line arguments
    remote_host = args.remote_host
    remote_user = args.username

    # Prompt for the password
    remote_pass = getpass(prompt='Enter SSH password: ')

    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select files
    file_paths = filedialog.askopenfilenames(
        title='Select files to transfer',
        filetypes=[("All Files", "*.*"), 
                   ("NES Files", "*.nes"),
                   ("SFC Files", "*.sfc"),
                   ("GBA Files", "*.gba"),
                   ("GB Files", "*.gb"),
                   ("GBC Files", "*.gbc"),
                   ("NDS Files", "*.nds")]
    )

    if not file_paths:
        print("No files selected.")
        return

    try:
        # Create SSH and SCP clients
        ssh = create_ssh_client(remote_host, REMOTE_PORT, remote_user, remote_pass)
        scp = SCPClient(ssh.get_transport())

        for file_path in file_paths:
            file_extension = os.path.splitext(file_path)[1]
            destination_dir = get_destination_dir(file_extension)

            if not destination_dir:
                print(f"No destination directory mapping for file extension: {file_extension}")
                continue

            remote_path = os.path.join(REMOTE_BASE_DIR, destination_dir)
            print(f"Transferring {file_path} to {remote_path}")

            # Ensure the remote directory exists
            ssh.exec_command(f'mkdir -p {remote_path}')
            
            # Transfer file to the destination directory on the remote device
            scp.put(file_path, remote_path)
    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication failed. Please check your username and password.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'scp' in locals():
            scp.close()
        if 'ssh' in locals():
            ssh.close()

if __name__ == '__main__':
    main()
