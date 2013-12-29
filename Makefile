target:
	python weed_scraper.py
	git pull
	git add *
	git commit -a -m "today's prices"
	git push
