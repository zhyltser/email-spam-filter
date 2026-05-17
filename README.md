# Email Spam Filter

A keyword-frequency-based spam classifier for email datasets, 
built with pure Python and object-oriented design.

## How It Works

1. **Training**: Scans a labeled email corpus, builds a frequency 
   dictionary — words appearing in spam emails get +1, words in 
   ham (legitimate) emails get -10.
2. **Classification**: Extracts the top 20 most spam-indicative keywords. 
   Emails containing ≥2 of these keywords are classified as SPAM.
3. **Preprocessing**: HTML tags, punctuation, and stopwords are stripped 
   before analysis.

## Project Structure

| File | Description |
|------|-------------|
| `filter.py` | Core classifier (MyFilter) |
| `basefilter.py` | Abstract base class |
| `trainingcorpus.py` | Labeled training data loader |
| `corpus.py` | Unlabeled corpus loader |
| `utils.py` | Text cleaning utilities |

## Usage

```python
from filter import MyFilter

f = MyFilter()
f.train("path/to/train_corpus/")
f.test("path/to/test_corpus/")
# Results written to !prediction.txt
```

## Known Limitations & Future Improvements

- Rule-based weight adjustment (−10 for ham) → could use TF-IDF or 
  Naive Bayes probability
- No cross-validation yet
- Could be extended with scikit-learn pipeline

## Requirements

Python 3.8+, no external dependencies.
