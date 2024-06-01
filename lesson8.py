
import hashlib


class Block:
    # Defining Block Structure
    def __init__ (self, no, nonce, data, hashcode, prev):
        self.no = no
        self.nonce = nonce
        self.data = data
        self.hashcode = hashcode
        self.prev = prev

    def getStringVal (self):
        return self.no, self.nonce, self.data, self.hashcode, self.prev
    

class BlockChain:
    # Defining simple Blockchain structure, adding blocks and chaining them together
    def __init__(self):
        self.chain = []
        self.prefix = "0000"
    
    def addNewBlock (self, data):
        no, nonce,  prev  = len(self.chain), 0 ,  "0" if len(self.chain)==0 else self.chain[-1].hashcode
        myHash = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
        block = Block(no,nonce,data,myHash,prev)
        self.chain.append (block)
    
    def printBlockChain(self) :
        chaintDict = {}
        for no in range (len(self.chain)) :
            chaintDict[no] = self.chain[no].getStringVal()
        print (chaintDict)
    
    def mineChain(self) :
        brokenLink = self.checkIfBroken()
        if (brokenLink==None):
            pass
        else:
            for block in self.chain[brokenLink.no:]:
                print ("Mining Block", block.getStringVal())
                self.mineBlock(block)
    
    def mineBlock (self, block) :
        nonce = 0
        myHash = hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
        while myHash[0:4]!=self.prefix :
            myHash = hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
            nonce = nonce + 1
        else:
            print("nonce",nonce)
            print ("new hash", myHash)
            self.chain[block.no].hashcode = myHash
            self.chain[block.no].nonce = nonce
            if (block.no<len(self.chain)-1) :
                self.chain[block.no+1].prev = myHash

# checking if the chain is broken
    def checkIfBroken(self):
        for no in range (len(self.chain)) :
            if (self.chain[no].hashcode[0:4]== self.prefix):
                pass
            else:
                return self.chain[no]
        return None   
    
    def changeData(self, no, data):
        self.chain[no].data = data
        self.chain[no].hashcode = hashlib.sha256(str(str(self.chain[no].nonce)+str(self.chain[no].data)).encode('utf-8')).hexdigest() 
    

b1=BlockChain()
b1.addNewBlock("hello")  
b1.printBlockChain()
b1.addNewBlock("world")
b1.printBlockChain()
b1.mineChain()

b2=BlockChain()
b2.addNewBlock("hey")  
b2.printBlockChain()
b2.addNewBlock("world")
b2.printBlockChain()
b2.mineChain()


class BlockChainNetwork:
# Comparing Blockchain network
    def compareBlockChains (self, bc1, *bchains):
        for bchain in bchains:
            if len(bc1.chain)!=len(bchain.chain) :
                print ("Network is broken")
            for bno in range(len(bc1.chain)) :
                if bc1.chain[bno].hashcode!=bchain.chain[bno].hashcode :
                    print ("Network is Broken in Chain")


check=BlockChainNetwork()
check.compareBlockChains(b1,b2)


