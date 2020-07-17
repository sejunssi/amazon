#!/bin/bash

tmux new -s extract_year -d

tmux send-keys "
python extract_year.py -f '2014/all.json'
wait" C-m


tmux send-keys "
python extract_year.py -f '2018/all.json'
wait" C-m

tmux kill-session -t extract_year

#
#tmux send-keys "
#python extract_year.py -y 2014 -f '2014/all.json'
#wait" C-m
#
#tmux send-keys "
#python extract_year.py -y 2014 -f '2018/all.json'
#wait" C-m

