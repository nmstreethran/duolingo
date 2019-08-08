#%%
# import libraries
import duolingo, json, csv, pandas

#%%
# import login information saved in a separate file
from login import *

#%%
# enter login information
lingo = duolingo.Duolingo(myusername, password = mypassword)

#%%
# extract vocab data for each language from site
nb_NO = lingo.get_vocabulary(language_abbr = 'nb') # Norwegian (Bokmål)

de_DE = lingo.get_vocabulary(language_abbr = 'de') # German

#%%
# save vocab data as json
# use indent >0 to pretty print the output
with open('nb_NO.json', 'w') as f:
    json.dump(nb_NO, f, indent = 2)

with open('de_DE.json', 'w') as f:
    json.dump(de_DE, f, indent = 2)

#%%
# save vocab data as csv
# use cp1252 encoding to print accented latin characters
df_nb = pandas.DataFrame(nb_NO['vocab_overview'])
df_nb.to_csv("nb_NO.csv", encoding = "cp1252")

df_de = pandas.DataFrame(de_DE['vocab_overview'])
df_de.to_csv("de_DE.csv", encoding = "cp1252")
