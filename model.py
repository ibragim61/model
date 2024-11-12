import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import ElasticNet
import numpy as np
import seaborn as sns

file = open('best_elastic_net', 'rb')
model = pickle.load(file)


df = pd.read_csv('StudentPerformanceFactors.csv')


df['Parental_Involvement'].replace({'Low': 1, 'Medium': 2, 'High': 3}, inplace=True)
df['Access_to_Resources'].replace({'Low': 1, 'Medium': 2, 'High': 3}, inplace=True)
df['Extracurricular_Activities'].replace({'No': 0, 'Yes': 1}, inplace=True)
df['Motivation_Level'].replace({'Low': 1, 'Medium': 2, 'High': 3}, inplace=True)
df['Internet_Access'].replace({'No': 0, 'Yes': 1}, inplace=True)
df['Family_Income'].replace({'Low': 1, 'Medium': 2, 'High': 3}, inplace=True)
df['Teacher_Quality'].replace({'Low': 1, 'Medium': 2, 'High': 3}, inplace=True)
df['School_Type'].replace({'Public': 0, 'Private': 1}, inplace=True)
df['Peer_Influence'].replace({'Negative': 1, 'Neutral': 2, 'Positive': 3}, inplace=True)
df['Learning_Disabilities'].replace({'No': 0, 'Yes': 1}, inplace=True)
df['Parental_Education_Level'].replace({'High School': 1, 'College': 2, 'Postgraduate': 3}, inplace=True)
df['Distance_from_Home'].replace({'Near': 1, 'Moderate': 2, 'Far': 3}, inplace=True)
df['Gender'].replace({'Male': 0, 'Female': 1}, inplace=True)


df['Teacher_Quality'] = df['Teacher_Quality'].fillna(df['Teacher_Quality'].mode().values[0])
df['Parental_Education_Level'] = df['Parental_Education_Level'].fillna(df['Parental_Education_Level'].mode().values[0])
df['Distance_from_Home'] = df['Distance_from_Home'].fillna(df['Distance_from_Home'].mode().values[0])

st.title("Приложение для предсказания")


columns = df.columns.tolist()
columns.remove('Exam_Score')


column_ = {
    'Hours_Studied': 'col1',
    'Attendance': 'col1',
    'Parental_Involvement': 'col1',
    'Access_to_Resources': 'col1',
    'Extracurricular_Activities': 'col2',
    'Sleep_Hours': 'col3',
    'Previous_Scores': 'col1',
    'Motivation_Level': 'col2',
    'Internet_Access': 'col3',
    'Tutoring_Sessions': 'col1',
    'Family_Income': 'col2',
    'Teacher_Quality': 'col3',
    'School_Type': 'col2',
    'Peer_Influence': 'col3',
    'Physical_Activity': 'col2',
    'Learning_Disabilities': 'col3',
    'Parental_Education_Level': 'col2',
    'Distance_from_Home': 'col3',
    'Gender': 'col2',
}

cont1 = st.container(border=True)
cont2 = st.container(border=True)

col1, col2, col3 = st.columns(3)


with col1:
    st.subheader("Важные")
with col2:
    st.subheader("Неважные")
with col3:
    st.subheader(" ")

    

input_data = {}


for column in columns:
    min_value = df[column].min()
    max_value = df[column].max()
    

    if column_[column] == 'col1':
        input_data[column] = col1.slider(column, min_value, max_value, value=(min_value + max_value) // 2)
    elif column_[column] == 'col2':
        input_data[column] = col2.slider(column, min_value, max_value, value=(min_value + max_value) // 2)
    else:
        input_data[column] = col3.slider(column, min_value, max_value, value=(min_value + max_value) // 2)


input_df = pd.DataFrame([input_data])





prediction = model.predict(input_df)






prediction_text = f'<h1 style="text-align: center; color: rgb(255, 75, 75);">{int(prediction[0])}</h1>'


st.markdown(prediction_text, unsafe_allow_html=True)
