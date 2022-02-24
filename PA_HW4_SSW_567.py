import json,requests 


def RepoLister(name):
    # name = input("Enter the username: ")
    url = "https://api.github.com/users/{}/repos".format(name)

    r = requests.get(url)
    z = json.loads(r.text)
    # pprint.pprint(z)
    for i in z:
        url2 = "https://api.github.com/repos/{}/{}/commits".format(name, i["name"])
        r2 = requests.get(url2)
        z2 = json.loads(r2.text)
        # pprint.pprint(len(z2))
        print("Repo: " + i["name"] + " Number of commits: " + str(len(z2)))

    return ("100")


print(RepoLister("prathyekareddy"))