# pt-br-classifier

## Description
Classifying Portuguese texts according to their variety (European or Brazilian Portuguese) 
The repository documents the entire process of building a ML model and deploying it:
- Scraping data from TED lectures with Scrapy (BRCrawler.py, PTCrawler.py)
- Basic data processing, setting up a classifier using scikit-learn (ptclassifier.ipynb)
- Exporting the model with joblib (ptclassifier.ipynb)
- Setting an API with Flask (flask_app.py)
- Make a <a href="http://marekcichy.alwaysdata.net/">basic frontend app</a> that consumes the API.

## Contributions
Are highly encouraged. First and foremost, any constructive criticism of the above is more than welcome.

Some paths I plan to explore in October:
- Scrape other kinds of texts (movie subtitles, media articles, blog posts, forum discussions) and check the model's performance
- Return weights for separate words and show their "brazilness" or "portugueseness" in the frontend (eXplainable AI)
- Use an LSTM network instead of NaiveBayes

## License
MIT
