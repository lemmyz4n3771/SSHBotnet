## SSHBotnet

This program creates an SSH botnet from a file containing IPs, ports, and ssh user login information (delimted by ":"). The following is a valid entry:

```bash
192.168.16.15:22:user:password
```

### Example Usage

```bash
$ python sshbotnet.py      
[-] Usage: sshbotnet.py botnet_creds.txt

$ python sshbotnet.py sshinfo.txt
[+] Connected to 127.0.0.1!
[+] Connected to 10.10.14.6!
[+] Connected to 10.10.11.119!

cmd> whoami
[*] Output for lemmy@127.0.0.1:
lemmy
[*] Output for drew@10.10.14.6:
drew
[*] Output for developer@10.10.11.119:
developer
```