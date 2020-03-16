import requests

my_query={"ename":"Kelly_asdf"}
response=requests.get("http://localhost:5000/esinfo",params=my_query)

print(response.status_code)
print(response.json())
