
class StudentRecordSystem:
    def __init__(self , filename ="Student.txt"):
        self.filename = filename
    #  add Students
    def add_student(self , name , marks):
        try:
            with open(self.filename , "a") as file:
                file.write(f"{name},{marks}\n")
                print(f"Student '{name}' added successfully!")
        except Exception as e:
                print(f"Error while adding student: {e}")
    # to view students in file
    def view_students(self):
         try:
            with open(self.filename , "r") as file:
                data = file.readlines()
                if not data:
                    print("No data Found....")
                    return
                print("\nStudent Records:")
                for line in data:
                    name , marks = line.strip().split(",")
                    print(f"Name: {name}, Marks: {marks}")
                    return
         except FileNotFoundError as e:
              print("File not found..")

    # to search for student in list 
    def search_student(self,name):
        try:
            with open(self.filename , "r") as file:
                found = False
                for line in file:
                    student_name , mark = line.strip().split(",")
                    if student_name.lower() ==  str(name).lower():
                        print(f"Found ={student_name}, Marks: {mark}")
                        found=True
                        return
                if not found:
                    print(f"Student '{name}' not found.")

        except FileNotFoundError as e:
            print('File not found...')
    
    # Delete Student by Name
    def delete_student(self, name):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            with open(self.filename, "w") as file:
                deleted = False
                for line in lines:
                    student_name, marks = line.strip().split(",")
                    if student_name.lower() != name.lower():
                        file.write(line)
                    else:
                        deleted = True

            if deleted:
                print(f"Student '{name}' deleted successfully.")
            else:
                print(f" Student '{name}' not found.")
        except FileNotFoundError:
            print("No records yet. Add a student first.")

# -------------------------------
#  Testing the System
# -------------------------------
system = StudentRecordSystem()

system.add_student("Rabin", 95)
system.add_student("Sita", 88)

system.view_students()

system.search_student("Rabin")
system.search_student("Hari")

system.delete_student("Sita")
system.view_students()