import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np



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



fig, ax = plt.subplots()
ax.scatter(df['Exam_Score'], df['Hours_Studied'])

st.header("Анализ данных")

st.subheader("Hours studied/Часы изучения")
st.pyplot(fig)
st.write("С большой уверенностью можно сказать, что данный признак будет очень важен для предскзания итогового результата")


st.subheader("Attendance/Посещаемость")
fig, ax = plt.subplots()
ax.scatter(df['Exam_Score'], df['Attendance'])
st.pyplot(fig)
st.write("Данный признак также будет иметь ключевое значение для итогового результата")



st.subheader("Previous Scores/Предыдущий результат")
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots()
ax.scatter(df['Exam_Score'], df['Previous_Scores'])
st.pyplot(fig)
st.write("На графике видно не сильную корреляцию, которая также будет влиять на результат")



st.subheader("Tutoring sessions/Занятия с репетитором")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Tutoring_Sessions", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
fig = plt.gcf()
st.pyplot(fig)
st.write("Видно что чем больше занятий с репетитором тем больше среднее значение увеличивается, но на большие баллы получают меньше")



st.subheader("Parental Involvement/Влияние родителей")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Parental_Involvement", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("Данный признак будет нести значение для резульатат")



st.subheader("Sleep Hours/Часы сна")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Sleep_Hours", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("По графику видно что лучше всего спать 6-8 часов")

st.subheader("Access to Resources/Доступ к ресурсам")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Access_to_Resources", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax

)
st.pyplot(fig)
st.write("Если у человека нет доступов к ресурсам, то он не сдаст выше 80 баллов")

 

st.subheader("Extracurricular Activities/Внеклассные мероприятия")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Extracurricular_Activities", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("Данный признак не влияет на итоговый результат")

st.subheader("Motivation Level/Уровень мотивации")
fig, ax = plt.subplots()

sns.boxenplot(
    df, x="Motivation_Level", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("Этот признак также не будет нести особой разниницы")

st.subheader("Internet Access/Доступ к интернету")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Internet_Access", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("Доступ к интернету очень сильно влият на результат экзамена, без интернета сдать больше 70 смогли лишь единицы")

st.subheader("Family Income/Семейный доход")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Family_Income", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("Есть не большая коррелляция, но незначительная для результата")

st.subheader("Teacher Quality/Квалифицированность учителя")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Teacher_Quality", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("На графике видно с очень сильным учителем выше средний балл, но на высоких баллах лучше средний учитель. Видимо для хорошего резульата нужно готовится больше самому и не надеется на квалификацию учителя")

st.subheader("School Type/Тип школы")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="School_Type", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("В обычной школе результаты лучше чем в часной, наверное это связано с тем что те кто ходит в частную школу не особо заботяся о экзаменах так как у них уже все есть")

st.subheader("Peer Influence/Влияние сверстников")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Peer_Influence", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("Если влияние сверстником плохое, то это сильно скажется на результате, но в остальном особой разницы не будет")

st.subheader("Physical Activity/Физическая активность")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Physical_Activity", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("У тех кто вообще не занимается или занимается избыточно результат будет определенно хуже, чем у тех кто уделяетс спроту 3-4 часа в неделю")

st.subheader("Learning Disabilities/Нарушения обучаемости")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Learning_Disabilities", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("На средних баллах особой разницы нет, но уже на более высокие сдавали лишь те у кого не было никаких нарушений в обучении")

st.subheader("Parental_Education_Level/Уровень родительского образования")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Parental_Education_Level", y="Exam_Score",
    color="b", width_method="linear", 
    ax = ax
)
st.pyplot(fig)
st.write("Данный признак будет влиять на итоговый результат, но он не будет основным")

st.subheader("Distance from Home/Дистанция до дома")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Distance_from_Home", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("На графике видно что после 80 баллов начинается прямая корреляция, чем ближе человек живет тем больше сдаст. Но на средних баллах никакой разницы нет")

st.subheader("Gender/Гендер")
fig, ax = plt.subplots()
sns.boxenplot(
    df, x="Gender", y="Exam_Score",
    color="b", width_method="linear",
    ax = ax
)
st.pyplot(fig)
st.write("Гендер не особо влияет на результат, но по графику видно, что на более высокие баллы обчно пишут девочки")


sns.heatmap(df.corr())

st.pyplot(plt)
st.write("На графике видно как сильно влияет каждый из признаков на результат. Например количество часов и посещаемость являются главными признаками, так как на графике они самые яркие, еще несколько признаков влияют по слабее, а остальные и вовсе не нужны.")
