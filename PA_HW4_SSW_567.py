import requests
import json


def fetchRepos(user_id):
    """ Fetch user's repositories and commits"""
    repo_storage = []
    repo_api = "https://api.github.com/users/"
    fetch_url = repo_api + user_id + '/repos'

    get_url = requests.get(fetch_url)
    repo_list = get_url.json()

    try:
        for line in repo_list:
            repo = line.get('name')
            repo_storage.append(repo)
    except (TypeError, KeyError, IndexError, AttributeError):
        raise ValueError('Not able to Fetch repositories from Entered User ID')

    return repo_storage

def number_of_commits(user_name, repo_name):
    """ Takes input as user's id and repo name and returns number of commits in that repo """
    get_url = requests.get('https://api.github.com/repos/{}/{}/commits'.format(user_name, repo_name))
    num_commits = get_url.json()

    if num_commits == 0:
        print('The respective repository has no commits!')

    return len(num_commits)

def main():
    """ Get user's Github ID as input """
    user_name = input("Please enter the GitHub user ID: ")

    for repo in fetchRepos(user_name):
        num_of_commits = number_of_commits(user_name, repo)
        print("Repo: " + repo + "Number of commits: " + str(num_of_commits))

if __name__ == '__main__':
    main()