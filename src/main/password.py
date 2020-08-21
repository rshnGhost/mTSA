from credentials.credentials import credentials

def fetch(argument):
    return credentials.get(argument)
