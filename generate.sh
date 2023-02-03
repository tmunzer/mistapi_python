#!/bin/zsh

if [ ! $1 ]
then
    echo "Missing version"
fi

echo "Updating OPENAPI local repo"
cd mist_openapi
git pull
cd ..

echo "Updating version in pyproject.toml to $1"
sed -e "s/version = .*/version = \"$1\"/g" pyproject.toml > new_pyproject.toml 
mv new_pyproject.toml pyproject.toml   

python3 ./generate_from_openapi.py
