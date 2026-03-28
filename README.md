# 夏元益-25361038-第二次人工智能编程作业
## 1. 任务拆解与 AI 协作策略
步骤一：让AI生成一段代码，用于存储每个学生个人信息（姓名，性别，学号，班级，学院）

步骤二：让AI帮我编写一个程序，能够实现学生信息的读取，我则根据所附txt文件修改open的文件名等进行代码书写

步骤三：让AI写四个函数，分别能够实现信息初始化与查找、随机点名、生成考场安排表、生成准考证目录与文件

步骤四：让AI把步骤二与步骤三的程序整合到一个class里面，名字就是 ExamSystem，我根据整合前后的区别对我的代码进行缩进与改写

步骤五：让它基于前面步骤生成的代码生成一个主函数，能够进行输入输出以及整个项目运行，通过我的个人习惯来进行个性化修改

步骤六：加入str魔术方法让student的信息可以友好打印



## 2. 核心 Prompt 迭代记录
AI生成的问题：没有使用面向对象：当我第一个步骤进行时，AI没有对student进行数据封装，没有进行class的定义

优化后prompt：我将问题改为：帮我生成一段代码，用一个Student类，来存储每个学生个人信息（姓名，性别，学号，班级，学院），以满足面向对象编程的要求

## 3. Debug 与异常处理记录
报错类型：UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 23: illegal multibyte sequence

将报错喂给AI：由于我前面是分散着进行代码拼接，所以输入输出的衔接并没有很到位，在主函数里输入的“人工智能编程语言学生名单.txt”不能被系统识别

修改：

## 4. 人工代码审查 (Code Review)
```python
def generate_seating(self):#这是用来生成考场座位的
    all_students=list(self.students.values())#需要将字典中“值”的元素全部转换成列表才方便进行random内置函数运行
    random.shuffle(all_students)#内置的随机打乱函数
    return all_students#返回一个列表

def save_seating(self,student_list):#这是用来保存生成的考场安排的
    try:#防错的一次尝试
        generate_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())#用标准格式来生成现在时间
        with open("考场安排表.txt",'w',encoding='utf-8') as f:#打开文件，需要用utf-8这种计算机能够读得懂的，不然光是中文文件名读不懂
            f.write(f"生成时间{generate_time}\n")#写入生成时间
            f.write(f"座位\t姓名\t学号\n")#写入其他信息
            for i,student in enumerate(student_list):#enumerate可以同时迭代索引和值，很方便
                f.write(f"{i+1}\t{student.name}\t{student.id}\n")#因为从零开始所以i+1，用于写入学生相应信息
        print("考场安排生成成功！")#温馨的提示

    except Exception as e:#把错误原因告诉我们
        print(f"生成考场安排时发生错误：{e}")

def Create_adtickets(self,students_list):#这是用来建立准考证文件夹的
    try:
        #如果不存在，那就创建，已存在的需要先清理
        folder_name="准考证.txt"#文件名字
        if not os.path.exists(folder_name):#不存在就创建
            os.mkdir(folder_name)#创建
            print(f"已创建文件夹：{folder_name}")

        #接着在该文件夹下面创建独立的准考证文件
        for i,student in enumerate(students_list):
            filename=os.path.join(folder_name,f"{i+1:02d}.txt")#格式要求是两位，并且要是一位就0开头，所以02d
            with open(filename,'w',encoding='utf-8') as f:
                f.write(f"考场座位号：{i+1}\n")#以下是写入信息
                f.write(f"姓名：{student.name}\n")
                f.write(f"学号：{student.id}\n")

        print("已成功创建准考证！")

    except Exception as e:
        print(f"生成准考证的时候发生错误：{e}")
```

# 贴入代码及人工注释
```python
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
        selected=random.sample(all_students,count)#随机生成列表中count个元素
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
                    f.write(f"{i+1}\t{student.name}\t{student.id}\n")
            print("考场安排生成成功！")#温馨的提示

        except Exception as e:
            print(f"生成考场安排时发生错误：{e}")

    def Create_adtickets(self,students_list):
        try:
            #如果不存在，那就创建，已存在的需要先清理
            folder_name="准考证.txt"
            if not os.path.exists(folder_name):#不存在就创建
                os.mkdir(folder_name)#创建
                print(f"已创建文件夹：{folder_name}")

            #接着在该文件夹下面创建独立的准考证文件
            for i,student in enumerate(students_list):
                filename=os.path.join(folder_name,f"{i+1:02d}.txt")#格式要求是两位，并且要是一位就0开头，所以02d
                with open(filename,'w',encoding='utf-8') as f:
                    f.write(f"考场座位号：{i+1}\n")#以下是写入信息
                    f.write(f"姓名：{student.name}\n")
                    f.write(f"学号：{student.id}\n")

            print("已成功创建准考证！")

        except Exception as e:
            print(f"生成准考证的时候发生错误：{e}")

def main():
    #这是主函数，用于用户交互，即输入输出
    print("="*50)#这是方便观看
    print("欢迎使用学生考试管理系统")
    print("=" * 50)

    # 创建考试系统实例
    try:
        system = ExamSystem("人工智能编程语言学生名单.txt")
    except Exception as e:
        print(f"系统初始化失败：{e}")
        return

    # 主循环
    while True:
        print("\n请选择功能：")
        print("1. 查找学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表和准考证")
        print("4. 退出系统")

        choice = input("请输入选项（1-4）：").strip()

        if choice == "1":# 查找学生功能
            student_id = input("请输入学号：").strip()
            student = system.find_students(student_id)

            if student:
                print("\n查询结果：")
                print(student)

        elif choice == "2":# 随机点名功能
            try:
                count = input("请输入需要点名的学生数量：").strip()
                selected = system.random_call(count)

                if selected:
                    print(f"\n随机点名的 {count} 名学生：")
                    print("-" * 40)
                    for i, student in enumerate(selected, start=1):
                        print(f"{i}. {student.name}（学号：{student.id}）")
                    print("-" * 40)

            except ValueError:
                print("错误：请输入有效的数字！")

        elif choice == "3": #生成考场安排表和准考证
            print("\n正在生成考场安排表...")
            seating_list = system.generate_seating()
            system.save_seating(seating_list)
            print("\n正在生成准考证文件...")#相关联所以这几个操作一起做了
            system.Create_adtickets(seating_list)

            print("\n所有文件生成完成！请查看程序根目录下的文件。")

        elif choice == "5":#用于退出系统
            print("感谢使用，再见！")
            break

        else:
            print("错误：无效选项，请重新选择！")

if __name__ == "__main__":
    main()







# #这是个调试
# try:
#     system = ExamSystem("人工智能编程语言学生名单.txt")
#     selected=system.random_call("2")
#     for student in selected:
#         print(student.name)
# except FileNotFoundError:
#     print("File not found")
```
