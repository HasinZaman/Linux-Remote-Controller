# Linux Remote Controller
 
## Description
Python application that permits devices on the local network to act as an input devices. The input devices are capable of changing volume, keyboard, and mouse by default. Other applications can be added to the Linux Remote Controller.

# Installation 

# 1  Installation
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
# 2 Run server for the first time
## 2.1 Run server.py for the First Time
```
python3 Server.py
```
## 2.2 Insert Server IP Address
To find the IP address of the server. First open Settings > Wifi > gear icon beside the connected wifi address. The IP of the server is the IPv4 address.
# 3 Set upon startup (Optional)
**Recommended**: Setting up 
## 3.1 Open crontab file
Open crontab in terminal
```
sudo crontab -e
``` 
## 3.2 Add Server.py to Crontab File
```
@reboot python3 /Server.py &
```
# How To Use

## 1 Joining for the first time
### 1.1 Manual
Write down the server IP address and port in a browser. The IP and Port are printed in a console by the Server.py
Example:
```
0.0.0.0:8080
```
### 1.2 QR Code
Every menu contains a QR code of the server address. Therefore, users can scan the QR code from another device to connect.
## 2 Save Address as Bookmark (Optional)
**Recommended**: Saving the page as a bookmark saves a significant amount of time and resources in connecting the server.
## 2 Menu
All the applications that can be handled by the server are stored underneath the QR Code.
## 3 Applications
### 3.1 Mouse Controller
The Mouse Controller is a means of controlling the mouse on the server. The Mouse Controller works as a virtual touchpad found on laptops. In which, the large square controls the movement of the mouse, and the two smaller buttons on the bottom control the left-click and right-click.
### 3.2 Keyboard Controller
The Keyboard Controller is a means of inputting letters and numbers on the server. The Keyboard Controller page has one text area and two buttons. Putting characters in the text area automatically simulates the associated keypress on the server. The enter and backspace buttons simulate enter and backspace keys.
### 3.3 Volume Controller
The Volume Controller is a means of controlling volume and other media features. The Volume Controller page possesses six buttons and one volume bar. The buttons control volume up, volume down, volume mute, skip to next, skip to previous, and pause-play. A red volume bar means that the server is muted.
# New Applications
The Server.py file automatically adds a new application when first running. Three files need to make a new application.
## 1 Server-side Python file
There should be a python script with the pages directory. The file needs to import Page abstract class. Followed by the declaration of a Controller class that implements the action abstract method. The action method should check if a POST call comes from the correct page. The __init__ method should declare self.name of the source page. Finally, the page should have a variable called page, which stores an instance of the created Page child class.
```python
from Page import *

class Controller(Page):
	def __init__(self):
	 	self.name = "Controller"
	def action(self, data, response):
		if self.validActionSource(data["page"]):
		pass

page = Controller()
```
## 2 Directory
A directory needs to be created to store the client-side page. The directory needs to have the same name as self.name.

## 3 Client Page
A HTML page should be created with the name assigned self.name. The should be formated in the following.
```HTML
<!DOCTYPE html>
<html>
	<head>
		<title>Volume Controller</title>
		<link rel="stylesheet" type="text/css" href="res/css/style.css">
		<link rel="stylesheet" type="text/css" href="pages/VolumeController/res/css/style.css">
	<body>
		<div class="remote">
			[UI CONTENT]
		</div>
		<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
		<script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
		<script src="pages/VolumeController/res/javascript/Controller.js"></script>
	</body>
</html>
```
**NOTE**: The format of the client page is irrelevant and straying from the template above does not break the application. It merely means the developer has to do more CSS.

## 4 Ajax
All Ajax calls should be formated as followed. The Page should be self.name instance defined in the server-side python file. The action should be the name of a method or a specific action to be done in the server-side python file.
```
$.ajax
({
	type:"POST",
	data:
	{
		page: [self.name from server side python script],
		action: [action that is being requested],
		optional param 1: val 1,
		...
		optional param n: val n,
	}
})
```
