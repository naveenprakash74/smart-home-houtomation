import RPi.GPIO as GPIO #i import this library to inable gpio pin
import time
import pyrebase #this library provide connectivity to firebase
from time import sleep
GPIO.setwarnings(False) #set hardware to false
GPIO.setmode(GPIO.BCM) #set gpio pin to BCM mode
GPIO.setup(13,GPIO.IN)#setup GPIO 13 to input mode
GPIO.setup(3,GPIO.OUT)#setup GPO3 to output mode
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.output(3,0)#here initialise 3 to off state
GPIO.output(5,0)
GPIO.output(7,0)
#ther are the api key provided by fire base to access firebase database
config = {
    apiKey: "AIzaSyCES87vYGikHZ8JY1dscUIYL2PGMgLZebM",
    authDomain: "newiot-5af23.firebaseapp.com",
    databaseURL: "https://newiot-5af23.firebaseio.com",
    projectId: "newiot-5af23",
    storageBucket: "newiot-5af23.appspot.com",
    #messagingSenderId: "582338804809"
  };

'''config = {
    "apiKey": "AIzaSyBCHe6sO7e6SbBHjvB0rWC3cxJK9w8Rwj8",
    "authDomain": "home-automation-bbd39.firebaseapp.com",
    "databaseURL": "https://home-automation-bbd39.firebaseio.com",
    "projectId": "home-automation-bbd39",
    "storageBucket": "home-automation-bbd39.appspot.com",
    #"messagingSenderId": "684489069755"
  };'''
firebase = pyrebase.initialize_app(config)#configure firebase
db = firebase.database()#connect to firebase database
print ("PROGRAM IS RUNNING")
while True:
    pir = db.child("led4").get() #this statment to check weather the led4 column present in database or not
    pir_status=pir.val()# this statment fatch values from database
    led1=db.child("led1").get()
    led1_status=led1.val()
    led2=db.child("led2").get()
    led2_status=led2.val()
    led3=db.child("led3").get()
    led3_status=led3.val()
    fan=db.child("fs").get()
    fan_status=fan.val()
    
    if pir_status=='"0"': #this statment check pir enable or not
        if led1_status=='"0"':
            GPIO.output(3,0)#off state
        if led1_status=='"1"':
            GPIO.output(3,1)# on state
        if led2_status=='"0"':
            GPIO.output(5,0) #off state
        if led2_status=='"1"':
            GPIO.output(5,1)#on state
        if led3_status=='"0"':
            GPIO.output(7,0)#off state
        if led3_status=='"1"':
            GPIO.output(7,1)
        if led3_status=='"1"' and fan_status=='"0"': #this statment to use dimmet control
            GPIO.output(21,1)#this pi is D0 pin of dimmer module
            GPIO.output(20,1)#this pi is D1 pin of dimmer module
            GPIO.output(16,1)#this pi is D2 pin of dimmer module
            GPIO.output(12,1)#this pi is D3 pin of dimmer module
        if led3_status=='"1"' and fan_status=='"4"':
            GPIO.output(21,0)
            GPIO.output(20,1)
            GPIO.output(16,0)
            GPIO.output(12,1)
        if led3_status=='"1"' and fan_status=='"8"':
            GPIO.output(21,1)
            GPIO.output(20,1)
            GPIO.output(16,1)
            GPIO.output(12,0)
        if led3_status=='"1"' and fan_status=='"12"':
            GPIO.output(21,1)
            GPIO.output(20,1)
            GPIO.output(16,0)
            GPIO.output(12,0)
        if led3_status=='"1"' and fan_status=='"15"':
            GPIO.output(21,0)
            GPIO.output(20,0)
            GPIO.output(16,0)
            GPIO.output(12,0)
    else:
        i=GPIO.input(13)
        if i==0:
            GPIO.output(3,0)
            GPIO.output(5,0)
            GPIO.output(7,0)
        else:
            GPIO.output(3,1)
            GPIO.output(5,1)
            GPIO.output(7,1)
            GPIO.output(21,0)
            GPIO.output(20,0)
            GPIO.output(16,0)
            GPIO.output(12,0)
    print (pir_status)# here we print the status of pins

    print (led1_status)
    print (led2_status)
    print (led3_status)
GPIO.cleanup()#here we clean all the values of gpio pins



