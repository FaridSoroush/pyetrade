import pyetrade

consumer_key = "39f9f7dde2cf5490e6f3b60333f57a0e"
consumer_secret = "bd1923fa3b10cfdcf5df679973d8f9beec7f3ce3e22c693e0ed722382b31ec25"

oauth = pyetrade.ETradeOAuth(consumer_key, consumer_secret)
print(oauth.get_request_token())  # Use the printed URL

verifier_code = input("Enter verification code: ")
tokens = oauth.get_access_token(verifier_code)
print(tokens)