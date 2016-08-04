#!/bin/bash
#
#This script sets the SHMMAX and SHMALL up for processing clusters in an automated way.
#The idea is to allow a process to use more memory in a single chunk, whichis good for 
#calculations.
#
# -This was written for Ubuntu/Debian, It likely will need some tweaking to work on a 
# -Redhat (or other) system
#
#Andrew Damin, 6/20/16

page_size=`getconf PAGE_SIZE`

if [ -z "$page_size" ]; then
  echo Error: Cannot determine page size, Something broke!
  exit 1
fi

totalram=`free -b | awk '/^Mem:/{print $2}'`
cutram=`expr \`free -b | awk '/^Mem:/{print $2}'\` \* 75 | awk '{printf "%.f", $1/100}'`
shmall=`expr $cutram / $page_size`
shmmax=`expr $totalram / 2`

echo ""
echo  Maximum shared segment size in bytes
echo $shmmax
echo "--------------"
echo  Maximum number of shared memory segments in pages
echo $shmall
echo "--------------"
echo "Applying..."
sleep 3

#Sets SHMMAX in running config
sysctl -w kernel.shmmax=$shmmax

#Checks to see if line exists in /etc/sysctl.conf and if it does not, add it
grep -q -F 'kernel.shmmax =' /etc/sysctl.conf || echo "kernel.shmmax = $shmmax" >> /etc/sysctl.conf

if [ $? -eq 0 ]; then
   echo Set SHMMAX successfully!
   else
   echo "Can't set SHMMAX, Did you forget to sudo?"
   exit 2
fi

#Sets SHMALL in running config
sysctl -w kernel.shmall=$shmall

#Checks to see if line exists in /etc/sysctl.conf and if it does not, add it
grep -q -F 'kernel.shmall =' /etc/sysctl.conf || echo "kernel.shmall = $shmall" >> /etc/sysctl.conf

if [ $? -eq 0 ]; then
   echo "Set SHMALL successfully!"
   echo ""
   echo "Done!"
   exit 0
   else
   echo "Can't set SHMALL, Did you forget to sudo?"
   exit 3
fi
