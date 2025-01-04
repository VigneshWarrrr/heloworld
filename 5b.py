import requests
url="https://google.com/data"
filename="googledata.txt"
response=requests.get(url)
with open("filename","wb") as f:
    f.write(response.content)
print("The data if transfered")