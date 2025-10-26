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
                'tutorial group': lst[0],
                'id': lst[1],
                'school': lst[2],
                'name': lst[3],
                'gender': lst[4],
                'gpa': float(lst[5])
            }
            students.append(student)
            
        counter += 1
        if counter > 50:
            break 

#Calculate the GPA band in one tutorial group and arrange gpa in ascending order
#
gpas = [student['gpa'] for student in students]
min_gpa = min(gpas)
max_gpa = max(gpas)
band_width = (max_gpa - min_gpa) / 5
students.sort(key=lambda x:x['gpa'])


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
                'tutorial group': lst[0],
                'id': lst[1],
                'school': lst[2],
                'name': lst[3],
                'gender': lst[4],
                'gpa': float(lst[5])
            }
            students.append(student)
            
        counter += 1
        if counter > 50:
            break 

#Calculate the GPA band in one tutorial group and arrange gpa in ascending order
#
gpas = [student['gpa'] for student in students]
min_gpa = min(gpas)
max_gpa = max(gpas)
band_width = (max_gpa - min_gpa) / 5
students.sort(key=lambda x:x['gpa'])

#Split the students grade into 5 bands. Initialising each band to be a list of students in a band. Save the sorted dictionary of students in a
#different band based on the different gpa

''' Thinking process:
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
'''


#Simplification:

students_sorted = sorted(students, key=lambda x: x["gpa"], reverse=True)
bands = [students_sorted[i:i+10]for i in range(0, 50, 10)]
band1, band2, band3, band4, band5 = bands

#Within each band, we should select one student from each band randomly. (We avoid choosing in order to prevent putting the underperforming student together with the 
#student that is not as outstanding in band 4)

for band in bands:
    random.shuffle(band)

num_groups = 10
#Creating a list 10 times
group = [[] for _ in range(num_groups)]


for band in bands:
    for i in range(num_groups):
        if band:  # Check if band still has students
            group[i].append(band.pop()) #The group should add students into the group, and remove the student from the band list.


# Print results with CORRECT field mapping
for i, g in enumerate(group, 1):
    print(f"Group {i}:")
    for student in g:
        print(f"  - Name: {student['name']}, ID: {student['id']}, Gender: {student['gender']}, School: {student['school']}, GPA: {student['gpa']}")
    print()

male = 0 
female = 0 

for student in students:
    gender_lower = student['gender'].lower() #Remove any capitalisation from the title
    if gender_lower in ['m','male']:
        male += 1
    elif gender_lower in ['f', 'female']:
        female += 1
print(male)
print(female)
exit()

# sorted__by_value = sorted(students.items(), key=lambda, item: item[1])
# sorted_gpa_by_value = dict(sorted_students_by_value)
# print(sorted__by_value)
# # Output: {'orange': 1, 'banana': 2, 'apple': 3}
#Split the students grade into 5 bands. Initialising each band to be a list of students in a band. Save the sorted dictionary of students in a
#different band based on the different gpa

''' Thinking process:
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
'''


#Simplification:

students_sorted = sorted(students, key=lambda x: x["gpa"], reverse=True)
bands = [students_sorted[i:i+10]for i in range(0, 50, 10)]
band1, band2, band3, band4, band5 = bands

#Within each band, we should select one student from each band randomly. (We avoid choosing in order to prevent putting the underperforming student together with the 
#student that is not as outstanding in band 4)

for band in bands:
    random.shuffle(band)

num_groups = 10
#Creating a list 10 times
group = [[] for _ in range(num_groups)]


for band in bands:
    for i in range(num_groups):
        if band:  # Check if band still has students
            group[i].append(band.pop()) #The group should add students into the group, and remove the student from the band list.


# Print results with CORRECT field mapping
for i, g in enumerate(group, 1):
    print(f"Group {i}:")
    for student in g:
        print(f"  - Name: {student['name']}, ID: {student['id']}, Gender: {student['gender']}, School: {student['school']}, GPA: {student['gpa']}")
    print()



# sorted__by_value = sorted(students.items(), key=lambda, item: item[1])
# sorted_gpa_by_value = dict(sorted_students_by_value)
# print(sorted__by_value)
# # Output: {'orange': 1, 'banana': 2, 'apple': 3}


''' Band width concept
    # Calculate band without math.floor
    band = int((gpa - min_gpa) / band_width)

    # Ensure band is between 0 and 4
    if band >= 5:
        band = 4
    
    student['band']=band
    print(student)


print(min_gpa)
print(max_gpa)
print(band_width)"
'''
