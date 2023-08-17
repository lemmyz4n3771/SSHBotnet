from pexpect import pxssh

class Client:
        def __init__(self, ip, port, username, password):
                self.ip = ip
                self.port = port
                self.username = username
                self.password = password
                self.session = self.connect()
        
        def connect(self):
            try:
                    session = pxssh.pxssh()
                    session.login(self.ip, self.username, self.password, port=self.port, sync_multiplier=5, auto_prompt_reset=False)
                    print(f'[+] Connected to {self.ip}!')
                    return session
            except Exception as e:
                    print(e)
                    print('[-] Connection error')
                    exit(1)
        def sendCmd(self, cmd):
            try:
                self.session.sendline(cmd)
                self.session.prompt()
                return self.session.before   
            except:
                pass
            return -1