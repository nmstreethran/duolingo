#%%
# import libraries
import duolingo
import json
import pandas
import os
import getpass
import configparser

#%%
# input login information in command line
myusername = input('Enter your Duolingo username: ')
mypassword = getpass.getpass('Enter your Duolingo password: ')

#%%
# enter login information
lingo = duolingo.Duolingo(myusername, password=mypassword)

# %%
# import list of languages learned by user
config = configparser.ConfigParser()
config.read('languages.conf')

# %%
# convert to list
languageList = [
    z.strip() for z in config.get('languages', 'languages').split('\n')]
# remove empty strings
languageList = list(filter(None, languageList))

#%%
# dictionary of languages and their codes
languageCodes = {
    'Arabic': 'ar',
    'Chinese': 'zh',
    'Czech': 'cz',
    'Danish': 'da',
    'Dutch': 'nl',
    'Esperanto': 'eo',
    'French': 'fr',
    'German': 'de',
    'Greek': 'el',
    'Hawaiian': 'hw',
    'Hebrew': 'he',
    'High Valyrian': 'hv',
    'Hindi': 'hi',
    'Hungarian': 'hu',
    'Indonesian': 'id',
    'Irish Gaelic': 'ga',
    'Italian': 'it',
    'Japanese': 'jp',
    'Klingon': 'tlh',
    'Korean': 'ko',
    'Latin': 'la',
    'Navajo': 'nv',
    'Norwegian (Bokmål)': 'nb',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Scottish Gaelic': 'gd',
    'Spanish': 'es',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Turkish': 'tr',
    'Ukranian': 'uk',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
}

#%%
# get list of languages learned by the user and their codes
languages = []
for language in languageList:
    for n, c in languageCodes.items():
        if n == language:
            languages.append((c, n))

#%%
# extracting data for each language in a loop
for code, name in languages:
    # extract vocabulary data from duolingo's vocabulary overview
    vocab = lingo.get_vocabulary(language_abbr=code)

    # save vocabulary data as json
    # use indent > 0 to pretty print the output
    with open('vocab_' + code + '.json', 'w') as f:
        json.dump(vocab, f, indent=2)

    # convert vocabulary overview to dataframe
    vocab_df = pandas.DataFrame(vocab['vocab_overview'])

    # drop duplicate words
    vocab_df = vocab_df.drop_duplicates('word_string')

    # translating words into english
    # define a generator to split the list of words to be translated
    # to chunks (to prevent 'Exception: Could not get translations'
    # caused by long lists)
    def splitlist(mylist, chunk_size):
        return [mylist[offs: offs + chunk_size] for
            offs in range(0, len(mylist), chunk_size)]

    # split the list of words into chunks with a maximum length of 500
    word_list = splitlist(vocab_df['word_string'].tolist(), 500)

    # create empty dataframe for merging
    vocab_merge = pandas.DataFrame()

    # translate each chunk and merge into the dataframe in a loop
    for t in word_list:
        # get translations from duolingo's dictionary
        trnslt = lingo.get_translations(t, source='en', target=code)

        # convert translation dictionary to dataframe
        trnslt_df = pandas.DataFrame(dict(
            [(k, pandas.Series(v)) for k, v in trnslt.items()])).transpose()

        # combine translation values into a single column
        trnslt_df = pandas.DataFrame(
            trnslt_df.apply(lambda x: x.str.cat(sep=', '), axis=1),
            columns=['translation'])

        # reset index and add keys to word_string column
        trnslt_df.index.names = ['word_string']
        trnslt_df.reset_index(level=0, inplace=True)
        
        # concatenate translated values from each loop
        # with the empty dataframe created
        vocab_merge = pandas.concat([vocab_merge, trnslt_df])

    # merge translated values with vocabulary overview
    vocab_df = vocab_df.merge(vocab_merge, on=['word_string'])

    # drop unnecessary columns
    vocab_df = vocab_df.drop([
        'id', 'last_practiced_ms', 'lexeme_id', 'normalized_string',
        'related_lexemes', 'skill_url_title', 'strength'], axis=1)

    # sort values by word_string, then skill
    vocab_df = vocab_df.sort_values(['word_string', 'skill'])

    # save vocabulary data as csv
    # use cp1252 encoding to print accented latin characters
    vocab_df.to_csv('vocab_' + code + '.csv', encoding='cp1252', index=None)

    # convert vocab into latex glossary
    file = open('vocab_.tex', 'w')
    file.write(
        # set glossary name via a latex command
        r'\chapter*{\MakeLowercase{' + name + ' -- English Dictionary}}\n')
    for index, row in vocab_df.iterrows():
        file.write(
            '\dictentry{' + str(row['word_string']) + '}{'
            + str(row['translation']) + '}\n')
    file.close()

    # compile latex document into pdf
    os.system('xelatex vocab.tex')
    os.system('makeglossaries vocab')
    os.system('xelatex vocab.tex')

    # rename latex glossary and pdf output to match the language
    os.rename('vocab_.tex', 'vocab_' + code + '.tex')
    os.rename('vocab.pdf', 'vocab_' + code + '.pdf')
