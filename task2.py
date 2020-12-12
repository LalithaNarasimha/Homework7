import pandas as pd
FILE_NAME = 'scores.csv'

st_grades = ''
st_gpa = 0.0

def get_student_grades(p_score):
#calculate gpa based on score
    if p_score >= 90:
        st_grades = 'A'
        st_gpa = 4.0
    elif p_score >= 80:
        st_grades = 'B'
        st_gpa = 3.0
    elif p_score >= 70:
        st_grades = 'C'
        st_gpa = 2.0
    elif p_score >= 60:
        st_grades = 'D'
        st_gpa = 1.0
    elif p_score < 60:
        st_grades = 'F'
        st_gpa = 0.0
    return st_gpa

#read csv file
df_scores = pd.read_csv(FILE_NAME, delimiter=',',header=0, index_col=0)
print(df_scores)

#create dataframe to convert the marks into gpa
df_student_gpa = df_scores.applymap(get_student_grades)
print(df_student_gpa)

#set precision to 2 decimal
pd.set_option('precision', 2)

#calculate individual gpa
student_mean = df_student_gpa.mean(axis = 0)
print(student_mean)

#calculate and display class gpa
student_mean = student_mean.transpose()
class_gpa = student_mean.mean()
print(f'The class GPA is {class_gpa:.2f}')



