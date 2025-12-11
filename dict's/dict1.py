student = {
    "name": "Mira",
    "age": 21,
    "course": "Engineering"
}

print(student)

print(student["name"])      # Access using key
print(student.get("age"))   # Safe access (returns None if key missing)
