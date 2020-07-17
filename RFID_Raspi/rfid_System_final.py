import serial
import time
import json
import SDL_DS3231

ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
ds3231.write_now()

ser = serial.Serial("/dev/ttyS0", 9600)

file = open('rfidData.json', 'r')
dataRead = json.load(file)
file.close()

id_array = [None] * 100

for key in dataRead:
    if(dataRead[key]['id'] != -1):
        #print(dataRead[key]['id'])
        id_array[ dataRead[key]['id'] ] = key

#print(id_array)
file = open('id_Data.json', 'w')
json_data = json.dumps(id_array)
file.write(json_data)
file.close()

while(1):
    isPresent = False
    received_data = ''
    rfid = ""
    print("receiving...")
    
    while(1):
        received_data = ser.read().decode('utf-8')
        if(received_data == '\n'):
            break;
        rfid += received_data

    if( len(rfid) == 4):
        print(rfid)
        file = open('rfidData.json', 'r')
        dataRead = json.load(file)
        file.close()

        file = open('id_Data.json', 'r')
        dataGet = json.load(file)
        file.close()

        rfid_received = dataGet[int(rfid)]
        intime = ds3231.read_datetime()
        dateString = intime.strftime("%d-%m-%Y, %H:%M")
        print(dateString)
        dataRead[rfid_received]['inTime'] = dateString
        
        file = open('rfidData.json', 'w')
        json_data = json.dumps(dataRead)
        file.write(json_data)
        file.close()
        continue

    file = open('rfidData.json', 'r')
    dataRead = json.load(file)
    file.close()

    isPresent = rfid in dataRead.keys()
    
    if(isPresent):
        file = open('rfidData.json', 'w')
        intime = ds3231.read_datetime()
        print("Access Granted")
        
        if(dataRead[rfid]['id'] == -1):
            ser.write( str.encode("1") )
            print("FingerPrint not present")
            receivedResponse = ser.read().decode('utf-8')

            if(receivedResponse == 'R'):
                received_digit = ''
                fingerPrint_ID = ""

                for i in range(4):
                    received_digit = ser.read().decode('utf-8')
                    fingerPrint_ID += received_digit

                dataRead[rfid]['id'] = int(fingerPrint_ID)
                #json_data = json.dumps(dataRead)
                #file.write(json_data)
                print(fingerPrint_ID)
                
        else:
            ser.write( str.encode("2") )
            print("FingerPrint present")

        dateString = intime.strftime("%d-%m-%Y, %H:%M")
        print(dateString)
        dataRead[rfid]['inTime'] = dateString
        json_data = json.dumps(dataRead)
        file.write(json_data)
        file.close()

    else:
        ser.write( str.encode("0") )
        print("Acess Denied")
        

    #file.close()
    time.sleep(0.5)
