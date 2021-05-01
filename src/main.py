from lib.app import LabelMaker
from lib.models.repository import Repository

if __name__ == "__main__":

    repo_name = input("Enter a repository name: ")
    token = input("Input your Github Token: ")

    repo = Repository(repo_name, token)
    app = LabelMaker(repo)

    if(app.create_labels()):

        print("Success!")
    else:
        print("An error has occurred. check the information and try again.")
