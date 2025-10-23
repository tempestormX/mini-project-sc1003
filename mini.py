import random 

#Open the csv file and put the data in a list in order
students = []
with open('records.csv','r') as file:
    counter = 0
    gpa_list = []
    for line in file:
        line=line.rstrip('\n')
        lst=line.split(',')
        print(lst)

        if counter == 0:  # Header row
            headers = lst
            print("Headers:", headers)
        else:
            # Create student dictionary
            student = {
                'id': lst[0],
                'name': lst[1],
                'gender': lst[2],
                'school': lst[3],
                'major': lst[4],
                'gpa': float(lst[5])
            }
            students.append(student)
            
        counter += 1
        if counter > 50:
            break 

#Calculate the GPA band in one tutorial group
gpas = [student['gpa'] for student in students]
min_gpa = min(gpas)
max_gpa = max(gpas)
band_width = (max_gpa - min_gpa) / 5
print(band_width)



#Arranging gpa in ascending order
gpa_ls = []
for student in students:
    gpa = student['gpa']
    gpa_ls.append(gpa)

    
gpa_ls.sort()

print(gpa_ls)
exit()


'''
    # Calculate band without math.floor
    band = int((gpa - min_gpa) / band_width)

    # Ensure band is between 0 and 4
    if band >= 5:
        band = 4
    
    student['band']=band
    print(student)





'''
'''
print(min_gpa)
print(max_gpa)
print(band_width)"



#Assign band to student
for student in students:
    gpa = student['gpa']
    # Calculate band without math.floor
    band = int((gpa - min_gpa) / band_width)

    # Ensure band is between 0 and 4
    if band >= 5:
        band = 4
    
    student['band']=band
    print(student)



'''
'''
def random_student_classifier(students):
    shuffled_students = students.copy()  # Create a copy to avoid modifying original
    random.shuffle(shuffled_students)
    return shuffled_students

def select_five(students):
    shuffled = random_student_classifier(students)
    selected_five = shuffled[:5]  # Get first 5 students
    for i in selected_ten:
        print(i)
    print(selected_five)
    return selected_five

# Usage
select_five(students)
'''
