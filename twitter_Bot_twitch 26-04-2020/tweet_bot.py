import tweepy
import time

class twitter_bot():
    def __init__(self):
        self.consumer_key = "I7e3ZtcMdQwVa4byulsDg5vEL"
        self.consumer_secret = "Xdpyh81PwdWKaVCLG9De42Is7rgEj0ciJL9Y7l3EEooDQXc9hY"
        self.access_token = "1254353542976020482-kexf4KtMUFjkqYaG3SEcLujcUU9aTC"
        self.access_token_secret = "kX7xFBgGFaERBbvjWDdW0X8K9EKR7IKZ2YayOBJrB6Rty"
        self.Tweet_Inicial = "Olá, sou o HaroldoBOT https://www.twitch.tv/lucasfernsilva"
        self.api= None
        self.array_rt= []
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
        filtro = "Olá, sou o HaroldoBOT1"
# Percorre pelos tweets e retweeta o que possui a palavra especifica
        for tweet in public_tweets:
            if filtro in tweet.text :
                print(tweet.id)
                self.api.retweet(tweet.id)
                self.array_rt.append(tweet.text)

        print(self.array_rt)




a = twitter_bot()

a.api_key()
a.curte_tweet()