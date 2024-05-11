# Part 2

Instruction to run a Hadoop program for n-gram frequencies

### Note

The Hadoop environment supported Python3 version for us.

## Steps

```python

cd ../..             

ls
#bin  boot  bootstrap.sh  dev  etc  hadoop-3.2.1.tar.gz  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

mkdir miniproject1  

cd miniproject1
#Copy input.txt, ngrammapper.py, ngramreducer.py from the submitted folder Part 2

cd opt/hadoop

bin/hadoop fs -mkdir miniprojectdfs

bin/hadoop fs -put /miniproject1/input.txt miniprojectdfs/input

bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/ngrammapper.py,/miniproject1/ngramreducer.py -input miniprojectdfs/ -output miniprojectdfs/output -mapper "python3 ngrammapper.py 2" -reducer "python3 ngramreducer.py"

bin/hdfs dfs -cat miniprojectdfs/output/*

```

# Part 3

In this part, we developed MapReduce programs to analyze a real anonymous log file and answer several questions based on the log data. The log file, named access_log, follows the Common Log Format with additional fields.

The python map-reduce programs are located at :
```bash
cd /miniproject1
```
```bash
cd opt/hadoop
bin/hadoop fs -mkdir -p /miniprojectdfs
```

## Problem 1

How many hits were made to the website directory “/images/smilies/”(including subdirectories and files)?


```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem1
```
```bash
bin/hadoop fs -put /opt/hadoop/access_log /miniprojectdfs/problem1
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p1mapper.py,/miniproject1/p1reducer.py -input /miniprojectdfs/problem1 -output /miniprojectdfs/problem1/output -mapper "python p1mapper.py" -reducer "python p1reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem1/output/*
```

## Problem 2

How many hits were made from the IP: 96.32.128.5?

```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem2
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p2mapper.py,/miniproject1/p2reducer.py -input /miniprojectdfs/problem1 -output /miniprojectdfs/problem2/output -mapper "python p2mapper.py" -reducer "python p2reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem2/output/*
```
## Problem 3

How many HTTP request methods are used in this file? What are they?
```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem3
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p3mapper.py,/miniproject1/p3reducer.py -input /miniprojectdfs/problem1 -output /miniprojectdfs/problem3/output -mapper "python p3mapper.py" -reducer "python p3reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem3/output/*
```
## Problem 4

Which path in the website has been hit most? How many hits were made to the path?
```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem4
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p4mapper.py,/miniproject1/p4reducer.py -input /miniprojectdfs/problem1 -output /miniprojectdfs/problem4/output -mapper "python p4mapper.py" -reducer "python p4reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem4/output/*
```
## Problem 5

Which IP accesses the website most? How many accesses were made by it?
```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem5
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p5mapper.py,/miniproject1/p5reducer.py -input /miniprojectdfs/problem1 -output /miniprojectdfs/problem5/output -mapper "python p5mapper.py" -reducer "python p5reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem5/output/*
```
## Problem 6

How many POST request were made?
```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem6
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p6mapper.py,/miniproject1/p6reducer.py -input /miniprojectdfs/problem1 -output /miniprojectdfs/problem6/output -mapper "python p6mapper.py" -reducer "python p6reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem6/output/*
```
## Problem 7

How many requests received a 404 status code?
```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem7
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p7mapper.py,/miniproject1/p7reducer.py -input /miniprojectdfs/problem1 -output /miniprojectdfs/problem7/output -mapper "python p7mapper.py" -reducer "python p7reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem7/output/*
```
## Problem 8

How much data was requested on 19/Dec/2020?
```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem8
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p8mapper.py,/miniproject1/p8reducer.py -input /miniprojectdfs/problem1 -output /miniprojectdfs/problem8/output -mapper "python p8mapper.py" -reducer "python p8reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem8/output/*
```
## Problem 9

List 3 IPs that access the most, and what is the total data flow size of each IP?
```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem9
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p9mapper.py,/miniproject1/p9reducer.py -input /miniprojectdfs/problem1 -output /miniprojectdfs/problem9/output -mapper "python p9mapper.py" -reducer "python p9reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem9/output/*
```
## Problem 10

How much data(in bytes) was successfully(with status code 200) requested on 16/Jan/2022?
```bash
bin/hadoop fs -mkdir -p /miniprojectdfs/problem10
```
To run this program on hadoop, we used the following command:
```bash
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files /miniproject1/p10mapper.py,/miniproject1/p10reducer.py -input /miniprojectdfs/problem10 -output /miniprojectdfs/problem10/output -mapper "python p10mapper.py" -reducer "python p10reducer.py"
```
To display the output, use the below command:
```bash
bin/hdfs dfs -cat /miniprojectdfs/problem10/output/*
```