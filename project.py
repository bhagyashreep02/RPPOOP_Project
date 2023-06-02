import streamlit as st
import pandas as pd
import entire_dataset as entire
import dataset2 as dts2

df1 = pd.read_csv("Faculty_data copy.csv")

st.sidebar.header("FACULTY DATA VISUALISATION")
option = st.sidebar.radio(" ",("Main page","Analytical data","Graphical data"))
st.sidebar.header("\n")
st.sidebar.header("\n")
st.sidebar.header("\n")
st.sidebar.header("\n")
st.sidebar.header("\n")
st.sidebar.text("* All input data must be \n entered in bold letters")


if option == "Main page":
    st.title("FACULTY DATA VISUALISATION")
    st.text(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.text("Click below to upload a new file or continue in the sidebar with the default file")
    uploaded_file = st.file_uploader("Select a CSV file to visualise data", accept_multiple_files=False)
    if uploaded_file:
        df1 = pd.read_csv(uploaded_file)
        st.text("File uploaded, continue in the sidebar")

def convert_df(df):
    return df.to_csv().encode('utf-8')

if option == "Analytical data":
    dept = st.selectbox("Select a department",(' ','ENTIRE DATASET', 'COMPUTER ENGINEERING','MANUFACTURING SCIENCE AND ENGINEERING',
                'ELECTRONICS AND TELECOMMUNICATION','METALLURGY AND MATERIAL TECHNOLOGY','MECHANICAL ENGINEERING',
                'CIVIL ENGINEERING','INSTRUMENTATION AND CONTROL ENGINEERING','ELECTRICAL ENGINEERING',
                'ENGINEERING EDUCATION', 'TOWN PLANNING','APPLIED CHEMISTRY','APPLIED MATHEMATICS',
                'MANAGEMENT','MASTERS IN BUSINESS ADMINISTRATION'))
    selected_option = st.selectbox("Select an operation",(' ','Faculty data','Retirement age','Gender count','Department wise gender count','Get email id\'s','Search email by name','Count by year of joining'))
    class EntireDataset:
        def __init__(self, df):
            self.df = df
        
        def faculty_data(self):
            data = entire.faculty_data(self.df)
            dframe = pd.DataFrame(data)
            self.display_table_and_download_csv(dframe, 'Faculty_data.csv')
    
        def retirement_age(self):
            data = entire.age_to_retirement(self.df)
            dframe = pd.DataFrame(data)
            self.display_table_and_download_csv(dframe, 'Retirement_age.csv')
    
        def gender_count(self):
            data = entire.count_Gender_whole(self.df)
            st.text(data)
    
        def department_wise_gender_count(self):
            data = entire.count_Gender_Department(self.df)
            dframe = pd.DataFrame(data)
            self.display_table_and_download_csv(dframe, 'Department_wise_gender.csv')
    
        def get_email_ids(self):
            data = entire.find_email(self.df)
            dframe = pd.DataFrame(data)
            self.display_table_and_download_csv(dframe, 'Email_id.csv')
    
        def search_email_by_name(self):
            title = st.text_input('Enter Name')
            data = entire.email(self.df, title)
            st.subheader(data)
    
        def count_by_year_of_joining(self):
            data = entire.date_of_joining(self.df)
            data1 = {"Joined on or after 2000": data[1], "Joined before 2000": data[0]}
            st.table(data1)
    
        def display_table_and_download_csv(self, dframe, filename):
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
                label="Download data as CSV",
                data=csv1,
                file_name=filename,
                mime='text/csv',
            )
            st.text("\n")
            st.table(dframe)

    class ComputerEngineering(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == "COMPUTER ENGINEERING"])
        def faculty_data(self):
            super().faculty_data()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()


    entire1= EntireDataset(df1)
    comp_eng = ComputerEngineering(df1)
    
    if dept == 'ENTIRE DATASET':
        if selected_option == 'Faculty data':
            entire1.faculty_data()
        elif selected_option == 'Retirement age':
            entire1.retirement_age()
        elif selected_option == 'Gender count':
            entire1.gender_count()
        elif selected_option == 'Department-wise gender count':
            entire1.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            entire1.get_email_ids()
        elif selected_option == 'Search email by name':
            entire1.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            entire1.count_by_year_of_joining()
    elif dept == 'COMPUTER ENGINEERING':
        if selected_option == 'Faculty data':
            comp_eng.faculty_data()
        elif selected_option == 'Retirement age':
            comp_eng.retirement_age()
        elif selected_option == 'Gender count':
            comp_eng.gender_count()
        elif selected_option == 'Department-wise gender count':
            comp_eng.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            comp_eng.get_email_ids()
        elif selected_option == 'Search email by name':
            comp_eng.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            comp_eng.count_by_year_of_joining()

