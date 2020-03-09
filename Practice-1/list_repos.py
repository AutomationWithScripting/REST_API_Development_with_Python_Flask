import sys
try:
    import requests
except  Exception as e:
    print(e)
    sys.exit(1)

response=requests.get("https://api.github.com/users/AutomationWithScripting/repos")
if response.status_code == 200:
    for each_repo in response.json():
        print(each_repo.get("name"))
