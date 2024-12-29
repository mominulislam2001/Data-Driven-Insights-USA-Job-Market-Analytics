from Job_Links import merge_scraped_files,scrap_links_post_date
dict_= {

    "data_analyst":{

        "Entry_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate':"link"  
        },
        "Mid_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate': "link"
        },
        "Senior_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate':"link"
        }},

    "data_scientist":{
           
        "Entry_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate':"link"
           },

        "Mid_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate': "link"
            },
        "Senior_level":{
            "bachelors":"link",
            "masters":"link",
            'doctorate':"link"}},
    
    "business_analyst":{
        
        "Entry_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate':"link"
           },
        "Mid_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate': "link"
            },
        "Senior_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate':"link"}},

    "data_engneering":{
        
        "Entry_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate':"link"
           },
        "Mid_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate': "link"
            },
        "Senior_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate':"link"}},

    "machine_learning_engineer":{
        
        "Entry_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate':"link"
           },
        "Mid_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate': "link"
            },
        "Senior_level":{
            "bachelors":"link"
            "masters":"link"
            'doctorate':"link"}}}


scrap_links_post_date(dict_)