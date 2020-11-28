import requests

def getGithubUser(username):
    response = requests.get("https://api.github.com/users/{}".format(username))
    return response

def showUserInfos(user):
    user = user.json()
    print("username:", user["login"])
    print("name:", user["name"])
    print("bio:", user["bio"])
    print("website:", user["blog"])

user = getGithubUser("florian-lefebvre")
showUserInfos(user)