from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


# referencia: https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a
df = pd.DataFrame(columns=['Player','Salary','Year']) # creates master dataframe
driver=webdriver.Chrome('D:\\ronald\\Descargas\\chromedriver_win32\\chromedriver')

for yr in range(1990,1991):
    page_num = str(yr) + '-' + str(yr+1) +'/'
    url = 'https://hoopshype.com/salaries/players/' + page_num
    driver.get(url)
    
    players = driver.find_elements_by_xpath('//td[@class="name"]')
    salaries = driver.find_elements_by_xpath('//td[@class="hh-salaries-sorted"]') 
    
    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)
    
    salaries_list = []
    for s in range(len(salaries)):
        salaries_list.append(salaries[s].text)
    
    data_tuples = list(zip(players_list[1:],salaries_list[1:]))
    temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary'])
    temp_df['Year'] = yr 
    df = df.append(temp_df) 
    
driver.close()

print(df)