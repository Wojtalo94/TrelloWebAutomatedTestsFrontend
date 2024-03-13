import csv


class UserData():
    def __init__(self, user_file):
        with open(user_file, 'r') as f:
            reader = csv.reader(f)
            self.user_data = dict(reader)

    def get_user_data(self, key):
        return self.user_data.get(key)