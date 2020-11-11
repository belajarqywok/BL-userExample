#!/bin/env python3
import re
import os
import sys
import pandas as pd
class dataProsessing:
    def __init__(self,nameFile):
        self.datas=pd.read_csv(nameFile,sep=",",index_col=0)
        self.parameters=int(len(self.datas.values)*(8^2)/10**2)
    def dataClassification(self):
        os.system("clear")
        self.getDatas=[]
        for indexData in range(self.parameters):
            self.getDatas.append({"nickname":self.datas.values[indexData][27],
                                  "fullname":self.datas.values[indexData][1],
                                  "email_address":self.datas.values[indexData][0],
                                  "email_domain":re.findall("@\S+",self.datas.values[indexData][0])[0]
                                })
            print("============= [ "+str(indexData+1)+" ] =============\n"
                  +"nickname : "+self.datas.values[indexData][27]+"\n"
                  +"fullname : "+self.datas.values[indexData][1]+"\n"
                  +"email    : "+self.datas.values[indexData][0]+"\n"
                  +"email domain : "+re.findall("@\S+",self.datas.values[indexData][0])[0]+"\n"
                  )
        return self.getDatas
class createDataCsv:
    def __init__(self,nameFile):
        self.all=dataProsessing(nameFile).dataClassification()
        dataFrame=pd.DataFrame(self.all)
        dataFrame.to_csv("example.csv",index=False,encoding="utf-8")
try:
    if __name__=="__main__":
        createDataCsv("Bukalapak - 500K Partial Out Of 13 Million.csv")
except KeyboardInterrupt:
    os.system("clear")
    pass
