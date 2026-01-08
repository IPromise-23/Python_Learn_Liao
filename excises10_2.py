# 请把下面的Student对象的gender字段对外隐藏起来，
# 用get_gender()和set_gender()代替，并检查参数有效性：
#思路：对外隐藏无非就是想让内部属性不被外部访问，检查参数有效性是下面测试板块的任务
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender    #禁止外部访问内部属性
    def get_gender(self):
        return self.__gender      #外部获取内部属性name、gender
    def set_gender(self,gender):
        if gender not in ("female","male"):#检查参数,避免传入无效参数
            raise ValueError('Your gender is not valid!')
        else:
            self.__gender =  gender   #外部修改内部属性的值

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')