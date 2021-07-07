# -*- coding: utf-8 -*-
"""

@author: Lakshmi Priya
"""

import tkinter as tk
from tkinter import messagebox
import geocoder
from twilio.rest import Client
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import time
import os
from twilio.rest import Client

lst=[]

geolocator = Nominatim(user_agent="Shield Of Security (SOS)")
source = geolocator.geocode("Westin Chennai")
dest = geolocator.geocode("tambaram railway station")
scode = (source.latitude, source.longitude)
dcode = (dest.latitude, dest.longitude)

currloc = scode


def sms(msg,number):
	account_sid = "<<Enter twilio account sid>>"
	auth_token = "<<Enter twilio auth token>>"
	client = Client(account_sid, auth_token)

	message = client.messages \
                	.create(
                     	body=msg,
                     	from_='+12562545424',
                     	#to='+919042330345'
                     	to=number
                 	)

#inp=input("Enter Message : ")
#number=input("Enter Number : ")
#sms(inp,number)

def whatsapp(msg,number):
	from twilio.rest import Client
	account_sid = "<<Enter twilio account sid>>"
	auth_token = "<<Enter twilio auth token>>"
	client = Client(account_sid, auth_token)

	from_whatsapp_number='whatsapp:+14155238886'
	to_whatsapp_number='whatsapp:'+number

	client.messages.create(
              	from_=from_whatsapp_number,
              	body=msg,
              	to=to_whatsapp_number)

#inp=input("Enter Message : ")
#number=input("Enter Number : ")
#whatsapp(inp,number)

def sosFunction():
	msg = "\nDeviation detected!!!\n" + "Location Coordinates: " +  str(currloc)
	for number in lst[1:3]:
		sms(msg,number)
		whatsapp(msg, number)

def showMsg():  
	messagebox.showinfo('Message', 'You clicked the Submit button!', font=("Helvetica", 32))
	sosFunction()

fields = 'Name', 'Emergency contact 1', 'Emergency contact 2', 'Country'

def fetch(entries):
	lst=[]
	for entry in entries:
		field = entry[0]
		text  = entry[1].get()
		print('%s: "%s"' % (field, text))
		lst.append(text)
	print(lst)
 

def makeform(root, fields):
	entries = []
	for field in fields:
		row = tk.Frame(root)
		lab = tk.Label(row, width=15, text=field, anchor='w', font=("Helvetica", 32))
		ent = tk.Entry(row, font=("Helvetica", 32))
		row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
		lab.pack(side=tk.LEFT)
		ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
		entries.append((field, ent))
	return entries

root = tk.Tk()
root.title('SHIELD OF SECURITY (S.O.S)')
#root.geometry('400x150')  

ents = makeform(root, fields)
b1 = tk.Button(root, text='Submit', font=("Helvetica", 32), command=(lambda e=ents: fetch(e)))
b1.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()

tkWindow = tk.Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Shield Of Security (SOS)')

def showMsg():  
	messagebox.showinfo('Message', 'SOS ACTIVATED!\nEmergency contacts alearted!')

button = tk.Button(tkWindow, text = 'SOS', font=("Helvetica", 32), command = showMsg)  
button.pack()  
tkWindow.mainloop()



print(source.address)
print()
print(dest.address)
print()

dist = great_circle(scode, dcode).miles
print(great_circle(scode, dcode).miles)

t1 = 5

count1 = 0
count2 = 0

while(True):
   	 
	time.sleep(t1)
	newloc = list(map(lambda x : x + 0, currloc))
	travelled = great_circle(currloc, newloc).miles
	currloc = newloc
	newdist = great_circle(currloc, dcode).miles
	if (newdist == 0 ):
		print("Destination Reached!!!")
		break
    
	if (newdist > dist):
		count2 += 1
		if(count2 == 4):
			msg = "\nDeviation detected!!!\n" + "Location Coordinates: " +  str(currloc)
			for number in lst[1:3]:
				sms(msg,number)
			print(msg)
  	 
	else:
		count2 = 0
   	 
	if(travelled == 0):
		count1 += 1
		if (count1 == 4):
			msg = "\nStagnation detected!!!\n" +  "Location Address:" + str(geolocator.reverse(str(currloc[0]) + ", " + str(currloc[1])))
			for number in lst[1:3]:
				sms(msg,number)
			print(msg)
       	 
	else:
		count1 = 0
   	 
	dist = newdist
	print(dist)
   	 

 

sosbutton = tk.Button(tkWindow, font=("Helvetica", 32), text='SOS', width=25, command=sosFunction)
stopbutton = tk.Button(tkWindow, font=("Helvetica", 32), text='Quit', width=25, command=tkWindow.destroy)

sosbutton.pack()
stopbutton.pack()

tkWindow.mainloop()

root.quit
root.mainloop()



fields2='Source','Destination'
tkWindow = tk.Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Shield Of Security (SOS)')
ents = makeform(tkWindow, fields2)
button1 = tk.Button(tkWindow, text='Start', font=("Helvetica", 32), command=(lambda e=ents: fetch(e)))
button1.pack(side=tk.LEFT, padx=5, pady=5)

button2 = tk.Button(tkWindow, text = 'SOS', font=("Helvetica", 32), command = showMsg)  
button2.pack()  

tkWindow.mainloop()
