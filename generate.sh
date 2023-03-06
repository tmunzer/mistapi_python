#!/bin/zsh

if [ ! $1 ]
then
    echo "Missing version"
    exit 0
fi

echo "Updating OPENAPI local repo"
cd mist_openapi
git pull
cd ..

echo "Updating version in pyproject.toml to $1"
sed -e "s/version = .*/version = \"$1\"/g" pyproject.toml > new_pyproject.toml 
mv new_pyproject.toml pyproject.toml   
sed -e "s/__version__ = .*/__version__ = \"$1\"/g" ./src/mistapi/__init__.py > ./src/mistapi/__init__.py.new
mv ./src/mistapi/__init__.py.new ./src/mistapi/__init__.py

python3 ./generate_from_openapi.py
