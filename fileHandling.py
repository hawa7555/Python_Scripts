import json

#file = open('finger_dummyDatabase.txt','r')
#for i in file:
#    print(i)
#file.close()
#array=[]                    
#array.append("369bffa")
#array.append("745bd33")
#print(array)
#print(array[0])
file = open('stringData.json','r')
dataRead = json.load(file)
#json_data= json.dumps(array)
#file.write(json_data)
file.close()
#print(dataRead["369bfffa"]["id"])
print(dataRead)
print(dataRead[0])
print(dataRead[1])
