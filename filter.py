import basefilter
from trainingcorpus import TrainingCorpus
from utils import mail_cleaner


class MyFilter(basefilter.BaseFilter):
    def __init__(self):
        super().__init__()
        # Initialize dictionaries to store keyword frequencies in spam and ham emails
        self.keywords = {}
        self.res = {}

    def train(self, corpus_train_dir):
        # Create a TrainingCorpus object for the given directory
        training_corpus = TrainingCorpus(corpus_train_dir)

        # Get spam and ham emails from the training corpus
        spams = training_corpus.spams()
        hams = training_corpus.hams()

        # Process spam emails
        for f_name, f_body in spams:
            checker = mail_cleaner(f_body)
            for word in checker.split():
                # Update keyword frequency in the dictionary
                if word.isnumeric():
                    self.keywords[word] = 0
                if word in self.keywords:
                    self.keywords[word] += 1
                else:
                    self.keywords[word] = 1

        # Process ham emails
        for f_name, f_body in hams:
            checker = mail_cleaner(f_body)
            for word in checker.split():
                # Decrease keyword frequency for ham emails
                if word in self.keywords:
                    self.keywords[word] -= 10

        # Remove specific words and numeric entries from the keyword dictionary
        for i, j in self.keywords.items():
            if i in ["you", "your", "our", "name", "text/html", "we", "will", "please", "us", "may", "name"]:
                self.keywords[i] = 0
            if i.isnumeric():
                self.keywords[i] = 0

        # Return the sorted keyword dictionary
        return dict(sorted(self.keywords.items(), key=lambda item: item[1]))

    def create_dict(self):
        counter = 0
        dictionary = {}

        # Check if the corpus is available
        if self.corpus is None:
            raise ValueError("Corpus not available")

        # Sort the keyword dictionary by frequency and get the top twenty keywords
        self.res = dict(sorted(self.keywords.items(), key=lambda item: item[1]))
        top_twenty_keywords = list(self.res.keys())[-20:]

        # Check if each email contains at least 2 of the top twenty keywords
        for i, j in self.corpus.emails():
            for word in j.split():
                if word in top_twenty_keywords:
                    counter += 1

            # Classify emails as "SPAM" if they contain at least 2 top keywords, otherwise "OK"
            result = "SPAM" if counter >= 2 else "OK"
            counter = 0
            dictionary[i] = result

        return dictionary
