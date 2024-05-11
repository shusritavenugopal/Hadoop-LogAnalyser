#!/bin/bash

# start ssh server
#/etc/init.d/ssh start

# format namenode

sudo $hadoop_path/bin/hdfs namenode -format

#start hadoop
$hadoop_path/sbin/start-dfs.sh
$hadoop_path/sbin/start-yarn.sh
$hadoop_path/sbin/mr-jobhistory-daemon.sh start historyserver
tail -f /dev/null