new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# 1.Import the sha256 hash function from the Python hashlib library

# import sha256
from hashlib import sha256

# 2. Create a variable called difficulty and assign it a value of 2. This sets the number of leading zeros that the hash we find must have. Create another variable called nonce and assign it to a value of 0. This will be our default starting value

difficulty = 2
nonce = 0

# 3. Using the .str() method, cast nonce and new_transactions into strings. Pass the two strings into the sha256 function. Store the resulting hash value into a variable called proof and print it out!
# Note: Use the .hexdigest() method over the resulting sha256 function to properly store the hash value.

# creating the proof 
proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()
# printing proof
print(proof)

# 4. Come up with some code that increments the nonce value until the generated hash has difficulty number of leading zeros. Once the desired proof has been found, store it in a variable called final_proof and print it out to see the correct hash!

# finding a proof that has 2 leading zeros
while (proof[:2] != '0' * difficulty):
  nonce += 1
  proof = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()

# printing final proof that was found
final_proof = proof
print(final_proof)