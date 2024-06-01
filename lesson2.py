 # 1. Every Block in the blockchain has a timestamp associated with it. In order to dynamically generate a timestamp, we must import a Python module that returns the current date and time.

from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)


# 2. Inside the datetime module there is a .now() method that returns the current date and time.Call the datetime module’s .now() method to print out the current date and time.

from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

# 3. Now let’s work on creating our Block. We will be passing transactions and previous_hash to the default constructor each time a Block is created.Complete the __init__() method inside the Block class by initializing the following instance variables: transactions, previous_hash, nonce (with a default value of 0)
class Block:
# default constructor for block class
  def __init__(self, transactions, previous_hash, nonce=0):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    pass
# create first object
s1 = Block(4500, 123, 0)

# access instance variable
print('Object 1')
print('Nonce:', s1.nonce)

# 4. Inside the __init__() method, create a timestamp instance variable that stores the current date and time

class Block:
# default constructor for block class
  def __init__(self, transactions, previous_hash, timestamp, nonce=0):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.timestamp = datetime.now()
    self.nonce = nonce
    pass
# create first object
s1 = Block(4500, 123, 0)

# access instance variable
print('Object 1')
print('Nonce:', s1.nonce)

