import pandas as pd
FILE_NAME = 'scores.csv'

mean_score_dict = {}
class_gpa = 0
avg_class_gpa = 0

#read csv file
scores = pd.read_csv(FILE_NAME, delimiter=',',header=0, index_col=0)
print(scores)

#convert the dataframe to dictionary
df_csv_dict = scores.to_dict()

#calculate gpa and display the class gpa
for key,values in df_csv_dict.items():
    total_gpa = 0
    avg_gpa = 0
    for subject, marks in values.items():
        if marks >= 90:
            gpa = 4.0
        elif marks >= 80:
            gpa = 3.0
        elif marks >= 70:
            gpa = 2.0
        elif marks >= 60:
            gpa = 1.0
        else:
            gpa = 0.0
        total_gpa = total_gpa + gpa
    avg_gpa = total_gpa/len(values)
    print(f'{key:<20}  {avg_gpa:.2f}') 
    class_gpa = class_gpa + avg_gpa
    avg_class_gpa = class_gpa/len(df_csv_dict)

print(f'The Class GPA is {avg_class_gpa:.2f}')

