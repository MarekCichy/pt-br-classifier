# pt-br-classifier

(versão portuguesa abaixo)

## Description
Classifying Portuguese texts according to their variety (European or Brazilian Portuguese) 
The repository documents the entire process of building a ML model and deploying it:
- Scraping data from TED lectures with Scrapy (BRCrawler.py, PTCrawler.py)
- Basic data processing, setting up a classifier using scikit-learn (ptclassifier.ipynb)
- Exporting the model with joblib (ptclassifier.ipynb)
- Setting an API with Flask (flask_app.py)
- Making a <a href="http://marekcichy.alwaysdata.net/" target="_blank">basic frontend app</a> that consumes the API.

For more details on the process, see my <a href="https://medium.com/@marekkcichy/nlp-basics-hands-on-a-portuguese-dialect-classifier-deployed-online-in-3-steps-53a8b3b88ea9">article on Medium</a>. 

## Contributions
Are highly encouraged. First and foremost, any constructive criticism of the above is more than welcome.

Some paths I plan to explore:
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
- Criação de um <a href="http://marekcichy.alwaysdata.net/" target="_blank">aplicativo básico de frontend</a> que consome a API.

Para mais detalhes sobre o processo, confira meu <a href="https://medium.com/data-hackers/como-criar-um-detector-de-sotaques-de-portugu%C3%AAs-com-palestras-ted-3487672f4f3b">artigo em Medium</a>.

## Contribuições
São muito bem-vindas. Princpalmente, qualquer crítica construtiva do acima mencionado é mais que desejada.

Algumas trilhas que pretendo explorar:
- Raspar outros gêneros de textos (legendas, artigos, blogues, fóruns) para verificar o modelo e melhorá-lo
- Mostrar os pesos para palavras individuais e mostrar sua "brasildade" ou "portuguesidade" no aplicativo (um punhado de eXplainable AI)
- Usar uma rede LSTM em vez de NaiveBayes

## License/Licença
MIT
