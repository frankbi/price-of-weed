#!/bin/bash

# get today's year, month and day for commit message
yearmonthday=$(date -d "yesterday 13:00 " '+%Y-%m-%d')

# pull before running script
git pull

python weed_scraper.py

git add -A

git commit -a -m "prices for $yearmonthday"

git push