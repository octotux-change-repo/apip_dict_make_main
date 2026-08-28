#tool name : apip
#version : alpha 0.1.0
#turn on : false
#peoole : cex
#run_mode:
#inux can run 
#windows can run
import time as ti
import itertools as itert
import pyfiglet as pfg
import os
import random as rand
import hashlib as hl
import gzip as gz
class ModeIterProducts:
    def __init__(self):
        self.list_serail_code=[]
        self.s = ["QWER","TYUI","OPA"]
        self.s2 = ["S","DFGH","JKLZ"]
        self.s3 = ["XCVB","NM","qwer"]
        self.s4 = ["tyui","opas","df"]
        self.s5 = ["tyui","opas","dfgh",]
        self.s6 = ["jklz","xcvb","nm"]
        self.crunch = {
                    "index1":self.s,
                    "index2":self.s2,
                    "index3":self.s3,
                    "index4":self.s4,
                    "index5":self.s6,
                    "index6":self.s6
                                                }
        self.l1=["'',.","</>?",r"\\|*("]
        self.l2 = [")","&^%$","#!;:"]
        self.crunch1 = {
            "i1":self.l1,
            "i2":self.l2,
        }
    def rash(self,val):
            val.clear()
    def _main_(self):
        for i in range(1,9):
            it=itert.product("NSL",repeat=i)
            for i in it:
                self.list_serail_code.append(''.join(i))
        print("[+]dict key is maked")
        print("[*]quiting the proccess,and creat a new process to program:[OK]")
    def _Main_(self):
        self.data1=[]
        self.data2=[]
        self.data3=[]
        self.digital=0
        self.datas=[]
        self.digits = ["0123","4567","789"]
        for o in self.digits:
            self.digital_32 = rand.randint(3,6)+1
            for f in range(self.digital_32):
                its=itert.product(o,repeat=f)
                for x in its:
                    self.data1.append(''.join(x))
                    print(pfg.figlet_format("HASHGIT_MAIN",font="slant"))
                    print("[+]dict key is maked")
                    print("[*]quiting the proccess,and creat a new process to program:[OK]")
                    print(f"[INFO]process value digit completed:{(len(self.data1)/round(22*(1024*1024*(10000/32))))}%")
                    os.system("cls")
        with open("./configure.txt","a") as f:
            for i in self.data1:
                f.write(i+".")
        for i in self.crunch.values():
            for o in i:
                self.digital_32 = rand.randint(3,6)+1
                for f in range(self.digital_32):
                    its=itert.product(o,repeat=f)
                    for x in its:
                        self.data2.append(''.join(x))
                        print(pfg.figlet_format("HASHGIT_MAIN",font="slant"))
                        print("[+]dict key is maked")
                        print("[*]quiting the proccess,and creat a new process to program:[OK]")
                        print(f"[INFO]process value digit completed:{(len(self.data1)/round(22*(1024*1024*(10000/32))))}%")
                        os.system("cls")
                        if len(self.data2) <= 6 :
                            print("[*]writing the file in the floader....")
                            for g in self.data2:
                                with open("./configure-2.txt","a") as f:
                                    f.write(g+".")
                        self.rash(self.data2)
        for i in self.crunch1.values():
            for o in i:
                for f in range(self.digital_32):
                    its=itert.product(o,repeat=f)
                    for x in its:
                        self.data3.append(''.join(x))
                        print(pfg.figlet_format("HASHGIT_MAIN",font="slant"))
                        print("[+]dict key is maked")
                        print("[*]quiting the proccess,and creat a new process to program:[OK]")
                        print(f"[INFO]process value digit completed:{(len(self.data1)/round(22*(1024*1024*(10000/32))))}%")
                        os.system("cls")
        with open("./configure-3.txt","a") as f:
            for i in self.data3:
                f.write(i+".")   
    def __call__(self):
        self._main_()
        self._Main_()
app=ModeIterProducts()
app.__call__()
print("[*]the program is non can make key dict")
print("[*]need open file:resame for continue done end step:make dict key file")
print("[INFO]you need have a size as 2GB I/O for save the program and products")
print("exting......")
ti.sleep(10)