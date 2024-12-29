from selenium import webdriver
import time
import pandas as pd 
import os
import re

# Defining Xpaths

def scrap_companies(path,links_column,start,end):

    name_path = f"//div[@itemprop='name' or @itemprop='name']"
    ratings_path = f"//span[@class='css-1n6k8zn e1wnkr790' or @class='css-htn3vt e1wnkr790']"
    
    reviews_path = f"(//a[@data-testid='headerMenuItemLink'])[3]"
    ceo_path = f"//span[@class='css-1w0iwyp e1wnkr790']"
    ceo_approve_path = f"//span[@class='css-4oitjw e1wnkr790']"
    company_founded_path = f"//div[@class='css-1w0iwyp e1wnkr790']"
    company_size_path = f"//li[@data-testid='companyInfo-employee']/child::node()[2]"
    company_revenue_path = f"//li[@data-testid='companyInfo-revenue']/child::node()[2]"
    company_industry_path = f"//a[@data-tn-element='industryInterLink']"
    company_headquarters_path = f"//li[@data-testid='companyInfo-headquartersLocation']"
    company_website_path = f"//a[@data-tn-element='companyLink[]']"
    
    average_rating_score_path = f"//span[@class='css-14om7mt e1wnkr790']"
    average_rating_path = f"//div[@class='css-5syd5t e37uo190']/child::node()[4]"
    
    show_more_btn_path = f"//li[@data-testid='companyInfo-headquartersLocation']/child::node()[3]"
    company_headquarters_path_after_click = f"//div[@data-ipl-modal-id='modal-1']/child::node()[2]/child::node()[1]"

    

    df = pd.read_csv(path)

    df = df.iloc[start:end+1,]

    i = 0

    driver = webdriver.Chrome()
    companies = []
    company_info = dict()

    for link in df[links_column]:

        
        
        
        try:
            
            driver.get(link)
            time.sleep(10)


            company_info = {
                
                "link_scrapped_from":link,
                'cname':None,
                'ratings': None,
                'review_count':None,
                'review_link':None,
                'company_size':None,
                'company_revenue':None,
                'company_industry':None,
                'company_headquarters_clipped':None,
                'company_headquarters_full':None,
                'ceo_name':None,
                'ceo_approve_percentage':None,
                'company_founded':None,
                'company_website_url':None,
                'Average_rating_score':None,
                'Average_rating':None


            }

            
    

            try:
                name = driver.find_element('xpath', name_path).text
                company_info['cname'] = name
            except Exception:
                pass

            
            try:
                no_of_ratings = driver.find_element('xpath', ratings_path).text
                company_info['ratings'] = no_of_ratings
            except Exception:
                pass

            
            try:
                no_of_reviews = driver.find_element('xpath', reviews_path)
                review_count = no_of_reviews.get_attribute('aria-label')
                company_info['review_count'] = review_count
            except Exception:
                pass

            try:
                review_link = no_of_reviews.get_attribute('href')
                company_info['review_link'] = review_link
            except Exception:
                pass

            try:
                company_size = driver.find_element('xpath', company_size_path).text
                company_info['company_size'] = company_size
            except Exception:
                pass

            try:
                company_revenue = driver.find_element('xpath', company_revenue_path).text
                company_info['company_revenue'] = company_revenue
            except Exception:
                pass

            try:
                company_industry = driver.find_element('xpath', company_industry_path).text
                company_info['company_industry'] = company_industry
            except Exception:
                pass

            try:
                company_headquarters_clipped = driver.find_element('xpath', company_headquarters_path).text
                company_info['company_headquarters_clipped'] = company_headquarters_clipped
            except Exception:
                pass

            try:
                ceo_name = driver.find_element('xpath', ceo_path).text
                company_info['ceo_name'] = ceo_name
            except Exception:
                pass

            try:
                ceo_approve_perc = driver.find_element('xpath', ceo_approve_path).text
                company_info['ceo_approve_percentage'] = ceo_approve_perc
            except Exception:
                pass

            try:
                company_founded = driver.find_element('xpath', company_founded_path).text
                company_info['company_founded'] = company_founded
            except Exception:
                pass

            try:
                show_more_btn = driver.find_element('xpath', show_more_btn_path)
                show_more_btn.click()
                time.sleep(2)  
            except Exception:
                pass

            try:
                company_headquarters_full = driver.find_element('xpath', company_headquarters_path_after_click).text
                company_info['company_headquarters_full'] = company_headquarters_full
            except Exception:
                pass

            try:
                company_website_link = driver.find_element('xpath', company_website_path).get_attribute('href')
                company_info['company_website_url'] = company_website_link
            except Exception:
                pass

            try:
                average_rating_score = driver.find_element('xpath',average_rating_score_path)
                company_info['Average_rating_score'] = average_rating_score.text

            except:
                pass

            try:
                average_rating = driver.find_element('xpath',average_rating_path)
                company_info['Average_rating'] = average_rating.text
            except:
                pass   

           # Work Well-Being Measures     

            measure_dict = {
           
            
            "Happiness":None,
            "Stress-free":None,
            "Purpose":None,
            "Satisfaction":None,
            "Flexibility":None,
            "Achievement":None,
            "Learning":None,
            "Inclusion":None,
            "Support":None,
            "Appreciation":None,
            "Energy":None,
            "Compensation":None,
            "Management":None,
            "Trust":None,
            "Belonging":None
 

            }
            
            

            try:
                see_all_results_btn_path = f"//button[@data-tn-element='work-wellbeing-all-dimensions']"
                see_all_results_btn = driver.find_element('xpath',see_all_results_btn_path)
                see_all_results_btn.click()
                time.sleep(6)

                for m in range(1,20):
                    try:
                        measure_path = f"(//h3[@class='css-1kl0g44 e1wnkr790'])[{m}]" 
                        measure = driver.find_element('xpath',measure_path).text
                        

                        if measure in measure_dict.keys():
                            measure_value_path = f"(//h3[@class='css-1kl0g44 e1wnkr790']/parent::*/following-sibling::*)[{m}]"
                            measure_value = driver.find_element('xpath',measure_value_path).text
                            
                            measure_dict[measure] = measure_value

                    except:
                        pass

            except:
                pass

            try:
                close_see_more_btn_path = "//button[@class='css-ejyn2z e8ju0x50']"
                close_see_more_btn = driver.find_element('xpath',close_see_more_btn_path)
                close_see_more_btn.click()
                time.sleep(1)
            except:
                pass


            company_info.update(measure_dict)
            companies.append(company_info)

            df  = pd.DataFrame(companies)
            print("Scrapped Company With Name : ",company_info['cname'])
            if i%10 == 0:
                df.to_csv(f"./company_scrap/company_info_{i}.csv")
                companies = []
            
            i+=1
            
        except:
            print("Something wrong link not fetched!!!")