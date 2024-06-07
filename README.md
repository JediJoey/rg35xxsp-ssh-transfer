# RG35XXSP SSH Transfer
Fork from https://github.com/xgbox/rg35xxsp-ssh-samba/ that uses scp to transfer roms onto the device in a user friendly manner.

`RG35XXSP SSH Transfer` is a Python utility that allows you to transfer ROM files to a remote host via SCP, organizing them into specific directories based on their file extensions.

## Features

- **File Transfer via SCP**: Securely transfer files to a remote host using SSH and SCP.
- **File Type Organization**: Automatically organizes files into directories based on their extensions.
- **GUI File Selection**: Use a file dialog to select files to transfer.

## Supported File Types

- `.nes` -> `FC`
- `.sfc` -> `SFC`
- `.gba` -> `GBA`
- `.gb` -> `GB`
- `.gbc` -> `GBC`
- `.nds` -> `NDS`

## Installation

Clone the repository and navigate to the project directory:

```sh
git clone <repository_url>
cd <project_directory>
```
Build and install the package using the provided Makefile:

```sh
make build
```

## Usage
To use the transfer tool, run the following command:

```sh
python3 tools/transfer.py <remote_host> -u <username>
```

Replace <remote_host> with the IP address of the remote host and <username> with your SSH username (default is root).

You will be prompted to enter your SSH password and to select files using a file dialog.

### Example
```sh
python3 tools/transfer.py 192.168.1.88 -u root
```
