all: setup collect-data display-analysis

setup:
	pip install matplotlib
	pip install requests
	pip install pandas
	pip install progress

collect-data:
	python vivino_info_scraper.py
	python vivino_reviews_scraper.py

display-analysis:
	python vivino_analysis.py
