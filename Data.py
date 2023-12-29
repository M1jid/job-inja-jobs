# for link in range(len(links)):
class Data:
    
    def data():
        titels = []
        locations = []
        lists = []
        columns = []
        a = 0
        b = 2
        c = 3
        d = 4
        f = 5
        i = 0
        from web_app import ReturnData
        import streamlit as st
        import import_ipynb
        from request import  Page
        from InputValues import Inputer
        from URLS import Urls_site
        from PIL import Image
        import pandas as pd 
        import requests
        from bs4 import BeautifulSoup

        titel , company , loc , links = ReturnData.return_data()
        
        
        
        
        for tite in range(len(titel)):
            tit = str(titel[tite])
            tit = tit.replace('\n                      ' , '')
            tit = tit.replace('\n                 ', '')
            titels .append(tit)
            location = str(loc[tite])
            location = location.replace('\n                      ', '')
            location = location.replace('    تهران، ', '')
            locations.append(location)


        titels = pd.DataFrame(titels , columns = ['job-inja_titels'])
        locations = pd.DataFrame(locations , columns = ['job-inja_locations'])
        company = pd.DataFrame(company , columns = ['job-inja_companys'])
        jobinja_data = pd.concat([titels , locations , company], axis=1)


        for link in  range(len(links)):
            page = requests.get(links[link])
            page_soup = BeautifulSoup(page.text , 'html.parser')
            page_soup_titel = page_soup.css.select(".c-jobView>ul>li>h4")
            page_soup_val = page_soup.css.select(".c-jobView>ul>li>div>span")


            for item in range(6):
                page_soup_tit  = str(page_soup_titel[item])
                page_soup_tit = page_soup_tit.replace('<h4 class="c-infoBox__itemTitle">','')
                page_soup_tit = page_soup_tit.replace('</h4>','')
                page_soup_tit = page_soup_tit.replace('\u200c','')
                page_soup_values = str(page_soup_val[item])
                page_soup_values = page_soup_values.replace('<span class="black">','')
                page_soup_values = page_soup_values.replace('</span>','')
                page_soup_values = page_soup_values.replace('\u200c','')
                page_soup_values = page_soup_values.replace('\n                                    ','')
                page_soup_values = page_soup_values.replace('تهران            ','')

                columns.append(page_soup_tit)
                lists.append(page_soup_values)
        jobinja_data ['job_category'] = lists[a]
        jobinja_data ['Type_cooperation'] = lists[b]
        jobinja_data ['work_experience'] = lists[c]
        jobinja_data ['rights']= lists[d]
        jobinja_data ['skills']= lists[f]



            

        for item in range(len(lists)+50):
 
            jobinja_data ['job_category'][item] = lists[a]
            a += 6
            
            jobinja_data ['Type_cooperation'][item]= lists[b]
            b += 6
            
            jobinja_data ['work_experience'][item]= lists[c]
            c += 6
            
            jobinja_data ['rights'][item]= lists[d]
            d += 6
            
            jobinja_data ['skills'][item]= lists[f]
            f += 6
            if a >= len(lists) or b >= len(lists) or c >= len(lists) or d >= len(lists) or f >= len(lists):
                break

        return jobinja_data


