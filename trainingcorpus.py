import os


class TrainingCorpus:
    def __init__(self, emails_path):
        self.emails_path = emails_path

    def get_class(self, filename):
        """Get the class (SPAM or OK) for a given filename from the '!truth.txt' file."""
        with open(os.path.join(self.emails_path, '!truth.txt'), 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith(filename):
                    return line.split()[1]

    def is_spam(self, file_name):
        return self.get_class(file_name) == "SPAM"

    def is_ham(self, file_name):
        return self.get_class(file_name) == "OK"

    def spams(self):
        """Generator function to iterate over SPAM-labeled files in the training corpus."""
        for filename in os.listdir(self.emails_path):
            if self.is_spam(filename):
                with open(os.path.join(self.emails_path, filename), 'r', encoding='utf-8') as file:
                    yield filename, file.read()

    def hams(self):
        """Generator function to iterate over OK-labeled files in the training corpus."""
        for filename in os.listdir(self.emails_path):
            if self.is_ham(filename):
                with open(os.path.join(self.emails_path, filename), 'r', encoding='utf-8') as file:
                    yield filename, file.read()
