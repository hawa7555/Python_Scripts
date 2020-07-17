import serial
import time

template = 'ef01ffffffff07000300000aef01ffffffff020082030156178200e0fec01ec006c0028000800080008000800000000000c000c002f80efc0efc0efc0e000000000000000000000000000000004919df5e6c22097e1ea39cfe5423e01e6624df7e18a8dbfe0f2bd9fe442d0a5e3b309fde49c0481e47b7a17f5292df5c76988afc1a9b5c9c583ac8fd4d9548da5a9d091b519ec9982f6aef01ffffffff020082539c9fb969aa08f65e3de0b676a95fd453bf21320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ac4ef01ffffffff0200820301561b7c00fffefffefffefffef00600020002000000000000000000000000000000000000000200000000000000000000000000000000559747de1319965e73245e7e62251efe29a559fe25a958de112a95be302c5b5e58afc8fe2d3219de23b3179e113351de4fb55ede19b9135e5f399fbe753b897e6b3e48fe0ec14f9e2973ef01ffffffff08008267c30936519d1d7f13a5019c109f40da102255f8659d481919401157412a878c43a99c7300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000db7'

def findSensor():
    port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex('ef01ffffffff01000713000000ff011a')
    port.write(packet)
    output = port.read(12)
    #packet = bytearray.fromhex('ef01ffffffff01000712000000ff0119')
    #port.write(packet)
    #output = port.read(12)
    print( output.hex() )
    if hex( output[9] ) == '0x0':
        print('Sensor Found')
    else:
        print('Sensor not Found')
        while(1):
            time.sleep(1)
    port.close()

def collectFinger_print(str):
    port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex('ef01ffffffff010003010005')
    print('Place finger')
    time.sleep(1)
    while(1):
        port.write(packet)
        output = port.read(12)
        if hex( output[9] ) == '0x0':
            result = generateCharacter_file(port, str)
            if(result):
                time.sleep(1.25)
                break
    port.close()

def generateCharacter_file(port, str):
    #port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex(str)
    port.write(packet)
    output = port.read(12)
    if hex( output[9] ) == '0x0':
        print('Remove finger')
        return 1
    else:
        print('Place finger correctly')
        return 0

def createTemplate():
    port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex('ef01ffffffff010003050009')
    port.write(packet)
    output = port.read(12)
    
    if hex( output[9] ) != '0x0':
        print('Place Same Finger')
        return 1
    port.close()
    print('FingerPrint Collected Successfully\n')
    return 0

def getTemplate():
    port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex('ef01ffffffff0100040801000e')
    port.write(packet)
    output = port.read(568)
    #print(output.hex())
    #print('\n')
    #print(output[1135])
    port.close()
    #getdata_fromTemplate(output.hex())
    storeTemplate( output.hex() )

def getdata_fromTemplate(input):

    #input = input.hex()
    finaldata = input[42:298] + input[320:576] + input[598:854] + input[876:1132]
    #storeTemplate(finaldata)
    #print(finaldata)

def storeTemplate(input):
    file = open('finger_dummyDatabase.txt','a')
    for i in range(1):
        #file.write( str(i) + '.' + input )
        file.write(input + '\n')
    #file.write(input + '\n')
    print('database created successfully\n')
    file.close()

def store_inLibrary():
    port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex('ef01ffffffff010006060103e800f9')
    port.write(packet)
    output = port.read(12)
    print( output.hex() )
    port.close()

def emptyLibrary():
    port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex('ef01ffffffff0100030d0011')
    port.write(packet)
    output = port.read(12)
    print( output.hex() )
    port.close()

def sendTemplate1(inputTemplate):
    port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex('ef01ffffffff0100040901000f')
    port.write(packet)
    output = port.read(12)
    #print(output.hex())
    packet = bytearray.fromhex(inputTemplate)
    port.write(packet)
    #print( packet.hex() )
    #print('data')
    port.close()


def sendTemplate2(inputTemplate):
    port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex('ef01ffffffff01000409020010')
    port.write(packet)
    output = port.read(12)
    #print(output.hex())
    packet = bytearray.fromhex(inputTemplate)
    port.write(packet)
    #output = port.read(12)
    #print( output.hex() )
    #print(packet.hex())
    #print('data')
    port.close()

def matchPrints():
    port = serial.Serial("COM3", 57600)
    packet = bytearray.fromhex('ef01ffffffff010003030007')
    port.write(packet)
    output = port.read(14).hex()

    if( output[19] ) == '0':
        print('found')

    #print( output[19] )
    port.close()

def printDatabase():
    file = open('finger_dummyDatabase.txt','r')
    for i in file:
        print(i)
    file.close()

def find_fingerPrint():
    file = open('finger_dummyDatabase.txt','r')
    for i in file:
        #print(i + '\n')
        sendTemplate2(i)
        matchPrints()
    file.close()

def storeLibrary_dummy(length):
    port = serial.Serial("COM3", 57600)
    dummy = 'ef01ffffffff0100060601'
    #checksum = 14
    for i in range(length):
            dummy = 'ef01ffffffff0100060601'
            hexI = hex(i)
            hexI = '0' * (6 - len(hexI)) + hexI[2:]
            checkH = hexI[:2]
            checkL = hexI[2:]
            #print(hexI)
            #print(checkH)
            #print(checkL)
            #print(hexI)
            checksum = 14 + int(checkH,16) + int(checkL,16)
            checkI = hex(checksum)
            checkI = '0' * (6 - len(checkI)) + checkI[2:]
            dummy = dummy + hexI + checkI
            #dummy = dummy + checkI
            packet = bytearray.fromhex(dummy)
            port.write(packet)
            output = port.read(12).hex()
            print(str(i) + output)
            #checksum = 14 + hexI
            #print(dummy)
    port.close()

#storeLibrary_dummy(8)
#findSensor()
#sendTemplate1(template)
#getTemplate()

findSensor()
#emptyLibrary()
result = 1
while(result):
    collectFinger_print('ef01ffffffff01000402010008')
    collectFinger_print('ef01ffffffff01000402020009')
    result = createTemplate()
#store_inLibrary()
#getTemplate()
#printDatabase()
#find_fingerPrint()
#storeLibrary_dummy(1000)











