import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

http.Handle("/", http.PageServer(http.Dirextory("./application")))

print(x.text)
