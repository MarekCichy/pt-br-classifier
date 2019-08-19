# pt-br-classifier

## Description
The repository documents the entire process of building a ML model and deploying it:
- Scraping data from TED lectures with Scrapy
- Basic data processing (Jupyter notebook, pandas)
- Setting up a classifier using scikit-learn
- Exporting the model with joblib
- Setting an API with Flask

## Contributions
Are highly encouraged. Some paths to explore:
- Scrape other kinds of texts (movie subtitles, media articles, blog posts, forum discussions) and check the model's performance
- Make a basic frontend app that consumes the API 
- Return weights for separate words and show their "brazilness" or "portugueseness" in the frontend (eXplainable AI)
- Use an LSTM network instead of NaiveBayes

## License
MIT
