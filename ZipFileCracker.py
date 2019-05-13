#!/usr/bin/python
import zipfile
from threading import Thread
import time
import sys
import getopt
import os
from termcolor import colored
global found
found=[]


class crackzip(Thread):
	
	
	def __init__(self,password,zfile):
		Thread.__init__(self)
		self.password=password
		self.zfile=zfile
	def run(self):
		global found
		try:
			self.zfile.extractall(pwd=self.password)
			found=self.password
		except:
			if(not len(found)):
				sys.stdout.write('\r'+self.password+'       ')
				sys.stdout.flush()
		i[0]=i[0]-1
		return
def banner():
	os.system("clear")
	print (colored('''


 ______       _____ _ _       ____                _             
|__  (_)_ __ |  ___(_) | ___ / ___|_ __ __ _  ___| | _____ _ __ 
  / /| | '_ \| |_  | | |/ _ \ |   | '__/ _` |/ __| |/ / _ \ '__|
 / /_| | |_) |  _| | | |  __/ |___| | | (_| | (__|   <  __/ |   
/____|_| .__/|_|   |_|_|\___|\____|_|  \__,_|\___|_|\_\___|_| 


	''',"yellow"))
	l="\t\t\t\t\tBy Mbemekou Fred\n"
	u=""
	for b in l:
		u=u+b
		sys.stdout.write('\t\t\t\r'+u)
		sys.stdout.flush()
		time.sleep(0.05)
def usage():
	print (colored("./ZipFileCracker.py -f <zipfile to crack> -w <wordlist to use to crack zipfile>","green"))
	sys.exit()




def thread_launcher(passwords,zfile):
	
	global i
	i=[]
	i.append(0)
	print "Cracking the file ..."
	while(len(passwords)):
		if(i[0]<4):
			i[0]=i[0]+1
			password=passwords.pop(0).strip("\n")
			thread=crackzip(password,zfile)
			thread.start()
			thread.join()
			if (len(found)):
				sys.stdout.write('\r')
				print(colored("[+]password found: "+found,"green"))
				sys.exit(0)
	if(not len(found)):
		sys.stdout.write('\r')
		print (colored("[-]password not found","red"))
		sys.exit(0)






def start(argv):
	banner()
	if(len(argv)<4):
		usage()
	try:
		opts,args=getopt.getopt(argv[1:],'f:w:')
	except Exception, e:
		print e
		sys.exit()
	for o,a in opts:
		if o=="-f":
			file_to_crack=a
		elif o=="-w":
			wordlist=a
		else:
			usage()
	try:		
		zfile=zipfile.ZipFile(file_to_crack)
	except Exception, e:
		print e
		sys.exit()
	try:
		f=open(wordlist)
		passwords=f.readlines()
	except Exception,e:
		print e
		sys.exit()
	thread_launcher(passwords,zfile)
start(sys.argv)

