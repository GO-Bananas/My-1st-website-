import requests
print("hello world")
sites= "https://official-joke-api.appspot.com/random_joke"


for i in range(25):
    responce = requests.get(sites).json() 
    setup = responce["setup"]
    punchline = responce["punchline"]
    print(setup)
    input()
    print(punchline)