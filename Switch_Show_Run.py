#!/usr/bin/python3

# purpose: grab running configs from the various switches
# created on: 10-18-22
# created by: FastMS
import pexpect
import re
import os
import subprocess
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import SSHDetect

os.system('clear')

def send_show_command(switch_ip, switch_un, switch_pw, command, prompt = '#'):

    try:
        with pexpect.spawn(f'ssh {switch_un}@{switch_ip} -oKexAlgorithms=+diffie-hellman-group14-sha1 -oHostKeyAlgorithms=+ssh-rsa', timeout=10, encoding='utf-8') as child:

            try:
                i = child.expect(['[Pp]assword','Are you sure you want to continue connecting (yes/no/[fingerprint])?'])
                if i == 0:
                    child.sendline(switch_pw)
                    child.expect(prompt)
                elif i == 1:
                    child.sendline('yes')
                    child.expect('[Pp]assword:')
                    child.sendline(switch_pw)
                    child.expect(prompt)
            except pexpect.TIMEOUT:
                exit()

            child.sendline(command)
            output = ''

            while True:
                match = child.expect([prompt, '--More--', pexpect.TIMEOUT])
                page = child.before.replace('\r\n', '\n')
                page = re.sub(' +\x08+ +\x08+', '\n', page)
                output += page
                if match == 0:
                    break
                elif match == 1:
                    child.send(' ')
                else:
                    print('Error: Timeout')
                    break
                
            output = re.sub('\n +\n', '\n', output)
            return output

    # change the cypher and the key exchange if needed
    except:
        # -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa, -c aes128-ctr
        with pexpect.spawn(f'ssh {switch_un}@{switch_ip} -oKexAlgorithms=+diffie-hellman-group-exchange-sha1, -c aes128-cbc', timeout=10, encoding='utf-8') as child:

            try:
                i = child.expect(['[Pp]assword','Are you sure you want to continue connecting (yes/no/[fingerprint])?'])
                if i == 0:
                    child.sendline(switch_pw)
                    try:
                        child.expect(prompt)
                    except:
                        child.expect('>')
                        child.sendline('en')
                        child.expect('[Pp]assword:')
                        child.sendline(switch_pw)
                        child.expect(prompt)
                elif i == 1:
                    child.sendline('yes')
                    child.expect('[Pp]assword:')
                    child.sendline(switch_pw)
                    child.expect(prompt)
            except pexpect.TIMEOUT:
                print('Elevated prompt not received.')
                exit()

            child.sendline(command)
            output = ''

            while True:
                match = child.expect([prompt, '--More--', pexpect.TIMEOUT])
                page = child.before.replace('\r\n', '\n')
                page = re.sub(' +\x08+ +\x08+', '\n', page)
                output += page
                if match == 0:
                    break
                elif match == 1:
                    child.send(' ')
                else:
                    print('Error: Timeout')
                    break
                
            output = re.sub('\n +\n', '\n', output)
            return output



if __name__ == '__main__':
    switch_un = 'USERNAME'
    # switch_pw = getpass() # getpassword
    switch_pw = subprocess.check_output("cat /home/USERNAME/.scripts/.scriptpass.txt | openssl enc -aes-256-cbc -md sha512 -a -d -pbkdf2 -iter 10000 -salt -pass pass:'PASSWORD_HERE'", shell=True, text=True).rstrip()
    # command = input('What command do you want to run? ')
    command = 'show run'

    # Get the connection dictionaries setup
    S1 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S2 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S3 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S4 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S5 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S6 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S7 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S8 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw} # HP switch
    S9 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw} # HP switch
    S10 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw} # HP switch
    S11 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw} # HP switch
    S12 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw} # HP switch
    S13 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S14 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S15 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S16 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S17 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S18 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S19 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S20 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    S21 = {'device_type':'autodetect','host':'IP_ADDRESS','username':'USERNAME','password':switch_pw}
    devices = [S1,S2,S3,S4,S5,S7,S8,S9,S10,S11,S12,S14,S16,S17,S18,S19,S20,S21]

    # iterate through all the switches in the dictionary
    for ip in devices:
        net_connect = ConnectHandler(**ip)
        guesser = SSHDetect(**ip   )
        best_match = guesser.autodetect()
        if ip == S1:
            ip = 'IP_ADDRESS'
        elif ip == S2:
            ip = 'IP_ADDRESS'
        elif ip == S3:
            ip = 'IP_ADDRESS'
        elif ip == S4:
            ip = 'IP_ADDRESS'
        elif ip == S5:
            ip = 'IP_ADDRESS'
        elif ip == S6:
            ip = 'IP_ADDRESS'
        elif ip == S7:
            ip = 'IP_ADDRESS'
        elif ip == S8:
            ip = 'IP_ADDRESS'
        elif ip == S9:
            ip = 'IP_ADDRESS'
        elif ip == S10:
            ip = 'IP_ADDRESS'
        elif ip == S11:
            ip = 'IP_ADDRESS'
        elif ip == S12:
            ip = 'IP_ADDRESS'
        elif ip == S13:
            ip = 'IP_ADDRESS'
        elif ip == S14:
            ip = 'IP_ADDRESS'
        elif ip == S15:
            ip = 'IP_ADDRESS'
        elif ip == S16:
            ip = 'IP_ADDRESS'
        elif ip == S17:
            ip = 'IP_ADDRESS'
        elif ip == S18:
            ip = 'IP_ADDRESS'
        elif ip == S19:
            ip = 'IP_ADDRESS'
        elif ip == S20:
            ip = 'IP_ADDRESS'
        elif ip == S21:
            ip = 'IP_ADDRESS'
        else:
            print('Error with switch.')

        if best_match == 'cisco_ios':
            result = send_show_command(ip, switch_un, switch_pw, command)
            if result != '':
                with open(f'./cisco/{ip}.txt', 'w') as f:
                    f.write(str(result))
            else:
                print(str(result))
        else:
            if result != '':
                with open(f'./hp/{ip}.txt', 'w') as b:
                    b.write(str(result))
            else:
                print(str(result))