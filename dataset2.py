import pandas as pd
df = pd.read_csv("Faculty_data copy.csv")

def faculty_dept(df):
    dept_counts=df.groupby('Department')['Last Name'].count().reset_index()
    dept_counts = dept_counts.rename(columns={'Last Name': 'Count'})
    return dept_counts

def faculty_doctorate(df):
    doc_counts=df.groupby('Doctorate Degree')['Last Name'].count().reset_index()
    doc_counts = doc_counts.rename(columns={'Last Name': 'Count'})
    return doc_counts

def faculty_pg(df):
    pg_counts=df.groupby('PG')['Last Name'].count().reset_index()
    pg_counts = pg_counts.rename(columns={'Last Name': 'Count'})
    return pg_counts

def faculty_app(df):
    app_counts=df.groupby('Appointment Type')['Last Name'].count().reset_index()
    app_counts = app_counts.rename(columns={'Last Name': 'Count'})
    return app_counts

def faculty_designation(df):
    des_counts=df.groupby('Designation')['Last Name'].count().reset_index()
    des_counts = des_counts.rename(columns={'Last Name': 'Count'})
    return des_counts