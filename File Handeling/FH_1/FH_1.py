class StudentRecordSystem:
    def __init__(self , filename ="Student.txt"):
        self.filename = filename

    def add_student(self , name , marks):
        try:
            with open(self.filename , "a") as file:
                file.write(f"{name},{marks}\n")
                print(f"Student '{name}' added successfully!")
        except Exception as e:
                print(f"❌ Error while adding student: {e}")
    
    def view_students(self):
         try:
            with open(self.filename , "r") as file:
                data = file.readlines()
                if not data:
                    print("No data Found....")
                    return
                print("\n📋 Student Records:")
                for line in data:
                    name , marks = line.strip().split(",")
                    print(f"Name: {name}, Marks: {marks}")
         except FileNotFoundError as e:
              print("File not found..")