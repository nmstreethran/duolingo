# Duolingo

My [Duolingo](https://www.duolingo.com/) vocabulary with English translations, extracted using a Python script into JSON and CSV formats. Updated approximately every week. 

I am currently learning Norwegian (Bokmål) and Latin. I sometimes try the German and Irish Gaelic courses too.

Duolingo has a [built-in feature to display learned words](https://www.duolingo.com/words). However, this is only available for a number of languages (in my case, only for German). It also does not display the translations within the learned words table. This Python script resolves these issues by producing CSV files of the vocabulary with English translations.

## Required Python packages

- [Unofficial Duolingo API by Kartik Talwar](https://github.com/KartikTalwar/Duolingo) 
- [JSON](https://docs.python.org/3/library/json.html)
- [Pandas](https://pandas.pydata.org/)

## Files

Python script: [duolingo_data.py](duolingo_data.py)

`login.py` stores the username and password. For example:

```py
myusername = 'my_duolingo_username'
mypassword = 'my_duolingo_password'
```

JSON files with vocabulary:

- Norwegian (Bokmål): [vocab_nb.json](vocab_nb.json)
- Latin: [vocab_la.json](vocab_la.json)
- German: [vocab_de.json](vocab_de.json)
- Irish Gaelic: [vocab_ga.json](vocab_ga.json)

CSV files with vocabulary (including translations):

- Norwegian (Bokmål): [vocab_nb.csv](vocab_nb.csv)
- Latin: [vocab_la.csv](vocab_la.csv)
- German: [vocab_de.csv](vocab_de.csv)
- Irish Gaelic: [vocab_ga.csv](vocab_ga.csv)

## License

[MIT License](LICENSE)

## Credits

- [Duolingo vocabulary overview](https://www.duolingo.com/vocabulary/overview): used to extract learned vocabulary
- Duolingo dictionary (`https://d2.duolingo.com/api/1/dictionary/hints/<target>/<source>?token=<words>`): used to translate learned words into English
