# Duolingo

Extracting learned [Duolingo](https://www.duolingo.com/) vocabulary with their English translations using the unofficial Duolingo API and a Python script.

Duolingo has a [built-in feature to display learned words](https://www.duolingo.com/words). However, this is only available for a number of languages (in my case, only for German). It also does not display the translations within the learned words table. This Python script resolves these issues by producing CSV files of the vocabulary with English translations.

I am currently learning Norwegian (Bokmål) and Latin. I sometimes try the German and Irish Gaelic courses too. You can follow my language learning progress [here](https://www.duolingo.com/nmstreethran).

## Required Python packages

- [Unofficial Duolingo API by Kartik Talwar](https://github.com/KartikTalwar/Duolingo) 
- [JSON](https://docs.python.org/3/library/json.html)
- [Pandas](https://pandas.pydata.org/)

## Running the script

Python script: [duolingo_data.py](duolingo_data.py)

`login.py` stores the username and password. For example:

```py
myusername = 'my_duolingo_username'
mypassword = 'my_duolingo_password'
```

After running this script, CSV and JSON files containing the vocabulary will be saved in the same directory, using the format `vocab_XX` in the extensions `.csv` and `.json` respectively. `XX` refers to the language code as defined by Duolingo. The codes in the table below are the ones I am aware of. When tested with the dictionary URL (`https://d2.duolingo.com/api/1/dictionary/hints/en/XX?token=hello`), the languages denoted `yes` produced an output. However, this script is not guaranteed to work for all languages that produced an output, especially ones with non-latin alphabets, as it has only been tested with German, Irish Gaelic, Latin and Norwegian (Bokmål).

**Code** | **Language** | **Latin alphabet?** | **Does it produce an output?**
--- | --- | --- | ---
ar | Arabic | no | yes
cs | Czech | yes | yes
cy | Welsh | yes | yes
da | Danish | yes | yes
de | German | yes | yes
el | Greek | no | yes
eo | Esperanto | yes | yes
es | Spanish | yes | yes
fr | French | yes | yes
ga | Irish Gaelic | yes | yes
he | Hebrew | no | yes
hi | Hindi | no | yes
hu | Hungarian | yes | yes
hv | High Valyrian | yes | yes
hw | Hawaiian | yes | yes
id | Indonesian | yes | yes
it | Italian | yes | yes
ja | Japanese | no | yes
ko | Korean | no | yes
la | Latin | yes | yes
nl | Dutch | yes | no
nb | Norwegian (Bokmål) | yes | yes
nv | Navajo | yes | yes
pl | Polish | yes | yes
pt | Portuguese | yes | yes
ro | Romanian | yes | yes
ru | Russian | no | yes
sv | Swedish | yes | yes
sw | Swahili | yes | yes
tlh | Klingon | yes | no
tr | Turkish | yes | yes
uk | Ukrainian | no | yes
vi | Vietnamese | yes | yes
zh | Chinese | no | no

## License

[MIT License](LICENSE)

## Credits

- [Duolingo vocabulary overview](https://www.duolingo.com/vocabulary/overview): used to extract learned vocabulary
- Duolingo dictionary (`https://d2.duolingo.com/api/1/dictionary/hints/<target>/<source>?token=<words>`): used to translate learned words into English
