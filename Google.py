#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup

# Fonction pour récupérer des liens d'articles depuis Google Actualités
def get_news_links(query, num_links=10):
    base_url = "https://www.google.com/search?q={}&tbm=nws".format(query)
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for link in soup.find_all('a', href=True):
        if 'url?q=' in link['href'] and 'webcache' not in link['href']:
            url = link['href'].split('url?q=')[1].split('&sa=')[0]
            links.append(url)

            if len(links) == num_links:
                break

    return links

# Fonction pour récupérer le texte d'un article à partir d'un lien
def get_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')
    text = ' '.join([paragraph.text for paragraph in paragraphs])

    return text

# Mots-clés pour la recherche
keywords = ['palestine israel', 'israel palestine', 'middle east conflict']

# Nombre d'articles à récupérer par mot-clé
articles_per_keyword = 10

# Récupérer et sauvegarder les articles
for keyword in keywords:
    news_links = get_news_links(keyword, num_links=articles_per_keyword)

    for i, link in enumerate(news_links):
        article_text = get_article_text(link)
        with open(f'{keyword}_article_{i+1}.txt', 'w', encoding='utf-8') as file:
            file.write(article_text)

print("La récupération des articles est terminée.")


# In[ ]:




