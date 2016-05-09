# https://registry.hub.docker.com/_/centos/
FROM centos:centos7

RUN yum -y install epel-release
RUN yum -y groupinstall 'Development Tools'
RUN yum -y install git make wget tar bzip2 python python-devel python-distribute python-pip

RUN pip install web.py

# download MITIE
RUN cd /; git clone https://github.com/mit-nlp/MITIE.git

# download MITIE models
RUN cd /MITIE; make MITIE-models

# build MITIE executables and libs
RUN cd /MITIE; make

# Bundle app source
ADD src /mitie-server

EXPOSE 8888
CMD ["/mitie-server/server.py", "0.0.0.0", "8888"]