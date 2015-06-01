##!/usr/bin/env bash

# #########################################################
# Update the OS
sudo yum -y update

# #########################################################
# Install development environment
sudo yum -y install epel-release
sudo yum -y groupinstall "Development Tools"
sudo yum -y install screen java-1.7.0-openjdk-devel python-pip
sudo yum -y install python-devel libxml2-devel libxslt-devel libjpeg-devel zlib-devel libpng12-devel yajl
sudo yum -y install cmake

# Disable SELinux for development
sudo sed -i 's/SELINUX=permissive/SELINUX=disabled/g' /etc/selinux/config /etc/selinux/config

# #########################################################
# Python Tools

# Upgrade Python package manager
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv

# IPython
#   Note:   ipython notebook --ip='*'
sudo pip install ipython[all]

# Pandas
#sudo pip install pandas

# Newspaper: Scraping, Extraction and NLP 
#cd /vagrant
#sudo pip install newspaper
#sudo curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python

# Goose: Content Extrction
#cd /vagrant
#sudo mkvirtualenv --no-site-packages goose
#git clone https://github.com/grangier/python-goose.git
#cd python-goose
#sudo pip install -r requirements.txt
#sudo python setup.py install

# Feedparser
#sudo pip install feedparser

# Work with CSV files on the command line
#sudo pip install csvkit

# Work with Excel files
#sudo pip install xlsx2csv

# Elasticsearch Client
#sudo pip install elasticsearch

# MySQL Python Connector
#wget --quiet http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.0.4-1.el7.noarch.rpm
#sudo rpm -ivh mysql-connector-python-2.0.4-1.el7.noarch.rpm

# PRAW - Reddit client
#sudo pip install praw


# #########################################################
# MITIE NLP
cd /vagrant
git clone https://github.com/mit-nlp/MITIE.git
cd /vagrant/MITIE

# download models
make MITIE-models

# build executables and libs
make

# build Java bindings
cd mitielib/java
mkdir build
cd build
cmake ..
cmake --build . --config Release --target install

# #########################################################
#
# NodeJs and common Libs
#
sudo yum -y install nodejs npm


# #########################################################
#
# Docker
#
sudo yum -y install docker
sudo systemctl daemon-reload
sudo systemctl restart docker


# #########################################################
#
# Scala
#
#cd /vagrant
#wget --quiet http://downloads.typesafe.com/scala/2.11.5/scala-2.11.5.rpm
#sudo rpm -ivh scala-2.11.5.rpm
