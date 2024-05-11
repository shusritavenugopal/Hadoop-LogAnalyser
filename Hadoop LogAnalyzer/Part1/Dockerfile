FROM ubuntu:18.04

USER root
ENV hadoop_path /opt/hadoop
ENV java_path /usr/lib/jvm/java-8-openjdk-amd64


RUN \
   apt-get update && apt-get install -y \
   ssh \
   rsync \
   vim \
   openjdk-8-jdk

RUN \
   wget https://archive.apache.org/dist/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz \
    && \
    tar -xzf hadoop-3.2.1.tar.gz && \
    mv hadoop-3.2.1 $hadoop_path && \
    echo "export JAVA_HOME=$java_path" >> $hadoop_path/etc/hadoop/hadoop-env.sh && \
    echo "PATH=$PATH:$hadoop_path/bin" >> ~/.bashrc
RUN /etc/init.d/ssh start

ADD *.xml $hadoop_path/etc/hadoop/
ADD *.jar $hadoop_path
ADD bootstrap.sh bootstrap.sh
ADD access_log $hadoop_path

EXPOSE 8088 50070 50075 50030 50060
cmd bash bootstrap.sh




#docker build .
#sudo docker images
#sudo docker run -it -d name /bin/bash
#
#sudo docker ps
#sudo docker exec -it name
