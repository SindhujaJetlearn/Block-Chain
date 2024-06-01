#1. # Python 3 code to check
# available algorithms
 
import hashlib
 
# prints all available algorithms
print ("The available algorithms are : ", end ="")
print (hashlib.algorithms_guaranteed)




# 2. Import sha256 from the hashlib Python library
from hashlib import sha256


#3. Create a variable called text. Initialize the variable with this string I am excited to learn about blockchain
text = "Sindhuja R"


#4. Create a sha256 hash object, using the constructor sha256() and pass the text variable as its argument. Assign the value of this object to a variable called hash_result.Be sure to use the .encode() method on the text variable. Call the .hexdigest() method on hash_result and print the result


# encoding I am excited to learn about blockchain using encode()
# then sending to SHA256()


hash_result = hashlib.sha256(text.encode())
print(hash_result)
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(hash_result.hexdigest())
 