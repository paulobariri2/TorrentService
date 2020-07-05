#!/bin/bash

ps

IFS=' '

read -ra ADDR <<< $(ps | grep transmission)

kill -9 ${ADDR[0]}

pwd

python3 /usr/src/app/updatetorrent.py ${ADDR[0]}
