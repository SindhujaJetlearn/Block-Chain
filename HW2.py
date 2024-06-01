from datetime import datetime

now=datetime.now()

print("now= ",now)


class Block:
    def __init__(self,data,p_hash,nonce=0):
        self.data=data
        self.previous_hash=p_hash
        self.nonce=nonce
        self.timestamp=datetime.now()


s1=Block("hello","000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19",216)
print(s1.previous_hash)
print(s1.data)
print(s1.timestamp)

s2=Block("Hi","000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf",132625)
print(s2.previous_hash)
print(s2.data)
print(s2.timestamp)