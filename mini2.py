import random 

# Open the csv file and put the data in a list in order
students = []
with open('records.csv','r') as file:
    counter = 0
    for line in file:
        line = line.rstrip('\n')
        lst = line.split(',')
        
        if counter == 0:  # Header row
            headers = lst
        else:
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

for i, student in enumerate(students):  # Show first 3 students
    print(f"Student {i+1}: {student}")
exit()

# Count total males and females
male = 0 
female = 0 
for student in students:
    gender_lower = student['gender'].lower()
    if gender_lower in ['m','male']:
        male += 1
    elif gender_lower in ['f', 'female']:
        female += 1

# Determine optimal gender ratio
if male > female:
    target_males_per_group = 3
    target_females_per_group = 2
else:
    target_males_per_group = 2
    target_females_per_group = 3

# Sort students by GPA and split into 5 bands
students_sorted = sorted(students, key=lambda x: x["gpa"], reverse=True)
bands = [students_sorted[i:i+10] for i in range(0, 50, 10)]

# Print GPA bands information
print("GPA Bands Distribution:")
for i, band in enumerate(bands, 1):
    band_gpas = [student['gpa'] for student in band]
    print(f"Band {i}: {min(band_gpas):.2f} - {max(band_gpas):.2f} GPA ({len(band)} students)")
print()

# Separate each band into males and females
band_males = []
band_females = []
for band in bands:
    males_in_band = []
    females_in_band = []
    for student in band:
        gender_lower = student['gender'].lower()
        if gender_lower in ['m','male']:
            males_in_band.append(student)
        elif gender_lower in ['f', 'female']:
            females_in_band.append(student)
    random.shuffle(males_in_band)
    random.shuffle(females_in_band)
    band_males.append(males_in_band)
    band_females.append(females_in_band)

num_groups = 10
groups = [[] for _ in range(num_groups)]
#For every num_groups that we are forming, we would initialise a 0
male_count = [0] * num_groups
female_count = [0] * num_groups

# Distribute students with gender optimization - one from each band
# Looking at each group one by one and analysing through each band, 
# 
for group_idx in range(num_groups):
    for band_idx in range(len(bands)):
         # Calculate how "full" the group is for boys and girls
        current_male_ratio = male_count[group_idx] / target_males_per_group
        current_female_ratio = female_count[group_idx] / target_females_per_group
        
        # Decision time: who to add next?
        if current_male_ratio < current_female_ratio and band_males[band_idx]:
            # If group needs more boys AND there are boys available in this band
            student = band_males[band_idx].pop(0)    # Take first boy from band
            groups[group_idx].append(student)        # Add to group
            male_count[group_idx] += 1               # Update boy counter
            
        elif band_females[band_idx]:
            # If girls are available in this band
            student = band_females[band_idx].pop(0)  # Take first girl from band
            groups[group_idx].append(student)        # Add to group
            female_count[group_idx] += 1             # Update girl counter
            
        elif band_males[band_idx]:
            # If boys are available in this band
            student = band_males[band_idx].pop(0)    # Take first boy from band
            groups[group_idx].append(student)        # Add to group
            male_count[group_idx] += 1               # Update boy counter

for i, g in enumerate(groups, 1):        # Look at each finished group
    males_in_group = 0                   # Reset counters for this group
    females_in_group = 0
    total_gpa = 0

    print(f"Group {i}:")                 # Print group header
    
    for student in g:                    # Look at each student in the group
        # Figure out which GPA band this student came from
        band_number = None
        for band_idx, band in enumerate(bands):
            if student in band:          # Check if student is in this band
                band_number = band_idx + 1
                print (band_number)
                exit()
                break
        
        # Count boys and girls
        if student['gender'].lower() in ['m','male']:
            males_in_group += 1
        else:
            females_in_group += 1
            
        total_gpa += student['gpa']      # Add to GPA total
        
        # Print student details
        print(f"  {student['name']} | {student['school']} | {student['gender']} | GPA: {student['gpa']:.2f} | Band: {band_number}")
    
    # Calculate and print group summary
    avg_gpa = total_gpa / len(g)
    print(f"  Summary: {males_in_group} males, {females_in_group} females, Average GPA: {avg_gpa:.2f}")
    print()


#School optimisation
#1. counter for number of unique schools 
#2. function to swap the students within each group
#3  set max times to swap the students within the group

