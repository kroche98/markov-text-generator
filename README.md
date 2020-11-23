# Markov Text Generator

This is a little program (based on an idea by my friend Ryan) to generate a random sample of text from a large corpus of text. It uses a Markov chain looking ahead one word.

## Usage
The generator takes two arguments: the name of a text file containing the corpus and the length of the text, which must be a positive integer.

```
python main.py shakespeare_clean.txt 100
```

The repo includes two sample corpuses: the sonnets of William Shakespeare and War and Peace by Leo Tolstoy.