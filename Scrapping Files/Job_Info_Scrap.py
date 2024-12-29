import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def extract_job_details(driver,role,level,degree,posted_date,link):
    
    print("Scrapping Job with link : " , link)
  
    contents = {
        "posted_date" : posted_date,
        'role':role,
        'level':level,
        'degree':degree,
        'link' : link,
        "job_title" : None,
        "company" : None,
        "company_url" : None,
        "rating":None,
        "location" : None,
        "salary" : None,
        "job_type":None,
        "job_kind":None,
        "benefits":None,
        "description":None
    }
    try:
        #job Title
        job_title_element=driver.find_element("xpath",'//h1[@class="jobsearch-JobInfoHeader-title css-1b4cr5z e1tiznh50"]/*[1]')
        contents["job_title"]=job_title_element.text
    except:
        
        print("Job title not found")

    try:
        # company name
        company_element = driver.find_element("xpath","//div[@data-testid='inlineHeader-companyName']//a")
        contents["company"] = company_element.text
        contents["company_url"] = company_element.get_attribute('href')
    
    except:
         print("company name, url not found")
 
    try:
        # ratings
        rating_element = driver.find_element('xpath', "//span[@class='css-ppxtlp e1wnkr790']")
        contents["rating"] = rating_element.text.split(' ')[0]
    except:
         print("rating not found")

    try:
        # location
        location_element = driver.find_element(By.ID, "jobLocationSectionWrapper")
        contents["location"] = location_element.text
    except:
         print("location not found")
        
    try:
        # salary   
        salary_element = driver.find_element(By.CSS_SELECTOR, "div#salaryInfoAndJobType span.css-19j1a75")
        contents["salary"] = salary_element.text
    
    except:

        contents["salary"] = "No Salary"
        
    try:
        # job type
        job_type_element = driver.find_element(By.CSS_SELECTOR, "div#salaryInfoAndJobType span.css-k5flys")
        contents["job_type"] = job_type_element.text.strip(' - ')
    except:
        print("job type not found")
       
    try:
        # job kind(remote or hybrid)
        job_kind= driver.find_element("xpath",'//div[@class="css-17cdm7w eu4oa1w0"]/*[1]')
        contents["job_kind"]=job_kind.text
    except: 
        print("job kind not found")
    try:
        #descriptions
        description= driver.find_element("xpath",'//div[@class="jobsearch-jobDescriptionText jobsearch-JobComponent-description css-kqe8pq eu4oa1w0"]')
        contents["description"]=description.text
    except:
        print("Description Not Found")
    
    try:
        button=driver.find_element("xpath",'//button[@data-testid="collapsedBenefitsButton"]')
        driver.execute_script("arguments[0].click();",button)
        time.sleep(2)
   
    except:
        pass

    #benefits lists
        
    benefit_list=list([])
   

    for i in range(1,16):
        try:
            benefits=driver.find_element("xpath",f'(//ul[@class="css-8tnble eu4oa1w0"]/*)[{i}]').text
            benefit_list.append(benefits)
        except:
            pass
    
    contents['benefits'] = benefit_list
    
   
    
    return contents

def scrap(start,end,range):
 
    i = start
    e = end
    r = range

    job_data = []
    df = pd.read_csv('G:\INTERN\data_engineer_merge\merged_links.csv')
    df = df.iloc[i:e+1,:]

    driver = webdriver.Chrome()

    for role,level,degree,link,posted_date in zip(df['role'],df['level'],df['degree'],df['links'],df['posted_date']):
        
       
        base_url = link
        posted_date = posted_date

        try:
            driver.get(base_url)
            job_details = extract_job_details(driver,role,level,degree,posted_date,base_url)
           
            if(job_details['job_title'] == None):
                driver.quit()
                driver = webdriver.Chrome()
           
            driver.get(base_url)
            job_details = extract_job_details(driver,role,level,degree,posted_date,base_url) 

            job_data.append(job_details)

        except:
            print(f"URL NOT FOUND !!!!")
        
        i+=1

        if i%r == 0 :
           
            # Convert job_data to a pandas DataFrame
            df = pd.DataFrame(job_data)

            # Save the DataFrame as a CSV file
            df.to_csv(f'G:\INTERN\jobs_info_csvs\job_data_{start}_{start+range}.csv', index=False)
            start = ( start + range ) 
            print("----------------")
            print("Saved File")
          
            df.drop(df.index, inplace=True)

            job_data = list([])
        
        print("Scrapping Done For link No " ,i)
        
        
        if i == e:
            print(f"Scrapping Done for {start} to {end} ")
            break

        

