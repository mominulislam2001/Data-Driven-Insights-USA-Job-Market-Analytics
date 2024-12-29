import pandas as pd
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def scrap_links_post_date(dict_):
    
    links_dict = dict()
    links_array = []
    posted_date_array = []

    for role,role_dict in dict_.items():
        
        for level,level_dict in role_dict.items():
            
            for degree,degree_link in level_dict.items():
                
                try:
                    links_array = []
                    links_dict = dict()
                    posted_date_array = []

                    driver = webdriver.Chrome()
                    
                    driver.get(degree_link)
                    
                    count_path = '//div[@class="jobsearch-JobCountAndSortPane-jobCount css-13jafh6 eu4oa1w0"]'
                    count = driver.find_element('xpath',count_path)
                    
                    count = re.sub(r'\D', '', count.text)
                    count = int(count)
                

                    max_page_10 = (int)(count/15)*10
                    
                    for page in range(0,max_page_10+10,10):
                        
                        try:
                            driver.get(degree_link+f"&start={page}")
                        
                            for anc_elem in range(1,16):
                                
                                item = driver.find_element(By.ID, "mosaic-jobResults")
                                jobs = item.find_elements(By.CLASS_NAME, "job_seen_beacon")
                                
                                for row in jobs:

                                    try:
                                        job_link_element = row.find_element(By.CSS_SELECTOR, "a.jcs-JobTitle")
                                        job_link = job_link_element.get_attribute("href")
                                        links_array.append(job_link) 

                                        posted_date_element = row.find_element(By.CSS_SELECTOR, "span[data-testid='myJobsStateDate']")
                                        posted_date = posted_date_element.text
                                        posted_date_array.append(posted_date)
                                   
                                    except Exception as e:
                                        print(e)

                                    
                            
                        except Exception as e:
                            print(e)
                    
            
                    

                    links_dict = {

                        "role" : role,
                        "level" : level,
                        "degree": degree,
                        "links": links_array,
                        "posted_date":posted_date_array
                        

                    }

                    link_df = pd.DataFrame(links_dict)
                    csv_name = f"{role}_{level}_{degree}_{len(links_array)}.csv"
                    path_to_save = f"./{csv_name}"
                    link_df.to_csv(path_to_save,index=False)

                    print("Extracting Data for ",role," | ", level, " | ",degree, " | ", "Link : ", degree_link , f" Done  total links {len(links_array)}")
                
                except Exception as e:
                    print(e)


def merge_scraped_files(extract_folder_name,save_folder_name):
        
    df_list = []
    for csv_name in os.listdir(f'./{extract_folder_name}'):
        df = pd.read_csv(f'./{extract_folder_name}/{csv_name}')
        df.drop_duplicates(subset=['links'], keep="first",inplace=True)
        df_list.append(df)
        

    all_df = pd.concat(df_list)
    all_df.to_csv(f'./{save_folder_name}/merged_links.csv',index=False)



        



