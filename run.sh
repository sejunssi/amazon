#!/bin/bash

tmux new -s preprocessing -d

tmux send-keys "
python extract_year.py -f '2014/all.json' &
python extract_year.py -f '2018/all.json' &
wait" C-m


tmux send-keys "
python inner_join.py
wait" C-m


tmux send-keys "
python inner_join_metadata.py -f 'merged_all'
wait" C-m

tmux kill-session -t preprocessing

