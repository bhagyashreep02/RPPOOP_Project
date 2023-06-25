import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dataset2 as dts
import entire_dataset as entire
import streamlit as st
df = pd.read_csv("Faculty_data copy.csv")

def faculty_dep_plot(df):
    dept_counts=dts.faculty_dept(df)
    sns.set_style('whitegrid')
    plt.figure(figsize=(12, 8))

# Create the bar plot using seaborn's barplot()
    ax = sns.barplot(x='Department', y='Count', data=dept_counts, palette='bright', alpha=0.8)

# Rotate the x-axis labels
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    plt.title('Number of Faculty in Each Department')
    plt.xlabel('Department')
    plt.ylabel('Number of Faculty')

    plt.tight_layout() 

    st.pyplot()

faculty_dep_plot()

def faculty_doctorate_plot(df):
    doc_counts=dts.faculty_doctorate(df)
    sns.set_style('whitegrid')
    plt.figure(figsize=(4, 4))

    colors = sns.color_palette('bright')
    plt.pie(doc_counts['Count'], labels=doc_counts['Doctorate Degree'], autopct='%1.1f%%', startangle=90, colors=colors)

    plt.title('Doctorate degree-Faculty')

    plt.axis('equal')  # Ensure the pie is drawn as a circle
    plt.savefig('plot2.png')
    st.pyplot()

def faculty_pg_plot(df):
    pg_counts=dts.faculty_pg(df)
    sns.set_style('whitegrid')
    plt.figure(figsize=(4, 4))
    colors = sns.color_palette('bright')
    plt.pie(pg_counts['Count'], labels=pg_counts['PG'], autopct='%1.1f%%', startangle=90, colors=colors)

    plt.title('Post Graduate-Faculty')

    plt.axis('equal')  
    st.pyplot()

def faculty_app_plot(df):
    app_counts=dts.faculty_app(df)
    sns.set_style('whitegrid')
    plt.figure(figsize=(4, 4))

    sns.histplot(data=app_counts, x='Appointment Type', weights='Count', kde=False, color='blue')

    plt.title('Distribution of Appointment Types')
    plt.xlabel('Appointment Type')
    plt.ylabel('Count')

    plt.xticks(rotation=45)

    st.pyplot()

def faculty_designation_plot(df):
    des_counts=dts.faculty_designation(df)
    sns.set_style('whitegrid')
    plt.figure(figsize=(4, 4))

    sns.histplot(data=des_counts, x='Designation', weights='Count', kde=False, color='green')

    plt.title('Distribution of Designations')
    plt.xlabel('Designation')
    plt.ylabel('Count')

    plt.xticks(rotation=45)

    st.pyplot()

    