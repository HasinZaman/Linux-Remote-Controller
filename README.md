# Linux Remote Controller
 
## Description
Python application that permits devices on the local network to act as an input devices. The input devices are capable of changing volume, keyboard, and mouse.

# Installation 

# 1.  Installation
 ## 1.1 Import Libaries
 ```
  sudo apt-get install python3-alsaaudio
 ```
 ```
  sudo apt-get install python3-qrcode[pil]
 ```
 ```
  sudo apt-get install xdotool
  ```
 ## 1.2 Download files
 The files can be downloaded and placed anywhere
# 2. Run server for the first time
 ## 2.1 Run server.py for the First Time
 ```
  python3 Server.py
 ```
 ## 2.2 Insert Server IP Address
 To find the IP address of the server. First open Settings > Wifi > gear icon beside the connected wifi address. The IP of the server is the IPv4 address.
# 3. Set up on start up
 ## 3.1 Open crontab file
 Open crontab in terminal
 ```
  sudo crontab -e
 ```
 
 ## 3.2 Add Server.py to Crontab File
 ```
  @reboot python3 /Server.py &
 ```
