import streamlit as st
import pandas as pd
import entire_dataset as entire
import dataset2 as dts2

df1 = pd.read_csv("Faculty_data copy.csv")

st.sidebar.header("FACULTY DATA VISUALISATION")
option = st.sidebar.radio(" ",("Main page","Analytical data","Graphical data"))
st.sidebar.header("\n")
uploaded_file = st.sidebar.file_uploader("Select a CSV file to visualise data", accept_multiple_files=False,type = ".csv")
if uploaded_file:
    df1 = pd.read_csv(uploaded_file)
    st.sidebar.text("File uploaded,\ncontinue with the operations above.")
else:
    st.sidebar.text("Default file being used,\ncontinue with operations above.")
st.sidebar.header("\n")
st.sidebar.text("* All input data must be\nentered in bold letters.")


def convert_df(df):
    return df.to_csv().encode('utf-8')


if option == "Main page":
    st.title("FACULTY DATA VISUALISATION")
    st.text(" ")
    st.divider()
    st.markdown("**_You can either continue with visualization with the default dataset or upload your dataset in the sidebar_**")
    st.divider()
    st.text(" ")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(" ")
    with col2:
        csv1 = convert_df(df1)
        st.download_button(
            label="Download data as CSV",
            data=csv1,
            file_name="DATASET.csv",
            mime='text/csv',
            )
    with col3:
        st.text(" ")
    with st.expander("View the default dataset"):
        st.table(df1)




if option == "Analytical data":
    dept = st.selectbox("Select a department",(' ','ENTIRE DATASET', 'COMPUTER ENGINEERING','MANUFACTURING SCIENCE AND ENGINEERING',
                'ELECTRONICS AND TELECOMMUNICATION','METALLURGY AND MATERIAL TECHNOLOGY','MECHANICAL ENGINEERING',
                'CIVIL ENGINEERING','INSTRUMENTATION AND CONTROL ENGINEERING','ELECTRICAL ENGINEERING',
                'ENGINEERING EDUCATION', 'TOWN PLANNING','APPLIED SCIENCE',
                'MANAGEMENT','MASTERS IN BUSINESS ADMINISTRATION'))
    selected_option = st.selectbox("Select an operation",(' ','Faculty data','Retirement age','Gender count','Department wise gender count','Get email IDs','Search email by name','Count by year of joining'))
    
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
        def search_email_by_name(self):
            super().search_email_by_name()
        def count_by_year_of_joining(self):
            super().count_by_year_of_joining()

    class Manufacturing(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MANUFACTURING SCIENCE AND ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
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

    class ENTC(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'ELECTRONICS AND TELECOMMUNICATION'])
        def faculty_data(self):
            super().faculty_data()
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

    class Metallurgy(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'METALLURGY AND MATERIAL TECHNOLOGY'])
        def faculty_data(self):
            super().faculty_data()
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

    class Mechanical(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MECHANICAL ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
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

    class Civil(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'CIVIL ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
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

    class Instrumentation(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'INSTRUMENTATION AND CONTROL ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
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

    class Electrical(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'ELECTRICAL ENGINEERING'])
        def faculty_data(self):
            super().faculty_data()
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

    class EnggEducation(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'ENGINEERING EDUCATION'])
        def faculty_data(self):
            super().faculty_data()
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

    class Planning(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'TOWN PLANNING'])
        def faculty_data(self):
            super().faculty_data()
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

    class AppSci(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'APPLIED SCIENCE'])
        def faculty_data(self):
            super().faculty_data()
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

    class Manage(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MANAGEMENT'])
        def faculty_data(self):
            super().faculty_data()
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

    class MBA(EntireDataset):
        def __init__(self, df):
            super().__init__(df[df['Department'] == 'MASTERS IN BUSINESS ADMINISTRATION'])
        def faculty_data(self):
            super().faculty_data()
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
        elif selected_option == 'Department wise gender count':
            comp_eng.department_wise_gender_count()
        elif selected_option == 'Get email IDs':
            comp_eng.get_email_ids()
        elif selected_option == 'Search email by name':
            comp_eng.search_email_by_name()
        elif selected_option == 'Count by year of joining':
            comp_eng.count_by_year_of_joining()

    elif dept == 'MANUFACTURING SCIENCE AND ENGINEERING':
        if selected_option == 'Faculty data':
            manu.faculty_data()
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

    elif dept == 'ELECTRONICS AND TELECOMMUNICATION':
        if selected_option == 'Faculty data':
            entc.faculty_data()
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

    elif dept == 'METALLURGY AND MATERIAL TECHNOLOGY':
        if selected_option == 'Faculty data':
            meta.faculty_data()
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

    elif dept == 'MECHANICAL ENGINEERING':
        if selected_option == 'Faculty data':
            mech.faculty_data()
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

    elif dept == 'CIVIL ENGINEERING':
        if selected_option == 'Faculty data':
            civil.faculty_data()
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

    elif dept == 'INSTRUMENTATION AND CONTROL ENGINEERING':
        if selected_option == 'Faculty data':
            instru.faculty_data()
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

    elif dept == 'ELECTRICAL ENGINEERING':
        if selected_option == 'Faculty data':
            elec.faculty_data()
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

    elif dept == 'ENGINEERING EDUCATION':
        if selected_option == 'Faculty data':
            engg.faculty_data()
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

    elif dept == 'TOWN PLANNING':
        if selected_option == 'Faculty data':
            plan.faculty_data()
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

    elif dept == 'APPLIED SCIENCE':
        if selected_option == 'Faculty data':
            appsci.faculty_data()
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

    elif dept == 'MANAGEMENT':
        if selected_option == 'Faculty data':
            manage.faculty_data()
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

    elif dept == 'MASTERS IN BUSINESS ADMINISTRATION':
        if selected_option == 'Faculty data':
            mba.faculty_data()
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
    
    

    
    

