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
def convert_df(df):
    return df.to_csv().encode('utf-8')

if option == "Analytical data":
    uploaded_file = st.file_uploader("Select a CSV file to visualise data", accept_multiple_files=False,type = ".csv")
    if uploaded_file:
        df1 = pd.read_csv(uploaded_file)
        st.text("File uploaded, continue in the sidebar")

    dept = st.selectbox("Select a department",(' ','ENTIRE DATASET', 'COMPUTER ENGINEERING','MANUFACTURING SCIENCE AND ENGINEERING',
                'ELECTRONICS AND TELECOMMUNICATION','METALLURGY AND MATERIAL TECHNOLOGY','MECHANICAL ENGINEERING',
                'CIVIL ENGINEERING','INSTRUMENTATION AND CONTROL ENGINEERING','ELECTRICAL ENGINEERING',
                'ENGINEERING EDUCATION', 'TOWN PLANNING','APPLIED CHEMISTRY','APPLIED MATHEMATICS',
                'MANAGEMENT','MASTERS IN BUSINESS ADMINISTRATION'))
    selected_option = st.selectbox("Select an operation",(' ','Faculty data','Retirement age','Gender count','Department wise gender count','Get email id\'s','Search email by name','Count by year of joining'))
    if dept == 'ENTIRE DATASET':
        df = pd.read_csv("Faculty_data copy.csv")
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='Faculty_data.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
        
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='Retirement_age.csv',
            mime='text/csv',
            )

            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='Department_wise_gender.csv',
            mime='text/csv',
            )

            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='Email_id.csv',
            mime='text/csv',
            )

            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)

    elif dept == 'COMPUTER ENGINEERING':
        df = df1[df1['Department'] == "COMPUTER ENGINEERING"]
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='comp_Faculty_data.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
        
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='comp_Retirement_age.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='comp_Department_wise_gender.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='comp_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)


    elif dept == 'MANUFACTURING SCIENCE AND ENGINEERING':
        df = df1[df1['Department'] == 'MANUFACTURING SCIENCE AND ENGINEERING']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='manufacturing_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='manufacturing_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='manufacturing_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='manufacturing_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)

    
    elif dept == 'ELECTRONICS AND TELECOMMUNICATION':
        df = df1[df1['Department'] == 'ELECTRONICS AND TELECOMMUNICATION']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='entc_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='entc_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='entc_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='entc_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)


    elif dept == 'METALLURGY AND MATERIAL TECHNOLOGY':
        df = df1[df1['Department'] == 'METALLURGY AND MATERIAL TECHNOLOGY']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='metallurgy_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='metallurgy_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='metallurgy_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='metallurgy_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)

    
    elif dept == 'MECHANICAL ENGINEERING':
        df = df1[df1['Department'] == 'MECHANICAL ENGINEERING']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='mechanical_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='mechanical_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='mechanical_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='mechanical_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)


    elif dept == 'CIVIL ENGINEERING':
        df = df1[df1['Department'] == 'CIVIL ENGINEERING']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='civil_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='civil_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='civil_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='civil_Email_id.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)


    elif dept == 'INSTRUMENTATION AND CONTROL ENGINEERING':
        df = df1[df1['Department'] == 'INSTRUMENTATION AND CONTROL ENGINEERING']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='instrumentation_Faculty_data.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='instrumentation_Retirement_age.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='instrumentation_Department_wise_gender.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='instrumentation_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)

    elif dept == 'ELECTRICAL ENGINEERING':
        df = df1[df1['Department'] == 'ELECTRICAL ENGINEERING']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='electrical_Faculty_data.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='electrical_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='electrical_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='electrical_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)

        
    elif dept == 'ENGINEERING EDUCATION':
        df = df1[df1['Department'] == 'ENGINEERING EDUCATION']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='engg_education_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='engg_education_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='engg_education_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='engg_education_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)


    elif dept == 'TOWN PLANNING':
        df = df1[df1['Department'] == 'TOWN PLANNING']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='planning_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='planning_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='planning_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='planning_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)

    
    elif dept == 'APPLIED CHEMISTRY':
        df = df1[df1['Department'] == 'APPLIED CHEMISTRY']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='appscience_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='appscience_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='appscience_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='appscience_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)


    elif dept == 'APPLIED MATHEMATICS':
        df = df1[df1['Department'] == 'APPLIED MATHEMATICS']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='appmath_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='appmath_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='appmath_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='appmath_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)


    elif dept == 'MANAGEMENT':
        df = df1[df1['Department'] == 'MANAGEMENT']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='management_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='management_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='management_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='management_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)


    elif dept == 'MASTERS IN BUSINESS ADMINISTRATION':
        df = df1[df1['Department'] == 'MASTERS IN BUSINESS ADMINISTRATION']
        if selected_option == 'Faculty data':
            data = entire.faculty_data(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='MBA_Faculty_data\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Retirement age":
            data = entire.age_to_retirement(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='MBA_Retirement_age\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Gender count":
            data = entire.count_Gender_whole(df)
            st.text(data)
        elif selected_option == "Department wise gender count":
            data = entire.count_Gender_Department(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='MBA_Department_wise_gender\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Get email id\'s":
            data = entire.find_email(df)
            dframe = pd.DataFrame(data)
            st.text("\n")
            st.markdown('**_Download a file with the following data_**')
            csv1 = convert_df(dframe)
            st.download_button(
            label="Download data as CSV",
            data = csv1,
            file_name='MBA_Email_id\'s.csv',
            mime='text/csv',
            )
            st.text("\n")
            st.table(data)
            
        elif selected_option == "Search email by name":
            title = st.text_input('Enter Name')
            data = entire.email(df,title)
            st.subheader(data)
        elif selected_option == 'Count by year of joining':
            data = entire.date_of_joining(df)
            data1 = {"Joined on or after 2000":data[1],"Joined before 2000":data[0]}
            st.table(data1)