uploaded_file = "Faculty_data copy.csv"
import pandas as pd
df = pd.read_csv("Faculty_data copy.csv")

def age_to_retirement(df):
    age = list(df['Current Age'])
    names = list(df['First Name'])
    lastname = list(df['Last Name'])
    n=len(age)
    years = []
    accept = []
    accept1 = []

    for i in age:
        retire = 60 - i
        if retire>=0:
            years.append(int(retire))

    for i in range(0,n):
        if age[i]<61:
            accept.append(names[i])
            accept1.append(lastname[i])
    
    final = {'FIRST NAME':accept,'LAST NAME':accept1,'AGE TO RETIREMENT':years}

    return final

def get_details(df,name1):
    firstname = list(df['First Name'])
    lastname = list(df['Last Name'])

    name2 = name1.split(" ")

    for i in range(len(firstname)):
        if firstname[i] == name2[0] and lastname[i] == name2[1]:
            df1 = df.loc[(df['First Name'] == name2[0]) & (df['Last Name'] == name2[1])]
            return df1.transpose()



def count_Gender_whole(df):
    gend = df['Gender'].value_counts()
    gend_overall = pd.DataFrame(gend).reset_index()
    gend_overall = gend_overall.rename(columns={'index': 'Gender', 'Gender': 'Count'})
    return gend_overall



def count_Gender_Department(df):
    gender_count = df.groupby(['Department', 'Gender']).size().reset_index(name='Count')
    return gender_count


def find_email(df):
    name = list(df['First Name'])
    email = list(df['Email Address'])
    final = {'NAME':name,'EMAIL ADDRESS':email}

    return final


def email(df,name1):
    firstname = list(df['First Name'])
    lastname = list(df['Last Name'])
    email = list(df['Email Address'])

    name2 = name1.split(" ")

    for i in range(len(firstname)):
        if firstname[i] == name2[0] and lastname[i] == name2[1]:
            return email[i]


def date_of_joining(df):
    date = list(df['Date of Joining'])
    count2000 = 0
    count = 0

    for i in date:
        date1 = i.split("/")
        if int(date1[2])>=2000:
            count2000 += 1
        else:
            count += 1

    return count,count2000

def faculty_data(df):
    name = list(df['First Name'])
    lstname = list(df['Last Name'])
    title = list(df['Title'])
    final = {'TITLE':title,'NAME':name,'LAST NAME':lstname}

    return final