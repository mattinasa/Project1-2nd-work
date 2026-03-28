###git目录C:\Users\13025\Desktop\大学\大一下学期\人工智能导论\week4\StudentsCheck
import os
import time
import random
import re#因为txt文本有\t也有空格，所以要标准化输入
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
                # print(len(lines))
                for line in lines:#枚举每一个学生
                    parts=re.split(r'\s+',line.strip())
                    name=parts[1]
                    gender=parts[2]
                    classNum=parts[3]
                    id=parts[4]
                    college=parts[5]
                    self.students[id] = Student(name,classNum,id,gender,college)#以学号为索引来输出吧

                    # #调试
                    # print(self.students[id].__str__())


        except FileNotFoundError:
            print("File not found")#比较友好地提示文件没有找到
            self.students = {}

    @staticmethod
    def validate(student_id):#一个简单的id基础格式校验，要求就是纯数字
        return student_id.isdigit()#判断是不是纯数字

    def find_students(self,student_id):#用于输入学号后输出这个学生的其他信息哦！
        if not self.validate(student_id):
            print("学号应为纯数字哦！")#友好提示
            return None
        try:#进行一次温和的try
            return self.students[student_id]
        except KeyError:
            print("没有找到这个学号的人哦！")#友好提示
            return None

    def random_call(self,count):
        total=len(self.students)
        if count.isdigit()==False:
            print("Sorry!需要输入数字！")
            return []
        count=int(count)
        if total<count:
            print("Sorry!输入的数字超过总人数了哦！")
            return []
        if count<=0:
            print("Sorry!请输入正数！")
            return []
        all_students=list(self.students.values())
        selected=random.sample(all_students,count)
        return selected

    def generate_seating(self):
        all_students=list(self.students.values())
        random.shuffle(all_students)#内置的随机打乱函数
        return all_students

    def save_seating(self,student_list):
        try:
            generate_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())#用标准格式来生成现在时间
            with open("考场安排表.txt",'w',encoding='utf-8') as f:
                f.write(f"生成时间{generate_time}\n")
                f.write(f"座位\t姓名\t学号\n")
                for i,student in enumerate(student_list):
                    f.wirte(f"{i}\t{student.name}\t{student.id}\n")
            print("考场安排生成成功！")#温馨的提示

        except Exception as e:
            print(f"生成考场安排时发生错误：{e}")

    def Create_adtickets(self,students_list):
        try:
            #如果不存在，那就创建，已存在的需要先清理
            folder_name="准考证.txt"
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                print(f"已创建文件夹：{folder_name}")

            #接着在该文件夹下面创建独立的准考证文件
            for i,student in enumerate(self.students_list):
                filename=os.path.join(folder_name,f"{i:02d}.txt")#格式要求是两位，并且要是一位就0开头，所以02d
                with open(filename,'w',encoding='utf-8') as f:
                    f.write(f"考场座位号：{i}\n")
                    f.write(f"姓名：{student.name}\n")
                    f.write(f"学号：{student.id}\n")

            print("已成功创建准考证！")

        except Exception as e:
            print(f"生成准考证的时候发生错误：{e}")











# #这是个调试
# try:
#     system = ExamSystem("人工智能编程语言学生名单.txt")
#     selected=system.random_call("2")
#     for student in selected:
#         print(student.name)
# except FileNotFoundError:
#     print("File not found")

