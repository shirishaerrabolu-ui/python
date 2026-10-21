student_data = {

    101: {"name": "Rahul", "class": 7, "subjects": ("Math", "Biology")},
    102: {"name": "Priya", "class": 8, "subjects": ("English", "Physics")},
    103: {"name": "Farhan", "class": 7, "subjects": ("Chemistry", "Telugu")},
    104: {"name": "Aman", "class": 9, "subjects": ("Hindi", "Geography")}
}


result = {}
seen_keys = []


for student_id in student_data:
    details =  student_data[student_id]
    unique_key = (details["name"], details["class"], details["subjects"])


    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for student_id in result:
    print("ID:", student_id)
    print("Name:", result[student_id]["name"])        
    print("Class:", result[student_id]["class"])        
    print("Subjects:", result[student_id]["subjects"])        
    print()        