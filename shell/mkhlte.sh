#!/bin/bash

# Depends on `brew install highlight`.
/opt/homebrew/bin/highlight -i $1 -o $2 -O html -k "JetBrainsMono Nerd Font" -K 12 -l --inline-css -T $1 -W 
