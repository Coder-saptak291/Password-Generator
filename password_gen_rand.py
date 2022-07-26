from flask import Flask
n = input("Enter your name : ")
nl=[]
for i in range(len(n)):
    nl.append(n[i])
# print(nl)
db = input("Enter your DOB : ")
dl=[]
for i in range(len(db)):
    dl.append(db[i])
# print(dl)
l = int(input("Enter the length of your password(at least 8 maximum 12) ="))
if l==(7+1):
    password=nl[0]+nl[1]+nl[2]+nl[3]+"@"+dl[1]+dl[1]+dl[2]+"|"
    print(f"Generated password is {password}")
if l==(8+1):
    password=nl[0]+nl[1]+nl[2]+nl[3]+nl[4]+"@"+dl[1]+dl[3]+dl[5]+"|"
    print(f"Generated password is {password}")
if l==(9+1):
    password=nl[0]+nl[1]+nl[2]+nl[3]+nl[4]+"@"+dl[1]+dl[3]+dl[5]+dl[1]+"|"
    print(f"Generated password is {password}")
if l==(10+1):
    password=nl[0]+nl[1]+nl[2]+nl[3]+nl[4]+"@"+dl[1]+dl[3]+dl[5]+dl[1]+dl[2]+"|"
    print(f"Generated password is {password}")
if l==(11+1):
    password=nl[0]+nl[1]+nl[2]+nl[3]+"@"+dl[1]+dl[3]+dl[5]+dl[1]+dl[2]+dl[4]+dl[1]+"|"
    print(f"Generated password is {password}")