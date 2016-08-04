#!/usr/bin/python

#This script generates VPN packages for clients and stores them in /root/vpninstallers<date>

import os
import time

#Input users here:

windows_users1=["user1","user2","user3"]

windows_users2=["user1","user2","user3"]

mac_users1=["user1","user2","user3"]

mac_users2=["user1","user2","user3"]

linux_users1=["user1","user2","user3"]

linux_users2=["user1","user2","user3"]

#---------------

cycle = int(input("Are you making 1.) cycle 1 keys or 2.) cycle 2 keys? : "))

i = 0
j = 0
k = 0
date=time.strftime("%m-%Y")

if cycle == 1:
        totalwin = len(windows_users1)
        totalmac= len(mac_users1)
        totallinux= len(linux_users1)
        while i < totalwin:
                print("Creating Windows installer for %s") % windows_users1[i]
                generateinstaller="/usr/local/openvpn_as/scripts/sacli --itype msi --cn %s GetInstaller" % windows_users1[i]
                os.system(generateinstaller)
                print("Creating destination folder and moving into there...")
                createdir="/bin/mkdir -p /root/vpninstallers-%s/%s" % (date, windows_users1[i])
                movewin="/bin/mv /usr/local/openvpn_as/etc/tmp/openvpn-connect-2.0.??.???.msi /root/vpninstallers-%s/%s/%s.msi" % (date, windows_users1[i], windows_users1[i])
                os.system(createdir)
                os.system(movewin)
                i = i + 1
        while j < totalmac:
                print("Creating Mac installer for %s") % mac_users1[j]
                generateinstaller="/usr/local/openvpn_as/scripts/sacli --itype dmg --cn %s GetInstaller" % mac_users1[j]
                os.system(generateinstaller)
                print("Creating destination folder and moving into there...")
                createdir="/bin/mkdir -p /root/vpninstallers-%s/%s" % (date, mac_users1[j])
                move="/bin/mv /usr/local/openvpn_as/etc/tmp/openvpn-connect-2.0.??.???.dmg /root/vpninstallers-%s/%s/%s.dmg" % (date, mac_users1[j], mac_users1[j])
                os.system(createdir)
                os.system(move)
                j = j + 1
        while k < totallinux:
                print("Creating Linux files for %s") % linux_users2[k]
                print("Creating destination folder and moving files there..")
                generateinstaller="/usr/local/openvpn_as/scripts/sacli -a openvpn -o /root/vpninstallers-%s/%s --cn %s get5" % (date, linux_users1[k], linux_users1[k])
                createdir="/bin/mkdir -p /root/vpninstallers-%s/%s" % (date, linux_users1[k])
                os.system(createdir)
                os.system(generateinstaller)
                k = k + 1
                elif cycle == 2:
        totalwin = len(windows_users1)
        totalmac= len(mac_users1)
        totallinux= len(linux_users1)
        while i < totalwin:
                print("Creating Windows installer for %s") % windows_users2[i]
                generateinstaller="/usr/local/openvpn_as/scripts/sacli --itype msi --cn %s GetInstaller" % windows_users2[i]
                os.system(generateinstaller)
                print("Creating destination folder and moving into there...")
                createdir="/bin/mkdir -p /root/vpninstallers-%s/%s" % (date, windows_users2[i])
                movewin="/bin/mv /usr/local/openvpn_as/etc/tmp/openvpn-connect-2.0.??.???.msi /root/vpninstallers-%s/%s/%s.msi" % (date, windows_users2[i], windows_users2[i])
                os.system(createdir)
                os.system(movewin)
                i = i + 1
        while j < totalmac:
                print("Creating Mac installer for %s") % mac_users2[j]
                generateinstaller="/usr/local/openvpn_as/scripts/sacli --itype dmg --cn %s GetInstaller" % mac_users2[j]
                os.system(generateinstaller)
                print("Creating destination folder and moving into there...")
                createdir="/bin/mkdir -p /root/vpninstallers-%s/%s" % (date, mac_users2[j])
                move="/bin/mv /usr/local/openvpn_as/etc/tmp/openvpn-connect-2.0.??.???.dmg /root/vpninstallers-%s/%s/%s.dmg" % (date, mac_users2[j], mac_users2[j])
                os.system(createdir)
                os.system(move)
                j = j + 1
        while k < totallinux:
                print("Creating Linux files for %s") % linux_users2[k]
                print("Creating destination folder and moving files there...")
                generateinstaller="/usr/local/openvpn_as/scripts/sacli -a openvpn -o /root/vpninstallers-%s/%s --cn %s get5" % (date, linux_users2[k], linux_users2[k])
                createdir="/bin/mkdir -p /root/vpninstallers-%s/%s" % (date, linux_users2[k])
                os.system(createdir)
                os.system(generateinstaller)
                k = k + 1
else:
        print("Invalid character!")

