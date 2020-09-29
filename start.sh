#!/bin/bash

# echo "===== Starting Xampp Server ====="
# sudo /opt/lampp/lampp start
# echo "===== Server Started ====="

echo "===== Initiating Environment ====="
source "/opt/lampp/htdocs/github/Instagram-Follower-List-Script/instaEnv/bin/activate"
echo "===== Environment Initialised ====="

cd /opt/lampp/htdocs/github/Instagram-Follower-List-Script/02\ Unfollow
echo "===== Arrived at proper directory ====="

now=$(date +"%m-%d-%Y=%T")
echo "Current time : $now"

echo "===== Starting the Script ====="
python3 main.py >./Logs/$now-out.txt 2>./Logs/$now-err.txt
echo "===== Script Completed ====="