from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd



def scrape_me( drive ):
    #global table
    column = ['Job_Title', 'Location', 'Job_Family', 'Application_Deadline']
    table = pd.DataFrame(columns= column) 
    
    path1_title =  'ctl00_siteContent_widgetLayout_rptWidgets_ctl03_widgetContainer_ctl00_rptResultsTable_ctl0'
    path2_title = '_rptResultsTableCell_ctl00_lnkCellLink'
    path_location = '_rptResultsTableCell_ctl01_lblCellLabel'
    path_familly = '_rptResultsTableCell_ctl02_lblCellLabel'
    path_date = '_rptResultsTableCell_ctl03_lblCellLabel'

    i = 0
    while True:
        try :
            if(i < 10):
                print('Element: '+ str(i) )
                path_i_title = path1_title + str(i) + path2_title 
                title = driver.find_element_by_id(path_i_title).text 

                path_i_location = path1_title + str(i) + path_location
                location = driver.find_element_by_id(path_i_location).text


                path_i_familly = path1_title + str(i) + path_familly
                familly = driver.find_element_by_id(path_i_familly).text 

                path_i_date = path1_title + str(i) + path_date
                date = driver.find_element_by_id(path_i_date).text  

                table.loc[table.shape[0]]=[ title, location, familly, date ]
            else:
                print('Element: '+ str(i) )
                path_i_title = path1_title[:-1] + str(i) + path2_title 
                title =  driver.find_element_by_id(path_i_title).text 

                path_i_location = path1_title[:-1] + str(i) + path_location
                location = driver.find_element_by_id(path_i_location).text

                path_i_familly = path1_title[:-1] + str(i) + path_familly
                familly = driver.find_element_by_id(path_i_familly).text  

                path_i_date = path1_title[:-1] + str(i) + path_date
                date = driver.find_element_by_id(path_i_date).text  

                table.loc[table.shape[0]]=[ title, location, familly, date ]

            i = i+1
        except:
            break
    return table


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://worldbankgroup.csod.com/ats/careersite/search.aspx?site=1&c=worldbankgroup&sid=%5E%5E%5EFLGscZMYY2RrwVaMR%2FtHYw%3D%3D&fbclid=IwAR01ArJTACY62QBo4sGuJnSmjMi8jXX7por4BYeoxpqzAuld8lbYYcdpOBw')


path = 0
table =  scrape_me( driver )

while True:
    #driver.get('https://worldbankgroup.csod.com/ats/careersite/search.aspx?site=1&c=worldbankgroup&sid=%5E%5E%5EFLGscZMYY2RrwVaMR%2FtHYw%3D%3D&fbclid=IwAR01ArJTACY62QBo4sGuJnSmjMi8jXX7por4BYeoxpqzAuld8lbYYcdpOBw')
    
    try  :
        inputElement = driver.find_element_by_xpath('//*[@class="pageNext pagerNavigationLink"]')
        inputElement.click()
        print("page "+ str(path) + ' has been scraped')
        path = path + 1
        table2 = scrape_me( driver )
        table = pd.concat([table, table2])

    except : 
        break


table.to_csv('WorldBankJobsBaby.csv', sep= ';', encoding = 'utf-8')

driver.close()

