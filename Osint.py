from termcolor import colored as c
import webbrowser as web
import time as t
print(c("==============================","green"))
print(c("      I.G. FRAMEWORK", "yellow"))
print(c("==============================","green"))
print("")
print(c("1) IP Address","green"))
print(c("2) Phone Numbers","green"))
print(c("3) Facebook I'd ","green"))
print(c("4) MetaData ","green"))
print(c("5) IP Address URL Create","green"))
print(c("6) Search image","green"))
print(c("7) OSINT Frameworks","green"))
print("")

input=input("Scan :-- ")
print("")
print(c("Scanning...", "red"))
time=t.sleep(5)
if input=="1":
	a=web.open("https://www.opentracker.net/feature/ip-tracker?ip=157.35.61.195")
if input=="2":
	b=web.open("https://www.truecaller.com/")
if input=="3":
	fb=web.open("https://m.facebook.com/login/?refsrc=deprecated")
if input=="4":
	meta=web.open("https://exif.tools")
if input=="5":
	iplogger=web.open("https://iplogger.org/")
if input=="6":
	img=web.open("https://facecheck.id/")
if input=="7":
	oinst=web.open("https://osintframework.com/")
	
	
