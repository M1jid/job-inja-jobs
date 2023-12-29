class Page:
    
    '''
    This class uses the classes in other files to send a request and receive a response .
    Selects the title and company name and location on the pages
    and puts it in a list.

    inputs  :
    class Urls_site  for return url site .

    outputs :
    list of titel & company name & locations .
     '''

    def page_request_jobinja():
        
        from bs4 import BeautifulSoup
        import import_ipynb
        import requests
        
        #return urls site
        from URLS import Urls_site
        

        
        #Creating lists for save data
        titel_job = []
        companyes = []
        locations = []
        
        #scrolling through the next related pages and send request
        for links in range(6):
            
            job_inja_page = requests.get(Urls_site.job_inja(page=f'&page={links}'))
            jobinja_suop  = BeautifulSoup(job_inja_page.text , 'html.parser')
            joninja_links = jobinja_suop.css.select(".u-mB30>div>ul>li")
            job_inja_titel= jobinja_suop.css.select("[class~=c-jobListView__titleLink]")
            cunter = 0 
        

           #Separating the required values and putting them in the list
            for titel in range(len(job_inja_titel)):
                job_inja_titel = jobinja_suop.css.select("[class~=c-jobListView__titleLink]")[titel]
                titel_job.append(job_inja_titel)
                job_inja_company = jobinja_suop.css.select(".c-jobListView__metaItem>span")[cunter]
                companyes.append(job_inja_company)
                job_inja_location = jobinja_suop.css.select(".c-jobListView__metaItem>span")[cunter+1]
                locations.append(job_inja_location)
                cunter += 3
        return (titel_job, companyes, locations)

# next version ==> def job_vision():
        
    
    
 
    