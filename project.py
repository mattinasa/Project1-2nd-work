class ExamSystem:
    def __init__(self,filename):
        self.filename = filename
        self.students = {}
        self.loading()

    def loading(self):
        try:
            with open(self.filename,'r') as f:
                lines = f.readlines()
                for i in range(1,len(lines)):
                    line = line.strip()


        except FileNotFoundError:
            print("File not found")
            self.students = {}