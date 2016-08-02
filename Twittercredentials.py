import tweepy

consumer_key = "YDB955QJn3JJmSvpX4xBCRDCY";

consumer_secret = "hG40gnkOlgWXWIfbMGICXfqRc5eKgxOGHxhIx303nbmBcAoAod";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "301198479-qXyHfBpibtBuoSekwDb3cu9Wt5JJxHqbfedCg4mc";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "Gpmt6rg7CziT0uO3uLOWmvYz5Jt7B16PbDsoBo7nbl3j4";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



