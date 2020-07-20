#!/bin/bash

tmux new -s inner_join -d

tmux send-keys "
python inner_join.py
wait" C-m

tmux send-keys "
tmux kill-session -t inner_join
wait" C-m
