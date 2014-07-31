#/bin/bash

cd data

mkdir -p today

cd ..

python get_today.py > data/today/data.json