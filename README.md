# Simple port scanner written in Python
A simple TCP port scanner written in Python as part of my leanring proccess on the basics of networking in Python. It includes features such as different scanning modes, multithreading, and command-line execution using arguments
## Requirements
- Python 3.x (no external libraries required)
## Scanning modes
- **Single port mode**: check if a specific port is open or closed
- **Range mode**: scans a consecutive range of ports (e.g., '20-100') and shows the status of each port.
# Using
### Single port mode
```bash
python port_scanner.py <ip> -p <port>
```
### Range mode
```bash
python port_scanner.py <ip> -r <start-end>
```
## Examples
### Single port mode
```bash
python port_scanner.py 192.168.1.1 -p 80
```
### Range mode
```bash
python port_scanner.py 192.168.1.1 -r 20-100
```
_Created in the 1st year of study_
