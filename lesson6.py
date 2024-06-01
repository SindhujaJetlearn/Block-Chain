import datetime 
import hashlib 


class Block:
    blockNo=0
    data=None 
    #pointer to the next block
    next=None 
    hash=None
    #A nonce is a random whole number iterated over and over again until the “Golden Nonce” is found 
    nonce=0
    previous_hash=0x0 
    timestamp=datetime.datetime.now()


    def __init__(self,data):
        self.data=data

    def hash(self):
        """"which calculates the hash of the block"""
        h=hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8')+
            str(self.data).encode('utf-8')+
            str(self.previous_hash).encode('utf-8')+
            str(self.timestamp).encode('utf-8')+
            str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()
    
    def __str__(self):
        """here, the output will display the block’s hash and the block number"""
        return "Block Hash:"+str(self.hash())+"\nBlockNo: "+str(self.blockNo)+"\nBlock Data: " + str(self.data) +"\nHashes: " +str(self.nonce) +"\n --------"
    

class Blockchain :
    """By increasing the difficulty, we effectively decrease the target range. Decreasing the target range makes it harder to mine a block, which is useful when dealing with a network that has many nodes working to find the acceptable hash"""
    diff=20
    """maximum nonce, set to 2 to the power of 32, which is the maximum number that can be stored in a 32-bit number. The nonce must be less than the target number to be accepted"""
    maxNonce=2**32
    """target number, set to 2 to the power of 256 minus the difficulty. In this case, the difficulty is 20"""
    target=2**(256-diff)

    block=Block("Genesis")
    """The start of any linked list is called the head. Since the head of our linked list is the Genesis block, we write that down in code as head = block.A random variable must be written before the head variable (in this case, dummy), to tell the computer that head does not point to the same object as block"""
    dummy=head=block

    def add(self,block):
        block.previous_hash=self.block.hash()
        block.blockNo=self.block.blockNo+1 
        self.block.next=block
        self.block=self.block.next

    def mine(self,block):
        """In order for blocks to added to the chain, the nodes try out different nonces until it finds a hash less than the target range"""
        for n in range(self.maxNonce):
            if int(block.hash(),16) <=self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce+=1


blockchain=Blockchain()

for n in range(10):
    """It calculates 10 random blocks"""
    blockchain.mine(Block("Block "+str(n+1)))


while blockchain.head!=None:
    print(blockchain.head)
    blockchain.head=blockchain.head.next
