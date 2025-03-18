class Educator:
    def prepareLesson(self):
        print("Preparing a general lesson plan.")

class ITInstructor(Educator):
    def prepareLesson(self):
        print("Preparing a technical lesson plan focusing on coding.")

    def teachCoding(self):
        print("Teaching coding basics like Python syntax and concepts.")

class DatabaseInstructor(ITInstructor):
    def teachCoding(self):
        print("Teaching coding with a focus on SQL integration with Python.")

    def demonstrateMySQL(self):
        print("Demonstrating MySQL queries and database operations.")

db_instructor = DatabaseInstructor()
db_instructor.prepareLesson()
db_instructor.teachCoding()
db_instructor.demonstrateMySQL()
