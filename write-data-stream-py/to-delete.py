# create a string using the decode() method of bytes.
# This method takes an encoding argument, such as UTF-8, and optionally an errors argument.
message = "Hello World"
myArray = bytearray()
myArray.extend(map(ord, message))


print(myArray)
print(type(myArray))

# Import time for sleep
import time

# While loop
while(True):
	print("looping...{message}").format(message)
	time.sleep(2)