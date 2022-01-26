import wikipedia_histories
import pandas
import os

test_titles = ['Butoconazole', 'Shaykh_Tabarsi']
titles = [
"Xinjiang",
"Chinese_Communist_Party",
"East_Turkestan_independence_movement",
"Tibetan_independence_movement",
"Human_rights_in_China",
"Chinese_intelligence_activity_abroad",
"Maoism",
"Falun_Gong",
"Chinese_language",
"Chinese_television",
"Taiwan",
"Tibet",
"Xinjiang_re-education_camps",
"Tiananmen_Square_protests_of_1989",
"WeChat",
"Mao_Zedong",
"Xi_Jinping"]

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

