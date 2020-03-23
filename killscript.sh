#!/bin/bash

ps

IFS=' '

read -ra ADDR <<< $(ps | grep transmission)

echo ${ADDR[0]}

kill -9 ${ADDR[0]}

#killall transmission-cli
