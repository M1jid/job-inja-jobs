
import streamlit as st
import import_ipynb
from request import  Page
from InputValues import Inputer
from URLS import Urls_site
from PIL import Image

#web app header 
st.title('          خوش امدید           ')
st.write("#This app searches the internet and returns you the desired job that companies want to hire.")

#to show image in web-app
img = Image.open("C:/Users/itel/request_scraping/jobinja_data/img.png")
st.image(img , width=800)

#show and change titel and location and category
title    = st.sidebar.text_input('Please enter your desired job title','هوش مصنوعی')
location = st.sidebar.text_input('Please enter your desired job location','تهران')
category = st.sidebar.text_input('Please enter your desired job category ','وب و برنامه نویسی')

Urls_site.job_inja(title,location)

v , companys , loc  = Page.page_request_jobinja()

st.write(f' find {len(v)} jobs in job inja')

titels_data    = []
companys_data  = []
locations_data = []

titels = [links['href'] for links in v ]
i = 0
#To delete unimportant
for links in range(len(v)):
    titelstr = str(v[links]).replace(str(titels[links]),'')
    titelstr = titelstr.replace('class="c-jobListView__titleLink" href="" target="_blank"','')
    titelstr = titelstr.replace('<a >','')
    titelstr = titelstr.replace( ' </a>','')
    titels_data.append(titelstr)
    st.header(titelstr)

    
    company = str(companys[i])
    company = company.replace('span','')
    company = company.replace('<>','')
    company = company.replace( '</>','')
    companys_data.append(company)
    st.write(company)

    
    location = loc[links]
    location = str(location)
    location = location.replace('span','')
    location = location.replace('<>','')
    location = location.replace( '</>','')
    locations_data.append(location)
    st.write(location)
    
    st.link_button('GO to link ;)',titels[links])
    st.write('_________________________________________')
    i += 2
    if i == len(v) or i==len(v)+1:
        break
    
    




site = st.sidebar.selectbox('select site job ==>job_inja',('job_inja','job_vision','e-estekhdam' , 'karboom','irantalent'))
st.sidebar.write('You selected:', site)
st.sidebar.write('***********************')
links = [links['href'] for links in v]

class ReturnData:
    '''
    this class for easier access to other files
    for return data 
    '''
    def return_data():
        return titels_data , companys_data , locations_data , links