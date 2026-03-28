###git目录C:\Users\13025\Desktop\大学\大一下学期\人工智能导论\week4\StudentsCheck
import os
import re #因为txt文本有\t也有空格，所以要标准化输入
class Student:
    def __init__(self,name,classNum,id,gender,college):#一个初始化，来存储除了“序号”以外的信息
        self.name=name
        self.classNum=classNum
        self.id=id
        self.gender=gender
        self.college=college

    def __str__(self):#用于友好输出，不然就会输出我们看不懂的东西
        return f"姓名：{self.name} 班级：{self.classNum} 性别：{self.gender} 学院：{self.college}"#索引用学号，就不需要输出学号了

class ExamSystem:
    def __init__(self,filename):
        self.filename = filename
        self.students = {}#将学生的信息设置为字典格式，方便按照学号查找
        self.loading()

    def loading(self):

        try:
            with open(self.filename,'r',encoding='utf-8') as f:#尝试打开文件
                lines = f.readlines()#读取学生信息
                lines=lines[1:]#去掉表头
                print(len(lines))
                for line in lines:#枚举每一个学生
                    parts=re.split(r'\s+',line.strip())
                    name=parts[1]
                    gender=parts[2]
                    classNum=parts[3]
                    id=parts[4]
                    college=parts[5]
                    self.students[id] = Student(name,classNum,id,gender,college)#以学号为索引来输出吧

                    #调试
                    print(self.students[id].__str__())


        except FileNotFoundError:
            print("File not found")#比较友好地提示文件没有找到
            self.students = {}

    @staticmethod
    def validate(student_id):#一个简单的id基础格式校验，要求就是纯数字
        return student_id.isdigit()#判断是不是纯数字

# #这是个调试
# try:
#     system = ExamSystem("人工智能编程语言学生名单.txt")
# except FileNotFoundError:
#     print("File not found")
