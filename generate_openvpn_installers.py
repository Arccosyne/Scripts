#!/usr/bin/python

# This script generates VPN packages for clients and stores them in
# /root/vpninstallers<date>

import os
import time
import datetime
import re
import random

# Figure out what the date is

now = datetime.datetime.now()
month = now.month
date = time.strftime("%m-%Y")

# Parse users:

pattern1 = re.compile("n199..")
pattern2 = re.compile("n299..")
users1 = []
users2 = []

with open("/etc/passwd") as file:
    for line in file:
        if int(line.split(":")[2]) > 1000 and pattern1.match(line.split(":")[0]) and not str(line.split(":")[6]).__contains__("nologin"):
            users1.append(line.split(":")[0])

with open("/etc/passwd") as file:
    for line in file:
        if int(line.split(":")[2]) > 1000 and pattern2.match(line.split(":")[0]) and not str(line.split(":")[6]).__contains__("nologin"):
            users2.append(line.split(":")[0])

# Define the password generator

def entropygen():
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   upperalphabet = alphabet.upper()
   pw_len = 32
   pwlist = []
   for i in range(pw_len//3):
      pwlist.append(alphabet[random.randrange(len(alphabet))])
      pwlist.append(upperalphabet[random.randrange(len(upperalphabet))])
      pwlist.append(str(random.randrange(10)))
   for i in range(pw_len-len(pwlist)):
      pwlist.append(alphabet[random.randrange(len(alphabet))])

      random.shuffle(pwlist)
      pwstring = "".join(pwlist)

# Define some settings:

cycle = int(input("Are you making 1.n199xx keys or 2. n299xx keys? : "))
date = time.strftime("%m-%Y")


def genwininst():
    if cycle in ['1', '1.']:
        destination = "/root/vpn-installers-%s/%s" % (date, users1[i])
        generateinstaller = "/usr/local/openvpn_as/scripts/sacli --itype msi --cn %s GetInstaller" % users1[i]
        mkdir = "mkdir -p %s" % destination
        movefiles = "/bin/mv /usr/local/openvpn_as/etc/tmp/openvpn-connect-2.1.*.msi /root/vpn-installers-%s/%s/%s.msi" % (date, users1[i], users1[i])
        print("Creating destination folder at %s") % destination
        os.system(mkdir)
        os.chdir(destination)
        entropy = entropygen()
        genkey = "openssl enc -aes-256-cbc -k %s -P -md sha256 | grep key | cut -d \"=\" -f2 > key.dat" % entropy
        os.system(genkey)
    else:
        destination = "/root/vpn-installers-%s/%s" % (date, users2[i])
        generateinstaller = "/usr/local/openvpn_as/scripts/sacli --itype msi --cn %s GetInstaller" % users2[i]
        mkdir = "mkdir -p %s" % destination
        movefiles = "/bin/mv /usr/local/openvpn_as/etc/tmp/openvpn-connect-2.1.*.msi /root/vpn-installers-%s/%s/%s.msi" % (date, users2[i], users2[i])
        print("Creating destination folder at %s") % destination
        os.system(mkdir)
        os.chdir(destination)
        entropy = entropygen()
        genkey = "openssl enc -aes-256-cbc -k %s -P -md sha256 | grep key | cut -d \"=\" -f2 > key.dat" % entropy
        os.system(genkey)

    os.system(generateinstaller)
    os.system(movefiles)


def genmacinst():
    if cycle in ['1', '1.']:
        destination = "/root/vpn-installers-%s/%s" % (date, users1[i])
        generateinstaller = "/usr/local/openvpn_as/scripts/sacli --itype dmg --cn %s GetInstaller" % users1[i]
        mkdir = "mkdir -p %s" % destination
        movefiles = "/bin/mv /usr/local/openvpn_as/etc/tmp/openvpn-connect-2.1.*.dmg /root/vpn-installers-%s/%s/%s.dmg" % (date, users1[i], users1[i])
        print("Creating destination folder at %s") % destination
        os.system(mkdir)
        os.chdir(destination)
        entropy = entropygen()
        genkey = "openssl enc -aes-256-cbc -k %s -P -md sha256 | grep key | cut -d \"=\" -f2 > key.dat" % entropy
        os.system(genkey)

    else:
        destination = "/root/vpn-installers-%s/%s" % (date, users2[i])
        generateinstaller = "/usr/local/openvpn_as/scripts/sacli --itype dmg --cn %s GetInstaller" % users2[i]
        mkdir = "mkdir -p %s" % destination
        movefiles = "/bin/mv /usr/local/openvpn_as/etc/tmp/openvpn-connect-2.1.*.dmg /root/vpn-installers-%s/%s/%s.dmg" % (date, users2[i], users2[i])
        print("Creating destination folder at %s") % destination
        os.system(mkdir)
        os.chdir(destination)
        entropy = entropygen()
        genkey = "openssl enc -aes-256-cbc -k %s -P -md sha256 | grep key | cut -d \"=\" -f2 > key.dat" % entropy
        os.system(genkey)

    os.system(generateinstaller)
    os.system(movefiles)


def genlinuxfiles():
    if cycle in ['1', '1.']:
        destination = "/root/vpn-installers-%s/%s" % (date, users1[i])
        mkdir = "mkdir -p %s" % destination
        generateinstaller = "/usr/local/openvpn_as/scripts/sacli -a openvpn -o /root/vpn-installers-%s/%s --cn %s get5" % (date, users1[i], users1[i])
        linuxzip = "zip linuxfiles.zip ca.crt client.crt client.key ta.key client.ovpn"
        os.chdir(destination)
        entropy = entropygen()
        genkey = "openssl enc -aes-256-cbc -k %s -P -md sha256 | grep key | cut -d \"=\" -f2 > key.dat" % entropy
        os.system(genkey)

    else:
        destination = "/root/vpn-installers-%s/%s" % (date, users2[i])
        mkdir = "mkdir -p %s" % destination
        generateinstaller = "/usr/local/openvpn_as/scripts/sacli -a openvpn -o /root/vpn-installers-%s/%s --cn %s get5" % (date, users2[i], users2[i])
        linuxzip = "zip linuxfiles.zip ca.crt client.crt client.key ta.key client.ovpn"
        os.chdir(destination)
        entropy = entropygen()
        genkey = "openssl enc -aes-256-cbc -k %s -P -md sha256 | grep key | cut -d \"=\" -f2 > key.dat" % entropy
        os.system(genkey)

    print("Creating destination folder at %s") % destination
    os.system(generateinstaller)

# Make Installers, make a key then encypt things with it.

if cycle == 1:
    for i in range(len(users1)):
        genwininst()
        genmacinst()
        genlinuxfiles()
        i = i + 1
else:
    for i in range(len(users2)):
        genwininst()
        genmacinst()
        genlinuxfiles()
        i = i + 1
