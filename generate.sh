#!/bin/zsh

cd mist_openapi
git pull
cd ..
python3 ./generate.py
