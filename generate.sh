#!/bin/zsh

cd mist_openapi
git pull
cd ..
python3 ./generate_from_openapi.py
