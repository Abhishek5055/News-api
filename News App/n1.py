import requests
lines =int(input("How many headlines do you want to see:"))
api_key="33a6b26cda9046009121cbc5c1b281c0"
def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+api_key
    news= requests.get(main_url).json()
    
    #print news
    article=news["articles"]
    
    news_article=[]
    for arti in article:
        news_article.append(arti["title"])
        
    for i in range(lines):
        print(news_article[i])
news()