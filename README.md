# Exiled
Exiled is a tool used to compromise and scan networks and computers. 
## Directory
- <a href="https://github.com/FlynAber/Exiled#Installation-and-Usage">Installation and Usage</a>
- <a href="https://github.com/FlynAber/Exiled#Features">Features</a>
- <a href="https://github.com/FlynAber/Exiled#exiled-server-commands">Exiled Server Commands</a>
## Installation and Usage
To install Exiled run the command:
```
git clone https://github.com/FlynAber/Exiled
```
Then to run Exiled enter the Exiled Directory and run :
```
python3 exiled
```
## Features
### Features Directory
- <a href="https://github.com/FlynAber/Exiled#IP-scanner">IP Scanner</a>
- <a href="https://github.com/FlynAber/Exiled#DOS">DOS</a>
- <a href="https://github.com/FlynAber/Exiled#Port-Scanner">Port Scanner</a>
- <a href="https://github.com/FlynAber/Exiled#Exiled-server">Exiled server</a>
### IP scanner
- IP scanner to scan a network for all operating IP addresses
### DOS
- Denial of Service attack (DOS) to flood the network with packets causing it to slow down considerably
### Port Scanner
- Scans a target computer or server for open ports
### Exiled server
- The Exiled server is hosted on your computer and is used in conjunction with the Exiled payload to gain access to a target computer and gather information.
- See <a href="https://github.com/FlynAber/Exiled#exiled-server-commands">Exiled server Commands</a> for a list of commands
## Exiled Server Commands
**Note: all commands can be viewed with the `help` command**
## Change line 64 in Exiled_pay.py to your IP address to allow connections. This is temporary until I add a method to create a new python file
### Windows CMD commands
 - for a full list of command prompt commands see <a href="https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands">Here</a>
### Change Directory
Change the current working directory of the shell on the target computer :
```
cd <directory>
```
### Downloading and uploading files
Download a file off the target computer
```
download <directory>
```
Upload a file to the target computer
```
upload <directory>
```
**Note: Directory can be found with the command `dir`** 
### Screenshot
Screenshot and save what is displayed to the target's screen
```
screenshot
```
### Key logging
start a keylogger on the target computer:
```
keys
```
Stop the keylogger:
```
keys_stop
```
**Note: The keys will be displayed once the `keys_stop` command has been issued**

#### WARNING: Don't use if you don't have permission from the target, I'm not responsible for any damages caused.
