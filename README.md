# ZipFileCracker
ZipFileCracker is a simple tool written in python to help you crack zip password .

Author: Mbemekou Fred

Requirements: Python 2.7.x        

Install apt-get -y install git  python-pip

pip install zipfile termcolor threading getopt

git clone https://github.com/mbemekou/ZipFileCracker.git     

cd ./ZipFileCracker 

chmod +x ZipFileCracker.py              

Use ./ZipFileCracker.py -f "zipfile to crack" -w "wordlist to use to crack zipfile"
  

arguments:                                                    

-f Insert the file path of the  zipfile                       

-w Insert the file path of the dictionnary file                

Example: ./ZipFileCracker2.py  -f /home/file.zip -w /usr/share/wordllist/rockyou.txt 
