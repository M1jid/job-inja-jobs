class Urls_site:
    
    ''' This class is for returning the url of requsts 

            inputs: titel, location, category, Page identifier
              
            outputs:
            urls for request
            
    '''
    
    #Createing job_inja site url
    def job_inja(job_titles = 'هوش مصنوعی',location = 'تهران',category = '=وب،%E2%80%8C+برنامه%E2%80%8Cنویسی+و+نرم%E2%80%8Cافزار&b=',page = '&page=1'):
        slice1 = 'https://www.jobinja.ir/jobs?filters[keywords][]='
        slice2 = job_titles
        slice3 = '&filters[locations][]='
        slice4 = location
        slice5 = '&filters[job_categories][]='
        slice6 = category
        slice7 = page
        link = slice1 + slice2 + slice3 + slice4 + slice5 + slice6 + slice7
        return link
    
    #Createing job_vision1 site url next version
    def job_vision1():
        linkjw = 'https://jobvision.ir/jobs/category/data-science-in-all-cities-of-tehran?page=1&sort=1'
        return str(linkjw)
    
    #Createing e_estekhdam site url next version
    def e_estekhdam():
        link = 'https://www.e-estekhdam.com/search/استخدام-برنامه-نویس-در-تهران-برای-هوش-مصنوعی'
        return str(link)
    
    #Createing kar_bom site url next version
    def kar_bom():
        link = 'https://www.karboom.io/jobs?q=هوش%20مصنوعی&address_city_id[]=87'
        return str(link)
    
    #Createing iran_talent site url next version
    def iran_talent():
        '''for The next version '''
        link = 'https://www.irantalent.com/jobs/jobs-in-tehran?keyword=هوش-مصنوعی&language=persian'
        return str(link)