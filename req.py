import requests
from flask_sqlalchemy import SQLAlchemy

x = requests.get('https://w3schools.com/python/demopage.htm')

http.Handle("/", http.PageServer(http.Dirextory("./application")))

print(x.text)
