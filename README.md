# SSH Brute Force Script

This Python script attempts to brute force SSH login credentials by trying multiple passwords from a provided file. It utilizes the `pwntools` library to interact with the SSH service and the `termcolor` library to colorize output in the terminal.

## Features

- **Host Input**: Specify the target host IP address.
- **Username Input**: Provide the username for the SSH connection.
- **Password List**: Provide a file containing a list of passwords to attempt or can use the default file containing password(passwordfile.txt).
- **Port Selection**: Option to specify a custom port (defaults to port 22).
- **Colored Output**: Success messages are displayed in green for easy identification.

## Prerequisites

Ensure that you have the following Python packages installed:

- `pwntools`: `pip install pwntools`
- `termcolor`: `pip install termcolor`

## Usage

To use the script, follow the instructions below.

### Basic Command

```bash
python script.py <host> -u <username> -P <passwordfile> [-p <port>]
