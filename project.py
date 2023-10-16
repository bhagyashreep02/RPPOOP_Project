import streamlit as st
import pandas as pd
import entire_dataset as entire
import dataset2 as dts2
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


df1 = pd.read_csv("Faculty_data copy.csv")

st.sidebar.header("FACULTY DATA VISUALISATION")
option = st.sidebar.radio(" ",("Main page","Analytical data","Graphical data"))
st.sidebar.divider()
uploaded_file = st.sidebar.file_uploader("Select a CSV file to visualise data", accept_multiple_files=False,type = ".csv")
if uploaded_file:
    df1 = pd.read_csv(uploaded_file)
    st.sidebar.text("File uploaded,\ncontinue with the operations above.")
else:
    st.sidebar.text("Default file being used,\ncontinue with operations above.")
st.sidebar.divider()
st.sidebar.text("* All input data must be\nentered in bold letters.")


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

def convert_df(df):
    return df.to_csv().encode('utf-8')



if option == "Main page":
    st.title("FACULTY DATA VISUALISATION")
    st.text(" ")
    st.text("===================================================================================================================")
    st.markdown("**_You can either continue with visualization with the default dataset or upload your dataset in the sidebar_**")
    st.text("===================================================================================================================")
    st.text(" ")
    col4,col5 = st.columns(2)
    tab1, tab2 = st.tabs(["\t\t\t\t\t\tView the default dataset\t", "\t\t\t\t\t\tDownload the default dataset\t"])
    with col4:
        with tab2:
            col1,col2,col3 = st.columns(3)
            with col2:
                csv1 = convert_df(df1)
                st.download_button(
                    label="Download default dataset as CSV",
                    data=csv1,
                    file_name="DATASET.csv",
                    mime='text/csv',
                    )
    with col5:
        with tab1:
            with st.expander("View the default dataset"):
                st.dataframe(df1)
    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1523961131990-5ea7c61b2107?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )




if option == "Analytical data":
    dept = st.selectbox("Select a department",(' ','ENTIRE DATASET', 'COMPUTER ENGINEERING','MANUFACTURING SCIENCE AND ENGINEERING',
                'ELECTRONICS AND TELECOMMUNICATION','METALLURGY AND MATERIAL TECHNOLOGY','MECHANICAL ENGINEERING',
                'CIVIL ENGINEERING','INSTRUMENTATION AND CONTROL ENGINEERING','ELECTRICAL ENGINEERING',
                'ENGINEERING EDUCATION', 'TOWN PLANNING','APPLIED SCIENCE',
                'MANAGEMENT','MASTERS IN BUSINESS ADMINISTRATION'))
    selected_option = st.selectbox("Select an operation",(' ','Faculty data','Search by name','Retirement age','Gender count','Department wise gender count','Get email IDs','Search email by name','Count by year of joining','Faculty in each Department','Doctorate Faculty','Postgraduate Faculty','Appointment-types of Faculty','Designation of Faculty'))
    
    class EntireDataset:
        def __init__(self, df):
            self.df = df

        def faculty_data(self):
            data = entire.faculty_data(self.df)
            dframe = pd.DataFrame(data)
            self.display_table_and_download_csv(dframe, 'Faculty_data.csv')

        def get_details(self):
            title = st.text_input('Enter Name')
            data = entire.get_details(self.df, title)
            st.table(data)
    
        def retirement_age(self):
            data = entire.age_to_retirement(self.df)
            dframe = pd.DataFrame(data)
            self.display_table_and_download_csv(dframe, 'Retirement_age.csv')
    
        def gender_count(self):
            data = entire.count_Gender_whole(self.df)
            st.table(data)
    
        def department_wise_gender_count(self):
            data = entire.count_Gender_Department(self.df)
            dframe = pd.DataFrame(data)
            self.display_table_and_download_csv(dframe, 'Department_wise_gender.csv')
            show_faculty_names = st.checkbox("Show Faculties by gender")
            if show_faculty_names:
                self.display_faculty_members_by_category(dframe, 'Gender')
    
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
        
        def faculty_depts(self):
            dframe=dts2.faculty_dept(self.df)
            self.display_table_and_download_csv(dframe, 'Faculty_dept.csv')
        
        def doctorate_Faculty(self):
            dframe=dts2.faculty_doctorate(self.df)
            self.display_table_and_download_csv(dframe, 'Doctorate_Faculty.csv')
            show_faculty_names = st.checkbox("Show corresponding Faculties")
            if show_faculty_names:
                self.display_faculty_members_by_category(dframe, 'Doctorate Degree')

        def postgrad_Faculty(self):
            dframe=dts2.faculty_pg(self.df)
            self.display_table_and_download_csv(dframe, 'Postgraduate_Faculty.csv')
            show_faculty_names = st.checkbox("Show corresponding Faculties")
            if show_faculty_names:
                self.display_faculty_members_by_category(dframe, 'PG')


        def appointment_types(self):
            dframe=dts2.faculty_app(self.df)
            self.display_table_and_download_csv(dframe, 'Appointment-types_faculty.csv')
            show_faculty_names = st.checkbox(" Show Faculty by appointment type")
    
            if show_faculty_names:
                self.display_faculty_members_by_category(dframe, 'Appointment Type')

        def designation_types(self):
            dframe=dts2.faculty_designation(self.df)
            self.display_table_and_download_csv(dframe, 'Designation_faculty.csv')
            show_faculty_names = st.checkbox(" Show Faculty by designation type")
    
            if show_faculty_names:
                self.display_faculty_members_by_category(dframe, 'Designation')
                
    
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
        
        def display_faculty_members_by_category(self, dframe, category_column):
            for index, row in dframe.iterrows():
                expander = st.expander(f"{row[category_column]} (Count: {row['Count']})")
                with expander:
                    st.write("Faculty Members:")
                    faculty_data = self.df[self.df[category_column] == row[category_column]]
                    for _, faculty_row in faculty_data.iterrows():
                        st.write(f"{faculty_row['Title']} {faculty_row['First Name']} {faculty_row['Last Name']}")


    class ComputerEngineering(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == "COMPUTER ENGINEERING"])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()


    class Manufacturing(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MANUFACTURING SCIENCE AND ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class ENTC(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'ELECTRONICS AND TELECOMMUNICATION'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()
        

    class Metallurgy(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'METALLURGY AND MATERIAL TECHNOLOGY'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()
        
        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class Mechanical(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MECHANICAL ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()
        
        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class Civil(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'CIVIL ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class Instrumentation(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'INSTRUMENTATION AND CONTROL ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class Electrical(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'ELECTRICAL ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()
        
        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class EnggEducation(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'ENGINEERING EDUCATION'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class Planning(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'TOWN PLANNING'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class AppSci(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'APPLIED SCIENCE'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()
        
        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class Manage(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MANAGEMENT'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()

    class MBA(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MASTERS IN BUSINESS ADMINISTRATION'])
        def faculty_data(self):
            super().faculty_data()
        def get_details(self):
            super().get_details()
        def retirement_age(self):
            super().retirement_age()
        def department_wise_gender_count(self):
            super().department_wise_gender_count()
        def get_email_ids(self):
            super().get_email_ids()
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

        def doctorate_Faculty(self):
            super().doctorate_Faculty()
        def postgrad_Faculty(self):
            super().postgrad_Faculty()
        def appointment_types(self):
            super().appointment_types()
        def designation_types(self):
            super().designation_types()




    entire1= EntireDataset(df1)
    comp_eng = ComputerEngineering(df1)
    manu = Manufacturing(df1)
    entc = ENTC(df1)
    meta = Metallurgy(df1)
    mech = Mechanical(df1)
    civil = Civil(df1)
    instru = Instrumentation(df1)
    elec = Electrical(df1)
    engg = EnggEducation(df1)
    plan = Planning(df1)
    appsci = AppSci(df1)
    manage = Manage(df1)
    mba = MBA(df1)

    
    
    if dept == 'ENTIRE DATASET':
        if selected_option == 'Faculty data':
            entire1.faculty_data()
        elif selected_option == 'Search by name':
            entire1.get_details()
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
        elif selected_option=='Faculty in each Department':
            entire1.faculty_depts()
        elif selected_option=='Doctorate Faculty':
            entire1.doctorate_Faculty()
        elif selected_option=='Postgraduate Faculty':
            entire1.postgrad_Faculty()
        elif selected_option=='Appointment-types of Faculty':
            entire1.appointment_types()
        elif selected_option=='Designation of Faculty':
            entire1.designation_types()

    elif dept == 'COMPUTER ENGINEERING':
        if selected_option == 'Faculty data':
            comp_eng.faculty_data()
        elif selected_option == 'Search by name':
            comp_eng.get_details()
        elif selected_option == 'Retirement age':
            comp_eng.retirement_age()
        elif selected_option == 'Gender count':
            comp_eng.gender_count()
        elif selected_option == 'Department wise gender count':
            comp_eng.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            comp_eng.get_email_ids()
        elif selected_option == 'Search email by name':
            comp_eng.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            comp_eng.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            comp_eng.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            comp_eng.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            comp_eng.appointment_types()
        elif selected_option == 'Designation of Faculty':
            comp_eng.designation_types()

    elif dept == 'MANUFACTURING SCIENCE AND ENGINEERING':
        if selected_option == 'Faculty data':
            manu.faculty_data()
        elif selected_option == 'Search by name':
            manu.get_details()
        elif selected_option == 'Retirement age':
            manu.retirement_age()
        elif selected_option == 'Gender count':
            manu.gender_count()
        elif selected_option == 'Department wise gender count':
            manu.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            manu.get_email_ids()
        elif selected_option == 'Search email by name':
            manu.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            manu.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            manu.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            manu.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
             manu.appointment_types()
        elif selected_option == 'Designation of Faculty':
            manu.designation_types()

    elif dept == 'ELECTRONICS AND TELECOMMUNICATION':
        if selected_option == 'Faculty data':
            entc.faculty_data()
        elif selected_option == 'Search by name':
            entc.get_details()
        elif selected_option == 'Retirement age':
            entc.retirement_age()
        elif selected_option == 'Gender count':
            entc.gender_count()
        elif selected_option == 'Department wise gender count':
            entc.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            entc.get_email_ids()
        elif selected_option == 'Search email by name':
            entc.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            entc.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            entc.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            entc.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            entc.appointment_types()
        elif selected_option == 'Designation of Faculty':
            entc.designation_types()

    elif dept == 'METALLURGY AND MATERIAL TECHNOLOGY':
        if selected_option == 'Faculty data':
            meta.faculty_data()
        elif selected_option == 'Search by name':
            meta.get_details()
        elif selected_option == 'Retirement age':
            meta.retirement_age()
        elif selected_option == 'Gender count':
            meta.gender_count()
        elif selected_option == 'Department wise gender count':
            meta.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            meta.get_email_ids()
        elif selected_option == 'Search email by name':
            meta.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            meta.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            meta.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            meta.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            meta.appointment_types()
        elif selected_option == 'Designation of Faculty':
            meta.designation_types()

    elif dept == 'MECHANICAL ENGINEERING':
        if selected_option == 'Faculty data':
            mech.faculty_data()
        elif selected_option == 'Search by name':
            mech.get_details()
        elif selected_option == 'Retirement age':
            mech.retirement_age()
        elif selected_option == 'Gender count':
            mech.gender_count()
        elif selected_option == 'Department wise gender count':
            mech.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            mech.get_email_ids()
        elif selected_option == 'Search email by name':
            mech.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            mech.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            mech.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            mech.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            mech.appointment_types()
        elif selected_option == 'Designation of Faculty':
            mech.designation_types()

    elif dept == 'CIVIL ENGINEERING':
        if selected_option == 'Faculty data':
            civil.faculty_data()
        elif selected_option == 'Search by name':
            civil.get_details()
        elif selected_option == 'Retirement age':
            civil.retirement_age()
        elif selected_option == 'Gender count':
            civil.gender_count()
        elif selected_option == 'Department wise gender count':
            civil.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            civil.get_email_ids()
        elif selected_option == 'Search email by name':
            civil.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            civil.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            civil.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            civil.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            civil.appointment_types()
        elif selected_option == 'Designation of Faculty':
            civil.designation_types()


    elif dept == 'INSTRUMENTATION AND CONTROL ENGINEERING':
        if selected_option == 'Faculty data':
            instru.faculty_data()
        elif selected_option == 'Search by name':
            instru.get_details()
        elif selected_option == 'Retirement age':
            instru.retirement_age()
        elif selected_option == 'Gender count':
            instru.gender_count()
        elif selected_option == 'Department wise gender count':
            instru.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            instru.get_email_ids()
        elif selected_option == 'Search email by name':
            instru.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            instru.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            instru.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            instru.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            instru.appointment_types()
        elif selected_option == 'Designation of Faculty':
            instru.designation_types()

    elif dept == 'ELECTRICAL ENGINEERING':
        if selected_option == 'Faculty data':
            elec.faculty_data()
        elif selected_option == 'Search by name':
            elec.get_details()
        elif selected_option == 'Retirement age':
            elec.retirement_age()
        elif selected_option == 'Gender count':
            elec.gender_count()
        elif selected_option == 'Department wise gender count':
            elec.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            elec.get_email_ids()
        elif selected_option == 'Search email by name':
            elec.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            elec.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            elec.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            elec.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            elec.appointment_types()
        elif selected_option == 'Designation of Faculty':
            elec.designation_types()

    elif dept == 'ENGINEERING EDUCATION':
        if selected_option == 'Faculty data':
            engg.faculty_data()
        elif selected_option == 'Search by name':
            engg.get_details()
        elif selected_option == 'Retirement age':
            engg.retirement_age()
        elif selected_option == 'Gender count':
            engg.gender_count()
        elif selected_option == 'Department wise gender count':
            engg.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            engg.get_email_ids()
        elif selected_option == 'Search email by name':
            engg.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            engg.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            engg.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            engg.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            engg.appointment_types()
        elif selected_option == 'Designation of Faculty':
            engg.designation_types()

    elif dept == 'TOWN PLANNING':
        if selected_option == 'Faculty data':
            plan.faculty_data()
        elif selected_option == 'Search by name':
            plan.get_details()
        elif selected_option == 'Retirement age':
            plan.retirement_age()
        elif selected_option == 'Gender count':
            plan.gender_count()
        elif selected_option == 'Department wise gender count':
            plan.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            plan.get_email_ids()
        elif selected_option == 'Search email by name':
            plan.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            plan.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            plan.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            plan.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            plan.appointment_types()
        elif selected_option == 'Designation of Faculty':
            plan.designation_types()

    elif dept == 'APPLIED SCIENCE':
        if selected_option == 'Faculty data':
            appsci.faculty_data()
        elif selected_option == 'Search by name':
            appsci.get_details()
        elif selected_option == 'Retirement age':
            appsci.retirement_age()
        elif selected_option == 'Gender count':
            appsci.gender_count()
        elif selected_option == 'Department wise gender count':
            appsci.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            appsci.get_email_ids()
        elif selected_option == 'Search email by name':
            appsci.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            appsci.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            appsci.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            appsci.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            appsci.appointment_types()
        elif selected_option == 'Designation of Faculty':
            appsci.designation_types()

    elif dept == 'MANAGEMENT':
        if selected_option == 'Faculty data':
            manage.faculty_data()
        elif selected_option == 'Search by name':
            manage.get_details()
        elif selected_option == 'Retirement age':
            manage.retirement_age()
        elif selected_option == 'Gender count':
            manage.gender_count()
        elif selected_option == 'Department wise gender count':
            manage.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            manage.get_email_ids()
        elif selected_option == 'Search email by name':
            manage.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            manage.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            manage.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            manage.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            manage.appointment_types()
        elif selected_option == 'Designation of Faculty':
            manage.designation_types()

    elif dept == 'MASTERS IN BUSINESS ADMINISTRATION':
        if selected_option == 'Faculty data':
            mba.faculty_data()
        elif selected_option == 'Search by name':
            mba.get_details()
        elif selected_option == 'Retirement age':
            mba.retirement_age()
        elif selected_option == 'Gender count':
            mba.gender_count()
        elif selected_option == 'Department wise gender count':
            mba.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            mba.get_email_ids()
        elif selected_option == 'Search email by name':
            mba.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            mba.count_by_year_of_joining()
        elif selected_option == 'Doctorate Faculty':
            mba.doctorate_Faculty()
        elif selected_option == 'Postgraduate Faculty':
            mba.postgrad_Faculty()
        elif selected_option == 'Appointment-types of Faculty':
            mba.appointment_types()
        elif selected_option == 'Designation of Faculty':
            mba.designation_types()

elif option=='Graphical data':
    dept = st.selectbox("Select a department",(' ','ENTIRE DATASET', 'COMPUTER ENGINEERING','MANUFACTURING SCIENCE AND ENGINEERING',
                'ELECTRONICS AND TELECOMMUNICATION','METALLURGY AND MATERIAL TECHNOLOGY','MECHANICAL ENGINEERING',
                'CIVIL ENGINEERING','INSTRUMENTATION AND CONTROL ENGINEERING','ELECTRICAL ENGINEERING',
                'ENGINEERING EDUCATION', 'TOWN PLANNING','APPLIED SCIENCE',
                'MANAGEMENT','MASTERS IN BUSINESS ADMINISTRATION'))
    selected_option = st.selectbox("Select an operation",(' ','Faculty in each Department','Faculty-doctorate','Faculty-Postgraduate','Faculty-appointment types','Faculty-designation types'))
    
    class EntireDataset:

        def __init__(self, df):
            self.df = df

        def fact_dep_plot(self):
            dept_counts=dts2.faculty_dept(self.df)
            sns.set_style('whitegrid')
            plt.figure(figsize=(12, 8))
            ax = sns.barplot(x='Department', y='Count', data=dept_counts, palette='bright', alpha=0.8)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
            plt.title('Number of Faculty in Each Department')
            plt.xlabel('Department')
            plt.ylabel('Number of Faculty')
            plt.tight_layout() 
            st.pyplot(plt)

        def faculty_doctorate_plot(self):
            doc_counts=dts2.faculty_doctorate(self.df)
            show_pie=st.checkbox("Piechart",False)
            show_bar=st.checkbox("Barchart",False)
            show_hist=st.checkbox("Histogram",False)
            if show_pie:
                sns.set_style('whitegrid')
                plt.figure(figsize=(1.7, 1.7))
                colors = sns.color_palette('bright')
                plt.pie(doc_counts['Count'], labels=doc_counts['Doctorate Degree'], autopct='%1.1f%%', startangle=90, colors=colors)
                plt.title('Doctorate degree-Faculty')
                plt.axis('equal')  # Ensure the pie is drawn as a circle
                st.pyplot(plt)
            if show_bar:
                st.subheader("Interactive Grouped Histogram - Distribution of Doctorate Professors")
                chart = alt.Chart(doc_counts).mark_bar().encode(
                x='Doctorate Degree:N',
                y='sum(Count):Q',
                color='Doctorate Degree:N',
                tooltip=['sum(Count):Q']
                ).properties(
                width=600,
                height=300
                )
                st.altair_chart(chart)
            if show_hist:
                sns.set_style('whitegrid')
                plt.figure(figsize=(3,3))
                sns.histplot(data=doc_counts, x='Doctorate Degree', weights='Count', kde=False, color='blue')
                plt.title('Distribution of Doctorate Professors')
                plt.xlabel('Doctorate')
                plt.ylabel('Count')
                plt.xticks(rotation=45, ha='center')
                st.pyplot(plt)

        def faculty_pg_plot(self):
            pg1_counts=dts2.faculty_pg(self.df)
            sns.set_style('whitegrid')
            plt.figure(figsize=(1.7, 1.7))
            colors = sns.color_palette('bright')
            plt.pie(pg1_counts['Count'], labels=pg1_counts['PG'], autopct='%1.1f%%', startangle=90, colors=colors)
            plt.title('Post Graduate-Faculty')
            plt.axis('equal')
            st.pyplot(plt)
        def faculty_app_plot(self):
            app_counts=dts2.faculty_app(self.df)
            sns.set_style('whitegrid')
            plt.figure(figsize=(3,3))
            sns.histplot(data=app_counts, x='Appointment Type', weights='Count', kde=False, color='blue')
            plt.title('Distribution of Appointment Types')
            plt.xlabel('Appointment Type')
            plt.ylabel('Count')
            plt.xticks(rotation=45, ha='center')
            st.pyplot(plt)

        def faculty_designation_plot(self):
            des_counts=dts2.faculty_designation(self.df)
            sns.set_style('whitegrid')
            plt.figure(figsize=(3,3))
            sns.histplot(data=des_counts, x='Designation', weights='Count', kde=False, color='green')
            plt.title('Distribution of Designations')
            plt.xlabel('Designation')
            plt.ylabel('Count')
            plt.xticks(rotation=45, ha='center') 
            st.pyplot(plt)

    class ComputerEngineering(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == "COMPUTER ENGINEERING"])        
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class Manufacturing(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MANUFACTURING SCIENCE AND ENGINEERING'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class ENTC(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'ELECTRONICS AND TELECOMMUNICATION'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class Metallurgy(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'METALLURGY AND MATERIAL TECHNOLOGY'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class Mechanical(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MECHANICAL ENGINEERING'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class Civil(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'CIVIL ENGINEERING'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class Instrumentation(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'INSTRUMENTATION AND CONTROL ENGINEERING'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class Electrical(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'ELECTRICAL ENGINEERING'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class EnggEducation(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'ENGINEERING EDUCATION'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class Planning(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'TOWN PLANNING'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class AppSci(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'APPLIED SCIENCE'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class Manage(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MANAGEMENT'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    class MBA(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MASTERS IN BUSINESS ADMINISTRATION'])
        def faculty_doctorate_plot(self):
            super().faculty_doctorate_plot()
        def faculty_pg_plot(self):
            super().faculty_pg_plot()
        def faculty_app_plot(self):
            super().faculty_app_plot()
        def faculty_designation_plot(self):
             super().faculty_designation_plot()

    
    entire2= EntireDataset(df1)
    comp_eng = ComputerEngineering(df1)
    manu = Manufacturing(df1)
    entc = ENTC(df1)
    meta = Metallurgy(df1)
    mech = Mechanical(df1)
    civil = Civil(df1)
    instru = Instrumentation(df1)
    elec = Electrical(df1)
    engg = EnggEducation(df1)
    plan = Planning(df1)
    appsci = AppSci(df1)
    manage = Manage(df1)
    mba = MBA(df1)


    if dept=='ENTIRE DATASET':
        if selected_option=='Faculty in each Department':
            entire2.fact_dep_plot()
        elif selected_option=='Faculty-doctorate':
            entire2.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            entire2.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            entire2.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            entire2.faculty_designation_plot()

    elif dept=='COMPUTER ENGINEERING':
        if selected_option=='Faculty-doctorate':
            comp_eng.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            comp_eng.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            comp_eng.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            comp_eng.faculty_designation_plot()

    elif dept=='MANUFACTURING SCIENCE AND ENGINEERING':
        if selected_option=='Faculty-doctorate':
            manu.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            manu.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            manu.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            manu.faculty_designation_plot()

    elif dept=='ELECTRONICS AND TELECOMMUNICATION':
        if selected_option=='Faculty-doctorate':
            entc.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            entc.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            entc.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            entc.faculty_designation_plot()

    elif dept== 'METALLURGY AND MATERIAL TECHNOLOGY':
        if selected_option=='Faculty-doctorate':
            meta.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            meta.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            meta.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            meta.faculty_designation_plot()

    elif dept=='MECHANICAL ENGINEERING':
        if selected_option=='Faculty-doctorate':
            mech.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            mech.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            mech.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            mech.faculty_designation_plot()

    elif dept=='CIVIL ENGINEERING':
        if selected_option=='Faculty-doctorate':
            civil.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            civil.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            civil.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            civil.faculty_designation_plot()

    elif dept== 'INSTRUMENTATION AND CONTROL ENGINEERING':
        if selected_option=='Faculty-doctorate':
            instru.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            instru.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            instru.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            instru.faculty_designation_plot()

    elif dept== 'ELECTRICAL ENGINEERING':
        if selected_option=='Faculty-doctorate':
            elec.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            elec.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            elec.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            elec.faculty_designation_plot()

    elif dept== 'ENGINEERING EDUCATION':
        if selected_option=='Faculty-doctorate':
            engg.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            engg.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            engg.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            engg.faculty_designation_plot()

    elif dept== 'TOWN PLANNING':
        if selected_option=='Faculty-doctorate':
            plan.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            plan.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            plan.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            plan.faculty_designation_plot()

    elif dept== 'APPLIED SCIENCE':
        if selected_option=='Faculty-doctorate':
            appsci.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            appsci.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            appsci.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            appsci.faculty_designation_plot()

    elif dept=='MANAGEMENT':
        if selected_option=='Faculty-doctorate':
            manage.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            manage.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            manage.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            manage.faculty_designation_plot()

    elif dept=='MASTERS IN BUSINESS ADMINISTRATION':
        if selected_option=='Faculty-doctorate':
            mba.faculty_doctorate_plot()
        elif selected_option=='Faculty-Postgraduate':
            mba.faculty_pg_plot()
        elif selected_option=='Faculty-appointment types':
            mba.faculty_app_plot()
        elif selected_option=='Faculty-designation types':
            mba.faculty_designation_plot()

    



    
    