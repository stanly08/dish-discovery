#!/bin/bash
cd /root/dish-discovery/ || exit
git pull origin master  # or the correct branch name
source /root/dish-discovery/venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart dish-discovery
