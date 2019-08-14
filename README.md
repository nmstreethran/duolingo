# Duolingo

My [Duolingo](https://www.duolingo.com/) vocabulary list, extracted using a Python script into JSON and CSV. Updated every week or so. 

I am currently learning Norwegian (Bokmål). I sometimes try the German and Irish Gaelic courses too.

## Required Python packages

- [Unofficial Duolingo API by Kartik Talwar](https://github.com/KartikTalwar/Duolingo) 
- [JSON](https://docs.python.org/3/library/json.html)
- [Pandas](https://pandas.pydata.org/)

## Files

Python script: [duolingo_data.py](/duolingo_data.py)

`login.py` stores the username and password. For example:

```py
myusername = 'my_duolingo_username'
mypassword = 'my_duolingo_password'
```

JSON files with vocabulary:

- Norwegian (Bokmål): [vocab_nb.json](/vocab_nb.json)
- German: [vocab_de.json](/vocab_de.json)
- Irish Gaelic: [vocab_ga.json](/vocab_ga.json)

CSV files with vocabulary (including translations):

- Norwegian (Bokmål): [vocab_nb.csv](/vocab_nb.csv)
- German: [vocab_de.csv](/vocab_de.csv)
- Irish Gaelic: [vocab_ga.csv](/vocab_ga.csv)

## License

[MIT License](/LICENSE)

## Credits

- [Duolingo vocabulary overview](https://www.duolingo.com/vocabulary/overview)
- Duolingo dictionary (`https://d2.duolingo.com/api/1/dictionary/hints/<target>/<source>?token=<words>`)
