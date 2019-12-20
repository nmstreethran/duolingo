# Duolingo

Extracting learned [Duolingo](https://www.duolingo.com/) vocabulary with their English translations using the unofficial Duolingo API and a Python script.

Duolingo has a [built-in feature to display learned words](https://www.duolingo.com/words). However, this is only available for a number of languages (in my case, only for German). It also does not display the translations within the learned words table. This Python script resolves these issues by producing CSV and PDF files of the vocabulary with English translations, extracted from Duolingo's dictionary and [vocabulary overview](https://www.duolingo.com/vocabulary/overview).

I am currently learning Norwegian (Bokmål) and Latin. I sometimes try the German and Irish Gaelic courses too. You can follow my language learning progress [here](https://www.duolingo.com/nmstreethran).

## Requirements

Python packages:
- [Unofficial Duolingo API by Kartik Talwar](https://github.com/KartikTalwar/Duolingo) 
- [JSON](https://docs.python.org/3/library/json.html)
- [Pandas](https://pandas.pydata.org/)
- [os](https://docs.python.org/3/library/os.html)

A TeX distribution, such as [TeX Live 2019](http://tug.org/texlive/) is needed to produce PDFs. Compiling the PDF files using [vocab.tex](vocab.tex) requires XeLaTeX and Makeglossaries. The compilation is done as follows:

```sh
xelatex vocab.tex
makeglossaries vocab
xelatex vocab.tex
```

## Running the script

Python script: [duolingo_data.py](duolingo_data.py)

You will be prompted to enter your Duolingo username and password in the terminal.

After running this script, CSV, JSON, TeX and PDF files containing the vocabulary will be saved in the same directory, using the naming convention `vocab_XX`. `XX` refers to the language code as defined by Duolingo. The codes in the table below are the ones I am aware of (mostly corresponding to [ISO 639](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)). When tested with the dictionary URL (`https://d2.duolingo.com/api/1/dictionary/hints/en/XX?token=hello`), the languages denoted `yes` produced an output. However, this script is not guaranteed to work for all languages that produced an output, especially ones with non-latin alphabets, as it has only been tested with German, Irish Gaelic, Scottish Gaelic, Latin and Norwegian (Bokmål).

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
gd | Scottish Gaelic | yes | yes
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

## Contributing

Feel free to open an issue or pull request.

## License

[MIT License](LICENSE)

