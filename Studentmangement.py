class StudentMangement:

#    __init__  Initializes self.d1 (like your earlier d1 dictionary).
    def __init__(self):
        self.d1 = {}
    
    def Add_student(self):
         n = int(input("Enter the number of students you want to add: "))
       
         for i in range(n):
            name = input("Enter the name: ")
            roll = int(input("Enter the Roll no.: "))
            marks = int(input("Enter the marks: "))

            self.d1[roll] = {'Name': name, 'Marks': marks}

         print("\nStudents added successfully!")
         print("Current Student Data:", self.d1)
         print()

    def Display_student(self):

        if not self.d1:
            print("\nNo student data available.\n")
            return
        else:
            print("\n--- Student Details ---")
            for roll, data in self.d1.items():
                print(f"Roll No: {roll}, Name: {data['Name']}, Marks: {data['Marks']}")
            print()

    def Search_by_Roll(self):
            roll = int(input("Enter the Roll number you want to search: "))

            if not self.d1:
                print("\nNo student data available.\n")
                return
            elif roll in self.d1:
                print(f"Name: {self.d1[roll]['Name']}, Marks: {self.d1[roll]['Marks']}")
            else:
                print("Student Not Found")

    def Show_class_average(self):
            if not self.d1:
                print("\nNo student data available.\n")
                return
            else:
                total_marks = sum(data['Marks'] for data in self.d1.values())
                avg = total_marks / len(self.d1)
                print("The Class Average is:", avg)

    def main(self):
        
        while True:
            print(""" \n  ******** Select choice below **********
                    1. Add Student
                    2. Display Student
                    3. Search by Roll no.
                    4. Show class Average
                    5. Exit \n """)
            
            choice =  (input("Enter the Choice :"))
            if choice == "1":
                self.Add_student()
            elif choice == "2":
                self.Display_student()
            elif choice == "3":
                self.Search_by_Roll()
            elif choice == "4":
                self. Show_class_average()
            elif choice == "5":
                break
            else:
                print("Choose number between 1-5")

if __name__ == "__main__":
    sm = StudentMangement() 
    sm.main()
        