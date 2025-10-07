# Create a dictionary with 5 students and their grades
# Add a new student
# Update an existing student's grade
# Find the student with the highest grade
# Calculate the average grade

students_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 92,
    "Eva": 88
}

# Add a new student
students_grades["Barry"] = 12
print("After adding Barry:", students_grades)


print(max(students_grades, key=students_grades.get))  # Find the student with the highest grade

average_grade = sum(students_grades.values()) / len(students_grades)
print("Average grade:", average_grade)

# Update an existing student's grade
students_grades["Alice"] = 90   
print("After updating Alice's grade:", students_grades)

print("Students and their grades:", students_grades)


for student, grade in students_grades.items():
    print(f"| {student} | {grade} |")
    
# Given a sentence, count how many times each word appears

sentence = "hello world hello"
word_count = {}
# Example: "hello world hello" → {"hello": 2, "world": 1}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word count:", word_count)

# Create a shopping cart using a list of dictionaries
# Each item should have: name, price, quantity
# Calculate total cost
# Add/remove items
shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 4},
    {"name": "banana", "price": 0.3, "quantity": 6},
    {"name": "orange", "price": 0.8, "quantity": 3}
]

# Calculate total cost
total_cost = sum(item["price"] * item["quantity"] for item in shopping_cart)
print("Total cost:", total_cost)

# Add an item
shopping_cart.append({"name": "grape", "price": 0.4, "quantity": 5})
print("After adding grape:", shopping_cart)

# Remove an item
shopping_cart = [item for item in shopping_cart if item["name"] != "banana"]
print("After removing banana:", shopping_cart)