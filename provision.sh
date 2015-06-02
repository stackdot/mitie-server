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

# #########################################################
#
# Docker
#
sudo yum -y install docker
sudo systemctl daemon-reload
sudo systemctl restart docker
