import pyrebase
import json
from datetime import datetime

now = datetime.now()
dateString = now.strftime("%d-%m-%Y, %H:%M")
print(dateString)

#time = time.localtime()
#current_time = time.strftime( "%H:%M", time.localtime() )
#print(current_time)

#firebase1 = firebase.FirebaseApplication("https://rfidsystem-b1ff5.firebaseio.com/",None)

#person = { "364721f8": {"name": "Bob", "inTime": 1773256000, "outTime": 1673284000, "id": -1 },
#           "369bfffa": {"name": "Harshal", "inTime": 1563256010, "outTime": 1763284020, "id": -1 } }
#print(person)
#json_data = json.dumps(person)

#response = firebase1.post("/rfid_data", json_data);
#print(response)

firebaseConfig = {
  "apiKey": "AIzaSyCX-BUAvUD70TWtgTtSvY_x7tLiVrheE7o",
  "authDomain": "rfidsystem-b1ff5.firebaseapp.com",
  "databaseURL": "https://rfidsystem-b1ff5.firebaseio.com/",
  "projectId": "rfidsystem-b1ff5",
  "storageBucket": "rfidsystem-b1ff5.appspot.com"
  
}

#firebase = pyrebase.initialize_app(firebaseConfig)
#database = firebase.database()

#inputUID = input("Enter rfid uid: ");

#name = input("Enter name: ");

#time = input("Enter time: ");
      
#dataDict = {}
#dataDict = {"name": name, "time": time}
#print(inputData);
#print(dataDict)

#response = database.child('rfid_data').child(inputUID).set(dataDict, None)

#response = database.child('rfid_data').get().val()
#json_data = json.dumps(response)

file = open('firebaseData.json', 'w+')
dataRead = json.load(file)
print(dataRead)
#json_data = json.dumps(person)
#file.write(json_data)
file.close()

#file = open('firebaseData.json', 'w')
#dataRead = json.load(file)
#dataRead['369bfffa']['id'] = 16
#json_data = json.dumps(dataRead)
#print(dataRead)
#file.write(json_data)
#print( json_data )
#print(dataRead)
#isPresent = inputUID in dataRead.keys()
#file.close()

#if(isPresent):
#    print("Acess Granted")

#    if(dataRead[inputUID]['id'] == -1):
#        print("FingerPrint Not Present")
#    else:
#        print("FingerPrint Present")
    
#else:

 #   print("Acess Denied")
    
#file.close()

#print(response)



