"""mini.py - form student groups from records.csv

This cleaned version fixes syntax errors, uses csv parsing, and includes
robust handling for missing/short files. It forms groups from the file
in batches of 50 students until all students are processed.
"""

import csv
import itertools
import os
import random
import sys


def read_students(start_index=0, count=50, filepath="records.csv"):
    """Read up to count students starting from start_index (after header).
    Returns a list of student dicts with keys: tutorial group, id, school, name, gender, gpa
    """
    students = []
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} not found")

    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader, None)  # skip header if present

        # skip start_index rows
        for _ in range(start_index):
            try:
                next(reader)
            except StopIteration:
                return students

        for _ in range(count):
            try:
                row = next(reader)
            except StopIteration:
                break
            if len(row) < 6:
                # skip malformed line
                continue
            try:
                gpa = float(row[5])
            except Exception:
                # skip rows with non-numeric GPA
                continue

            student = {
                'tutorial group': row[0].strip(),
                'id': row[1].strip(),
                'school': row[2].strip(),
                'name': row[3].strip(),
                'gender': row[4].strip(),
                'gpa': gpa,
            }
            students.append(student)

    return students


def count_total_students(filepath="records.csv"):
    """Count total number of student records (excluding header)."""
    if not os.path.exists(filepath):
        return 0
        
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader, None)  # skip header
        return sum(1 for row in reader)


def form_groups(students, num_groups=10):
    """Form groups from a list of student dicts.
    Returns list of groups (each group is a list of students).
    """
    if not students:
        return []

    students_sorted = sorted(students, key=lambda x: x['gpa'], reverse=True)

    # split into up to 5 bands as evenly as possible
    n = len(students_sorted)
    band_size = max(1, n // 5)
    bands = [students_sorted[i:i + band_size] for i in range(0, n, band_size)]

    # split each band by gender
    band_males = []
    band_females = []
    for band in bands:
        males = [s for s in band if s['gender'].strip().lower() in ('m', 'male')]
        females = [s for s in band if s['gender'].strip().lower() in ('f', 'female')]
        random.shuffle(males)
        random.shuffle(females)
        band_males.append(males)
        band_females.append(females)

    total_males = sum(len(m) for m in band_males)
    total_females = sum(len(f) for f in band_females)

    if total_males > total_females:
        target_males_per_group, target_females_per_group = 3, 2
    else:
        target_males_per_group, target_females_per_group = 2, 3

    groups = [[] for _ in range(num_groups)]
    male_count = [0] * num_groups
    female_count = [0] * num_groups

    # distribute one student from each band into each group
    for band_idx in range(len(bands)):
        for group_idx in range(num_groups):
            # try to pick a student to respect the gender targets
            picked = False
            if male_count[group_idx] < target_males_per_group and band_males[band_idx]:
                groups[group_idx].append(band_males[band_idx].pop())
                male_count[group_idx] += 1
                picked = True
            elif female_count[group_idx] < target_females_per_group and band_females[band_idx]:
                groups[group_idx].append(band_females[band_idx].pop())
                female_count[group_idx] += 1
                picked = True
            elif band_males[band_idx]:
                groups[group_idx].append(band_males[band_idx].pop())
                male_count[group_idx] += 1
                picked = True
            elif band_females[band_idx]:
                groups[group_idx].append(band_females[band_idx].pop())
                female_count[group_idx] += 1
                picked = True

    return groups


def print_groups(groups, students_sorted, bands, batch_number=1):
    """Print groups with band information."""
    # Precompute band assignments for faster lookup
    student_to_band = {}
    for band_idx, band in enumerate(bands):
        for student in band:
            # Use a unique identifier (name + id) to handle duplicate names
            student_key = f"{student['name']}_{student['id']}"
            student_to_band[student_key] = band_idx + 1  # Band 1 = highest GPA

    print(f"=== BATCH {batch_number} ===")
    print(f"Total students in this batch: {len(students_sorted)}")
    print()
    
    for i, g in enumerate(groups, 1):
        print(f"Group {i}:")
        males_in_group = 0
        females_in_group = 0
        total_gpa = 0.0
        
        for student in g:
            # Determine which band the student came from
            student_key = f"{student['name']}_{student['id']}"
            band_number = student_to_band.get(student_key, "Unknown")
            
            gender_lower = student['gender'].lower()
            if gender_lower in ['m','male']:
                males_in_group += 1
            elif gender_lower in ['f', 'female']:
                females_in_group += 1
            total_gpa += student['gpa']
            print(f"  {student['name']} | {student['school']} | {student['gender']} | GPA: {student['gpa']:.2f} | Band: {band_number}")
        
        if g:
            avg_gpa = total_gpa / len(g)
            print(f"  Summary: {males_in_group} males, {females_in_group} females, Average GPA: {avg_gpa:.2f}")
        else:
            print("  Summary: Empty group")
        print()


if __name__ == "__main__":
    BATCH_SIZE = 50
    NUM_GROUPS = 10
    
    try:
        # Count total students first
        total_students = count_total_students()
        if total_students == 0:
            print("No student records found in the file.")
            sys.exit(1)
            
        print(f"Total students in file: {total_students}")
        print(f"Processing in batches of {BATCH_SIZE} students...")
        print("=" * 60)
        
        batch_number = 1
        start_index = 0
        
        # Process file in batches until all students are processed
        while True:
            print(f"Reading batch {batch_number} (students {start_index + 1} to {start_index + BATCH_SIZE})...")
            students = read_students(start_index, BATCH_SIZE)
            
            if not students:
                print("No more students to process.")
                break
                
            print(f"Processing {len(students)} students in batch {batch_number}...")
            
            # Sort students for band creation
            students_sorted = sorted(students, key=lambda x: x['gpa'], reverse=True)
            n = len(students_sorted)
            band_size = max(1, n // 5)
            bands = [students_sorted[i:i + band_size] for i in range(0, n, band_size)]

            # Form groups for this batch
            groups = form_groups(students, num_groups=NUM_GROUPS)
            
            # Print groups for this batch
            print_groups(groups, students_sorted, bands, batch_number)
            
            # Update for next batch
            start_index += BATCH_SIZE
            batch_number += 1
            
            # Add separator between batches
            if start_index < total_students:
                print("=" * 60)
                print()
        
        print(f"Processing complete! Processed {batch_number - 1} batch(es) total.")
        
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)