#!/bin/bash

mkdir -p /opt/testbot
cd /opt/testbot

apt update -y
apt install -y python3 python3-pip

python3 -m pip install -U python-telegram-bot --break-system-packages

curl -sL https://raw.githubusercontent.com/voin57rus/seper_puper/main/bot.py -o bot.py

nohup python3 bot.py > bot.log 2>&1 &

echo "BOT INSTALLED"