import json
import requests
from lib.models.repository import Repository


class LabelMaker:

    def __init__(self, repository: Repository):
        self.repository = repository
        self.labels = self.get_labels_by_json()
        self.old_labels = self.get_old_labels_by_github()
        self.clean_old_labels()

    def get_labels_by_json(self,  filename: str = 'labels.json') -> dict:
        with open(filename) as json_file:
            labels = json.load(json_file)
        return labels

    def create_labels(self) -> bool:
        for label in self.labels.items():

            current_label = {
                'name': label[1]["name"],
                'description': label[1]["description"],
                'color': label[1]["color"]
            }

            requests.post(
                self.repository.url,
                headers=self.repository.headers,
                data=json.dumps(current_label))
        return True

    def get_old_labels_by_github(self):

        labels_dict = requests.get(
            self.repository.url,
            headers=self.repository.headers).json()

        old_labels = []

        if len(labels_dict) != 0:

            for label in labels_dict:
                old_labels.append(label["name"])

        return old_labels

    def clean_old_labels(self):

        if len(self.old_labels) != 0:

            for label in self.old_labels:

                requests.delete(
                    "{0}/{1}".format(self.repository.url, label), headers=self.repository.headers)
