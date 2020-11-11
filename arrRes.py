#!/bin/env python3
import re
import pandas as pd
class dataRequests:
    def __init__(self,nameFile,length):
        self.file=pd.read_csv(nameFile)
        self.resLength=length
    def processing(self):
        self.result=[]
        for index in range(self.resLength):
            self.result.append({
                "nickname":self.file.values[index][0],
                "fullname":self.file.values[index][1],
                "email_address":self.file.values[index][2],
                "email_domain":self.file.values[index][3]
            })
        return self.result
