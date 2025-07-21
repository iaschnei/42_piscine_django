#/bin/sh

curl --silent $1 | grep href | cut --fields 2 --delimiter '"'