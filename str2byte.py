#turn char to num
a = ord('A')
print (a)
a = ord('中')
print (a)
a = chr(66)
print (a)
a = chr(25991)
print (a)

print('----------------------')
# turn str to bytes
a = 'ABC'.encode('ascii')
print(a)

# turn bytes to str ascii
a = b'ABC'.decode('ascii')
print(a)

print('----------------------')
# caculate byte length
a = 'ABC'
print(len(a))

