#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import json
import configparser
import time

# Lire les configurations depuis config.ini
config = configparser.ConfigParser()
config.read('config.ini')

newsapi_key = config['newsapi']['api_key']

# Mots-clés pour la recherche de tweets sur le conflit entre Palestine et Israël
keywords = [
    'palestine israel',
    'israel palestine',
    'middle east conflict',
    'gaza strip',
    'west bank',
    'israeli-palestinian conflict',
    'two-state solution',
    'settlements',
    'UN resolution',
    'Jerusalem status',
    'peace process',
    'palestinian territories',
    'israeli settlements',
    'hamas',
    'fatah',
    'IDF',
    'PLO',
    'Palestinian Authority',
    'oslo accords',
    'gaza war',
    'west bank protests',
    'temple mount incident',
    'jerusalem',
    'gaza city',
    'ramallah',
    'tel aviv',
    'hebron',
    'human rights violations',
    'international diplomacy',
    'refugee crisis',
    'religious tensions',
    'border conflicts'
]

# Paramètres de recherche
language = 'en'  # Langue des articles (anglais)
total_tweets = 200  # Nombre total de tweets souhaités

# Initialiser les variables
tweets_count = 0
page = 1

# Ouvrir le fichier pour sauvegarder les tweets
with open('all_tweets.txt', 'w', encoding='utf-8') as file:
    while tweets_count < total_tweets:
        for keyword in keywords:
            # URL de l'API NewsAPI avec pagination
            url = f'https://newsapi.org/v2/everything?q={keyword}&language={language}&apiKey={newsapi_key}&page={page}'

            # Effectuer la requête GET à l'API
            response = requests.get(url)

            # Vérifier si la requête a réussi (code de statut 200)
            if response.status_code == 200:
                # Charger les données JSON de la réponse
                data = json.loads(response.text)

                # Vérifier si des articles ont été trouvés
                if data['totalResults'] > 0:
                    # Parcourir les articles
                    for article in data['articles']:
                        # Sauvegarder le titre et l'URL du tweet dans le fichier
                        file.write(article['title'] + '\n')
                        file.write(article['url'] + '\n')
                        file.write('-' * 30 + '\n')
                        tweets_count += 1

                        # Vérifier si le nombre total de tweets souhaités a été atteint
                        if tweets_count >= total_tweets:
                            break

                    # Passer à la page suivante
                    page += 1

                    # Ajouter une pause de 5 secondes entre les requêtes
                    time.sleep(2)
                else:
                    print(f"Aucun article trouvé pour le mot-clé '{keyword}'.")
            elif response.status_code == 429:
                print(f"Erreur 429: Taux limite atteint. Pause d'une minute.")
                time.sleep(60)  # Pause d'une minute en cas d'erreur 429
            else:
                print(f"Erreur de requête: {response.status_code}")

print("La recherche et la sauvegarde des tweets sont terminées.")


# In[ ]:




