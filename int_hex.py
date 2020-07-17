i = 1000
dummy = 'ef01ffffffff0100060601'
hexValue = hex(i)
hexValue = '0' * (6 - len(hexValue)) + hexValue[2:]
#print(hexValue)
#length = len(hexValue) - 4
#for i in range(length):
#    hexValue[i] = 0
dummy = dummy + hexValue
print(dummy)
