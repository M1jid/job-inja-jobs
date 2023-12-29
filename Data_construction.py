class DataConstruction:
    def data():
        import import_ipynb
        from Data import Data
        from sklearn.preprocessing import OneHotEncoder
        import pandas as pd
        data = Data.data()
        dataset = data.copy()
        onehote = OneHotEncoder(sparse_output=False)
        Type_cooperation = onehote.fit_transform(dataset[['Type_cooperation']])
        job_time = pd.DataFrame(Type_cooperation)
        job_time.columns = ['Full_time','Part-time']
        dataset = dataset.drop('Type_cooperation',axis=1)

        Data_df= pd.concat([dataset,job_time],axis=1)

        Data_df['job-inja_locations'] = 1
        Data_df['job_category'] = 1


        # job-inja_locations	 1 = tehran
        # job_category	 1 = ai developer
        datas = onehote.fit_transform(Data_df[['work_experience']])
        datass = pd.DataFrame(datas)
        datass.columns = ['telecommuting','3-6 Years ','No record'  , 'internship','-three years']
        Data_df = Data_df.drop('work_experience',axis=1)
        data_df = pd.concat([Data_df,datass],axis=1)


        Rights = onehote.fit_transform(data_df[['rights']])
        Rights = pd.DataFrame(Rights)
        Rights.columns = ['10m','14m','an agreement','removed','removedd']
        data_df = data_df.drop('rights',axis=1)
        Rights = Rights.drop('removed',axis=1)
        datasets = pd.concat([data_df,Rights],axis=1)




        skills = onehote.fit_transform(data_df[['skills']])
        skills = pd.DataFrame(skills)
        skills.columns = ['Ai','Back-end','Flutter','Machine Vision','React','Bi','T','english','data_analysis','t','BI','ai']
        skills = skills.drop('T',axis=1)
        skills = skills.drop('t',axis=1)
        data_df = data_df.drop('skills',axis=1)
        datasetss = pd.concat([data_df,skills],axis=1)

        data_numbr = datasetss.select_dtypes(include='float64')
        data_numbr = data_numbr .astype('float32')
        data_numbr.to_csv('data.csv',index=0)