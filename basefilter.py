import corpus
import os


class BaseFilter:
    def __init__(self):
        pass

    def train(self, corpus_test_dir):
        """Placeholder method for training the filter."""
        pass

    def test(self, corpus_test_dir):
        self.corpus = corpus.Corpus(corpus_test_dir)

        # Generate predictions and write to a file
        self.dict = self.create_dict()
        file = os.path.join(corpus_test_dir, "!prediction.txt")
        with open(file, 'w', encoding='utf-8') as f:
            for x in self.dict:
                f.write(x + " " + self.dict[x] + "\n")

    def create_dict(self):
        """Placeholder method for creating a dictionary of predictions."""
        raise NotImplementedError("create_dict method must be implemented in derived classes.")






