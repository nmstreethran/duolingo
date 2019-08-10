#%%
# import libraries
import duolingo, json, pandas

#%%
# import login information saved in a separate file
from login import *

#%%
# enter login information
lingo = duolingo.Duolingo(myusername, password = mypassword)

#%%
# list of languages
lang = ['nb', 'de', 'ga'] # Norwegian (Bokmål), German, Irish Gaelic

#%%
# extracting data for each language in a loop
for x in lang:

    # extract vocabulary data from duolingo's vocabulary overview
    vocab = lingo.get_vocabulary(language_abbr = x)

    # save vocabulary data as json
    # use indent > 0 to pretty print the output
    with open("vocab_" + str(x) + ".json", 'w') as f:
        json.dump(vocab, f, indent = 2)
    
    # convert vocabulary overview to dataframe
    vocab_df = pandas.DataFrame(vocab['vocab_overview'])

    # drop duplicate words
    vocab_df = vocab_df.drop_duplicates('word_string')

    # translating words to english
    # define a generator to split the list of words to be translated to chunks (to prevent 'Exception: Could not get translations' errors caused by long lists)
    def SplitList(mylist, chunk_size):
        return [mylist[offs: offs + chunk_size] for offs in range(0, len(mylist), chunk_size)]

    # split the list of words into chunks with a maximum length of 500
    word_list = SplitList(vocab_df['word_string'].tolist(), 500)

    # create empty dataframe for merging
    vocab_merge = pandas.DataFrame()
    
    # translate each chunk and merge into the dataframe in a loop
    for t in word_list:

        # get translations from duolingo's dictionary
        trnslt = lingo.get_translations(t, source = 'en', target = x)

        # convert translation dictionary to dataframe
        trnslt_df = pandas.DataFrame(dict([(k, pandas.Series(v)) for k, v in trnslt.items()])).transpose()

        # combine translation values into a single column
        trnslt_df = pandas.DataFrame(trnslt_df.apply(lambda x: x.str.cat(sep = ', '), axis = 1), columns = ['translation'])

        # reset index and add keys to word_string column
        trnslt_df.index.names = ['word_string']
        trnslt_df.reset_index(level = 0, inplace = True)

        # concatenate translated values from each loop with the empty dataframe created
        vocab_merge = pandas.concat([vocab_merge, trnslt_df])
    
    # merge translated values with vocabulary overview
    vocab_df = vocab_df.merge(vocab_merge, on = ['word_string']) 

    # save vocabulary data as csv
    # use cp1252 encoding to print accented latin characters
    vocab_df.to_csv("vocab_" + str(x) + ".csv", encoding = "cp1252")
