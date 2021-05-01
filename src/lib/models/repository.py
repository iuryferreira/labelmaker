class Repository:

    def __init__(self, repo_name: str, token: str):
        self.url = "https://api.github.com/repos/{0}/labels".format(repo_name)
        self.repo_name = repo_name
        self.token = token
        self.headers = {'Authorization': 'token %s' % self.token}
