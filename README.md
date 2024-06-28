# Cloud Computing Project - Hadoop LogAnalyser

## Overview:
This project explores setting up Hadoop in Docker, developing MapReduce programs for log analysis, and solving specific problems using Hadoop clusters. The report includes detailed configurations, scripts, and solutions for various tasks.

## File Structure:
The attached zip file contains separate folders for each part of the project:
- **Part 1: Setting up Hadoop in Docker**
  - Dockerfile
  - bootstrap.sh
  - core-site.xml
  - hdfs-site.xml
  - mapred-site.xml
  - yarn-site.xml
- **Part 2: MapReduce Programs**
  - ngrammapper.py
  - ngramreducer.py
  - input.txt
- **Part 3: Log Analysis**
  - Mapper and Reducer scripts for each problem

## Setting up Hadoop in Docker:
1. Build a Docker image based on the provided Dockerfile.
2. Generate public-private RSA key pair using the ssh-keyget command.
3. Initialize core components of a Hadoop cluster using start-dfs.sh and start-yarn.sh scripts.

## MapReduce Programs:
- Analyze log files using MapReduce programs.
- Solve specific problems based on log data, such as counting hits to a website directory and calculating n-gram frequencies.

## Instructions for Running the Project:
1. Ensure Docker is installed on your system.
2. Execute the provided scripts to set up Hadoop in Docker.
3. Run MapReduce programs using the provided commands for log analysis.
4. Refer to individual parts for detailed instructions and solutions.

## Project Submission:
For any inquiries or assistance related to this project, please contact:
- Bhavana Devulapally
- Shusrita Venugopal
- Neha Navarkar

Feel free to reach out to us for further clarification or support. Thank you for exploring our Project!

---
