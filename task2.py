import pandas as pd
FILE_NAME = 'scores.csv'

def get_grade_gpa(score):
    # calculate the gpa for each student 
    GPA = [
        (90, 4.00),
        (80, 3.00),
        (70, 2.00),
        (60, 1.00),
        (00, 0.00)]

    return [point for key, point in GPA if score >= key][0]
  
scores = pd.read_csv(FILE_NAME, delimiter=',',header=0, index_col=0)
print(scores)

#Convert the marks to gpa
grade_points = scores.applymap(get_grade_gpa)
print(grade_points)

#calculate the mean of each student
mean_gpa = grade_points.mean()
print(mean_gpa)

#display the class GPA
mean_gpa = mean_gpa.transpose()
mean_gpa = mean_gpa.mean()
print(f'The clas GPA is {mean_gpa:.2f} ')
