# RFID-Attendance
Introduction: (Ref)
https://randomnerdtutorials.com/security-access-using-mfrc522-rfid-reader-with-arduino/
-----------------------------------
Description
RFID means radio-frequency identification. RFID uses electromagnetic fields to transfer data over short distances. RFID is useful to identify people, to make transactions, etc…

You can use an RFID system to open a door. For example, only the person with the right information on his card is allowed to enter. An RFID system uses:

tags attached to the object to be identified, in this example we have a keychain and an electromagnetic card. Each tag has his own identification (UID).
tags

![image](https://user-images.githubusercontent.com/45501284/169653632-09eef8ff-ddf4-411b-8ac6-796a3abcb5af.png)


two-way radio transmitter-receiver, the reader, that send a signal to the tag and read its response.

![image](https://user-images.githubusercontent.com/45501284/169653639-063bf0a6-a516-4284-864c-33b4168409a5.png)

--------------------------------------------------------------
readerSpecifications
Input voltage: 3.3V
Frequency: 13.56MHz
-----------------------------------------------
Library download
Here’s the library you need for this project:

Download the RFID library here https://github.com/miguelbalboa/rfid/archive/master.zip created by miguelbalboa
Unzip the RFID library
Install the RFID library in your Arduino IDE
Restart your Arduino IDE

---------------------------------------------------------------------
Pin	Wiring to Arduino Uno
SDA	    Digital 10
SCK	    Digital 13
MOSI	Digital 11
MISO	Digital 12
IRQ	    unconnected
GND	    GND
RST	    Digital 9
3.3V	3.3V
Caution: You must power this device to 3.3V!

![image](https://user-images.githubusercontent.com/45501284/169653721-5460f8c3-9a85-4e33-b4e5-a3eb209c2899.png)

------------------------------------------------------------------

Here we will explain how the system will work:

The system should read from the rfid and store it in an excel file if it is matching the data recorded. 


Steps to follow : 

1) Software requirment: 
    - pyhton3 
    - Arduino IDE 
        - Download library RFID MCR

2) Upload Arduino code rfid.ino and take note for the com number 
3) open the csv folder registered_ids.xlsx 
4) Add you tag id + staff infomration 
5) open python code and modify the com number with your actual com number
6) run the code and scan the rfid tag 
7) close the code then check attendace_report.xlsx 

![image](https://user-images.githubusercontent.com/45501284/167119227-fb1b1858-f6ec-4512-bf5d-728ac4e3861c.png)
