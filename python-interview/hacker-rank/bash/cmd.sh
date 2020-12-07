#!/bin/bash

awk '{avg=($2+$3+$4)/3; print $0, ":", (avg<50)?"FAIL":(avg<80)?"B":"A"}'
awk '{if ($4 !~ /[0-9]/) print "Not all scores are available for", $1}' 
awk '{print $1, ":", ($2<50||$3<50||$4<50) ? "Fail" : "Pass"}'
awk 'ORS=NR%2?";":"\n"'

find . -name "*.txt" -exec cat {} \;
find . -name "*.txt" -exec ls -la --color {} \;
find . -name "*.txt" -printf "%p %k KB\n"
find . -name "*.txt" -ls
find . -name "*.txt" -ls -perm 777 -size +1k
find / -name kernel -type d exec ls -l {} \;  
find / -name kernel -type d | xargs ls -l 

sed 's/\bthe\b/this/'
sed 's/thy/{&}/ig'
sed 's/thy/your/ig'

ls | xargs cat
ls lS
ls lShr
ls -l --sort=time
tar -cf archieve.tar .
tar -tf archieve.tar 
tar -czf archieve2.tar.gz .
tar -xvzf /root/archieve.tar.gz

useradd -m erdem
passwd erdem
su - erdem
deluser -r erdem

adduser erdem
cat /etc/adduser.conf
chown -R erdem:erdem /tmp
chmod g-x e.txt
cmod a+x e.txt
chmod u+x e.txt
export PATH=$PATH:/root/bin

hostname -i
ip address | grep inet
ip route

cat /etc/default/useradd
nano /etc/ssh/sshd_config -> PasswordAuthentication no
echo $0

adduser erdem sudo
nano /etc/sudoers
nano /etc/network/interfaces

ssh-keygen -t rsa -b 4096
eval `ssh-agent -s`
ssh-add
sudo erdem@192.168.1.68 mkdir .ssh
chmod 700 .ssh/; chmod 640 .ssh/authorized_keys 