#!/bin/bash

ps

IFS=' '

read -ra ADDR <<< $(ps | grep transmission)

kill -9 ${ADDR[0]}
