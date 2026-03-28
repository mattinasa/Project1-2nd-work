class Student:
    def __init__(self,name,classNum,id,gender,college):#一个初始化，来存储除了“序号”以外的信息
        self.name=name
        self.classNum=classNum
        self.id=id
        self.gender=gender
        self.college=college

    def __str__(self):#用于友好输出，不然就会输出我们看不懂的东西
        return f"姓名：{self.name} 班级：{self.classNum} 学号：{self.id} 性别：{self.gender} 学院：{self.college}"

class ExamSystem:
    def __init__(self,filename):
        self.filename = filename
        self.students = {}#将学生的信息设置为字典格式，方便按照学号查找
        self.loading()

    def loading(self):
        try:
            with open(self.filename,'r') as f:#尝试打开文件
                lines = f.readlines()#读取学生信息

                for i in range(1,len(lines)):#枚举每一个学生

                    student=[]#存储除了学号以外的信息，用于value

                    for j in range(6):#枚举学生的每一个信息，然后除了学号以外存储在一个列表里，当作value
                        if j!=4:#除了学号
                            student.append(lines[i][j].strip())

                    self.students[lines[i][4].strip()] = student


        except FileNotFoundError:
            print("File not found")
            self.students = {}

    @staticmethod
    def validate(student_id):#一个简单的id基础格式校验，要求就是纯数字
        return student_id.isdigit()
