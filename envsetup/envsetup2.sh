#! /bin/bash

echo 'vagrant' | sudo -S ls
sudo apt-get update
sudo apt-get --yes install python-pip python3-pip git
sudo pip install virtualenv
sudo pip3 install virtualenv

sudo apt-get --yes install software-properties-common
sudo apt-add-repository --yes ppa:ansible/ansible
sudo apt-get update
sudo apt-get --yes install ansible

sudo apt-get --yes install python-dev python3-dev
sudo apt-get --yes install libevent-dev

sudo apt-get --yes install tcpdump graphviz imagemagick python-gnuplot python-crypto python-pyx
sudo pip install scapy

sudo pip3 install --upgrade pip
sudo pip3 install jupyter

sudo add-apt-repository --yes ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get --yes install sublime-text-installer

cd ~
wget https://download.jetbrains.com/python/pycharm-community-2016.3.2.tar.gz
tar xzvf pycharm-community-2016.3.2.tar.gz 
sudo mv pycharm-community-2016.3.2 /opt/
sudo mv /opt/pycharm-community-2016.3.2/ /opt/pycharm
sudo ln -s /opt/pycharm/bin/pycharm.sh /usr/local/bin/pycharm 

sudo apt-add-repository --yes universe
sudo apt-get update
sudo apt-get --yes install wireshark


