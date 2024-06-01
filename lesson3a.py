
#1. # Python 3 code to check
# available algorithms
 
import hashlib
 
# prints all available algorithms
print ("The available algorithms are : ", end ="")
print (hashlib.algorithms_guaranteed)




# 2. Import sha256 from the hashlib Python library
from hashlib import sha256


#3. Create a variable called text. Initialize the variable with this string I am excited to learn about blockchain
text = "I am excited to learn about blockchain!"


#4. Create a sha256 hash object, using the constructor sha256() and pass the text variable as its argument. Assign the value of this object to a variable called hash_result.Be sure to use the .encode() method on the text variable. Call the .hexdigest() method on hash_result and print the result


# encoding I am excited to learn about blockchain using encode()
# then sending to SHA256()


hash_result = hashlib.sha256(text.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(hash_result.hexdigest())
 
#\r moves the cursor to the beginning of the line and then outputting characters as normal(carriage return)
print ("\r")


# Try changing the text variable and see how the hash gets completely different.


# initializing string
str = "jetlearn"
 
# encoding jetlearn using encode()
# then sending to SHA224()
result = hashlib.sha224(str.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())
 
print ("\r")
 
# initializing string
str = "GeeksforGeeks"
 
# encoding GeeksforGeeks using encode()
# then sending to SHA512()
result = hashlib.sha512(str.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())
 
print ("\r")
 
# initializing string
str = "Jetlearn"
 
# encoding Jetlearn using encode()
# then sending to SHA1()
result = hashlib.sha1(str.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
