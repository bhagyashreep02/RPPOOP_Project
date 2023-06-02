import pandas as pd
import streamlit as st
import entire_dataset as entire

class EntireDataset:
    def __init__(self, df):
        self.df = df
    
    def faculty_data(self):
        data = entire.faculty_data(self.df)
        dframe = pd.DataFrame(data)
        self.display_table_and_download_csv(data, 'Faculty_data.csv')
    
    def retirement_age(self):
        data = entire.age_to_retirement(self.df)
        dframe = pd.DataFrame(data)
        self.display_table_and_download_csv(data, 'Retirement_age.csv')
    
    def gender_count(self):
        data = entire.count_Gender_whole(self.df)
        st.text(data)
    
    def department_wise_gender_count(self):
        data = entire.count_Gender_Department(self.df)
        dframe = pd.DataFrame(data)
        self.display_table_and_download_csv(data, 'Department_wise_gender.csv')
    
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
        super().display_table_and_download_csv(self.df, 'comp_Faculty_data.csv')

    def retirement_age(self):
        super().retirement_age()
        super().display_table_and_download_csv(self.df, 'comp_Retirement_age.csv')

    def department_wise_gender_count(self):
        super().department_wise_gender_count()
        super().display_table_and_download_csv(self.df, 'comp_Department_wise_gender.csv')

    def get_email_ids(self):
        super().get_email_ids()
        super().display_table_and_download_csv(self.df, 'comp_Email_id\'s.csv')

class ManufacturingScienceAndEngineering(EntireDataset):
    def __init__(self, df):
        super().__init__(df[df['Department'] == 'MANUFACTURING SCIENCE AND ENGINEERING'])
    
    def faculty_data(self):
        super().faculty_data()
        super().display_table_and_download_csv(self.df, 'manufacturing_Faculty_data.csv')

    def retirement_age(self):
        super().retirement_age()
        super().display_table_and_download_csv(self.df, 'manufacturing_Retirement_age.csv')

    def department_wise_gender_count(self):
        super().department_wise_gender_count()
        super().display_table_and_download_csv(self.df, 'manufacturing_Department_wise_gender.csv')

    def get_email_ids(self):
        super().get_email_ids()
        super().display_table_and_download_csv(self.df, 'manufacturing_Email_id\'s.csv')

class ElectronicsAndTelecommunication(EntireDataset):
    def __init__(self, df):
        super().__init__(df[df['Department'] == 'ELECTRONICS AND TELECOMMUNICATION'])
    
    def faculty_data(self):
        super().faculty_data()
        super().display_table_and_download_csv(self.df, 'elec_Faculty_data.csv')

    def retirement_age(self):
        super().retirement_age()
        super().display_table_and_download_csv(self.df, 'elec_Retirement_age.csv')

    def department_wise_gender_count(self):
        super().department_wise_gender_count()
        super().display_table_and_download_csv(self.df, 'elec_Department_wise_gender.csv')

    def get_email_ids(self):
        super().get_email_ids()
        super().display_table_and_download_csv(self.df, 'elec_Email_id\'s.csv')

class MetallurgyAndMaterialTechnology(EntireDataset):
    def __init__(self, df):
        super().__init__(df[df['Department'] == 'METALLURGY AND MATERIAL TECHNOLOGY'])
    
    def faculty_data(self):
        super().faculty_data()
        super().display_table_and_download_csv(self.df, 'metallurgy_Faculty_data.csv')

    def retirement_age(self):
        super().retirement_age()
        super().display_table_and_download_csv(self.df, 'metallurgy_Retirement_age.csv')

    def department_wise_gender_count(self):
        super().department_wise_gender_count()
        super().display_table_and_download_csv(self.df, 'metallurgy_Department_wise_gender.csv')

    def get_email_ids(self):
        super().get_email_ids()
        super().display_table_and_download_csv(self.df, 'metallurgy_Email_id\'s.csv')

class MechanicalEngineering(EntireDataset):
    def __init__(self, df):
        super().__init__(df[df['Department'] == 'MECHANICAL ENGINEERING'])
    
    def faculty_data(self):
        super().faculty_data()
        super().display_table_and_download_csv(self.df, 'mechanical_Faculty_data.csv')

    def retirement_age(self):
        super().retirement_age()
        super().display_table_and_download_csv(self.df, 'mechanical_Retirement_age.csv')

    def department_wise_gender_count(self):
        super().department_wise_gender_count()
        super().display_table_and_download_csv(self.df, 'mechanical_Department_wise_gender.csv')

    def get_email_ids(self):
        super().get_email_ids()
        super().display_table_and_download_csv(self.df, 'mechanical_Email_id\'s.csv')

# Usage example:
df = pd.read_csv("Faculty_data copy.csv")
entire = EntireDataset(df)
comp_eng = ComputerEngineering(df)
mech_eng = MechanicalEngineering(df)

# Example usage:
selected_department = 'COMPUTER ENGINEERING'
selected_option = 'Faculty data'

if selected_department == 'ENTIRE DATASET':
    if selected_option == 'Faculty data':
        entire.faculty_data()
    elif selected_option == 'Retirement age':
        entire.retirement_age()
    elif selected_option == 'Gender count':
        entire.gender_count()
    elif selected_option == 'Department-wise gender count':
        entire.department_wise_gender_count()
    elif selected_option == 'Get email IDs':
        entire.get_email_ids()
    elif selected_option == 'Search email by name':
        entire.search_email_by_name()
    elif selected_option == 'Count by year of joining':
        entire.count_by_year_of_joining()
elif selected_department == 'COMPUTER ENGINEERING':
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
elif selected_department == 'MECHANICAL ENGINEERING':
    if selected_option == 'Faculty data':
        mech_eng.faculty_data()
    elif selected_option == 'Retirement age':
        mech_eng.retirement_age()
    elif selected_option == 'Gender count':
        mech_eng.gender_count()
    elif selected_option == 'Department-wise gender count':
        mech_eng.department_wise_gender_count()
    elif selected_option == 'Get email IDs':
        mech_eng.get_email_ids()
    elif selected_option == 'Search email by name':
        mech_eng.search_email_by_name()
    elif selected_option == 'Count by year of joining':
        mech_eng.count_by_year_of_joining()
