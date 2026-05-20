#!/bin/bash

cd /opt/testbot

pkill -f bot.py

curl -sL https://raw.githubusercontent.com/voin57rus/seper_puper/main/bot.py -o bot.py

nohup python3 bot.py > bot.log 2>&1 &

echo "BOT UPDATED"