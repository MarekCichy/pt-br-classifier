# pt-br-classifier

## Description
Classifying Portuguese texts according to their variety (European or Brazilian Portuguese) 
The repository documents the entire process of building a ML model and deploying it:
- Scraping data from TED lectures with Scrapy (BRCrawler.py, PTCrawler.py)
- Basic data processing, setting up a classifier using scikit-learn (ptclassifier.ipynb)
- Exporting the model with joblib (ptclassifier.ipynb)
- Setting an API with Flask (flask_app.py)
- Making a <a href="http://marekcichy.alwaysdata.net/"  target="_blank">basic frontend app</a> that consumes the API.

## Contributions
Are highly encouraged. First and foremost, any constructive criticism of the above is more than welcome.

Some paths I plan to explore in October:
- Scrape other kinds of texts (movie subtitles, media articles, blog posts, forum discussions) and check the model's performance
- Return weights for separate words and show their "brazilness" or "portugueseness" in the frontend (eXplainable AI)
- Use an LSTM network instead of NaiveBayes

## Descrição
Classificar textos em português em função do variante (Português europeu e brasileiro) 
O repositório documenta todo o processo de construção de um modelo de aprendizagem automática e sua implantação:
- Raspagem de dados de palestras TED com Scrapy (BRCrawler.py, PTCrawler.py)
- Processamento básico de dados, montagem de um classificador com scikit-learn (ptclassifier.ipynb)
- Exportação do modelo com joblib (ptclassifier.ipynb)
- Configuração de uma API com Flask (flask_app.py)
- Criação de um <a href="http://marekcichy.alwaysdata.net/"  target="_blank">aplicativo básico de frontend</a> que consome a API.

## Contribuições
São muito bem-vindas. Princpalmente, qualquer crítica construtiva do acima mencionado é mais que desejada.

Algumas trilhas que pretendo explorar em Outubro:
- Raspar outros gêneros de textos (legendas, artigos, blogues, fóruns) para verificar o modelo e melhorá-lo
- Mostrar os pesos para palavras individuais e mostrar sua "brasildade" ou "portuguesidade" no aplicativo (um punhado de eXplainable AI)
- Usar uma rede LSTM em vez de NaiveBayes

## License/Licença
MIT
