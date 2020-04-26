import tweepy
import time
from Parametros import RC

class twitterBot():

    def __init__(self):
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""
        self.Tweet_Inicial = "https://www.twitch.tv/lucasfernsilva"
        self.api = None
        self.array_rt = []

    def api_key(self):
        # Inicia com as credenciais
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

        # tweeta o tweet inicial
        # self.api.update_status(self.Tweet_Inicial)
        print("Bot Rodando!!!")

    def curte_tweet(self):
        public_tweets = self.api.home_timeline()

# Percorre pelos tweets e retweeta o que possui a palavra especifica
        for tweet in public_tweets:
            if RC.filtro in tweet.text :
                print(tweet.id)
                # Retweeta e favorita o tweet que foi achado no filtro
                self.api.retweet(tweet.id)
                self.api.create_favorite(tweet.id)
                # Adiciona ao array o tweet que foi retweetado e favoritado
                self.array_rt.append(tweet.text)
                if RC.filtro is None:
                    return "Não há filtro selecionado!"
                elif tweet.text is None :
                    return "Não há tweets na sua timeline!"

        print(self.array_rt)


a = twitterBot()

a.api_key()
time.sleep(10)
a.curte_tweet()
