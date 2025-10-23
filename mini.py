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

#Calculate the GPA band in one tutorial group and arrange gpa in ascending order
gpas = [student['gpa'] for student in students]
min_gpa = min(gpas)
max_gpa = max(gpas)
band_width = (max_gpa - min_gpa) / 5
students.sort(key=lambda x:x['gpa'])
band1 = []
band2 = []
band3 = []
band4 = []
band5 = []
for i in range(0,50):
    if i<10:
        band1.append(students[i])
    if i>10 and i<20:
        band2.append(students[i])
    if i>20 and i<30:
        band3.append(students[i])
    if i>30 and i<40:
        band4.append(students[i])
    if i>40 and i<50:
        band5.append(students[i])
print(band1)
print(band2)
exit()


gpa_ls.sort()
print(gpa_ls)


# sorted__by_value = sorted(students.items(), key=lambda, item: item[1])
# sorted_gpa_by_value = dict(sorted_students_by_value)
# print(sorted__by_value)
# # Output: {'orange': 1, 'banana': 2, 'apple': 3}


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
