#!/bin/bash
#This a script to backup a server to a remote Rsync server.
#It make a backup on the target server in the /backup/<server>/daily/<date>
#You must have key based SSH logins setup prior to running this. It will create a log
#in the folder it is launched from.
#
#Also, be aware that as this should be run as root (to preserve permissions for recovery)
#You should also disable ssh logins using passwords and restrict the IPs that are allowed
#to login the the server using SSH!
#
#Change values in <> to match your environment.
#
#This script requires sendmail to be installed.

HOST=<Your server's name>
RSYNC=/usr/bin/rsync
SSH=/usr/bin/ssh
TARGET=/backup/$host/daily/
SERVER=<IP or DNS name of server>
DATE=`date +%F`
SENDMAIL=`which sendmail`
LOG=/root/backupscript/log
#What you want to back up:
SOURCE1=/etc/apache2
SOURCE2=/etc/dhcp
SOURCE3=/etc/dhcp3
SOURCE4=/home/user
SOURCE5=/opt/sqlbk
SOURCE6=/opt/music
#Make sure the destination folders exist
ssh root@$SERVER "mkdir -p $TARGET/$SOURCE1"
ssh root@$SERVER "mkdir -p $TARGET/$SOURCE2"
ssh root@$SERVER "mkdir -p $TARGET/$SOURCE3"
ssh root@$SERVER "mkdir -p $TARGET/$SOURCE4"
ssh root@$SERVER "mkdir -p $TARGET/$SOURCE5"
ssh root@$SERVER "mkdir -p $TARGET/$SOURCE6"
#Make changelog dir
mkdir -p $LOG
#Backup all the things!
$RSYNC -azv --numeric-ids -e $SSH $SOURCE1 root@$SERVER:$TARGET/$SOURCE1 >> $LOG/log-$DATE
$RSYNC -azv --numeric-ids -e $SSH $SOURCE2 root@$SERVER:$TARGET/$SOURCE2 >> $LOG/log-$DATE
$RSYNC -azv --numeric-ids -e $SSH $SOURCE3 root@$SERVER:$TARGET/$SOURCE3 >> $LOG/log-$DATE
$RSYNC -azv --numeric-ids -e $SSH $SOURCE4 root@$SERVER:$TARGET/$SOURCE4 >> $LOG/log-$DATE
$RSYNC -azv --numeric-ids -e $SSH $SOURCE5 root@$SERVER:$TARGET/$SOURCE5 >> $LOG/log-$DATE
$RSYNC -azv --numeric-ids -e $SSH $SOURCE6 root@$SERVER:$TARGET/$SOURCE6 >> $LOG/log-$DATE
#Email results
if [ $? -eq 0 ]
then
mail -s "$HOST's backup for `date +%F` Succeeded" <Your email address> < $LOG/log-$DATE
else
mail -s "$HOST's backup for `date +%F` FAILED!" <Your email address> < $LOG/log-$DATE
fi
