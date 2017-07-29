#!/bin/bash

#This script will generate one-off VPN installers for any user already setup on a OpenVPN server

echo "What account are you creating a installer for?"
read USER

cut -d':' -f1 /etc/passwd | grep $USER >/dev/null
if [ $? -eq 0 ]; then
   NAME=`cat /etc/passwd | grep $USER | cut -d ':' -f5 | cut -d ',' -f1`
   echo "What OS? Windows(w), MacOS(m) or a pack of Linux files(l)?"
   read -${BASH_VERSION+e}r OS
   case $OS in
      "w")
         WINDOWS=$(/usr/local/openvpn_as/scripts/sacli --itype msi --cn $USER Getinstaller ARG1 2>&1)
         LOCATION=`echo $WINDOWS | cut -d' ' -f3`
         mv $LOCATION /tmp/$USER-`date +%F`.msi
         echo "Created Windows VPN installer for $NAME at /tmp/$USER-`date +%F`.msi"
         ;;
      "m")
         MAC=$(/usr/local/openvpn_as/scripts/sacli --itype dmg --cn $USER Getinstaller ARG1 2>&1)
         LOCATION=`echo $MAC | cut -d' ' -f3`
         mv $LOCATION /tmp/$USER-`date +%F`.dmg
         echo "Created Mac VPN installer for $NAME at /tmp/$USER-`date +%F`.dmg"
         ;;
      "l")
         mkdir /tmp/$USER-`date +%F`
         /usr/local/openvpn_as/scripts/sacli -a openvpn -o /tmp/$USER-`date +%F` --cn $USER get5
         echo "Created Linux VPN config files for $NAME and put them at /tmp/$USER-`date +%F`"
         ;;
      *)
         echo "Only Windows, MacOS and Linux are supported!"
         ;;
   esac
else
   echo "Error: User was not found!"
fi
