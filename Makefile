target:
	python weed_scraper.py
	git pull
	git add -A
	git commit -a -m "today's prices"
	git push

push:
	git pull
	git add -A
	git commit -a -m "updates, made on the fly!"
	git push