#!/bin/bash

tmux new -s extract_inner_join -d

tmux send-keys "
python inner_join_metadata.py -f1 'filename'
wait" C-m