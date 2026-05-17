import os


class Corpus:
    def __init__(self, emails_path):
        self.emails_path = emails_path

    def emails(self):
        for file_name in os.listdir(self.emails_path):
            # Skip files starting with '!'
            if file_name.startswith('!'):
                continue

            file_path = os.path.join(self.emails_path, file_name)

            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    body = file.read()
                    yield file_name, body
