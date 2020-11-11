#!/bin/env python3
import datetime
class createUserHistory:
    def __init__(self,fileName,history):
        self.f=open(fileName,"a")
        self.History=history
    def create(self):
        self.f.writelines("date : "+datetime.datetime.now().strftime("%H")+"-"+datetime.datetime.now().strftime("%d")+"-"+datetime.datetime.now().strftime("%m")+"-"+datetime.datetime.now().strftime("%Y")+"\n"
                          +"link : "+self.History+"\n"
                          +"===========================================\n"
        )
        self.f.close