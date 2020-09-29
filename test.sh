#!/bin/bash

# Crontab Commands

# List all the crontabs available
# crontab -l

# Edit Crontab
# crontab -e

# Delete Crontab
# crontab -r

# Edit other users crontab
# crontab -u user1 -e 

# echo "===== Starting Xampp Server ====="
# sudo /opt/lampp/lampp start
# echo "===== Server Started ====="

echo "===== Initiating Environment ====="
source "/mnt/E4687B61687B3182/CSE/Insta script/instaEnv/bin/activate"
echo "===== Environment Initialised ====="

cd /mnt/E4687B61687B3182/CSE/Insta\ script/Unfollow
echo "===== Arrived at proper directory ====="

now=$(date +"%m-%d-%Y=%T")
echo "Current time : $now"

echo "===== Starting the Script ====="
echo "Script started" >./Logs/$now-out.txt 2>./Logs/$now-err.txt
echo "===== Script Completed ====="