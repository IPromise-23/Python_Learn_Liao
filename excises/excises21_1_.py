#请编写函数，在Sqlite中根据分数段查找指定的名字：

#os是Python的系统交互模块,用于处理文件路径、文件操作
#sqlite3是内置的SQLite数据库操作模块
import os, sqlite3

#__file__是Python内置变量,代表当前脚本文件本身的路径(比如脚本叫demo.py，__file__就是demo.py的完整路径)
#os.path.dirname(__file__)用来获取当前脚本所在的文件夹路径
#os.path.join(目录, 文件名)：把 “脚本所在目录” 和 “test.db” 拼接成完整的数据库文件路径，确保test.db会被创建在当前脚本的同一文件夹下（避免路径混乱）。
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)#连接到SQLite数据库
cursor = conn.cursor()#创建一个Cursor,通过Cursor执行SQL语句
#execute——处决、执行
#执行一条SQL语句，创建user表
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
#继续执行一条SQL语句，插入一条记录
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
#提交事务
conn.commit()
#关闭Cursor
cursor.close()
#关闭Connection
conn.close()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect(db_file)#连接到SQLite数据库
    try:
        cursor = conn.cursor()#创建游标对象
        #执行参数化SQL查询
        #BETWEEN ? AND ?：匹配分数在[low, high]区间的记录
        #ORDER BY score ASC：按分数升序排序
        cursor.execute(
            'SELECT name FROM user WHERE score BETWEEN ? AND ? ORDER BY score ASC',
            (low, high) #传入参数，替换SQL中的?
        )
        #抓取所有查询结果(返回的是元组列表)
        results = cursor.fetchall()
        #提取每个元组中的name字段并组成列表返回
        name_list = [row[0] for row in results]
        return name_list
    finally:
        #无论是否出错，都确保关闭游标和连接（释放资源）
        cursor.close()
        conn.close()


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
