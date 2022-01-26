import wikipedia_histories
import pandas
import os

# Titles to search are defined in query_terms.py, so this can be kept out of 
# commits.
from query_terms import titles

root_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(root_dir, 'data')
out_file = os.path.join(data_dir, 'wikiped.csv')

grand_dataframe = pandas.DataFrame()

for title in titles:
    page = wikipedia_histories.get_history(title, include_text=False)
    dataframe = wikipedia_histories.to_df(page)
    print("Appending {}".format(title))
    grand_dataframe = grand_dataframe.append(dataframe)    
    grand_dataframe.to_csv(out_file)

