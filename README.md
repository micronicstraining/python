# python
Python Zero-to-Hero course material and labs

Environment setup

0) Install VirtualBox - https://www.virtualbox.org/wiki/Downloads

1) Install Vagrant - https://www.vagrantup.com/downloads.html

2) On this page click "clone or download" and download zip

3) Extract the zip file and go to envsetup folder

$ unzip python-master.zip

$ cd python-master

$ cd envsetup

You need to be in the same directory as Vagrantfile.

4) Provision the VM with vagrant

$ vagrant up

Give it some time as it installs the necessary tools.

Look at envsetup.sh for details on what is being installed in case you would prefer setting up your local machine instead of a VM.  The script has been written and tested only for Ubuntu.

5) Login to VM:

Username: vagrant
Password: vagrant

6) Open terminal by clicking top left icon and typing terminal.

7) Open pycharm to ensure it installed

Inside the VM terminal:
$ pycharm

Create a new project and wait for everything to initialize and sync.
If you look at the bottom status bar in the PyCharm window it may
sync for quite a while.

8) Close pycharm once everything syncs.

9) Stop the VM via vagrant command.

In your outter terminal:
$ vagrant halt

If you have questions, need help setting up or find a mistake please contact me: avakyan@gmail.com
