import requests

r = requests.get('https://raw.githubusercontent.com/JSteinbauer/test_repository/master/test_urls.txt')

print(r)
