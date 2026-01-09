***Python_Learning***<a id="开头"></a>

注意点：
print(len(str('')))    #0个字符，一个''
print(len(str(' ')))   #1个字符，注意和上一个区分，这个是' ',是有空格的
print(len(str('a ')))  #2个字符，一个'a'和一个' '
注意不要陷入死循环，缩进一定要看准，比如自增，到底在不在while语句内部实现

---

# 第四章

在vscode中想要注释用 ctrl+/，取消同理
PowerShell命令行模式--->在命令行中输入命令python就进入到了python交互模式--->交互模式下exit()就可以退回到命令行模式
命令行模式下还可以执行.py 文件   eg. 命令行下输入python hello.py
目录设定 cd D:\VsCodeProjects\lxfclass  注意cd后要加空格
SyntaxError表示输入的python代码有语法错误
在Python交互式模式下，可以直接输入代码，然后执行，并立刻得到结果；在命令行模式下，可以直接运行.py文件
直接输入python进入交互模式，相当于启动了Python解释器，等待你一行一行地输入源代码，每输入一行就执行一行。
直接运行.py文件相当于启动了Python解释器，然后一次性把.py文件的源代码给执行了，你是没有机会以交互的方式输入源代码的。

---

# 第五章 Python基础

任何一种编程语言都有自己的一套语法，编译器负责把符合语法的程序代码转换成CPU能够执行的机器码然后执行
python采用四个空格的缩进，并且python对大小写很敏感

## 5.1.数据类型和变量

### 整数和负整数

十六进制用前缀0x和0-9，a-f表示（比如0xff00）    

对于很大的数字 10_000_000=10000000,通过添加下划线的方式来确定数量大小（同理十六进制数也可以这样操作）

### 浮点数（小数）

casue按照科学计数法表示时，一个浮点数的小数点位置是可变的 1.23x10^9^=12.3x10^8^=1.23e9

### 字符串

用'单引号'或者"双引号"括起来的任意文本   eg. 当字符串内部既包含"又包含'时，可以用转义字符\来表示'I\'m\"OK\"!'

### 转义字符

转义字符`\`可以转义很多字符，比如`\n`表示换行，`\t`表示制表符，字符`\`本身也要转义，所以`\\`表示的字符就是`\`，可以在Python的交互式命令行用`print()`打印字符串：

```plain
>>> print('I\'m ok.')
I'm ok.
>>> print('I\'m learning\nPython.')
I'm learning
Python.
>>> print('\\\n\\')
\
\
```

### 布尔值

布尔值=布尔代数（只是代表表示形式）   布尔值只有True&False，并且可以用and、or、not来进行运算 

布尔值常用语条件判断
eg.
age=input("请输入你的年龄：")
if int(age)>=18:
    print("你已经成年了")
else:
    print("你还未成年")

### 空值

用None表示，是一个特殊的空值，不等于0,0是有意义的

### 变量（任意数据类型）

code中用变量名表示变量，变量名必须是大小写英文、数字和下划线的组合而且不能用数字开头
Python中等号是赋值语句，可以把任意数据类型赋值给变量，同一个变量也可以反复赋值（而且可以是不同类型的变量）   动态语言
理解变量在计算机内存中的表示
当我们写：a = 'ABC'时，Python解释器干了两件事情：
在内存中创建了一个'ABC'的字符串；
在内存中创建了一个名为a的变量，并把它指向'ABC'。
也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：
a = 'ABC'
b = a
a = 'XYZ' 
print(b)

结果应该为'ABC'

### 常量（不能变的变量）

PI=3.1415926……
用全部大写的变量名表示常量是习惯上的用法

在Python中，有两种除法，一种除法是`/`：

```plain
>>> 10 / 3
3.3333333333333335
```

`/`除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：

```plain
>>> 9 / 3
3.0
```

还有一种除法是`//`，称为地板除，两个整数的除法仍然是整数：

```plain
>>> 10 // 3
3
```

整数的地板除`//`永远是整数，即使除不尽。要做结果为浮点数的除法，使用`/`就可以。

因为`//`除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：

```plain
>>> 10 % 3
1
```

无论整数做`//`除法还是取余数，结果永远是整数，所以，整数运算的结果永远是精确的。

## 5.2.字符串和编码

### 字符编码

计算机只能处理数字，若要处理文本，必须把文本转换为数字
ASCII到Unicode，为了节省存储空间，在计算机内存中统一使用Unicode，要保存到硬盘或者传输时转换为UTF-8编码
Python的字符串用Unicode编码，支持多种语言
ord()函数获取字符的整数表示，chr()函数把编码转为对应的字符
Python的字符串类型是str，在内存中用Unicode表示，一个字符对应若干个字节。传输或者保存到磁盘时，str要变为以字节为单位的bytes。
Python对bytes类型的数据用带b前缀的单引号或双引号表示：  x = b'ABC'
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
用Unicode表示的str通过encode()可以编码为指定的bytes

```plain
>>>'ABC'.encode('ascii')
b'ABC'
'中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
b'ABC'.decode('ascii')
'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
要计算str包含多少个字符，可以用len()函数：
len('ABC')
3
len('中文')
2
len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
len(b'ABC')
3
len(b'\xe4\xb8\xad\xe6\x96\x87')
6
len('中文'.encode('utf-8'))
6
可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
```

### 格式化

#### %

采用的格式化方式和C语言是一致的，用`%`实现，举例如下：

```plain
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
```

`%`用来格式化字符串的。在字符串内部，`%s`表示用字符串替换，`%d`表示用整数替换，有几个`%?`占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个`%?`，括号可以省略

常见的占位符有：

| 占位符 | 替换内容     |
| ------ | ------------ |
| %d     | 整数         |
| %f     | 浮点数       |
| %s     | 字符串       |
| %x     | 十六进制整数 |

有些时候，字符串里面的`%`是一个普通字符怎么办？这个时候就需要转义，用`%%`来表示一个`%`：

```plain
>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
```

#### format()

另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：

```plain
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'
```

#### f-string

最后一种格式化字符串的方法是使用以`f`开头的字符串，称之为`f-string`，它和普通字符串不同之处在于，字符串如果包含`{xxx}`，就会以对应的变量替换：

```plain
>>> r = 2.5
>>> s = 3.14 * r ** 2
>>> print(f'The area of a circle with radius {r} is {s:.2f}')
The area of a circle with radius 2.5 is 19.62
```

上述代码中，`{r}`被变量`r`的值替换，`{s:.2f}`被变量`s`的值替换，并且`:`后面的`.2f`指定了格式化参数（即保留两位小数），因此，`{s:.2f}`的替换结果是`19.62`。

## 5.3.使用list和tuple

### 列表list

一种有序集合，可以随时添加和删除其中的元素，可以用**索引**来访问list中每一个位置的元素
eg.
classmates=['Michael','Bob','Tracy']
classmates[0]  # 'Michael'
classmates[1]  # 'Bob'
classmates[2]  # 'Tracy'

索引不得超出范围，要确保索引不要越界，要取最后一个元素时，除了计算索引位置还可以直接用-1做索引来直接获取最后一个元素
list是一个可变的有序表，可以追加元素到末尾

- classmates.append('Adam')  # 添加元素到末尾

- classmates.insert(i,'Jack')  # 插入元素到指定位置i

- classmates.pop()  # 删除末尾元素

- classmates.pop(i)  # 删除指定位置i的元素

- classmates[i]='Michael'  # 替换指定位置i的元素

- 列表list内部的元素的数据类型也可以不同   L=['A',123,False]

- 此外，list内部可以再嵌套一个list:

  ```plain
  >>> s = ['python', 'java', ['asp', 'php'], 'scheme']
  >>> len(s)
  4
  ```

  注意`s`只有4个元素，其中`s[2]`又是一个list，拆开写：

  ```plain
  >>> p = ['asp', 'php']
  >>> s = ['python', 'java', p, 'scheme']
  ```

  要拿到`'php'`可以写`p[1]`或者`s[2][1]`，因此`s`可以看成是一个二维数组。

- 空的list长度为0  len([])=0

### tuple元组

类似于list，但是tuple一旦初始化后就**不能修改**

```plain
>>> classmates = ('Michael', 'Bob', 'Tracy')
```

现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，可以正常地使用`classmates[0]`，`classmates[-1]`，但不能赋值成另外的元素。因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

> classmates=['Michael','Bob','Tracy']   /这是list []
> classmates=('Michael','Bob','Tracy')   /这是tuple ()

tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就**必须被确定下来**，比如：

```plain
>>> t = (1, 2)
>>> t
(1, 2)
```

如果要定义一个空的tuple，可以写成`()`：

```plain
>>> t = ()
>>> t
()
```

要定义一个只有1个元素的tuple，如果这么定义：

```plain
>>> t = (1)
>>> t
1
```

那么定义的不是tuple，是`1`这个数！这是因为括号`()`既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是`1`。

所以，只有1个元素的tuple定义时必须加一个逗号`,`，来消除歧义：

```plain
>>> t = (1,)
>>> t
(1,)
```

Python在显示只有1个元素的tuple时，也会加一个逗号`,`，以免你误解成数学计算意义上的括号。

最后来看一个**“可变的”tuple**：

```plain
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```

这个tuple定义的时候有3个元素，分别是`'a'`，`'b'`和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？

定义的时候tuple包含的3个元素：

![tuple-1](https://liaoxuefeng.com/books/python/basic/list-tuple/step-1.png)

当我们把list的元素`'A'`和`'B'`修改为`'X'`和`'Y'`后，tuple变为：

![tuple-2](https://liaoxuefeng.com/books/python/basic/list-tuple/step-2.png)

表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。**tuple一开始指向的list并没有改成别的list**，<!--tuople指向为list而非list内元素，list变化但是tuple没有变-->所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向`'a'`，就不能改成指向`'b'`，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。那就不能有list啦

## 5.4.条件判断

### if语句

从上往下判断（匹配），若在某个判断上是True，则执行该判断对应的语句后，就忽略掉剩下的elif和else
if <条件判断1>:
    <执行1>
elif <条件判断2>:   #elif是else if的缩写
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
input()返回的数据类型是str，不能与整数直接比较，必须把str转换成整数，可以用int()来实现
int()可以将一个值转换为整数，可以把字符串等类型转换为整数后进行数值运算和比较

```python
birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')
```

输入`1982`，结果报错：

```plain
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() > int()
```

这是因为`input()`返回的数据类型是`str`，`str`不能直接和整数比较，必须先把`str`转换成整数。Python提供了`int()`函数来完成这件事情：

```python
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
%再次运行就能得到正确的结果
```

## 5.5.模式匹配

### match语句

if语句往往过于冗长，可读性比较差，如果要针对某个变量匹配若干种情况可以用match语句
score = 'B'
match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: #case_表示任意值，表示匹配到其他任何情况
        print('score is ???.')

### 复杂匹配

match语句不仅可以匹配单个值，还可以匹配多个值、一定范围，并把匹配后的值绑定到变量
age = 9
match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')
在上面这个示例中，第一个case x if x < 10表示当age < 10成立时匹配，且赋值给变量x，第二个case 10仅匹配单个值，第三个case 11|12|...|18能匹配多个值，用|分隔。

### 匹配列表（用match来匹配）

```python
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
```

第一个`case ['gcc']`表示列表仅有`'gcc'`一个字符串，没有指定文件名，报错；

第二个`case ['gcc', file1, *files]`表示列表第一个字符串是`'gcc'`，第二个字符串绑定到变量`file1`，后面的任意个字符串绑定到`*files`（符号`*`的作用将在[函数的参数](https://liaoxuefeng.com/books/python/function/parameter/index.html)中讲解），它实际上表示至少指定一个文件；

第三个`case ['clean']`表示列表仅有`'clean'`一个字符串；

最后一个`case _`表示其他所有情况。

可见，`match`语句的匹配规则非常灵活，可以写出非常简洁的代码。

## 5.6.循环

### for x in...循环

```python
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```

执行这段代码，会依次打印`names`的每一个元素：

```plain
Michael
Bob
Tracy
```

所以`for x in ...`循环就是把每个元素代入变量`x`，然后执行缩进块的语句。

#0——100求和代码
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
list(range(5))的结果为[0,1,2,3,4]
break,continue在for ... in ...语句中也可以使用

### while循环

==只要条件满足就不断循环直至条件不满足==

```python
#利用循环依次对list中的每个名字打印出Hello, xxx!
names = ['Alice', 'Bob', 'Charlie', 'David']
#用两种循环语句，for和while，分别实现上述功能
for name in names:
    print('Hello,',name+'!')
	print('Hello,%s!'%name)   #另一种形式
#while语句
i=0
while i < len(names):
    print('Hello,',names[i]+'!')
    i =i+ 1
```

#### break语句（提前退出循环）

break可以==**提前退出循环**==(举个例子)

```python
n=1
while n<=100:
    if n>10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n=n+1
print('end')#注意:只有这个语句不在while循环内,即n=11时,if满足,执行break后直接到这一行的print()语句,而不执行打印当下n值和自增语句
```

#### continue语句（跳过当次循环执行下一次循环）

continue可以跳过当前这次循环直接开始下一次循环

```python
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # if 为真，执行 continue，回到 while继续下一轮循环，后续的print()语句不会执行
    print(n)
#注意不要陷入死循环，把自增操作放到continue后面很容易进入死循环，此时可以用Crtl+C退出程序
n = 0
while n < 10:
    if n % 2 == 0:
        continue
    n = n + 1 #这就陷入死循环
    #解释：n=0进入if判断为True，执行continue重回while，跳过了自增和print()，那么此时n仍然为0，这就陷入了死循环
    print(n)
    
#死循环再例 excises7_1.py   逻辑未补全造成死循环
def trim(s):
    m=0
    while m <= len(s):
        if s[m:m+1] == ' ':  # 如果是空格
            m += 1
            continue  # 跳过当前迭代，进入下一次
        break   #注意：这一行是后面加的，作用是非空格时直接终止循环，用于补全逻辑
				#重点：如果不是空格，这里没有任何操作！  被contiune跳过了呢
#当遇到非空格字符时，if 条件不成立，代码会跳过m +=1和continue，直接回到 while 循环的判断条件。此时m的值没有变化，m <= len(s)的条件永远成立 ，就陷入了死循环。
#综上可见，死循环就是自增值未发生改变而导致的，无关乎continue执行与否，而是循环没有终止。为了避免死循环，一定要确保循环有退出条件。
```

==`continue`和`break`这两个语句通常要搭配if使用==

## 5.7.dict和set

### 字典 dict（键-值）

全称dictionary，使用键-值（key-value）存储，可以**快速查找**

除了**初始化**时将数据放入dict的方法，还可以**通过key放入**

一个key只能对应一个值，只显示最近的更新值

如果key不存在，dict就会报错，因此可以用in或get()判断key是否存在

```python
d={'Michael':95,'Bob':75,'Tracy':85}
print('A' in d)  #False
print(d.get('A',-1))   #-1,若不指定返回值则返回None
print(d.get('Michael'))   #输出为95
```

想要删除一个key，用pop(key)，对应的value也会从dict中删除

**dict用空间换时间**，dict的**key必须是不可变对象**，因为dict根据key来计算value的存储位置（哈希算法） 

Python中字符串、整数等都不可变，但是list可变不能作为key，最常用的key是字符串

要将由多个元组tuple构成的列表转换为字典，可以利用 Python 中字典的创建特性。如果列表中的每个元组包含两个元素（键和值），可以直接使用 dict() 函数进行转换。

```python
#列表转换为字典
tuple_list = [('a', 1), ('b', 2), ('c', 3)]
dict(tuple_list)={'a': 1, 'b': 2, 'c': 3}
#处理包含多个元素的元组
multi_element_list = [('a', 1, 'x'), ('b', 2, 'y'), ('c', 3, 'z')]
#只取每个元组的前两个元素作为键值对
result_dict = dict((item[0], item[1]) for item in multi_element_list)
```

### set（键的集合，无值）

和dict类似，是一组key的集合，但不存储value（这是与dict的唯一区别），set中没有重复的key

要创建一个set，用`{x,y,z,...}`列出每个元素：

```plain
>>> s = {1, 2, 3}
>>> s
{1, 2, 3}
```

或者提供一个list作为输入集合：

```plain
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
```

注意，传入的参数`[1, 2, 3]`是一个list，而显示的`{1, 2, 3}`只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。

重复元素在set中自动被过滤：

```plain
>>> s = {1, 1, 2, 2, 3, 3}
>>> s
{1, 2, 3}
```

通过`add(key)`方法可以添加元素到set中，可以重复添加，但不会有效果：

```plain
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
```

通过`remove(key)`方法可以删除元素：

```plain
>>> s.remove(4)
>>> s
{1, 2, 3}
```

**set可以看成数学意义上的无序和无重复元素的集合**，因此，两个set可以做数学意义上的交集、并集等操作：

```plain
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
```

set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。

### 不可变对象&可变对象

一旦创建，值不可变；一旦修改，就会创建新对象 int\float\bool\str\tuple

可变对象：创建后可以修改值，但不会创建新对象

对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

```plain
>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']
```

而对于不可变对象，比如str，对str进行操作呢：

```plain
>>> a = 'abc'
>>> a.replace('a', 'A')
'Abc'
>>> a
'abc'
```

虽然字符串有个`replace()`方法，也确实变出了`'Abc'`，但变量`a`最后仍是`'abc'`，应该怎么理解呢？

我们先把代码改成下面这样：

```plain
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'
```

要始终牢记的是，`a`是变量，而`'abc'`才是字符串对象！有些时候，我们经常说，对象`a`的内容是`'abc'`，但其实是指，`a`本身是一个变量，它指向的对象的内容才是`'abc'`：

```
┌───┐     ┌───────┐
│ a │────▶│ 'abc' │
└───┘     └───────┘
```

当我们调用`a.replace('a', 'A')`时，实际上==调用方法`replace`是作用在字符串对象`'abc'`上的==，而这个方法虽然名字叫`replace`，但却没有改变字符串`'abc'`的内容。相反，==`replace`方法创建了一个新字符串`'Abc'`并返回==，如果我们用变量`b`指向该新字符串，就容易理解了，变量`a`仍指向原有的字符串`'abc'`，但变量`b`却指向新字符串`'Abc'`了：

```
┌───┐     ┌───────┐
│ a │────▶│ 'abc' │
└───┘     └───────┘
┌───┐     ┌───────┐
│ b │────▶│ 'Abc' │
└───┘     └───────┘
```

所以，==对于不变对象来说，调用对象自身的任意方法，也不会改变该对象**自身的内容**==。相反，这些方法会**创建新的对象并返回**，这样，就保证了不可变对象本身永远是不可变的。

---

# 第六章 函数

函数就是最基本的一种代码抽象的方式

## 6.1.调用函数

对于Python的内置函数，可以直接从Python的官方网站[查看内置函数](https://docs.python.org/3/library/functions.html)，也可以在交互式命令行通过`help(abs)`查看`abs`函数的帮助信息。

确保传入的参数数量是对的，比如abs()，只能放入一个参数而且参数类型要被接受，比如当出现abs(1,2) abs('a')等等时就会报错

### 数据类型转换

int()可以把其他数据类型转换为整数

函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

```plain
>>> a = abs #变量a指向abs函数
>>> a(-1) #所以也可以通过a调用abs函数
1
```

## 6.2.定义函数

### def语句定义函数

定义一个函数要使用`def`语句，依次写出==**函数名、括号、括号中的参数和冒号`:`**==，然后，在缩进块中编写函数体，==函数的返回值用`return`语句返回==。

以自定义一个求绝对值的`my_abs`函数为例：

```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))
```

函数体的内部语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回

如果没有return语句，函数执行完毕后也会返回结果，但结果为None

在Python交互环境中定义函数时，注意Python会出现`...`的提示。函数定义结束后需要按两次回车重新回到`>>>`提示符下：

```
┌─────────────────────────────────────────────────────────┐
│Windows PowerShell                                 - □ x │
├─────────────────────────────────────────────────────────┤
│>>> def my_abs(x):                                       │
│...     if x >= 0:                                       │
│...         return x                                     │
│...     else:                                            │
│...         return -x                                    │
│...                                                      │
│>>> my_abs(-9)                                           │
│9                                                        │
│>>>                                                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

如果你已经把`my_abs()`的函数定义保存为`abstest.py`文件了，那么，可以在该**文件的当前目录下**启动Python解释器，用`from abstest import my_abs`来导入`my_abs()`函数，注意`abstest`是文件名（不含`.py`扩展名）：

```
┌─────────────────────────────────────────────────────────┐
│Windows PowerShell                                 - □ x │
├─────────────────────────────────────────────────────────┤
│>>> from abstest import my_abs                           │
│>>> my_abs(-9)                                           │
│9                                                        │
│>>>                                                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 空函数  pass语句

定义一个什么事也不做的空函数，可以用`pass`语句：

```python
def nop():
    pass
```

`pass`可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个`pass`，让代码能运行起来。

`pass`还可以用在其他语句里，比如：

```python
if age >= 18:
    pass
```

缺少了`pass`，代码运行就会有语法错误

### 参数检查

调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
不过参数类型不对时，Python解释器就无法帮我们检查。（内置函数会检查出参数错误，自定义函数则不会，因此说明我们的自定义函数不够完善，需要修改自定义函数的定义，增加对参数类型的检查）
数据类型检查可以用内置函数isinstance()实现:

```python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
```

### 多个返回值

返回多个值 Python函数返回多值本质上就是返回一个tuple

函数体内部可以用`return`随时返回函数结果；

函数执行完毕也没有`return`语句时，自动`return None`

## 6.3.函数的参数

定义函数时，把参数的名字和位置确定下来后函数的接口定义就完成了

### 位置参数

调用参数时传入的两个值**按照位置顺序依次赋给参数变量**

```python
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

对于这个修改后的`power(x, n)`函数，可以计算任意n次方：

```plain
>>> power(5, 2)
25
>>> power(5, 3)
125
```

修改后的`power(x, n)`函数有两个参数：`x`和`n`，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数`x`和`n`。

### 默认参数

默认参数一定一定要设置为*==**不可变对象**==*

简化函数调用，在定义函数时给定默认值，只输入一个必选参数时，另一个参数就按默认的给定

- **==注意事项：①必选参数在前，默认参数在后；②设置默认参数（变化小的参数）==**

默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。

```python
#对于一个学生信息注册程序，设置默认年龄和城市，减少参数传入
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
```

大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：

```plain
>>> enroll('Sarah', 'F')
name: Sarah
gender: F
age: 6
city: Beijing
```

只有与默认参数不符的学生才需要提供额外的信息：

```python
enroll('Bob', 'M', 7)  # 按顺序提供默认参数,city参数没有提供仍然使用默认值
enroll('Adam', 'M', city='Tianjin')   # 按顺序提供默认参数
```

有多个默认参数时，调用的时候，既可以按顺序提供默认参数（无须提供参数名，按顺序即可），也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。

> ==**默认参数如果使用不当也会掉坑里**==

先定义一个函数，传入一个list，添加一个`END`再返回：

```python
def add_end(L=[]):
    L.append('END')
    return L
```

当你正常调用时，结果似乎不错：

```plain
>>> add_end([1, 2, 3])
[1, 2, 3, 'END']
>>> add_end(['x', 'y', 'z'])
['x', 'y', 'z', 'END']
```

当你使用默认参数调用时，一开始结果也是对的：

```plain
>>> add_end()
['END']
```

但是，再次调用`add_end()`时，结果就不对了：

```plain
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
```

默认参数是`[]`，但是函数似乎每次都“记住了”上次添加了`'END'`后的list。

原因解释如下：

Python函数在定义的时候，默认参数`L`的值就被计算出来了，即`[]`，因为默认参数`L`也是一个变量，它指向对象`[]`，每次调用该函数，如果改变了`L`的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的`[]`了。

要修改上面的例子，我们可以用`None`这个不变对象来实现：

```python
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

现在，无论调用多少次，都不会有问题：

```plain
>>> add_end()
['END']
>>> add_end()
['END']
```

为什么要设计`str`、`None`这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。

### 可变参数 *args   接收tuple

传入参数的个数可变 

*args可变参数，args接收一个tuple

可变参数就是传入的**参数个数是可变**的，可以为任意个参数，这些可变参数在函数**调用时组装为一个tuple**
比如：计算a^2^ + b^2^ + c^2^ + ……
要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：

```python
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

但是调用的时候，需要先组装出一个list或tuple：

```plain
>>> calc([1, 2, 3])
14
>>> calc((1, 3, 5, 7))
84
```

如果利用可变参数，调用函数的方式可以简化成这样：

```plain
>>> calc(1, 2, 3)
14
```

所以，我们把函数的参数改为可变参数：

```python
def calc(*numbers):    #无非就是在参数numbers前多了一个*
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

在函数内部，参数numbers接收到的是一个tuple。但是，调用该函数时，可以传入任意个参数，包括0个参数。

如果已经有一个list或者tuple，要调用一个可变参数时，可以在list或tuple前面加一个`*`号，把list或tuple的元素变成可变参数传进去：

```plain
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
```

`*nums`表示把`nums`这个list的所有元素作为可变参数传进去。

### 关键字参数 **kw  接收dict

**kw关键字参数，kw接收一个dict

**==*###区分于可变参数###*==**

|          可变参数 *args           |         关键字参数 **kw          |
| :-------------------------------: | :------------------------------: |
| 函数调用时组装为一个==**tuple**== | 函数调用时组装为一个**==dict==** |
|          传入任意个参数           | 传入任意个==**含参数名**==的参数 |

举个例子吧！

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

函数`person`除了必选参数`name`和`age`外，还接受关键字参数`kw`。在调用该函数时，可以==只传入必选参数==：

```plain
>>> person('Michael', 30)
name: Michael age: 30 other: {}
```

也可以传入==任意个数的关键字参数==：

```plain
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```

关键字参数它可以扩展函数的功能。比如，在`person`函数里，我们保证能接收到`name`和`age`这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。

和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：

```plain
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

当然，上面复杂的调用可以用简化的写法：

```plain
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

`**extra`表示把`extra`这个dict的所有key-value用关键字参数传入到函数的`**kw`参数，`kw`将获得一个dict，注意`kw`获得的dict是`extra`的一份==拷贝==，对`kw`的改动不会影响到函数外的`extra`。

### 命名关键字参数

对于关键字参数，函数的调用者可以==**传入任意不受限制的关键字参数**==。在函数内部可以通过`kw`检查知道到底传入了哪些关键字参数

以`person()`函数为例，我们希望检查是否有`city`和`job`参数：

```python
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
```

但是调用者仍可以传入不受限制的关键字参数：

```plain
>>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
```

如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收`city`和`job`作为关键字参数。这种方式定义的函数如下：

```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```

和关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，==`*`后面的参数被视为**命名关键字参数**==。

```plain
#调用方式如下
>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer
```

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了：

```python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```

**==命名关键字参数必须传入参数名==**，这和位置参数不同。如果没有传入参数名，调用将报错：

```plain
>>> person('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
```

由于调用时缺少参数名`city`和`job`，Python解释器把前两个参数视为位置参数，后两个参数传给`*args`，但缺少命名关键字参数导致报错。

命名关键字参数可以有缺省值，从而简化调用：

```python
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
```

由于命名关键字参数`city`具有默认值，调用时，可不传入`city`参数：

```plain
>>> person('Jack', 24, job='Engineer')
Jack 24 Beijing Engineer
```

使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个`*`作为特殊分隔符。如果缺少`*`，Python解释器将无法识别位置参数和命名关键字参数：

```python
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
```

### 参数组合

必选参数、默认参数、可变参数、关键字参数、命名关键字参数可以组合使用
但是参数定义的顺序（优先级）必须是：必选参数、默认参数、可变参数、命名关键字参数、关键字参数比如定义一个函数，包含上述若干种参数：

```python
def f1(a, b, c=0, *args, **kw):  #位置参数a,b;默认参数c;可变参数;关键字参数
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```

在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

```plain
>>> f1(1, 2)  #按照默认位置依次传递给a,b
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)  #c的数值改变
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')   #关键字参数调用时是字典形式
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
```

最神奇的是通过一个tuple和dict，你也可以调用上述函数：

```plain
>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```

==对于任意函数，都可以通过类似`func(*args, **kw)`的形式调用它，无论它的参数是如何定义的。==

## 6.4.递归函数

函数内部可以调用其他函数，当一个==函数在内部调用自己本身==时，这个函数就是**递归函数**

比如n！，用fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。

于是，`fact(n)`用递归的方式写出来就是：

```python
def fact(n):
    if n==1:
        return 1 #函数体的内部语句一旦执行到return时，函数就执行完毕，并返回结果
    return n * fact(n - 1)
```

如果我们计算`fact(5)`，可以根据函数定义看到计算过程如下：

```
=> fact(5)
=> 5 * fact(4)
=> 5 * (4 * fact(3))
=> 5 * (4 * (3 * fact(2)))
=> 5 * (4 * (3 * (2 * fact(1))))
=> 5 * (4 * (3 * (2 * 1)))
=> 5 * (4 * (3 * 2))
=> 5 * (4 * 6)
=> 5 * 24
=> 120
```

递归函数的优点是定义简单，逻辑清晰。理论上，==所有的递归函数都可以写成循环的方式==，但循环的逻辑不如递归清晰。

使用递归函数需要==**注意防止栈溢出**==。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试`fact(1000)`：

```plain
>>> fact(1000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in fact
  ...
  File "<stdin>", line 4, in fact
RuntimeError: maximum recursion depth exceeded in comparison
```

解决递归调用栈溢出的方法是通过==**尾递归**==优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

### 尾递归(等价于循环)

**==尾递归==**：**在函数返回的时候，==调用自身本身==，并且return语句不包含表达式**。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

上面的`fact(n)`函数由于`return n * fact(n - 1)`引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是==要把每一步的乘积传入到递归函数中==：

```python
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
```

`return fact_iter(num - 1, num * product)`仅返回递归函数本身，`num - 1`和`num * product`在函数调用前就会被计算，不影响函数调用。

`fact(5)`对应的`fact_iter(5, 1)`的调用如下：

```
=> fact_iter(5, 1)
=> fact_iter(4, 5)
=> fact_iter(3, 20)
=> fact_iter(2, 60)
=> fact_iter(1, 120)
=> 120
```

尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的`fact(n)`函数改成尾递归方式，也会导致栈溢出。

Python中任何递归函数都存在栈溢出的问题。

---

# 第七章 高级特性

**代码越少，开发效率越高**

## 7.1.切片

在`list`或`tuple`中取部分元素，对于取指定索引范围的操作用循环十分繁琐。切片`Slice`能简化这种操作

比如取一个`list L`中的前三个元素，用`L[0:3]`即可，表示索引从0开始直到索引3为止，但不包括索引3

`L[0:3]=L[:3]`,索引从0开始则0可以省略

Python支持倒数切片，**倒数第一个元素的索引为-1**

```plain
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
>>> L[-2:]
['Bob', 'Jack']
L[-2:-1]
['Bob']
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[-2:]
['Bob', 'Jack']
L[-2:-1]
['Bob']
```

**==注意L[-1:-0]的返回值为空字符串，即结果为[]==**

切片操作十分有用

```plain
#我们先创建一个0-99的数列：
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, ..., 99]
```

```plain
#可以通过切片轻松取出某一段数列。比如前10个数：
>>> L[:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```plain
#前10个数，每两个取一个：
>>> L[:10:2]
[0, 2, 4, 6, 8]
```

```plain
#所有数，每5个取一个：
>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
```

```plain
#只写[:]就可以原样复制一个list：
>>> L[:]
[0, 1, 2, 3, ..., 99]
```

tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

```plain
>>> (0, 1, 2, 3, 4, 5)[:3]
(0, 1, 2)
```

这里==**注意**==，`[:2]`表示从数字下标0取到2，`[::2]`第一个冒号表示取所有数，第二个冒号`:2`表示每两个取一个

字符串`'xxx'`也可以看成是一种list，每个元素就是一个字符。字符串也可以用切片操作，只是操作结果仍是字符串：

```plain
>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[::2]
'ACEG'
```

在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。

## 7.2迭代

对于一个给定的`list`或`tuple`，可以用`for...in`循环来遍历(Python)，这种遍历就是==**迭代`Iteration`**==
Python的for循环不仅可以用于list和tuple上，还可以作用于其他可迭代对象上（只要是可迭代对象，for循环就可以正常运行）
==**对于可迭代对象，不论是否有下标，都可以迭代**==

```plain
#迭代字典dict
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
...
a
c
b
```

因为`dict`的存储不是按照`list`的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

- 默认情况下，`dict`迭代的是key;

- 如果要迭代value，可以用`for value in d.values()`;

- 如果要同时迭代key和value，可以用`for k, v in d.items()`。

由于字符串也是可迭代对象，因此，也可以作用于`for`循环：

```plain
>>> for ch in 'ABC':
...     print(ch)
...
A
B
C
```

所以，当我们使用`for`循环时，只要作用于一个**可迭代对象**，`for`循环就可以正常运行，而我们不太关心该对象究竟是`list`还是其他数据类型。

### 判断可迭代对象

通过` collections.abc `模块的` Iterable `类型判断
```plain
>>> from collections.abc import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
```

如果要对`list`实现类似Java那样的下标循环怎么办？Python内置的`enumerate`函数可以把一个`list`变成**==索引-元素==**对，这样就可以在`for`循环中同时迭代索引和元素本身：

```plain
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
```

上面的`for`循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：

```plain
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print(x, y)
...
1 1
2 4
3 9
```

## 7.3.列表生成式

列表生成式 List Comprehensions   是可以用于**创建list的生成式**

比如 [1,2,3,4]可以用list(range(1,5))创建
<!--range(x1,x2)中x1表示开始的数，x2表示有几个数-->

但是[1x1,2x2,3x3,...,10x10]如何创建呢

- 方法一，循环：

```python
L=list(range(1,11)) #[1,2,3,4,5,6,7,8,9,10]
n=0
for i in L:
    L[n]=i*i
    n+=1
print(L)
#另一种方法
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
```

- 方法二，列表生成式

列表生成式可以用一行语句代替循环生成上面的list：

```plain
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

写列表生成式时，把要生成的元素`x * x`放到前面，后面跟`for`循环，就可以把list创建出来，十分有用

for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

```plain
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
```

还可以使用两层循环，可以生成全排列：

```plain
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

```plain
>>> import os # 导入os模块，模块的概念后面讲到
>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
```

`for`循环其实可以同时使用两个甚至多个变量，比如`dict`的`items()`可以同时**迭代**key和value：

```plain
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k, v in d.items():
...     print(k, '=', v)
...
y = B
x = A
z = C
```

因此，列表生成式也可以使用两个变量来生成list：

```plain
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']
```

把一个list中所有的字符串变成小写：

```plain
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
```

将一个整数的每一位数字转换为列表的方法:
先将整数转为字符串，再遍历每个字符并转换回整数：

```python
num = 12345
digit_list = [int(d) for d in str(num)]
print(digit_list)  # 输出: [1, 2, 3, 4, 5]
```

### 列表生成式的if...else用法
以下代码能正常输出偶数：

```plain
>>> [x for x in range(1, 11) if x % 2 == 0]
[2, 4, 6, 8, 10]
```

但是，我们**不能**在最后的`if`加上`else`：

```plain
>>> [x for x in range(1, 11) if x % 2 == 0 else 0]
  File "<stdin>", line 1
    [x for x in range(1, 11) if x % 2 == 0 else 0]
                                              ^
SyntaxError: invalid syntax
```

这是因为跟在`for`后面的`if`是一个**筛选条件**，不能带`else`，否则如何筛选呢？

如果把`if`写在`for`前面则**必须**加`else`，否则报错：

```plain
>>> [x if x % 2 == 0 for x in range(1, 11)]
  File "<stdin>", line 1
    [x if x % 2 == 0 for x in range(1, 11)]
                       ^
SyntaxError: invalid syntax
```

这是因为`for`前面的部分是一个**表达式**，它必须根据`x`计算出一个结果。考察表达式：`x if x % 2 == 0`，它无法根据`x`计算出结果，因为缺少`else`，必须加上`else`：

```plain
>>> [x if x % 2 == 0 else -x for x in range(1, 11)]
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
```

上述`for`前面的表达式`x if x % 2 == 0 else -x`才能根据`x`计算出确定的结果。

==可见，在一个列表生成式中，`for`前面的`if ... else`是**表达式（必须计算出结果）**，而`for`后面的`if`是**过滤（筛选）条件**，不能带`else`。==

## 7.4.生成器 generator（保存算法）

由于内存限制，**列表容量肯定是有限**的。当创建一个大列表并且只访问了前面几个元素时，后面大部分元素占用的空间被白白浪费了

设想，如果==列表元素可以按照某种算法推算==出来，那么可以在循环过程中**不断**推算出后续的元素，这样就不需要创建完整的list，从而节省了大量的空间。

生成器的优势:惰性计算(只在需要时生成下一行,不占用大量内存);无限序列(无限生成,可以用while true语句);简洁优雅,逻辑清晰.

生成器generator可以做到一边循环一边计算

### 生成器的创建

#### 方法一，把列表生成式的`[]`改成`()`：

```plain
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>
```

创建`L`和`g`的区别仅在于最外层的`[]`和`()`，`L`是一个list，而`g`是一个generator。

- 打印出generator的每一个元素

如果要一个一个打印出来，可以通过`next()`函数获得generator的下一个返回值：

```plain
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> next(g)
16
>>> next(g)
25
>>> next(g)
36
>>> next(g)
49
>>> next(g)
64
>>> next(g)
81
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

generator保存的是**算法**，每次调用`next(g)`，就计算出`g`的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出`StopIteration`的错误。

正确的方法调用`next(g)`是使用`for`循环，因为generator也是可迭代对象：

```plain
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)
... 
0
1
4
9
16
25
36
49
64
81
```

所以，我们创建了一个generator后，基本上永远不会调用`next()`，而是通过`for`循环来迭代它，并且不需要关心`StopIteration`的错误。

#### 方法二，函数实现生成器(函数定义中包括yield关键字)

当generator用类似列表生成式的`for`循环无法实现的时候，还可以用函数来实现。

比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
```

**==*注意*==**，赋值语句：

```python
a, b = b, a + b
```

相当于：

```python
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
```

但不必显式写出临时变量t就可以赋值。

上面的函数可以输出斐波那契数列的前N个数：

```plain
>>> fib(6)
1
1
2
3
5
8
'done'
```

`fib`函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和generator仅一步之遥。要把`fib`函数变成generator函数，只需要把`print(b)`改为`yield b`就可以了：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
```

这就是定义generator的另一种方法。如果一个函数定义中包含`yield`关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator：

```plain
>>> f = fib(6)
>>> f
<generator object fib at 0x104feaaa0>
```

**==generator函数和普通函数的执行流程不一样==**：普通函数是**顺序执行**，遇到`return`语句或者最后一行函数语句就返回。而变成generator的函数，在**每次调用`next()`的时候执行**，遇到`yield`语句返回，再次执行时从上次返回的`yield`语句处继续执行。

举个简单的例子，定义一个generator函数，依次返回数字1，3，5：

```python
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
```

调用该generator函数时，首先要生成一个generator对象，然后用`next()`函数不断获得下一个返回值：

```plain
>>> o = odd()
>>> next(o)
step 1
1
>>> next(o)
step 2
3
>>> next(o)
step 3
5
>>> next(o)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

可以看到，`odd`不是普通函数，而是generator函数，在执行过程中，**遇到`yield`就中断，下次又继续执行**。执行3次`yield`后，已经没有`yield`可以执行了，所以，第4次调用`next(o)`就报错。

***==注意==***：调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。

当这样调用`next()`每次都返回1：

```plain
>>> next(odd())
step 1
1
>>> next(odd())
step 1
1
>>> next(odd())
step 1
1
```

原因在于`odd()`会创建一个新的generator对象，上述代码实际上创建了3个完全独立的generator，对3个generator分别调用`next()`当然每个都会返回第一个值。

正确的写法是创建一个generator对象，然后不断对这一个generator对象调用`next()`：

```plain
>>> g = odd()
>>> next(g)
step 1
1
>>> next(g)
step 2
3
>>> next(g)
step 3
5
```

回到`fib`的例子，我们在循环过程中不断调用`yield`，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。

同样的，把函数改成generator函数后，我们基本上从来不会用`next()`来获取下一个返回值，而是直接使用`for`循环来迭代：

```plain
>>> for n in fib(6):
...     print(n)
...
1
1
2
3
5
8
```

但是用`for`循环调用generator时，发现拿不到generator的`return`语句的返回值。如果想要拿到返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中：

```plain
>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done
```

**==小结==**
generator的工作原理就是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。

对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

区分普通函数和generator函数，普通函数调用直接返回结果：

```plain
>>> r = abs(6)
>>> r
6
```

generator函数的调用实际返回一个generator对象：

```plain
>>> g = fib(6)
>>> g
<generator object fib at 0x1022ef948>
```

## 7.5.迭代器

### 可迭代对象 Iterable

可以直接作用于for循环的数据类型

- 集合数据类型，如l`ist`列表、`tuple`元组、`dict`字典、`set`<!--只有key没有value-->、`str`字符串等；

- generator，包括生成器和带`yield`的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：`Iterable`。

可以使用`isinstance()`判断一个对象是否是`Iterable`对象：

```plain
>>> from collections.abc import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
```

### 迭代器 Iterator

生成器不但可以作用于`for`循环，还可以被`next()`函数不断调用并返回下一个值，直到最后抛出`StopIteration`错误表示无法继续返回下一个值了

可以被`next()`函数调用并不断返回下一个值的对象称为迭代器：`Iterator`。

可以使用`isinstance()`判断一个对象是否是`Iterator`对象：

```plain
>>> from collections.abc import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。

想要把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter()`函数：

```plain
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

那么为什么`list`、`dict`、`str`等数据类型不是`Iterator`？

这是因为Python的`Iterator`对象表示的是一个**数据流**，==`Iterator`对象可以被`next()`函数调用并不断返回下一个数据==，直到没有数据时抛出`StopIteration`错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过`next()`函数实现按需计算下一个数据，所以`Iterator`的计算是**==惰性==**的，只有在需要返回下一个数据时它才会计算。==yield==

`Iterator`甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

**小结**

凡是可作用于`for`循环的对象都是`Iterable`类型；

凡是可作用于`next()`函数的对象都是`Iterator`类型，它们表示一个惰性计算的序列；

集合数据类型如`list`、`dict`、`str`等是`Iterable`但不是`Iterator`，不过可以通过`iter()`函数获得一个`Iterator`对象。

Python的`for`循环本质上就是通过不断调用`next()`函数实现的，例如：

```python
for x in [1, 2, 3, 4, 5]:
    pass
```

实际上完全等价于：

```python
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```

---

# 第八章 函数式编程

函数是Python内建支持的一种封装，通过把大段代码拆成函数再用一层层的函数调用，就可以简化复杂任务，这种分解就是面向过程的程序设计。函数就是面向过程的程序设计的基本单元

函数式编程`Functional Programming`，也可以归结到面向过程的程序实际，但它的思想更接近数学计算

**==计算机&&计算==**

- 计算机中，CPU执行指令，汇编语言是最贴近计算的语言

- 计算，指的是数学意义上的计算，越抽象的计算离计算机硬件越远

函数式编程是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量。因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程:确定的输入能得到确定的输出.

==函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！==

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

## 8.1.高阶函数

### 高阶函数概念总览

`Higher-order function`高阶函数

把函数作为参数传入，这样的函数就是高阶函数，函数式编程就是指这种高度抽象的编程范式

**==变量可以指向函数==**
abs(-10)是函数调用，abs是函数本身
要获得函数调用的结果，可以把结果赋值给变量  x=abs(-10)
函数本身可以赋值给变量，即**变量可以指向函数**
如果一个变量指向了一个函数，那么可以用这个变量来调用函数

```plain
>>> f = abs
>>> f(-10)
10
#f已经指向了abs函数本身，直接调用函数abs()和调用变量f()完全相同
```

**==函数名也是变量==**

**函数名就是指向函数的变量**，对于`abs()`这个函数，完全可以把函数名`abs`看成变量，它指向一个可以计算绝对值的函数   比如可以让变量`abs`指向一个整数` abs=10`，但一般不这么写

**注**：由于`abs`函数实际上是定义在`import builtins`模块中的，所以要让修改`abs`变量的指向在其它模块也生效，要用`import builtins; builtins.abs = 10`

==**传入函数**==

变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个用变量指向的函数作为参数，即为高阶函数

**个人理解**：函数的参数能接受变量，变量能指向函数（比如`f=abs`，则`f()=abs()`）,高阶函数无非就是多层函数，一层套一层。在数学中就是复合函数

一个最简单的高阶函数

```python
f=abs
def add(x, y, f):
    return f(x) + f(y)
```

当我们调用`add(-5, 6, abs)`时，参数x，y和f分别接收-5，6和`abs`，根据函数定义，我们可以推导计算过程为：
x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
编写高阶函数就是让函数的参数能接收别的函数

### 8.1.1 map/reduce

Python内建了`map()`和`reduce()`函数。

Google大名鼎鼎的论文“[MapReduce: Simplified Data Processing on Large Clusters](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)”，能解释map/reduce的概念。

#### map

- `map()`函数接收两个参数，一个是函数，一个是`Iterable`，`map`将**传入的函数依次作用到可迭代对象的序列的每个元素**，并把结果作为新的迭代器`Iterator`返回。
  - 释义：`map()`中有两个输入值：函数和可迭代对象；一个输出值：迭代器

举例说明，比如我们有一个函数f(x)=x^2^，要把这个函数作用在一个list `[1, 2, 3, 4, 5, 6, 7, 8, 9]`上，就可以用`map()`实现如下：

```
            f(x) = x * x

                  │
                  │
  ┌───┬───┬───┬───┼───┬───┬───┬───┐
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

[ 1   2   3   4   5   6   7   8   9 ]

  │   │   │   │   │   │   │   │   │
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

[ 1   4   9  16  25  36  49  64  81 ]
```

现在，我们用Python代码实现：

```plain
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

`map()`传入的第一个参数是`f`，即函数对象本身。由于结果`r`是一个`Iterator`，`Iterator`是惰性序列，因此通过`list()`函数让它把整个序列都计算出来并返回一个list。

你可能会想，不需要`map()`函数，写一个循环，也可以计算出结果：

```python
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
```

的确可以，但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？

所以，`map()`作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x^2^，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：

```plain
>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

只需要一行代码。

#### reduce

- `reduce`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算，其效果就是：

```python
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

比方说对一个序列求和，就可以用`reduce`实现：

```plain
>>> from functools import reduce
>>> def add(x, y):
...     return x + y
...
>>> reduce(add, [1, 3, 5, 7, 9])
25
```

当要把序列`[1, 3, 5, 7, 9]`变换成整数`13579`时，`reduce`就可以派上用场：

```plain
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> reduce(fn, [1, 3, 5, 7, 9])
13579
```

这个例子本身没多大用处，但是，如果考虑到字符串`str`也是一个序列，对上面的例子稍加改动，配合`map()`，我们就可以写出把`str`转换为`int`的函数：

```plain
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2num(s):
...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
...     return digits[s]
...
>>> reduce(fn, map(char2num, '13579'))
13579
```

```python
def char2num(s):
     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
     return digits[s]

print(list(map(char2num, '13579')))
#结果[1, 3, 5, 7, 9]，要用list()把map()生成的迭代器转换为list，即把整个序列都计算出来并返回一个list。
```

整理成一个`str2int`的函数就是：

```python
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
```

还可以用lambda函数进一步简化成：

```python
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
```

也就是说，假设Python没有提供`int()`函数，那么完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！

[lambda函数](#8.3 匿名函数)的用法在匿名函数中有介绍

- 小结
  - `map`用于将一个函数作用于一个序列，以此得到另一个序列；
  - `reduce`用于将一个函数依次作用于**上次计算的结果**和**序列的下一个元素**，以此得到最终结果。

### 8.1.2 filter

Python内建的`filter()`函数用于过滤序列。

和`map()`类似，`filter()`也接收一个函数和一个序列。和`map()`不同的是，`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。

例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

```python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
```

把一个序列中的空字符串删掉，可以这么写：

```python
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']
```

可见用`filter()`这个高阶函数，关键在于正确实现一个“筛选”函数。

`filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回`list`。

> 这一点同`map()`函数

下面给出一个``filter()``函数的实际例子。

**==用filter求素数==**

计算[素数](http://baike.baidu.com/view/10626.htm)的一个方法是[埃氏筛法](http://baike.baidu.com/view/3784258.htm)，它的算法理解起来非常简单：

首先，列出从`2`开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数`2`，它一定是素数，然后用`2`把序列的`2`的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数`3`，它一定是素数，然后用`3`把序列的`3`的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数`5`，然后用`5`把序列的`5`的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。

用Python来实现这个算法，可以先构造一个从`3`开始的奇数序列：

```python
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
```

注意这是一个生成器，并且是一个无限序列。

然后定义一个筛选函数：

```python
def _not_divisible(n):
    return lambda x: x % n > 0
```

最后，定义一个生成器，不断返回下一个素数：

```python
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
```

这个生成器先返回第一个素数`2`，然后，利用`filter()`不断产生筛选后的新的序列。

由于`primes()`也是一个无限序列，所以调用时需要设置一个退出循环的条件：

```python
# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
```

注意到`Iterator`是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，代码却非常简洁。

- 小结

`filter()`的作用是从一个序列中筛出符合条件的元素。由于`filter()`使用了惰性计算，所以只有在取`filter()`结果的时候，才会真正筛选并每次返回下一个筛出的元素。

### 8.1.3 sorted

排序`sort`,无论是冒泡排序还是快速排序，排序的核心是比较两个元素的大小

数字自然可以直接比较，但是字符串或者两个字典dict直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来

`sorted()`也是一个高阶函数。用`sorted()`排序的关键在于==**实现一个映射函数**==。

Python内置的`sorted()`函数就可以对list进行排序：

```plain
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```

此外，`sorted()`函数也是一个高阶函数，它还可以接收一个`key`函数来实现自定义的排序，例如按绝对值大小排序：

```plain
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```

key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过`key=abs`处理过的list：

```python
list = [36, 5, -12, 9, -21]

keys = [36, 5,  12, 9,  21]
```

然后`sorted()`函数按照keys进行排序，并按照对应关系返回list相应的元素：

```
keys sort   => [5, 9,  12,  21, 36]
                |  |    |    |   |
result sort => [5, 9, -12, -21, 36]
```

我们再看一个字符串排序的例子：

```plain
>>> sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
```

默认情况下，对字符串排序，是按照ASCII的大小比较的，由于`'Z' < 'a'`，结果，大写字母`Z`会排在小写字母`a`的前面。

现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。

这样，我们给`sorted`传入key函数，即可实现忽略大小写的排序：

```plain
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']
```

要进行反向排序，不必改动key函数，可以传入第三个参数`reverse=True`：

```plain
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```

从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

## 8.2 返回函数

高阶函数除了可以接受函数作为参数，还可以把函数作为结果值返回。

现在想要实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：

```python
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
```

如果不需要立刻求和，而是在后面的代码中，根据需要再计算时则可以不返回求和的结果，而是**返回求和的函数**：

```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
```

当我们调用`lazy_sum()`时，返回的并不是求和结果，而是求和函数：

```plain
>>> f = lazy_sum(1, 3, 5, 7, 9)
>>> f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
```

调用函数`f`时，才真正计算求和的结果：

```plain
>>> f()
25
```

在这个例子中，我们在函数`lazy_sum`中又定义了函数`sum`，并且，内部函数`sum`可以引用外部函数`lazy_sum`的参数和局部变量，当`lazy_sum`返回函数`sum`时，**相关参数和变量都保存在返回的函数中**，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

请再注意一点，当我们调用`lazy_sum()`时，每次调用都会返回一个新的函数，即使传入相同的参数：

```plain
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
```

`f1()`和`f2()`的调用结果互不影响。

### 闭包(内层函数引用了外层函数的局部变量)

注意到返回的函数在其定义内部引用了局部变量`args`，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了`f()`才执行。我们来看一个例子：

```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
```

在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。

你可能认为调用`f1()`，`f2()`和`f3()`结果应该是`1`，`4`，`9`，但实际结果是：

```plain
>>> f1()
9
>>> f2()
9
>>> f3()
9
```

全部都是`9`！原因就在于返回的函数`f()`引用了变量`i`，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量`i`已经变成了`3`，因此最终结果为`9`。

==**注意**==     返回闭包时牢记一点：**返回函数不要引用任何循环变量，或者后续会发生变化的变量**。

如果一定要引用循环变量就要再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
```

再看看结果：

```plain
>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9
```

缺点是代码较长，可利用lambda函数缩短代码。

### nonlocal

使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常：

```python
def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn
# inc() 函数返回内层函数 fn 的引用（注意不是调用结果）
#闭包使得内层函数 fn 能够访问外层函数 inc 的局部变量 x
#即使外层函数 inc 已经执行完毕并返回，变量 x 仍然被保留在闭包中
#当调用 f() 时，会返回 x + 1 的结果，即 1
#需要注意的是，由于 fn 函数只是读取 x 的值而没有修改它。如果尝试在 fn 中修改 x 的值，则需要使用 nonlocal 关键字来声明

f = inc()
print(f()) # 1
print(f()) # 1
```

但是，如果对外层变量赋值，由于Python解释器会把`x`当作函数`fn()`的局部变量，它会报错：

```python
def inc():
    x = 0
    def fn():
        # nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2
```

原因是`x`作为局部变量并没有初始化，直接计算`x+1`是不行的。但我们其实是想引用`inc()`函数内部的`x`，所以需要在`fn()`函数内部加一个`nonlocal x`的声明。加上这个声明后，解释器把`fn()`的`x`看作外层函数的局部变量，它已经被初始化了，可以正确计算`x+1`。

==**提示 **==   使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。

- 小结

一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

## 8.3 匿名函数(关键字lambda)

在传入函数时，有时不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以`map()`函数为例，计算f(x)=x^2^时，除了可以定义一个`f(x)`的函数外，还可以直接传入匿名函数：

```plain
>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

通过对比可以看出，匿名函数`lambda x: x * x`实际上就是：

```python
def f(x):
    return x * x
```

关键字`lambda`表示匿名函数，冒号前面的`x`表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写`return`，返回值就是该表达式的结果。

用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，**匿名函数也是一个函数对象**，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

```plain
>>> f = lambda x: x * x
>>> f
<function <lambda> at 0x101c6ef28>
>>> f(5)
25
```

同样，也可以把匿名函数作为返回值返回，比如：

```python
def build(x, y):
    return lambda: x * x + y * y#返回的是匿名函数,调用时操作为f()

f=build(3,4)#f是一个函数对象.不是函数的执行结果
f()#25
print(f)#<function build.<locals>.<lambda> at 0x105508ae0>
print(f())#25
```

## 8.4 装饰器

### 装饰器概念

装饰器的作用是在不修改原函数的情况下为其增加额外功能

装饰器的本质：`@decorator`放在函数上等于在函数定义时执行decorator(原函数)，并把decorator的返回值赋回原函数名,也就是说装饰器在“定义/导入时”被调用一次，不是在函数调用时。

**返回原函数**意味着**装饰器只在装饰时做一件事**（例如打印、注册、记录元数据），**然后返回原函数本身**，**保持函数调用行为不变**。返回原函数表示==“不包装、不替换”==，仅在定义阶段产生副作用

**返回一个 wrapper**（封装函数），则原函数名会被替换为 wrapper，后续**每次调用都会执行 wrapper 中的额外逻辑**（比如在调用前后打印时间），这是==“运行时增强”==的常见做法。

> 以上内容详见案例对比分析

由于函数也是一个对象，而且函数对象可以被赋值给变量，因此可以通过变量调用该函数

```plain
>>> def now():
...     print('2024-6-1')
...
>>> f = now
>>> f()
2024-6-1
```

函数对象有一个`__name__`属性（注意：是前后各两个下划线），可以拿到函数的名字：

```plain
>>> now.__name__
'now'
>>> f.__name__
'now'
```

现在，假设我们要增强`now()`函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改`now()`函数的定义，这种在代码运行期间**动态增加功能**的方式，称之为“装饰器”（Decorator）。

==本质上，decorator就是一个返回函数的高阶函数。==所以，我们要定义一个能打印日志的decorator，可以定义如下：

```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper#返回wrapper,每次调用时都会执行wrapper中的额外逻辑
```

观察上面的`log`，它是一个**==decorator：接受一个函数func作为参数并返回一个函数wrapper==**。我们要借助Python的@语法，把decorator置于函数的定义处：

```python
@log    #@log放到now()函数的定义处,相当于执行了语句now = log(now)
def now():
    print('2024-6-1')
```

调用`now()`函数，不仅会运行`now()`函数本身，还会在运行`now()`函数前打印一行日志：

```plain
>>> now()
call now():  #这个是日志
2024-6-1     #这个是return func(*args, **kw)的运行结果（调用原始函数）
```

由于`log()`是一个decorator，返回一个函数`wrapper`，所以，原来的`now()`函数仍然存在，只是现在同名的`now`变量指向了新的函数，于是调用`now()`将执行新函数(返回的wrapper()函数)

`wrapper()`函数的参数定义是`(*args, **kw)`，因此，`wrapper()`函数可以接受任意参数的调用。在`wrapper()`函数内，首先打印日志，再紧接着调用原始函数。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```

这个3层嵌套的decorator用法如下：

```python
@log('execute')
def now():
    print('2024-6-1')
```

执行结果如下：

```plain
>>> now()
execute now():
2024-6-1
```

和两层嵌套的decorator相比，3层嵌套的效果是这样的：

```plain
>>> now = log('execute')(now)
```

我们来剖析上面的语句，首先执行`log('execute')`，返回的是`decorator`函数，再调用返回的函数，参数是`now`函数，返回值最终是`wrapper`函数。

以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有`__name__`等属性，但你去看经过decorator装饰之后的函数，它们的`__name__`已经从原来的`'now'`变成了`'wrapper'`：

```plain
>>> now.__name__
'wrapper'
```

因为返回的那个`wrapper()`函数名字就是`'wrapper'`，所以，需要把原始函数的`__name__`等属性复制到`wrapper()`函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写`wrapper.__name__ = func.__name__`这样的代码，Python内置的`functools.wraps`就是干这个事的，所以，一个完整的decorator的写法如下：

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

或者针对带参数的decorator：

```python
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)   #均是在函数返回值为wrapper，即函数参数为原始函数名的下面第一行定义的
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```

`import functools`是导入`functools`模块。模块的概念稍候讲解。现在，只需记住在定义`wrapper()`的前面加上`@functools.wraps(func)`即可。

- 小结

在面向对象（Object Oriented Programming，OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。

### 案例对比分析（是否改变调用行为）

```python
#装饰时打印，返回原函数（不改变调用行为）  这是一层   装饰器注册/标记机制
def metric(fn):
    # 装饰器函数，接受一个函数fn作为参数
    print('decorate:', fn.__name__)   # 在定义/导入时立即执行，打印被装饰函数的名称
    return fn                       # 直接返回原始函数，不做任何包装

@metric    # 相当于执行语句foo=metric(foo)，在模块加载时就会执行
def foo():
    print('call foo')  # 函数体内容，在调用foo()时才会执行

#输出（导入/定义时）:
#decorate: foo
#调用 foo() 时只会输出:
#call foo
```

```python
#返回 wrapper，改变调用行为（每次调用都会执行额外逻辑）   这是两层   函数增强型装饰器
def log(func):
    # 在 log 内部定义一个包装函数 wrapper，它可以接受任意数量的位置参数 (*args) 和关键字参数 (**kw)
    def wrapper(*args, **kw):
        print('begin call')
        res = func(*args, **kw)   #调用传入的原始函数，这里就是调用原函数bar(),执行print('in bar'),打印出in bar.  func(*args,*kw)是执行原函数bar(),res是一个变量(用于接收原函数执行后的返回值)
        print('end call')
        return res  # 返回原始函数的结果（如果没有显式return，则默认返回 None,这里就没有返回值哦!）    return res的本质是把原函数的返回值“透传”出去,这句话是在wrapper函数的定义内,如果没有这句话,那么不管原函数bar()有无返回值,装饰后的函数调用结果都会是None
    return wrapper  # 返回内部定义的 wrapper 函数对象

# 使用 @log 装饰器修饰 bar 函数
@log     #@log相当于执行语句bar=log(bar)
def bar():#bar函数中无return语句,默认返回None
    print('in bar')

#输出（导入时无打印），调用 bar(): 
#begin call
#in bar
#end call
```

**==两段代码的主要区别==**

1. **装饰器行为不同**：
   - 第一段的 `metric` 装饰器直接==返回原函数==，只是在装饰时打印一条信息
   - 第二段的`log`装饰器==返回一个包装函数 `wrapper==`，改变了原函数的行为
2. **执行时机不同**：
   - 第一段：在模块加载/函数定义时就立即执行打印操作
   - 第二段：只有在调用被装饰函数时才执行额外逻辑（前后打印日志）

## 8.5 偏函数

Python的`functools`模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。这里的偏函数和数学上的偏函数不一样

在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

`int()`函数可以把字符串转换为整数，当仅传入字符串时，`int()`函数默认按十进制转换：

```plain
>>> int('12345')
12345
```

但`int()`函数还提供额外的`base`参数，默认值为`10`。如果传入`base`参数，就可以做N进制的转换：

```plain
>>> int('12345', base=8)
5349
>>> int('12345', 16)
74565
```

假设要转换大量的二进制字符串，每次都传入`int(x, base=2)`非常麻烦，于是，我们想到，可以定义一个`int2()`的函数，默认把`base=2`传进去：

```python
def int2(x, base=2):
    return int(x, base)
```

这样，我们转换二进制就非常方便了：

```plain
>>> int2('1000000')
64
>>> int2('1010101')
85
```

`functools.partial`就是帮助我们创建一个偏函数的，不需要我们自己定义`int2()`，可以直接使用下面的代码创建一个新的函数`int2`：

```plain
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
```

所以，简functools.partial`的作用就是，==把一个函数的**某些参数给固定住**（也就是设置默认值），**返回一个新的函数**，调用这个新函数会更简单。==

注意到上面的新的`int2`函数，仅仅是把`base`参数重新设定默认值为`2`，但也可以在函数调用时传入其他值：

```plain
>>> int2('1000000', base=10)
1000000
```

最后，创建偏函数时，实际上可以接收函数对象、`*args`和`**kw`这3个参数，当传入：

```plain
int2 = functools.partial(int, base=2)
```

实际上固定了int()函数的关键字参数`base`，也就是：

```python
int2('10010')
```

相当于：

```python
kw = { 'base': 2 }
int('10010', **kw)
```

当传入：

```python
max2 = functools.partial(max, 10)
```

实际上会把`10`作为`*args`的一部分自动加到左边，也就是：

```python
max2(5, 6, 7)
```

相当于：

```python
args = (10, 5, 6, 7)
max(*args)
```

结果为`10`

- 小结

当函数的参数个数太多，需要简化时，使用`functools.partial`可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

---

# 第九章 模块

在Python中，一个.py文件就称之为一个模块（Module）

使用模块的好处:

- 提高了代码的可维护性

- 编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。

==使用模块还可以避免函数名和变量名冲突==。**相同**名字的函数和变量完全可以分别存在**不同**的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。但是也要注意，尽量不要与内置函数名字冲突。点[这里](http://docs.python.org/3/library/functions.html)查看Python的所有内置函数。

为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）

举个例子，一个`abc.py`的文件就是一个名字叫`abc`的模块，一个`xyz.py`的文件就是一个名字叫`xyz`的模块

现在，假设我们的`abc`和`xyz`这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如`mycompany`，按照如下目录存放：

```
mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py
```

引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，`abc.py`模块的名字就变成了`mycompany.abc`，类似的，`xyz.py`的模块名变成了`mycompany.xyz`。

请注意，每一个包目录下面都会有一个`__init__.py`的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。`__init__.py`可以是空文件，也可以有Python代码，因为`__init__.py`本身就是一个模块，而它的模块名就是`mycompany`。

类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：

```
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py
```

文件`www.py`的模块名就是`mycompany.web.www`，两个文件`utils.py`的模块名分别是`mycompany.utils`和`mycompany.web.utils`。

==**特别注意**==

自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为`sys.py`，否则将无法导入系统自带的sys模块。

`mycompany.web`也是一个模块，请指出该模块对应的.py文件。

- 总结

  模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

  创建自己的模块时，要注意：

  - 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
  - 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行`import abc`，若成功则说明系统存在此模块。

## 9.1 使用模块

pass



---

# 第十章 面向对象编程

面向对象编程——Object Oriented Programing,OOP  一种程序设计思想，==把对象作为程序的基本单元==，一个对象包含了**数据**和操作数据的**函数**

面向对象的三大特点:**==数据封装、继承、多态==**

## 面向对象和面向过程的区分

**程序设计**：

- **面向过程**：把计算机程序看作一系列的**命令集合**，即**一组函数的顺序执行**。为了简化程序设计，面向过程把函数继续分为子函数，把大块函数通过切割成小块函数来降低系统的复杂度

- **面向对象**：把计算机程序看作一组**对象的集合**，**每个对象都可以接收并处理别的对象发过来的消息**，计算机程序的执行就是一系列消息在各个对象之间传递

Python中所有数据类型都可以视为对象，也可以自定义对象。自定义的对象数据类型就是面向对象中的类class概念

==用一个例子来说明 **面向过程** 和 **面向对象** 在程序流程上的不同之处。==

- 面向过程  一组函数的顺序执行

```python
#假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
#而处理学生成绩可以通过函数实现，比如打印学生的成绩：
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
```

- 面向对象

当采用面向对象的程序设计思想，我们**首选思考的不是程序的执行流程，而是`Student`这种数据类型应该被视为一个==对象==**，这个对象拥有`name`和`score`这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个`print_score`消息，让对象把自己的数据打印出来。

```python
class Student(object):#定义类,作为模板用来创建实例
    def __init__(self, name, score):
	#构造方法,__init__是Python类的构造方法,用Student类创建对象时这个方法会自动执行,用来初始化对象的“属性” 
	#self是必填的第一个参数,代表当前创建的实例对象本身,name和score是传入的参数
        self.name = name#把传入的参数赋值给当前实例的属性
        self.score = score

    def print_score(self):
	#实例方法,代表对象的行为
        print('%s: %s' % (self.name, self.score))
#用Student类封装了“学生”的特征(name、score属性)和行为(print_score方法)
#每一个通过Student创建的对象,都有自己独立的name和score,能通过print_score打印信息
```

**给对象==发消息==`print_score`实际上就是==调用对象对应的关联函数==**，称之为对象的方法（Method）。面向对象的程序写出来就像这样：

```python
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
```

面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。

所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。

面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

## 10.1.类和实例

面向对象最重要的概念就是**==类（Class）==**和==**实例（Instance）**==，必须牢记**==类是抽象的模板==**，比如`Student`类，而==**实例是根据类创建出来的一个个具体的“对象”**==，每个对象都拥有相同的方法，但各自的数据可能不同。

### 创建类和实例

仍以Student类为例，在Python中，定义类是通过`class`关键字：

```python
class Student(object):
    pass
```

`class`后面紧接着是类名，即`Student`，类名通常是大写开头的单词，紧接着是`(object)`，表示该类是从哪个类继承下来的，`object`是 Python 中所有类的 “基类”.

定义好了`Student`类，就可以根据`Student`类创建出`Student`的实例，创建实例是通过类名+()实现的：

```plain
>>> bart = Student()
>>> bart
<__main__.Student object at 0x10a67a590>
>>> Student
<class '__main__.Student'>
```

可以看到，变量`bart`指向的就是一个`Student`的实例，后面的`0x10a67a590`是内存地址，每个object的地址都不一样，而`Student`本身则是一个类。

可以**自由地给一个实例变量绑定属性**，比如，给实例`bart`绑定一个`name`属性：

```plain
>>> bart.name = 'Bart Simpson'
>>> bart.name
'Bart Simpson'
```

由于**==类可以起到模板==**的作用，因此，在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的`__init__`方法，在**创建实例**的时候，就把`name`，`score`等**属性绑定**上去：

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
```

**注意**：特殊方法`__init__`前后分别有**<u>==两个下划线==</u>**！！！

注意到`__init__`方法的**第一个参数**==永远是`self`，表示创建的实例本身==，因此，在`__init__`方法内部，就可以把各种属性绑定到`self`，因为==`self`就指向创建的实例本身==。

有了`__init__`方法，在创建实例的时候，就**不能传入空的参数了**，必须传入与`__init__`方法<u>匹配</u>的参数，但`self`不需要传，Python解释器自己会把实例变量传进去：

```plain
>>> bart = Student('Bart Simpson', 59)
>>> bart.name
'Bart Simpson'
>>> bart.score
59
```

和普通的函数相比，==在类中定义的函数只有一点不同，就是第一个参数永远是实例变量`self`==，并且，==调用时不传递该参数==。除此之外，类的方法和普通函数没有什么区别，所以仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

### 数据封装	访问数据时直接在类的内部定义访问数据的函数

面向对象编程的一个重要特点就是**数据封装**。在上例`Student`类中，每个实例拥有各自的name和score数据。可以通过函数来访问这些数据，比如打印学生成绩:

```python
>>> def print_score(std):
...     print('%s: %s' % (std.name, std.score))
...
>>> print_score(bart)
Bart Simpson: 59
```

但是，既然`Student`实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在`Student`类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些==封装数据的函数是和`Student`类本身是关联起来的，称之为类的方法==：

```python
class Student(object):
    def __init__(self, name, score):  #构造方法,self指向创建的实例本身
        self.name = name
        self.score = score

    def print_score(self):#实例方法
        print('%s: %s' % (self.name, self.score))
```

要定义一个方法，除了第一个参数是`self`外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了`self`不用传递，其他参数正常传入：

```plain
>>> bart.print_score()
Bart Simpson: 59
```

这样一来，我们从外部看`Student`类，就只需要知道，创建实例需要给出`name`和`score`，而如何打印，都是在`Student`类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。

封装的另一个好处是可以给`Student`类增加新的方法，比如`get_grade`方法可以直接在实例变量上调用，不需要知道内部实现细节：

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
```

- 类：创建实例的模版        

- 实例：一个一个具体的对象，各个实例拥有的数据互相独立，互不影响

**方法就是与实例绑定的函数**，**方法可以直接访问实例的数据**
通过在实例上调用方法，就直接操作了对象内部的数据，无需知道方法内部的实现细节
Python允许对实例变量绑定任何数据，对于两个实例变量虽然都是同一个类的不同实例，但拥有的变量名称可能不同

```plain
>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
#做一些解释说明：bart.age = 8 只是为 bart 这个特定实例添加了一个名为 age 的属性，这个操作不会影响到 lisa 实例，lisa 仍然只有在 Student 类构造函数中定义的属性（如 name 和 score），age没有定义
```

## 10.2.访问限制	属性名称前加上__,实现仅可内部访问

Class内部，可以有属性和方法（实例方法本质就是函数，与实例绑定，定义在类的内部,可以直接访问实例的数据），而**==外部代码==**可以通过**直接调用==实例变量的方法==来操作数据**，这样，就隐藏了内部的复杂逻辑。

从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的`name`、`score`属性：

```plain
>>> bart = Student('Bart Simpson', 59)
>>> bart.score
59
>>> bart.score = 99
>>> bart.score
99
```

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，在Python中，实例的变量名如果以`__`开头，就变成了一个私有变量（private），只有<u>**内部可以访问，外部不能访问**</u>，所以，我们把Student类改一改：

```python
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```

改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问`实例变量.__name`和`实例变量.__score`了：

```plain
>>> bart = Student('Bart Simpson', 59)
>>> bart.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'
```

这样就确保了外部代码不能随意修改对象内部的状态，通过访问限制的保护，代码更加健壮。

当外部代码要获取name和score时可以给`Student`类增加`get_name`和`get_score`这样的方法：

```python
class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
```

当又要允许外部代码修改score时就可以再给Student类增加`set_score`方法：

```python
class Student(object):
    ...

    def set_score(self, score):
        self.__score = score
```

为什么要定义一个方法大费周折？因为在方法中，可以==检查参数==，避免传入无效的参数：

```python
class Student(object):
    ...

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
```

需要注意的是，在Python中，变量名类似`__xxx__`的是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用`__name__`、`__score__`这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问`__name`是因为Python解释器对外把`__name`变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问`__name`变量：

```plain
>>> bart._Student__name
'Bart Simpson'
```

但是一般不要这么干，因为不同版本的Python解释器可能会把`__name`改成不同的变量名。

总的来说就是，Python本身没有任何机制阻止你干坏事，==一切全靠自觉==。

最后注意下面的这种**==<u>*错误写法*</u>==**：

```plain
>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
```

表面上看，外部代码“成功”地设置了`__name`变量，但实际上这个`__name`变量和class内部的`__name`变量*不是*一个变量！内部的`__name`变量已经被Python解释器自动改成了`_Student__name`，而外部代码给`bart`新增了一个`__name`变量。不信试试：

```plain
>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
```

## 10.3.继承和多态

### 继承

OOP程序设计中，当定义一个class的时候，可以从某个现有的class继承，新的class称为子类Subclass，被继承的class称为基类、父类、超类 Base class/Super class

比如，我们已经编写了一个名为`Animal`的class，有一个`run()`方法可以直接打印：

```python
class Animal(object):
    def run(self):
        print('Animal is running...')
```

当我们需要编写`Dog`和`Cat`类时，就可以直接从`Animal`类继承：

```python
class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

对于`Dog`来说，`Animal`就是它的父类，对于`Animal`来说，`Dog`就是它的子类。`Cat`和`Dog`类似。

继承最大的好处是子类获得了父类的全部功能。由于`Animal`实现了`run()`方法，因此，`Dog`和`Cat`作为它的子类，什么事也没干，就自动拥有了`run()`方法：

```python
dog = Dog()
dog.run()

cat = Cat()
cat.run()
```

运行结果如下：

```plain
Animal is running...
Animal is running...
```

当然，也可以对子类增加一些方法，比如Dog类：

```python
class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')
```

继承的第二个好处需要我们对代码做一点改进。

之前的代码中，无论是`Dog`还是`Cat`，它们`run()`的时候，显示的都是`Animal is running...`，符合逻辑的做法是分别显示`Dog is running...`和`Cat is running...`，因此，对`Dog`和`Cat`类改进如下：

```python
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')
```

再次运行，结果如下：

```plain
Dog is running...
Cat is running...
```

当子类和父类都存在相同的`run()`方法时，子类的`run()`覆盖了父类的`run()`，在代码运行的时候，总是会调用子类的`run()`。这样，我们就获得了继承的另一个好处：==**多态**==

### 多态

首先要对数据类型再作一点说明。当我们**==定义一个class的时候==等于==定义了一种数据类型==**。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：

```python
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
```

判断一个变量是否是某个类型可以用`isinstance()`判断：

```plain
>>> isinstance(a, list)
True
>>> isinstance(b, Animal)
True
>>> isinstance(c, Dog)
True
```

看来`a`、`b`、`c`确实对应着`list`、`Animal`、`Dog`这3种类型。

试试：

```plain
>>> isinstance(c, Animal)
True
```

看来`c`不仅仅是`Dog`，`c`还是`Animal`！

因为`Dog`是从`Animal`继承下来的，当我们创建了一个`Dog`的实例`c`时，我们认为`c`的数据类型是`Dog`没错，但`c`同时也是`Animal`也没错，`Dog`本来就是`Animal`的一种！

所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：

```plain
>>> b = Animal()
>>> isinstance(b, Dog)
False
```

`Dog`可以看成`Animal`，但`Animal`不可以看成`Dog`。

要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个`Animal`类型的变量：

```python
def run_twice(animal):
    animal.run()
    animal.run()
```

当我们传入`Animal`的实例时，`run_twice()`就打印出：

```plain
>>> run_twice(Animal())
Animal is running...
Animal is running...
```

当我们传入`Dog`的实例时，`run_twice()`就打印出：

```plain
>>> run_twice(Dog())
Dog is running...
Dog is running...
```

看上去没啥意思，但是仔细想想，如果我们再定义一个`Tortoise`类型，也从`Animal`派生：

```python
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
```

当我们调用`run_twice()`时，传入`Tortoise`的实例：

```plain
>>> run_twice(Tortoise())
Tortoise is running slowly...
Tortoise is running slowly...
```

可以发现新增一个`Animal`的子类，不必对`run_twice()`做任何修改，实际上，任何依赖`Animal`作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

**==多态的好处==**就是，当我们需要传入`Dog`、`Cat`、`Tortoise`……时，我们只需要接收`Animal`类型就可以了，因为`Dog`、`Cat`、`Tortoise`……都是`Animal`类型，然后，按照`Animal`类型进行操作即可。由于`Animal`类型有`run()`方法，因此，传入的任意类型，只要是`Animal`类或者子类，就会自动调用实际类型的`run()`方法，这就是多态的意思：

对于一个变量，我们只需要知道它是`Animal`类型，无需确切地知道它的子类型，就可以放心地调用`run()`方法，而具体调用的`run()`方法是作用在`Animal`、`Dog`、`Cat`还是`Tortoise`对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种`Animal`的子类时，只要确保`run()`方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

- 对扩展开放：允许新增`Animal`子类；

- 对修改封闭：不需要修改依赖`Animal`类型的`run_twice()`等函数。

继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。比如如下的继承树：

```
                ┌───────────────┐
                │    object     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │   Animal    │           │    Plant    │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │   Cat   │  │  Tree   │  │ Flower  │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
```

### 静态语言 vs 动态语言

对于静态语言（例如Java）来说，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或者它的子类，否则，将无法调用`run()`方法。

对于Python这样的动态语言来说，则不一定需要传入`Animal`类型。我们只需要保证传入的对象有一个`run()`方法就可以了：

```python
class Timer(object):
    def run(self):
        print('Start...')
```

这就是动态语言的==“鸭子类型”==，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个`read()`方法，返回其内容。但是，许多对象，只要有`read()`方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了`read()`方法的对象。

继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。   

### 鸭子类型的理解

```python
class Animal(object):   #编写Animal类
    def run(self):
        print("Animal is running...")

class Dog(Animal):  #Dog类继承Amimal类，没有run方法
    pass

class Cat(Animal):  #Cat类继承Animal类，有自己的run方法
    def run(self):
        print('Cat is running...')
    pass

class Car(object):  #Car类不继承，有自己的run方法
    def run(self):
        print('Car is running...')

class Stone(object):  #Stone类不继承，也没有run方法
    pass

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Car())
run_twice(Stone())

#输出结果如下：
Animal is running...
Animal is running...
Animal is running...
Animal is running...
Cat is running...
Cat is running...
Car is running...
Car is running...
AttributeError: 'Stone' object has no attribute 'run'
```

## 10.4.获取对象信息

拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法

### 使用type()   判断基本类型

基本类型都可以用用type()来判断对象类型
```plain
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
```

如果一个变量指向函数或者类，也可以用`type()`判断：

```plain
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>
```

**==`type()`函数返回对应的Class类型==**。如果我们要在`if`语句中判断，就需要比较两个变量的type类型是否相同：

```plain
>>> type(123)==type(456)
True
>>> type(123)==int
True
>>> type('abc')==type('123')
True
>>> type('abc')==str
True
```

判断基本数据类型可以直接写`int`，`str`等，但要判断一个对象是否是函数时可以使用`types`模块中定义的常量：

```plain
>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
```

### 使用isinstance()  判断class类型

对于class的继承关系来说，使用`type()`就很不方便。我们要判断class的类型，可以使用`isinstance()`函数。

我们回顾上次的例子，如果继承关系是：

```plain
object -> Animal -> Dog -> Husky
```

那么，`isinstance()`就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：

```plain
>>> a = Animal()
>>> d = Dog()
>>> h = Husky() #哈士奇
```

然后，判断：

```plain
>>> isinstance(h, Husky)
True
```

没有问题，因为`h`变量指向的就是Husky对象。

再判断：

```plain
>>> isinstance(h, Dog)
True
```

`h`虽然自身是Husky类型，但由于Husky是从Dog继承下来的，所以，`h`也还是Dog类型。

==`isinstance()`判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。==

因此，我们可以确信，`h`还是Animal类型：

```plain
>>> isinstance(h, Animal)
True
```

同理，实际类型是Dog的`d`也是Animal类型：

```plain
>>> isinstance(d, Dog) and isinstance(d, Animal)
True
```

但是，`d`不是Husky类型：

```plain
>>> isinstance(d, Husky)
False
```

能用`type()`判断的基本类型也可以用`isinstance()`判断：

```plain
>>> isinstance('a', str)
True
>>> isinstance(123, int)
True
>>> isinstance(b'a', bytes)
True
```

`isinstance()`还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

```plain
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True
```

==<u>**注：**</u>==总是**优先使用**`isinstance()`判断类型，可以将指定类型及其子类“一网打尽”。

### 使用dir()

如果==**要获得一个对象的所有属性和方法**==，可以使用`dir()`函数，它==**返回一个包含字符串的list**==，比如，获得一个str对象的所有属性和方法：

```plain
>>> dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
```

类似`__xxx__`的属性和方法在Python中都是有特殊用途的，比如`__len__`方法返回长度。在Python中，如果你调用`len()`函数试图获取一个对象的长度，实际上，在`len()`函数内部，它自动去调用该对象的`__len__()`方法，所以，下面的代码是等价的：

```plain
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
```

我们自己写的类，如果也想用`len(myObj)`的话，就自己写一个`__len__()`方法：

```plain
>>> class MyDog(object):
...     def __len__(self):  #self指向创建的实例本身
...         return 100
...
>>> dog = MyDog()
>>> len(dog)  即dog.__len__()，根据上面的函数定义，返回值为100
100
```

剩下的都是普通属性或方法，比如`lower()`返回小写的字符串：

```plain
>>> 'ABC'.lower()
'abc'
```

仅仅把属性和方法列出来是不够的，配合`getattr()`、`setattr()`以及`hasattr()`，我们可以直接操作一个对象的状态：

```plain
>>> class MyObject(object):
...     def __init__(self):
...         self.x = 9    #实例.属性，这里x代表属性
...     def power(self):
...         return self.x * self.x
...
>>> obj = MyObject()
```

可以测试该对象的属性：

```plain
>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19
```

如果试图获取不存在的属性，会抛出AttributeError的错误：

```plain
>>> getattr(obj, 'z') # 获取属性'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyObject' object has no attribute 'z'
```

可以传入一个default参数，如果属性不存在，就返回默认值：

```plain
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404
```

也可以获得对象的方法：

```plain
>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81
```

- 小结

通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

```python
sum = obj.x + obj.y
```

就不要写：

```python
sum = getattr(obj, 'x') + getattr(obj, 'y')
```

一个正确的用法的例子如下：

```python
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
```

假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。`hasattr()`就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有`read()`方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要`read()`方法返回的是有效的图像数据，就不影响读取图像的功能。

## 10.5.实例属性和类属性

Python是动态语言，由类创建的**实例**可以**任意绑定属性**。

给实例绑定属性的方法是通过实例变量，或者通过`self`变量：

```python
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
```

如果`Student`类本身需要绑定一个属性,则可以直接在class中定义属性，这种属性是类属性，归`Student`类所有：

```python
class Student(object):
    name = 'Student'
```

当我们定义了一个类属性后，这个属性归类所有，类的所有实例都可以访问到。来测试一下：

```plain
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
```

从上面的例子可以看出，在编写程序的时候，==千万不要对实例属性和类属性使用相同的名字==，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

- 小结

  实例属性属于各个实例所有，互不干扰；           **独立**

  类属性属于类所有，所有实例共享一个属性；  **官大一级**

  不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误   **同名易混淆**

---

# 第十一章 面向对象高级编程

面向对象程序设计OOP中最基础的三个概念：==**数据封装、继承、多态**==

本章将继续讨论高级特性，**==多重继承、定制类、元类==**等概念

## 11.1.使用\_\_slots\_\_

<!--`\_\_slot\_\_`标题中出现双下划线用转义字符表-->

当定义了一个`class`并创建了一个`class`的实例后，可以==**给该实例绑定任何属性和方法**==，这就是动态语言的灵活性。先定义`class`：

```python
class Student(object):
    pass
```

给实例绑定一个属性：

```plain
>>> s = Student()
>>> s.name = 'Michael' # 动态给实例绑定一个属性
>>> print(s.name)
Michael
```

还可以给实例绑定一个方法（与数据封装，即对class绑定作区分）：

```python
def set_age(self, age): # 定义一个函数作为实例方法  self会自动接收调用该方法的实例对象本身（类似其他语言的 this）
	self.age = age
from types import MethodType
#普通函数不能直接赋值给实例作为方法（直接赋值的话，函数不会自动接收self参数），MethodType会帮我们处理self的自动传递逻辑
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
#左边 s.set_age：给实例s动态添加一个名为set_age的属性（这个属性是方法）。
#右边MethodType(set_age,s)：把普通函数set_age包装成“实例方法”，并绑定到实例s
#绑定后，s.set_age就不再是普通函数了，而是属于s的实例方法，调用时会自动把s作为第一个参数（self）传入。
s.set_age(25) # 调用实例方法
s.age # 测试结果为25
```

给一个实例绑定的方法，对另一个实例是不起作用的：

```plain
>>> s2 = Student() # 创建新的实例
>>> s2.set_age(25) # 尝试调用方法
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'
```

为了给所有实例都绑定方法，可以给`class`绑定方法：

```plain
>>> def set_score(self, score):
...     self.score = score
...
>>> Student.set_score = set_score
```

给`class`绑定方法后，所有实例均可调用：

```plain
>>> s.set_score(100)
>>> s.score
100
>>> s2.set_score(99)
>>> s2.score
99
```

通常情况下，上面的`set_score`方法可以直接定义在`class`中，但动态绑定允许我们在程序运行的过程中动态给`class`加上功能，这在静态语言中很难实现。

### 使用\_\_slots\_\_    限制class的实例能添加的属性

想要限制实例的属性：比如只允许对Student实例添加`name`和`age`属性

为了达到限制的目的，Python允许在定义`class`的时候，定义一个特殊的`__slots__`变量，来限制该`class`实例能添加的属性：

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

试试：

```plain
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```

由于`'score'`没有被放到`__slots__`中，所以不能绑定`score`属性，试图绑定`score`将得到`AttributeError`的错误。

使用`__slots__`要注意，==**`__slots__`定义的属性仅对<u>当前类实例</u>起作用，对<u>继承的子类</u>是不起作用的**==：

```plain
>>> class GraduateStudent(Student):
...     pass
...
>>> g = GraduateStudent()
>>> g.score = 9999
```

除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`

## 11.2.使用@property   限制参数更改的范围

绑定属性的时候，如果直接把属性暴露，没法检查参数，导致成绩可以随便更改：

```python
s = Student()
s.score = 9999
```

为了限制socre的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获得成绩，在set_score()里可以检查参数

```python
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must be between 0~100!')
        self._score=value
```

现在，对任意的`Student`实例进行操作，就不能随心所欲地设置`score`了：

```plain
>>> s = Student()
>>> s.set_score(60) # ok!
>>> s.get_score()
60
>>> s.set_score(9999)
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```

上面的调用方法又略显复杂，没有直接用属性这么直接简单。

**装饰器（decorator）可以给函数动态加上功能**，对于类的方法，装饰器一样起作用。Python**<u>内置</u>**的`@property`装饰器就是负责把一个方法变成属性调用的：

```python
class Student(object):
    @property
    def score(self):
        return self._score
    
	@score.setter
	def score(self,value):
    	if not isinstance(value,int):
        	raise ValueError('score must be an integer!')
    	if value<0 or value>100:
        	raise ValueError('score must be between 0~100!')
    	self._score=value
```

`@property`的实现比较复杂，我们先考察如何使用:
把一个getter方法变成属性，只需要加上`@property`就可以了，此时，`@property`本身又创建了另一个装饰器`@score.setter`，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

```plain
>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.score(60)
>>> s.score # OK，实际转化为s.score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```

注意到这个神奇的`@property`，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

```python
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2025 - self._birth
```

上面的`birth`是可读写属性，而`age`就是一个只读属性，因为`age`可以根据`birth`和当前时间计算出来。
要特别注意：==**属性的方法名不要和实例变量重名**==。例如，以下的代码是错误的：

```python
class Student(object):

    # 方法名称和实例变量均为birth:

	@property
	def birth(self):
		return self.birth
```

这是因为调用`s.birth`时，首先转换为方法调用，在执行`return self.birth`时，又视为访问`self`的属性，于是又转换为方法调用`self.birth()`，造成==**无限递归**==，最终导致栈溢出报错`RecursionError`。

`@property`广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

## 11.3.多重继承   从多个类获得继承，一个子类同时获得多个父类的所有功能

继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。

回忆一下`Animal`类层次的设计，假设我们要实现以下4种动物：

- Dog - 狗狗；
- Bat - 蝙蝠；
- Parrot - 鹦鹉；
- Ostrich - 鸵鸟。

如果按照哺乳动物和鸟类归类，我们可以设计出这样的类的层次：

```
                ┌───────────────┐
                │    Animal     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │   Mammal    │           │    Bird     │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │   Bat   │  │ Parrot  │  │ Ostrich │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
```

但是如果按照“能跑”和“能飞”来归类，我们就应该设计出这样的类的层次：

```
                ┌───────────────┐
                │    Animal     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │  Runnable   │           │   Flyable   │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │ Ostrich │  │ Parrot  │  │   Bat   │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
```

如果要把上面的两种分类都包含进来，我们就得设计更多的层次：

- 哺乳类：能跑的哺乳类，能飞的哺乳类；
- 鸟类：能跑的鸟类，能飞的鸟类。

这么一来，类的层次就复杂了：

```
                ┌───────────────┐
                │    Animal     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │   Mammal    │           │    Bird     │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│  MRun   │  │  MFly   │  │  BRun   │  │  BFly   │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
     │            │            │            │
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │   Bat   │  │ Ostrich │  │ Parrot  │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
```

如果要再增加“宠物类”和“非宠物类”，这么搞下去，类的数量会呈指数增长，很明显这样设计是不行的。

正确的做法是采用**==多重继承==**。首先，主要的类层次仍按照哺乳类和鸟类设计：

```python
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass
```

要给动物再加上`Runnable`和`Flyable`的功能，只需要先定义好`Runnable`和`Flyable`的类：

```python
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
```

对于需要`Runnable`功能的动物，就多继承一个`Runnable`，例如`Dog`：

```python
class Dog(Mammal, Runnable):
    pass
```

对于需要`Flyable`功能的动物，就多继承一个`Flyable`，例如`Bat`：

```python
class Bat(Mammal, Flyable):
    pass
```

通过多重继承，==**一个子类就可以同时获得多个父类的所有功能**==。

### MixIn

设计类的继承关系时，主线都是**单一继承**下来的，例如，`Ostrich`继承自`Bird`。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让`Ostrich`除了继承自`Bird`外，再同时继承`Runnable`。这种设计通常称之为**MixIn**。

为了更好地看出继承关系，我们把`Runnable`和`Flyable`改为`RunnableMixIn`和`FlyableMixIn`。类似的，你还可以定义出肉食动物`CarnivorousMixIn`和植食动物`HerbivoresMixIn`，让某个动物同时拥有好几个MixIn：

```python
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
```

**MixIn的目的就是给一个类增加多个功能**，这样，在设计类的时候，我们优先考虑**通过多重继承来组合多个MixIn的功能**，而不是设计多层次的复杂的继承关系。

Python自带的很多库也使用了MixIn。举个例子，Python自带了`TCPServer`和`UDPServer`这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由`ForkingMixIn`和`ThreadingMixIn`提供。通过组合，我们就可以创造出合适的服务来。

比如，编写一个多进程模式的TCP服务，定义如下：

```python
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
```

编写一个多线程模式的UDP服务，定义如下：

```python
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
```

如果你打算搞一个更先进的协程模型，可以编写一个`CoroutineMixIn`：

```python
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
```

这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

## 11.4.定制类

看到类似`__slots__`这种形如`__xxx__`的变量或者函数名就要注意，这些在Python中是有特殊用途的。

`__slots__`我们已经知道怎么用了，`__len__()`方法我们也知道是为了能让class作用于`len()`函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

### \_\_str\_\_

我们先定义一个`Student`类，打印一个实例：

```plain
>>> class Student(object):
...     def __init__(self, name):
...         self.name = name
...
>>> print(Student('Michael'))
<__main__.Student object at 0x109afb190>
```

打印出一堆`<__main__.Student object at 0x109afb190>`，不好看。

只需要定义好`__str__()`方法，就可以返回一个好看的字符串：

```plain
>>> class Student(object):
...     def __init__(self, name):
...         self.name = name
...     def __str__(self):
...         return 'Student object (name: %s)' % self.name
...
>>> print(Student('Michael'))
Student object (name: Michael)
```

这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。

但是直接敲变量不用`print`，打印出来的实例还是不好看：

```plain
>>> s = Student('Michael')
>>> s
<__main__.Student object at 0x109afb310>
```

这是因为**直接显示变量**调用的不是`__str__()`，而是`__repr__()`，两者的区别是`__str__()`**返回用户看到的字符串**，而`__repr__()`**返回程序开发者看到的字符串**，也就是说，`__repr__()`是为调试服务的。

解决办法是再定义一个`__repr__()`。但是通常`__str__()`和`__repr__()`代码都是一样的，所以，有个偷懒的写法：

```python
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
```

### \_\_iter\_\_

如果一个类想被用于`for ... in`循环，类似list或tuple那样，就必须实现一个`__iter__()`方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环。

我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
```

现在，试试把Fib实例作用于for循环：

```plain
>>> for n in Fib():
...     print(n)
...
1
1
2
3
5
...
46368
75025
```

### \_\_getitem\_\_

Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：

```plain
>>> Fib()[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Fib' object does not support indexing
```

要表现得像list那样按照下标取出元素，需要实现`__getitem__()`方法：

```python
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
#range(n)会生成一个 “从0到n-1的整数序列”（比如n=3时，range(3)是[0,1,2]）
#for x in range(n)的本质是：让x依次取这个序列里的每个元素，循环执行的次数等于序列的长度（也就是n次）
#x只是接收range(n)序列中元素的 “占位变量”，循环的次数由range(n)的长度（即n）决定
            a, b = b, a + b
        return a
```

现在，就可以按下标访问数列的任意一项了：

```plain
>>> f = Fib()
>>> f[0]
1
>>> f[1]
1
>>> f[2]
2
>>> f[3]
3
>>> f[10]
89
>>> f[100]
573147844013817084101
```

但是list有个神奇的切片方法：

```plain
>>> list(range(100))[5:10]
[5, 6, 7, 8, 9]
```

对于Fib却报错。原因是`__getitem__()`传入的参数可能是一个int，也可能是一个切片对象`slice`，所以要做判断：

```python
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
```

现在试试Fib的切片：

```plain
>>> f = Fib()
>>> f[0:5]
[1, 1, 2, 3, 5]
>>> f[:10]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

但是没有对step参数作处理：

```plain
>>> f[:10:2]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

也没有对负数作处理，所以，要正确实现一个`__getitem__()`还是有很多工作要做的。

此外，如果把对象看成`dict`，`__getitem__()`的参数也可能是一个可以作key的object，例如`str`。

与之对应的是`__setitem__()`方法，把对象视作list或dict来对集合赋值。最后，还有一个`__delitem__()`方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

### \_\_getattr\_\_

正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义`Student`类：

```python
class Student(object):
    def __init__(self):
        self.name = 'Michael'
```

调用`name`属性，没问题，但是，调用不存在的`score`属性，就有问题了：

```plain
>>> s = Student()
>>> print(s.name)
Michael
>>> print(s.score)
Traceback (most recent call last):
  ...
AttributeError: 'Student' object has no attribute 'score'
```

错误信息很清楚地告诉我们，没有找到`score`这个attribute。

要避免这个错误，除了可以加上一个`score`属性外，还可以写一个`__getattr__()`方法，动态返回一个属性。修改如下：

```python
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
```

当调用不存在的属性时，比如`score`，Python解释器会试图调用`__getattr__(self, 'score')`来尝试获得属性，这样，我们就有机会返回`score`的值：

```plain
>>> s = Student()
>>> s.name
'Michael'
>>> s.score
99
```

返回函数也是完全可以的：

```python
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
```

只是调用方式要变为：

```plain
>>> s.age()
25
```

==**<u>注意</u>**==，只有在没有找到属性的情况下，才调用`__getattr__`，已有的属性则不会在`__getattr__`中查找。

此外，注意到任意调用如`s.abc`都会返回`None`，这是因为我们定义的`__getattr__`默认返回就是`None`。要让class只响应特定的几个属性，我们就要按照约定，抛出`AttributeError`的错误：

```python
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
```

这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

这种完全动态调用的特性可以针对完全动态的情况作调用。

举个例子：

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

- http://api.server/user/friends
- http://api.server/user/timeline/list

如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的`__getattr__`，我们可以写出一个链式调用：

```python
#下面定义的这个类的作用;“把链式调用的属性名，拼接成API路径”
class Chain(object):
    def __init__(self, path=''):
        # 初始化时，存当前的路径片段（默认是空字符串）
        self._path = path

    def __getattr__(self, path):
        # 当访问不存在的属性时，自动调用这个方法
        # 把“当前路径”和“新属性名”用/拼接，返回一个新的Chain实例
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        # 当打印这个对象时，返回最终拼接好的路径
        return self._path

    __repr__ = __str__  # 让交互环境里直接显示路径（和print效果一致）
```

试试：

```plain
>>> Chain().status.user.timeline.list
'/status/user/timeline/list'
```

这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变

**==<u>对链式调用做一个解释</u>==**：

```plain
##链式调用的执行过程（以Chain().status.user.timeline.list为例）
一步一步看，每一次 “点属性” 到底发生了什么：
--步骤 1：Chain() → 创建第一个实例
调用Chain()时，__init__的path默认是''，所以这个实例的self._path = ''。
--步骤 2：.status → 触发__getattr__，生成新实例
因为第一个实例没有status属性，所以自动调用__getattr__(self, 'status')：
拼接路径：'%s/%s' % ('', 'status') → 结果是'/status'；
返回一个新的 Chain 实例，这个新实例的self._path = '/status'。
--步骤 3：.user → 再次触发__getattr__，生成新实例
现在访问的是 “步骤 2 生成的新实例” 的user属性（这个实例也没有user属性），调用__getattr__(self, 'user')：
拼接路径：'%s/%s' % ('/status', 'user') → 结果是'/status/user'；
返回又一个新的Chain实例，self._path = '/status/user'。
--步骤 4：.timeline → 重复拼接逻辑
访问这个新实例的timeline属性，调用__getattr__：
拼接路径：'/status/user' + '/timeline' → '/status/user/timeline'；
返回新实例，self._path更新为这个值。
--步骤 5：.list → 最后一次拼接
访问list属性，调用__getattr__：
拼接路径：'/status/user/timeline' + '/list' → '/status/user/timeline/list'；
返回最终的 Chain 实例，self._path是这个完整路径。
--步骤 6：显示结果
当你在交互环境里输入Chain().status.user.timeline.list时，Python 会调用__repr__方法（因为__repr__ = __str__），返回self._path，也就是最终的路径'/status/user/timeline/list'。

**为什么这个写法很实用？
原来写SDK需要给每个API路径写一个方法（比如get_user_friends()、get_user_timeline()），但用这个Chain类：
不管 API 路径怎么变（比如新增/user/favorites），只需要写Chain().user.favorites，自动拼接路径；
API 路径修改时，不用改Chain类的代码，直接改链式调用的属性名就行，非常灵活。
```

还有些REST API会把参数放到URL中，比如GitHub的API：

```plain
GET /users/:user/repos
```

调用时，需要把`:user`替换为实际用户名。如果我们能写出这样的链式调用：

```plain
Chain().users('michael').repos
```

就可以非常方便地调用API了

### \_\_call\_\_

一个对象实例可以有自己的属性和方法，当我们调用实例方法时，用`instance.method()`来调用。

想要==**直接在实例本身上调用**==呢，对于任何类，只需要定义一个`__call__()`方法，就可以直接对实例进行调用。请看示例：

```python
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
```

调用方式如下：

```plain
>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.
```

`__call__()`还可以定义参数。==**对实例进行直接调用就好比对一个函数进行调用一样**==，完全可以把对象看成函数，把函数看成对象

如果把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个`Callable`对象，比如函数和我们上面定义的带有`__call__()`的类实例：

```plain
>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False
```

通过`callable()`函数，我们就可以判断一个对象是否是“可调用”对象。

- 小结

Python的`class`允许定义许多定制方法，可以让我们非常方便地生成特定的类。

本节介绍的是最常用的几个定制方法，还有很多可定制的方法，请参考[Python的官方文档](http://docs.python.org/3/reference/datamodel.html#special-method-names)。

## 11.5.使用枚举类

当我们需要**<u>==定义常量==</u>**时，一个办法是用大写变量通过整数来定义，例如月份：

```python
JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12
```

好处是简单，缺点是类型是`int`，并且仍然是变量。

更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了`Enum`类来实现这个功能：

```python
from enum import Enum    #enum为枚举的缩写
#enum是 Python 自带的模块，Enum是其中的 “枚举类模板”，可以用它来创建自己的枚举类型
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#这行代码的作用是生成一个叫Month的枚举类，参数含义：
#第一个参数'Month'：是这个枚举类的“名字”（只是标识，一般和变量名Month保持一致）；
#第二个参数('Jan', ..., 'Dec')：是枚举类的成员列表（这里是12个月份的缩写）。
#执行这行后，Python 会自动做2件事：
#把每个成员（比如Jan）变成Month类的唯一实例（可以理解为“带名字的常量”）；
#给每个成员自动分配一个value属性（默认从1开始计数：Jan.value=1，Feb.value=2，…，Dec.value=12）
```

这样我们就获得了`Month`类型的枚举类，可以直接使用`Month.Jan`来引用一个常量，或者枚举它的所有成员：

```python
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
#Month.__members__是枚举类的内置属性，存着所有成员的“名字 - 实例”键值对（比如'Jan'对应Month.Jan）；
#循环中：
#name是成员的名字（比如'Jan'）；
#member是对应的枚举实例（比如Month.Jan）；
#member.value是自动分配的数字（比如Jan对应1）。
```

`value`属性则是自动赋给成员的`int`常量，默认从`1`开始计数。

如果需要更精确地控制枚举类型，可以从`Enum`派生出自定义类：

```python
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

`@unique`装饰器可以帮助我们检查保证没有重复值。

访问这些枚举类型可以有若干种方法：

```plain
>>> day1 = Weekday.Mon
>>> print(day1)
Weekday.Mon
>>> print(Weekday.Tue)
Weekday.Tue
>>> print(Weekday['Tue'])
Weekday.Tue
>>> print(Weekday.Tue.value)
2
>>> print(day1 == Weekday.Mon)
True
>>> print(day1 == Weekday.Tue)
False
>>> print(Weekday(1))
Weekday.Mon
>>> print(day1 == Weekday(1))
True
>>> Weekday(7)
Traceback (most recent call last):
  ...
ValueError: 7 is not a valid Weekday
>>> for name, member in Weekday.__members__.items():
...     print(name, '=>', member)
...
Sun => Weekday.Sun
Mon => Weekday.Mon
Tue => Weekday.Tue
Wed => Weekday.Wed
Thu => Weekday.Thu
Fri => Weekday.Fri
Sat => Weekday.Sat
```

可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

- 小结

`Enum`可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。

## 11.6.使用元类

### type()   动态创建类

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

比方说我们要定义一个`Hello`的class，就写一个`hello.py`模块：

```python
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
```

当Python解释器载入`hello`模块时，就会**==依次执行该模块的所有语句==**，执行结果就是**==动态创建出一个`Hello`的class对象==**，测试如下：

```plain
>>> from hello import Hello
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class 'hello.Hello'>
```

`type()`函数可以查看一个类型或变量的类型，`Hello`是一个class，它的类型就是`type`，而`h`是一个实例，它的类型就是class

我们说class的定义是运行时动态创建的，而创建class的方法就是使用`type()`函数。

`type()`函数**==既可以<u>返回一个对象的类型</u>，又可以<u>创建出新的类型</u>==**

比如，我们可以通过`type()`函数创建出`Hello`类，而无需通过`class Hello(object)...`的定义：

```plain
>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class '__main__.Hello'>
```

要创建一个class对象，`type()`函数依次传入3个参数：

1. class的名称；
2. 继承的父类集合元组，注意Python支持多重继承，如果只有一个父类，别忘了**tuple的单元素写法**；
3. class的方法名称与函数绑定，这里我们把函数`fn`绑定到方法名`hello`上。

通过`type()`函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用`type()`函数创建出class。

正常情况下，我们都用`class Xxx...`来定义类，但是，`type()`函数也允许我们**动态创建类**，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

### metaclass    控制类的创建行为（创建/修改类）

除了使用`type()`动态创建类以外，要控制类的创建行为，还可以使用metaclass。

metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

所以，**==metaclass允许你创建类或者修改类==**。换句话说，你可以把类看成是metaclass创建出来的“实例”。

metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，<u>**以下内容看不懂也没关系，因为基本上你不会用到。**</u>

我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个`add`方法：

定义`ListMetaclass`，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

```python
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
```

有了`ListMetaclass`，我们在定义类的时候还要指示使用`ListMetaclass`来定制类，传入关键字参数`metaclass`：

```python
class MyList(list, metaclass=ListMetaclass):
    pass
```

当我们传入关键字参数`metaclass`时，魔术就生效了，它指示Python解释器在创建`MyList`时，要通过`ListMetaclass.__new__()`来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

`__new__()`方法接收到的参数依次是：

1. 当前准备创建的类的对象；cls
2. 类的名字；name
3. 类继承的父类集合；bases
4. 类的方法集合；attrs

测试一下`MyList`是否可以调用`add()`方法：

```plain
>>> L = MyList()
>>> L.add(1)
>> L
[1]
```

而普通的`list`没有`add()`方法：

```plain
>>> L2 = list()
>>> L2.add(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'add'
```

动态修改有什么意义？直接在`MyList`定义中写上`add()`方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。

但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

ORM全称“Object Relational Mapping”，即**<u>==对象-关系映==</u>**射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

让我们来尝试编写一个ORM框架。

编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个`User`类来操作对应的数据库表`User`，我们期待他写出这样的代码：

```python
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
```

其中，父类`Model`和属性类型`StringField`、`IntegerField`是由ORM框架提供的，剩下的魔术方法比如`save()`全部由父类`Model`自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。

现在，我们就按上面的接口来实现该ORM。

首先来定义`Field`类，它负责保存数据库表的字段名和字段类型：

```python
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
```

在`Field`的基础上，进一步定义各种类型的`Field`，比如`StringField`，`IntegerField`等等：

```python
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
```

下一步，就是编写最复杂的`ModelMetaclass`了：

```python
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
```

以及基类`Model`：

```python
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
```

当用户定义一个`class User(Model)`时，Python解释器首先在当前类`User`的定义中查找`metaclass`，如果没有找到，就继续在父类`Model`中查找`metaclass`，找到了，就使用`Model`中定义的`metaclass`的`ModelMetaclass`来创建`User`类，也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

在`ModelMetaclass`中，一共做了几件事情：

1. 排除掉对`Model`类的修改；
2. 在当前类（比如`User`）中查找定义的类的所有属性，如果找到一个`Field`属性，就把它保存到一个`__mappings__`的dict中，同时从类属性中删除该`Field`属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
3. 把表名保存到`__table__`中，这里简化为表名默认为类名。

在`Model`类中，就可以定义各种操作数据库的方法，比如`save()`，`delete()`，`find()`，`update`等等。

我们实现了`save()`方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出`INSERT`语句。

编写代码试试：

```python
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
```

输出如下：

```plain
Found model: User
Found mapping: email ==> <StringField:email>
Found mapping: password ==> <StringField:password>
Found mapping: id ==> <IntegerField:uid>
Found mapping: name ==> <StringField:username>
SQL: insert into User (password,email,username,id) values (?,?,?,?)
ARGS: ['my-pwd', 'test@orm.org', 'Michael', 12345]
```

可以看到，`save()`方法已经打印出了可执行的SQL语句，以及参数列表，只需要真正连接到数据库，执行该SQL语句，就可以完成真正的功能。

不到100行代码，我们就通过metaclass实现了一个精简的ORM框架，是不是非常简单？

- 小结

metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。

---

# 第十二章 错误、调试和测试

在程序运行过程中，总会遇到各种各样的==**错误**==

- 程序编写错误——修复bug
 `比如本来应该输出整数结果输出了字符串`
- 用户错误输入——检查用户输入
 `比如让用户输入email地址，结果得到一个空字符串`
- 程序运行中无法预测的错误——异常
   `比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了`

Python内置了一套异常处理机制，来帮助我们进行错误处理。

此外，我们也需要**跟踪程序的执行来查看变量的值是否正确**，这个过程称为==**调试**==。<u>Python的pdb可以让我们以单步方式执行代码</u>。

最后，==**编写测试**==也很重要。有了良好的测试，就可以在程序修改后反复运行，确保程序输出符合我们编写的测试。

## 12.1 错误处理

在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数`open()`，成功时返回文件描述符（就是一个整数），出错时返回`-1`。

用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错：

```python
def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass
```

一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。

所以高级语言通常都内置了一套==`try...except...finally...`==的**<u>==错误处理机制==</u>**

### try

让我们用一个例子来看看`try`的机制：

```python
try:
    print('try...')
    r = 10 / 0
    print('result:', r)   #第三行出错了，这一行内容不会执行，直接跳转到except语句块
except ZeroDivisionError as e:#错误处理代码
    print('except:', e)
finally:
    print('finally...')
print('END')
```

当我们认为某些代码可能会出错时，就可以用`try`来运行这段代码，如果执行出错，则后续代码不会继续执行，并直接跳转至错误处理代码，即`except`语句块，执行完`except`后，如果有`finally`语句块，则执行`finally`语句块，至此，执行完毕。

上面的代码在计算`10 / 0`时会产生一个除法运算错误：

```plain
try...
except: division by zero
finally...
END
```

从输出可以看到，当错误发生时，后续语句`print('result:', r)`不会被执行，`except`由于捕获到`ZeroDivisionError`，因此被执行。最后，`finally`语句被执行。然后，程序继续按照流程往下走。

如果把除数`0`改成`2`，则执行结果如下：

```plain
try...
result: 5
finally...
END
```

由于没有错误发生，所以`except`语句块不会被执行，但是`finally`如果有，则一定会被执行（可以没有`finally`语句）。

错误应该有很多种类，如果发生了不同类型的错误，应该由不同的`except`语句块处理。没错，可以有多个`except`来捕获不同类型的错误：

```python
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')
```

`int()`函数可能会抛出`ValueError`，所以我们用一个`except`捕获`ValueError`，用另一个`except`捕获`ZeroDivisionError`。

此外，如果没有错误发生，可以在`except`语句块后面加一个`else`，当没有错误发生时，会自动执行`else`语句：

```python
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
```

Python的错误其实也是class，所有的**==错误类型都继承自`BaseException`==**，所以在使用`except`时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

```python
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
```

第二个`except`永远也捕获不到`UnicodeError`，因为`UnicodeError`是`ValueError`的子类，如果有，也被第一个`except`给捕获了。

Python所有的错误都是从`BaseException`类派生的，常见的错误类型和继承关系看[这里](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

使用`try...except`捕获错误还有一个巨大的好处，就是可以**==跨越多层调用==**，比如函数`main()`调用`bar()`，`bar()`调用`foo()`，结果`foo()`出错了，这时，只要`main()`捕获到了，就可以处理：

```python
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
```

也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写`try...except...finally`的麻烦。

### 调用栈  定位错误的位置

如果**==错误没有被捕获，它就会一直往上抛==**，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看`err.py`：

```python
# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
```

执行，结果如下：

```plain
$ python3 err.py
Traceback (most recent call last):
  File "err.py", line 11, in <module>
    main()
  File "err.py", line 9, in main
    bar('0')
  File "err.py", line 6, in bar
    return foo(s) * 2
  File "err.py", line 3, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
```

出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链：

错误信息第1行：

```plain
Traceback (most recent call last):     #traceback 追溯
```

告诉我们这是错误的跟踪信息。

第2~3行：

```plain
  File "err.py", line 11, in <module>
    main()
```

调用`main()`出错了，在代码文件`err.py`的第11行代码，但原因是第9行：

```plain
  File "err.py", line 9, in main
    bar('0')
```

调用`bar('0')`出错了，在代码文件`err.py`的第9行代码，但原因是第6行：

```plain
  File "err.py", line 6, in bar
    return foo(s) * 2
```

原因是`return foo(s) * 2`这个语句出错了，但这还不是最终原因，继续往下看：

```plain
  File "err.py", line 3, in foo
    return 10 / int(s)
```

原因是`return 10 / int(s)`这个语句出错了，这是错误产生的源头，因为下面打印了：

```plain
ZeroDivisionError: integer division or modulo by zero
```

根据错误类型`ZeroDivisionError`，我们判断，`int(s)`本身并没有出错，但是`int(s)`返回`0`，在计算`10 / 0`时出错，至此，找到错误源头。

**==提示==**：出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

### 记录错误   logging模块记录错误信息

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以==把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去==。

Python内置的`logging`模块可以非常容易地记录错误信息：

```python
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
```

同样是出错，但程序打印完错误信息后会继续执行，并正常退出：

```plain
$ python3 err_logging.py
ERROR:root:division by zero
Traceback (most recent call last):
  File "err_logging.py", line 11, in main
    bar('0')
  File "err_logging.py", line 7, in bar
    return foo(s) * 2
  File "err_logging.py", line 4, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
END
```

通过配置，`logging`还可以把错误记录到日志文件里，方便事后排查。

### 抛出错误

因为**==错误是class==**，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是**<u>有意创建并抛出</u>**的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，==**用`raise`语句抛出一个错误的实例**==：

```python
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
```

执行，可以最后跟踪到我们自己定义的错误：

```plain
$ python3 err_raise.py 
Traceback (most recent call last):
  File "err_throw.py", line 10, in <module>
    foo('0')
  File "err_throw.py", line 7, in foo
    raise FooError('invalid value: %s' % s)
__main__.FooError: invalid value: 0
```

只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如`ValueError`，`TypeError`），尽量使用Python内置的错误类型。

最后，我们来看另一种错误处理的方式：

```python
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
```

在`bar()`函数中，我们明明已经捕获了错误，但是，打印一个`ValueError!`后，又把错误通过`raise`语句抛出去了，这不有病么？

其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

`raise`语句如果不带参数，就会把当前错误原样抛出。此外，在`except`中`raise`一个Error，还可以把一种类型的错误转化成另一种类型：

```python
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
```

只要是合理的转换逻辑就可以，但是，决不应该把一个`IOError`转换成毫不相干的`ValueError`。

- 小结

Python内置的`try...except...finally`用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。

## 12.2 调试 

程序能一次写完并正常运行的概率很小，总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。

第一种方法简单直接粗暴有效，就是用`print()`把可能有问题的变量打印出来看看：

```python
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()
```

执行后在输出中查找打印的变量值：

```plain
$ python err.py
>>> n = 0
Traceback (most recent call last):
  ...
ZeroDivisionError: integer division or modulo by zero
```

用`print()`最大的坏处是将来还得删掉它，想想程序里到处都是`print()`，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。

### 断言 assert()

凡是用`print()`来辅助查看的地方，都可以用断言（assert）来替代：

```python
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
```

`assert`的意思是，表达式`n != 0`应该是`True`，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，`assert`语句本身就会抛出`AssertionError`：

```plain
$ python err.py
Traceback (most recent call last):
  ...
AssertionError: n is zero!
```

程序中如果到处充斥着`assert`，和`print()`相比也好不到哪去。不过，启动Python解释器时可以用`-O`参数来关闭`assert`：

```plain
$ python -O err.py
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

**==注意==**：断言的开关“-O”是英文大写字母O，不是数字0。

关闭后，可以把所有的`assert`语句当成`pass`来看。

### logging模块

把`print()`替换为`logging`是第3种方式，和`assert`比，`logging`不会抛出错误，而且可以输出到文件：

```python
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
```

`logging.info()`就可以输出一段文本。运行，发现除了`ZeroDivisionError`，没有任何信息。怎么回事？

别急，在`import logging`之后添加一行配置再试试：

```python
import logging
logging.basicConfig(level=logging.INFO)
```

看到输出了：

```plain
$ python err.py
INFO:root:n = 0
Traceback (most recent call last):
  File "err.py", line 8, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
```

这就是`logging`的好处，它允许你指定记录信息的级别，有`debug`，`info`，`warning`，`error`等几个级别，当我们指定`level=INFO`时，`logging.debug`就不起作用了。同理，指定`level=WARNING`后，`debug`和`info`就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

`logging`的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

### pdb

第4种方式是启动Python的调试器pdb，让**==程序以单步方式运行==**，可以随时查看运行状态。我们先准备好程序：

```python
# err.py
s = '0'
n = int(s)
print(10 / n)
```

然后启动：

```plain
$ python -m pdb err.py
> /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
-> s = '0'
```

以参数`-m pdb`启动后，pdb定位到下一步要执行的代码`-> s = '0'`。输入命令`l`来查看代码：

```plain
(Pdb) l
  1     # err.py
  2  -> s = '0'
  3     n = int(s)
  4     print(10 / n)
```

输入命令`n`可以单步执行代码：

```plain
(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
-> n = int(s)
(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
-> print(10 / n)
```

任何时候都可以输入命令`p 变量名`来查看变量：

```plain
(Pdb) p s
'0'
(Pdb) p n
0
```

输入命令`q`结束调试，退出程序：

```plain
(Pdb) q
```

这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。

### pdb.set_trace()

这个方法也是用pdb，但是不需要单步执行，我们只需要`import pdb`，然后在==可能出错的地方==放一个`pdb.set_trace()`，就可以设置一个==断点==：

```python
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() #运行到这里会自动暂停
print(10 / n)
```

运行代码，程序会自动在`pdb.set_trace()`**暂停并进入pdb调试环境**，可以用命令`p`查看变量，或者用命令`c`继续运行：

```plain
$ python err.py 
> /Users/michael/Github/learn-python3/samples/debug/err.py(7)<module>()
-> print(10 / n)
(Pdb) p n
0
(Pdb) c
Traceback (most recent call last):
  File "err.py", line 7, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
```

这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。

### IDE

如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：

Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件

PyCharm：http://www.jetbrains.com/pycharm/

- 小结

写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。虽然用IDE调试起来比较方便，但是最后你会发现，==logging才是终极武器==。

## 12.3 单元测试

### 单元测试概述

如果你听说过“测试驱动开发”（TDD：Test-Driven Development），单元测试就不陌生。

==**<u>单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作</u>**==。

比如对函数`abs()`，我们可以编写出以下几个测试用例：

1. 输入正数，比如`1`、`1.2`、`0.99`，期待返回值与输入相同；
2. 输入负数，比如`-1`、`-1.2`、`-0.99`，期待返回值与输入相反；
3. 输入`0`，期待返回`0`；
4. 输入非数值类型，比如`None`、`[]`、`{}`，期待抛出`TypeError`。

把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。

如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通过，要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。

单元测试通过后有什么意义？如果我们对`abs()`函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对`abs()`函数原有的行为造成影响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。

这种**以测试为驱动的开发模式**最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在修改的时候，可以极大程度地保证该模块行为仍然是正确的。

我们来编写一个`Dict`类，这个类的行为和`dict`一致，但是可以通过属性来访问，用起来就像下面这样：

```plain
>>> d = Dict(a=1, b=2)
>>> d['a']
1
>>> d.a
1
```

`mydict.py`代码如下：

```python
class Dict(dict):#Dict类继承自内置的dict类,默认拥有dict的所有功能
    def __init__(self, **kw):#初始化方法
        super().__init__(**kw)#调用父类dict的构造方法,把传入的关键字参数初始化到字典中

    def __getattr__(self, key):
        try:
            return self[key]#尝试用self[key]（字典的键访问方式）获取值
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
```

为了编写单元测试，我们需要引入Python自带的`unittest`模块，编写`mydict_test.py`如下：

```python
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):#编写测试类,从unittest.TestCase继承
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)           #断言函数返回的结果与真实值相等
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()#创建空的Dict实例d
        with self.assertRaises(KeyError):
            value = d['empty']#with块内代码执行语句d['empty'],因为Dict继承了dict，空字典取不存在的键（'empty'）会抛出KeyError；
#with self.assertRaises(异常类型)是unittest框架提供的上下文管理方法,作用时断言with代码块内的代码一定会抛出指定类型的一场,如果块内代码没抛出异常这个测试用例就会失败
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty#with块内执行d.empty：这是属性式访问，会触发Dict的__getattr__方法 —— 方法内尝试取self['empty']（会抛KeyError），然后被捕获并转换为AttributeError抛出；
```

编写单元测试时，我们需要编写一个测试类，从`unittest.TestCase`继承。

**以`test`开头的方法就是测试方法**，不以`test`开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个`test_xxx()`方法。由于`unittest.TestCase`提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是`assertEqual()`：

```python
self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
```

另一种重要的断言就是期待抛出指定类型的Error，比如通过`d['empty']`访问不存在的key时，断言会抛出`KeyError`：

```python
with self.assertRaises(KeyError):
    value = d['empty']
```

而通过`d.empty`访问不存在的key时，我们期待抛出`AttributeError`：

```python
with self.assertRaises(AttributeError):
    value = d.empty
```

### 运行单元测试

一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在`mydict_test.py`的最后加上两行代码：

```python
#这两行代码是为了让测试脚本“按需运行单元测试”
if __name__ == '__main__':#判断当前是否是直接运行这个测试脚本
    unittest.main()
#__name__是Python给每个模块(.py文件)分配的内置变量
#当直接运行这个模块_比如执行python mydict_test.py,__name__的值会被设为‘__main__’
#当这个模块被其他模块导入_比如import mydict_test,__name__的值会是模块名
```

这样就可以把`mydict_test.py`当做正常的python脚本运行：

```plain
$ python mydict_test.py
```

---

另一种方法是在命令行通过参数`-m unittest`直接运行单元测试：

```plain
$ python -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。

在开发阶段，很多时候，我们希望反复执行某一个测试方法，例如`test_attr()`，而不是每次都运行所有的测试方法，可以通过指定`module.class.method`来运行单个测试方法：

```plain
$ python -m unittest mydict_test.TestDict.test_attr
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

其中，`module`是文件名`mydict_test`（不含`.py`），`class`是测试类`TestDict`，`method`是指定的测试方法名`test_attr`。

如果希望执行`test_attr()`和`test_attrerror()`两个测试方法，我们可以传入`-k`参数，用`attr`来匹配：

```plain
$ python -m unittest mydict_test -k attr -v
test_attr (mydict_test.TestDict.test_attr) ... ok
test_attrerror (mydict_test.TestDict.test_attrerror) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

观察上述命令，`-v`参数能打印出具体执行的测试方法，`-k attr`参数筛选出了包含`attr`的测试方法。可见，单元测试的执行是十分灵活的。

### setUp与tearDown

可以在单元测试中编写两个特殊的`setUp()`和`tearDown()`方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

`setUp()`和`tearDown()`方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在`setUp()`方法中连接数据库，在`tearDown()`方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

```python
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
```

可以再次运行测试看看每个测试方法调用前后是否会打印出`setUp...`和`tearDown...`。

- 小结

单元测试可以有效地**测试某个程序模块的行为**，是未来重构代码的信心保证。

单元测试的**测试用例要覆盖常用的输入组合、边界条件和异常**。

单元测试**代码要非常简单**，如果测试代码太复杂，那么测试代码本身就可能有bug。

单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。  

## 12.4 文档测试  doctest模块可以提取注释中的代码并执行测试

很多文档都有示例代码。比如[re模块](https://docs.python.org/3/library/re.html)就带了很多示例代码：

```plain
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
```

可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致。

这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，那么，可不可以自动执行写在注释中的这些代码呢？

答案是肯定的。

当我们编写注释时，如果写上这样的注释：

```python
def abs(n):
    '''
    Function to get absolute value of number.
    
    Example:
    
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)
```

无疑更明确地告诉函数的调用者该函数的期望输入和输出。

并且，Python内置的**==“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试==**。

doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用`...`表示中间一大段烦人的输出。

让我们用doctest来测试上次编写的`Dict`类：

```python
# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
```

运行`python mydict2.py`：

```plain
$ python mydict2.py
```

什么输出也没有。这说明我们编写的doctest运行都是正确的。如果程序有问题，比如把`__getattr__()`方法注释掉，再运行就会报错：

```plain
$ python mydict2.py
**********************************************************************
File "/Users/michael/Github/learn-python3/samples/debug/mydict2.py", line 10, in __main__.Dict
Failed example:
    d1.x
Exception raised:
    Traceback (most recent call last):
      ...
    AttributeError: 'Dict' object has no attribute 'x'
**********************************************************************
File "/Users/michael/Github/learn-python3/samples/debug/mydict2.py", line 16, in __main__.Dict
Failed example:
    d2.c
Exception raised:
    Traceback (most recent call last):
      ...
    AttributeError: 'Dict' object has no attribute 'c'
**********************************************************************
1 items had failures:#有一个测试对象出现失败
   2 of   9 in __main__.Dict#函数的9个测试用例中2个失败
***Test Failed*** 2 failures.#整体测试失败,总计2个失败项
```

注意到最后3行代码。当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。所以，不必担心doctest会在非测试环境下执行。

注意⚠️:doctest 会把 “预期输出” 的每一行都当作 “需要**严格匹配**的内容”

- 小结

doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。

---

# 第十三章 同步IO编程

**==IO在计算机中指Input/Output，也就是输入和输出==**。由于程序运行时数据是在**内存**中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。

比如打开浏览器，访问新浪首页，浏览器这个程序就需要通过网络IO获取新浪的网页。浏览器首先会发送数据给新浪服务器，告诉它我想要首页的HTML，这个动作是往外发数据，叫Output，随后新浪服务器把网页发过来，这个动作是从外面接收数据，叫Input。所以，通常，程序完成IO操作会有Input和Output两个数据流。当然也有只用一个的情况，比如，从磁盘读取文件到内存，就只有Input操作，反过来，把数据写到磁盘文件里，就只是一个Output操作。

IO编程中，**Stream**（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。   	  ==I\O都是针对**内存**而言，数据流入内存是I，数据流出内存是O==

由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘要接收这100M数据可能需要10秒，怎么办呢？有两种办法：

- ①CPU等着，也就是**<u>程序暂停执行后续代码</u>**，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为**==同步IO==**；

- ②CPU不等待，只是告诉磁盘，“您慢慢写，我接着干别的事去了”，于是，<u>**后续代码可以立刻接着执行**</u>，这种模式称为==**异步IO**==。

同步和异步的区别就在于**<u>是否等待IO执行的结果</u>**。好比你去麦当劳点餐，你说“来个汉堡”，服务员告诉你，对不起，汉堡要现做，需要等5分钟，于是你站在收银台前面等了5分钟，拿到汉堡再去逛商场，这是同步IO。你说“来个汉堡”，服务员告诉你，汉堡需要等5分钟，你可以先去逛商场，等做好了，我们再通知你，这样你可以立刻去干别的事情（逛商场），这是异步IO。

很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是<u>**回调模式**</u>，如果服务员发短信通知你，你就得不停地检查手机，这是**轮询模式**。总之，==异步IO的复杂度远远高于同步IO==。

操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用，Python也不例外。我们后面会详细讨论Python的IO编程接口。

注意，==**本章的IO编程都是同步模式**==，异步IO由于复杂度太高，后续涉及到服务器端程序开发时再讨论。

## 13.1 文件读写

读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。

==**在磁盘上读写文件的功能都是由操作系统提供的**==，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

### 读文件

要以读文件的模式打开一个文件对象，使用Python内置的`open()`函数，传入文件名和标示符：

```plain
# 显式指定编码为utf-8（大多数文本文件的编码）
>>> f = open('D:/桌面/test.txt', 'r', encoding='utf-8')
#注意错误：文件编码不匹配。Python 默认用系统编码（Windows 下通常是gbk）读取文件，但test.txt实际编码可能是utf-8（或其他编码），所以gbk解码器无法识别文件中的字节。
```

在 Python 字符串中，`\` 是 “转义符”，因此想要表示路径可以有以下几种方法

- f = open(r'D:\桌面\test.txt', 'r', encoding='utf-8')  # r表示“原始字符串”，\不会被转义
- f = open('D:/桌面/test.txt', 'r', encoding='utf-8')

标示符`'r'`表示读，这样，我们就成功地打开了一个文件。

如果文件不存在，`open()`函数就会抛出一个`IOError`的错误，并且给出错误码和详细的信息告诉你文件不存在：

```plain
>>> f=open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'
```

如果文件打开成功，接下来，调用`read()`方法可以一次读取文件的全部内容，Python把内容读到内存，用一个`str`对象表示：

```plain
>>> f.read()
'这是一个测试文件是否能被正常打开的文档'
```

最后一步是调用`close()`方法关闭文件。**文件使用完毕后必须关闭**，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：

```plain
>>> f.close()
```

由于文件读写时都有可能产生`IOError`，一旦出错，后面的`f.close()`就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用`try ... finally`来实现：

```python
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
```

但是每次都这么写实在太繁琐，所以，Python引入了`with`语句来自动帮我们调用`close()`方法：

```python
with open('/path/to/file', 'r') as f:
    print(f.read())
```

这和前面的`try ... finally`是一样的，但是代码更佳简洁，并且不必调用`f.close()`方法。

调用`read()`会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用`read(size)`方法，每次最多读取size个字节的内容。另外，调用`readline()`可以每次读取一行内容，调用`readlines()`一次读取所有内容并按行返回`list`。因此，要根据需要决定怎么调用。

如果文件很小，`read()`一次性读取最方便；如果不能确定文件大小，反复调用`read(size)`比较保险；如果是配置文件，调用`readlines()`最方便：

```python
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
```

### file-like Object

像`open()`函数返回的这种有个`read()`方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个`read()`方法就行。

`StringIO`就是在内存中创建的file-like Object，常用作临时缓冲。

### 二进制文件

前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用`'rb'`模式打开文件即可：

```plain
>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

### 字符编码

要读取非UTF-8编码的文本文件，需要给`open()`函数传入`encoding`参数，例如，读取GBK编码的文件：

```plain
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'
```

遇到有些编码不规范的文件，你可能会遇到`UnicodeDecodeError`，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，`open()`函数还接收一个`errors`参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

```plain
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
```

### 写文件

写文件和读文件是一样的，唯一区别是调用`open()`函数时，传入标识符`'w'`或者`'wb'`表示写文本文件或写二进制文件：

```plain
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
```

你可以反复调用`write()`来写入文件，但是务必要调用`f.close()`来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用`close()`方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用`close()`的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用`with`语句来得保险：

```python
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```

要写入特定编码的文本文件，请给`open()`函数传入`encoding`参数，将字符串自动转换成指定编码。

以`'w'`模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入`'a'`以追加（append）模式写入。

所有模式的定义及含义可以参考Python的[官方文档](https://docs.python.org/3/library/functions.html#open)。

在Python中，文件读写是通过`open()`函数打开的文件对象完成的。使用`with`语句操作文件IO是个好习惯。

## 13.2 StringIO & BytesIO

### StringIO

很多时候，数据读写不一定是文件，也可以在内存中读写。

`StringIO`顾名思义就是在内存中读写`str`。

要把`str`写入`StringIO`，我们需要先创建一个`StringIO`，然后，像文件一样写入即可：

```plain
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> f.write('world!')
6
>>> print(f.getvalue())
hello world!
```

`getvalue()`方法用于获得写入后的`str`。

要读取`StringIO`，可以用一个`str`初始化`StringIO`，然后，像读文件一样读取：

```plain
>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')
>>> while True:
...     s = f.readline()
...     if s == '':
...         break
...     print(s.strip())
...
Hello!
Hi!
Goodbye!
```

### BytesIO

`StringIO`操作的只能是`str`，如果要操作二进制数据，就需要使用`BytesIO`。

`BytesIO`实现了在内存中读写`bytes`，我们创建一个``Bytes`IO`，然后写入一些bytes：

```plain
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
```

请注意，写入的不是`str`，而是经过UTF-8编码的`bytes`。

和`StringIO`类似，可以用一个`bytes`初始化`BytesIO`，然后，像读文件一样读取：

```plain
>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
```

- 小结

`StringIO`和`BytesIO`是在内存中操作`str`和`bytes`的方法，使得和读写文件具有一致的接口。

## 13.3 操作文件和目录

操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如`dir`、`cp`等命令。

操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的`os`模块也可以直接调用操作系统提供的接口函数。

打开Python交互式命令行，我们来看看如何使用`os`模块的基本功能：

```plain
>>> import os
>>> os.name # 操作系统类型
'posix'		#mac系统
```

```plain
>>> import os
>>> os.name
'nt'    #win系统
```

如果是`posix`，说明系统是`Linux`、`Unix`或`macOS`，如果是`nt`，就是`Windows`系统。

要获取详细的系统信息，可以调用`uname()`函数：

```plain
>>> os.uname()
posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')

```

注意`uname()`函数在Windows上不提供，也就是说，**`os`模块的某些函数是跟操作系统相关的**。

### 环境变量

在操作系统中定义的**环境变量**，全部保存在`os.environ`这个变量中，可以直接查看：

```plain
>>> os.environ
environ({'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326', 'LOGNAME': 'michael', 'USER': 'michael', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin', ...})
```

要获取某个环境变量的值，可以调用`os.environ.get('key')`：

```plain
>>> os.environ.get('PATH')
'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
>>> os.environ.get('x', 'default')
'default'
```

### 操作文件和目录

操作文件和目录的函数一部分放在`os`模块中，一部分放在`os.path`模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

```plain
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
```

把两个路径合成一个时，不要直接拼字符串，而要通过`os.path.join()`函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，`os.path.join()`返回这样的字符串：

```plain
part-1/part-2
```

而Windows下会返回这样的字符串：

```plain
part-1\part-2
```

同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过`os.path.split()`函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

```plain
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
```

`os.path.splitext()`可以直接让你得到文件扩展名，很多时候非常方便：

```plain
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
```

这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

文件操作使用下面的函数。假定当前目录下有一个`test.txt`文件：

```plain
# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')
```

但是复制文件的函数居然在`os`模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

```plain
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
```

要列出所有的`.py`文件，也只需一行代码：

```plain
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
```

是不是非常简洁？

- 小结

Python的`os`模块封装了操作系统的目录和文件操作，要注意这些函数有的在`os`模块中，有的在`os.path`模块中。

## 13.4 序列化  变量从内存中变为可存储或传输的过程

在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：

```python
d = dict(name='Bob', age=20, score=88)
```

可以随时修改变量，比如把`name`改成`'Bill'`，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的`'Bill'`存储到磁盘上，下次重新运行程序，变量又被初始化为`'Bob'`。

我们**==把变量从内存中变成可存储或传输的过程称之为序列化==**，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了`pickle`模块来实现序列化。

首先，我们尝试把一个对象序列化并写入文件：

```plain
>>> import pickle
>>> d = dict(name='Bob', age=20, score=88)
>>> pickle.dumps(d)
b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
```

`pickle.dumps()`方法把任意对象序列化成一个`bytes`，然后，就可以把这个`bytes`写入文件。或者用另一个方法`pickle.dump()`直接把对象序列化后写入一个file-like Object：

```plain
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)
>>> f.close()
```

看看写入的`dump.txt`文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。

当我们要把对象从磁盘读到内存时，可以先把内容读到一个`bytes`，然后用`pickle.loads()`方法反序列化出对象，也可以直接用`pickle.load()`方法从一个`file-like Object`中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：

```plain
>>> f = open('dump.txt', 'rb')
>>> d = pickle.load(f)
>>> f.close()
>>> d
{'age': 20, 'score': 88, 'name': 'Bob'}
```

变量的内容又回来了！

当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。

Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

### JSON   实现在不同的编程语言之间传递对象

如果我们要==**在不同的编程语言之间传递对象，就必须把对象序列化为标准格式**==，比如XML，但更好的方法是==**序列化为JSON**==，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

| JSON类型   | Python类型 |
| ---------- | ---------- |
| {}         | dict       |
| []         | list       |
| "string"   | str        |
| 1234.56    | int或float |
| true/false | True/False |
| null       | None       |

Python内置的`json`模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：

```plain
>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)
'{"age": 20, "score": 88, "name": "Bob"}'
```

`dumps()`方法返回一个`str`，内容就是标准的JSON。类似的，`dump()`方法可以直接把JSON写入一个`file-like Object`。

要把JSON反序列化为Python对象，用`loads()`或者对应的`load()`方法，前者把JSON的字符串反序列化，后者从`file-like Object`中读取字符串并反序列化：

```plain
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json_str)
{'age': 20, 'score': 88, 'name': 'Bob'}
```

由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的`str`与JSON的字符串之间转换。

### JSON进阶

Python的`dict`对象可以直接序列化为JSON的`{}`，不过，很多时候，我们更喜欢用`class`表示对象，比如定义`Student`类，然后序列化：

```plain
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))
```

运行代码，毫不留情地得到一个`TypeError`：

```plain
Traceback (most recent call last):
  ...
TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
```

错误的原因是`Student`对象不是一个可序列化为JSON的对象。

如果连`class`的实例对象都无法序列化为JSON，这肯定不合理！

别急，我们仔细看看`dumps()`方法的参数列表，可以发现，除了第一个必须的`obj`参数外，`dumps()`方法还提供了一大堆的可选参数：

https://docs.python.org/3/library/json.html#json.dumps

这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把`Student`类实例序列化为JSON，是因为默认情况下，`dumps()`方法不知道如何将`Student`实例变为一个JSON的`{}`对象。

**可选参数`default`就是把任意一个对象变成一个可序列为JSON的对象**，我们只需要为`Student`专门写一个转换函数，再把函数传进去即可：

```python
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
```

这样，`Student`实例首先被`student2dict()`函数转换成`dict`，然后再被顺利序列化为JSON：

```plain
>>> print(json.dumps(s, default=student2dict))
{"age": 20, "name": "Bob", "score": 88}
```

不过，下次如果遇到一个`Teacher`类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意`class`的实例变为`dict`：

```python
print(json.dumps(s, default=lambda obj: obj.__dict__))
```

因为通常`class`的实例都有一个`__dict__`属性，它就是一个`dict`，用来存储实例变量。也有少数例外，比如定义了`__slots__`的class。

同样的道理，如果我们要把JSON反序列化为一个`Student`对象实例，`loads()`方法首先转换出一个`dict`对象，然后，我们传入的`object_hook`函数负责把`dict`转换为`Student`实例：

```python
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
```

运行结果如下：

```plain
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> print(json.loads(json_str, object_hook=dict2student))
<__main__.Student object at 0x10cd3c190>
```

打印出的是反序列化的`Student`实例对象。

- 小结

Python语言特定的序列化模块是`pickle`，但如果要把序列化搞得更通用、更符合Web标准，就可以使用`json`模块。

`json`模块的`dumps()`和`loads()`函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。

---

# 第十四章 进程和线程

现代操作系统比如Mac OS X，UNIX，Linux，Windows等，都是支持==**“多任务”**==的操作系统。

简单地说，==**“多任务”**==就是**<u>操作系统可以同时运行多个任务</u>**。打个比方，你一边在用浏览器上网，一边在听MP3，一边在用Word赶作业，这就是多任务，至少同时有3个任务正在运行。还有很多任务悄悄地在后台同时运行着，只是桌面上没有显示而已。

CPU执行代码都是顺序执行的，单核CPU的操作系统轮流让各个任务==**交替执行**==，任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。表面上看，每个任务都是交替执行的，但是，由于CPU的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样。    **==单核CPU快速地交替执行——制造“同时执行”的错觉==**

真正的**==并行执行==**多任务只能在多核CPU上实现，由于任务数量远远多于CPU的核心数量，操作系统也会自动把很多任务==**轮流调度到每个核心上执行**==。                                                  ==**多核CPU并行执行多任务，任务过多时轮流调度到各个核心执行**==

对于操作系统来说，==**一个任务就是一个进程**==（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。

有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把**==进程内的“子任务”称为线程==**（Thread）。

由于每个进程至少要干一件事，所以，**<u>一个进程至少有一个线程</u>**。当然，像Word这种复杂的进程可以有多个线程，多个线程可以同时执行，**<u>多线程的执行方式和多进程是一样的</u>**，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。

要同时执行多个任务的方法：

- 启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。

- 启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。

- 启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然这种模型更复杂，实际很少采用。

总结一下就是，多任务的实现有3种方式：

- 多进程模式；
- 多线程模式；
- 多进程+多线程模式。

同时执行多个任务通常各个任务之间需要相互通信和协调；有时，任务1必须暂停等待任务2完成后才能继续执行，有时，任务3和任务4又不能同时执行，所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单线程的程序。

因为复杂度高，调试困难，所以，不是迫不得已，我们也不想编写多任务。但是，有很多时候，没有多任务还真不行。想想在电脑上看电影，就必须由一个线程播放视频，另一个线程播放音频，否则，单线程实现的话就只能先把视频播放完再播放音频，或者先把音频播放完再播放视频，这显然是不行的。

==**线程是最小的执行单元,而进程由至少一个线程组成**==。如何调度进程和线程，完全<u>**由操作系统决定**</u>，程序自己不能决定什么时候执行，执行多长时间。多进程和多线程的程序涉及到<u>同步、数据共享</u>的问题，编写起来更复杂。

## 14.1 多进程

要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。

### fork   创建子进程

Unix/Linux操作系统提供了一个`fork()`系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是`fork()`调用一次，返回两次，因为**操作系统自动把当前进程（称为父进程）复制了一份（称为子进程）**，然后，分别在父进程和子进程内返回。

子进程永远返回`0`，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用`getppid()`就可以拿到父进程的ID。

Python的`os`模块封装了常见的系统调用，其中就包括`fork`，可以在Python程序中轻松创建子进程：

```python
import os

print('Process (%s) start...' % os.getpid())    #os.getpid()返回的是当前执行该代码的进程的ID 
# Only works on Unix/Linux/macOS:
pid = os.fork()       #fork()调用一次，子进程返回0，父进程返回子进程ID
if pid == 0:    #pid==0，返回0说明当前执行代码的进程为子进程，那么要用getppid()返回父进程ID
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:          #pid!=0,说明当前执行代码的进程是父进程，且返回的pid为子进程的ID
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
```

运行结果如下：

```plain
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
```

由于Windows没有`fork`调用，上面的代码在Windows上无法运行。而Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！

有了`fork`调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就`fork`出子进程来处理新的http请求。

### multiprocessing    跨平台多进程

如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有`fork`调用，难道在Windows上无法用Python编写多进程的程序？

由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。`multiprocessing`模块就是跨平台版本的多进程模块。

`multiprocessing`模块提供了一个`Process`类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：

```python
from multiprocessing import Process  # 导入多进程模块的Process类，用于创建子进程
#Process(target=函数名, args=参数元组) 定义子进程要执行的逻辑和参数。
import os  # 导入操作系统接口模块，用于获取进程ID

# 定义子进程要执行的函数
def run_proc(name):
    # 打印子进程名称和子进程的PID（os.getpid()返回当前执行此代码的进程ID，此处是子进程）
    # os.getpid()主进程中调用返回主进程PID，子进程中调用返回子进程PID。
    print('Run child process %s (%s)...' % (name, os.getpid())) 

# 主程序入口（Windows系统下多进程必须加此判断，避免递归创建子进程）
if __name__=='__main__':
    # 打印主进程的PID（此时os.getpid()执行在主进程，返回主进程ID）
    print('Parent process %s.' % os.getpid())
    # 创建子进程对象：指定子进程要执行的函数run_proc，以及传入的参数('test',)
    # 相当于创建子进程p，内容是执行函数run_proc,参数是元组('test',)
    p = Process(target=run_proc, args=('test',))   
    # 提示子进程即将启动
    print('Child process will start.')
    # 启动子进程（仅调用此方法，子进程才会被创建并运行，否则只是定义了进程对象） p.start()表示子进程开始执行函数run_proc
    p.start()
    # 主进程等待子进程执行完成后再继续运行（若不加此方法，主进程可能在子进程执行完前就退出）
    p.join()
    # 子进程执行完毕后，主进程打印结束提示
    print('Child process end.')
```

执行结果如下：

```plain
Parent process 928.
Child process will start.
Run child process test (929)...
Child process end.
```

创建子进程时，只需要传入一个执行函数和函数的参数，创建一个`Process`实例，用`start()`方法启动，这样创建进程比`fork()`还要简单。

`join()`方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

### Pool

如果要启动大量的子进程，可以用==**进程池**==的方式批量创建子进程：

```python
# 从multiprocessing模块导入Pool类（用于创建进程池，管理多个子进程）
from multiprocessing import Pool
# 导入os（获取进程ID）、time（计时）、random（生成随机休眠时间）模块
import os, time, random

# 定义子进程要执行的「耗时任务函数」
def long_time_task(name):
    # 打印当前任务名 + 执行该任务的子进程PID（os.getpid()返回当前进程ID）
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()  # 记录任务开始时间（时间戳）
    # 随机休眠0~3秒（模拟耗时操作）
    time.sleep(random.random() * 3)
    end = time.time()  # 记录任务结束时间
    # 打印任务名 + 任务运行时长（保留2位小数）
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# 主程序入口（Windows多进程必须加此判断，避免递归创建子进程）
if __name__=='__main__':
    # 打印主进程的PID（此时代码在主进程执行）
    print('Parent process %s.' % os.getpid())
    # 创建「进程池」，容量为4（最多同时运行4个进程，避免进程过多消耗资源）
    # 超过的任务会排队，等现有进程完成后自动复用进程
    p = Pool(4)
    # 循环创建5个任务（任务编号0~4）
    for i in range(5):
        # 异步提交任务到进程池：
        # 参数1是要执行的函数，参数2是函数的参数元组（这里传任务编号i）
        # 异步意味着主进程提交任务后不会等待，继续执行后续代码
        p.apply_async(long_time_task, args=(i,))
    # 主进程提交完所有任务后，打印「等待所有子进程完成」的提示
    print('waiting for all subprocesses done...')
    # 关闭进程池：禁止向进程池提交新任务（但已提交的任务会继续执行）
    p.close()
    # 主进程阻塞，等待进程池内所有子进程执行完毕
    p.join()
    # 所有子进程完成后，主进程打印「全部完成」的提示
    print('All subprocesses done.')
```

上述代码的执行流程：

1. **主进程启动**：打印主进程 PID，创建容量为 4 的进程池。
2. **提交任务**：循环提交 5 个任务到进程池（任务 0~4），由于是异步提交，==主进程快速提交完所有任务==，打印`waiting for all subprocesses done...`。
3. 进程池执行任务：
   - 进程池先启动 4 个进程，并行执行任务 0~3；
   - 当其中任意一个任务完成（比如任务 2 先结束），进程池会复用该进程，执行排队的任务 4；
   - 每个任务执行时，会打印自己的名称和对应的子进程 PID（注意：进程池会复用进程，所以不同任务可能用同一个 PID）。
4. **等待与结束**：所有任务完成后，主进程通过`p.join()`解除阻塞，打印`All subprocesses done.`。

执行结果如下：

```plain
Parent process 16782.  # 主进程PID
waiting for all subprocesses done...
Run task 0 (16783)...  # 任务0由子进程16783执行
Run task 1 (16784)...  # 任务1由子进程16784执行
Run task 2 (16785)...  # 任务2由子进程16785执行
Run task 3 (16786)...  # 任务3由子进程16786执行
Task 1 runs 0.89 seconds.  # 任务1先完成
Run task 4 (16784)...  # 复用子进程16784执行任务4
Task 0 runs 1.23 seconds.
Task 3 runs 1.56 seconds.
Task 2 runs 2.10 seconds.
Task 4 runs 2.75 seconds.
All subprocesses done.
```

代码解读：

对`Pool`对象调用`join()`方法会等待所有子进程执行完毕，调用`join()`之前必须先调用`close()`，调用`close()`之后就不能继续添加新的`Process`了。

请注意输出的结果，task `0`，`1`，`2`，`3`是立刻执行的，而task `4`要等待前面某个task完成后才执行，这是因为`Pool`的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是`Pool`有意设计的限制，并不是操作系统的限制。如果改成：

```python
p = Pool(5)
```

就可以同时跑5个进程。

由于`Pool`的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

### 控制子进程I\O   subprocess模块

很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

`subprocess`模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

下面的例子演示了如何在Python代码中运行命令`nslookup www.python.org`，这和命令行直接运行的效果是一样的：

```python
import subprocess
#nslookup 查询域名的DNS信息
print('$ nslookup www.python.org')
# 调用subprocess.call执行外部命令：
# 参数是列表形式 [命令名, 命令参数]，这里执行“nslookup www.python.org”
# subprocess.call会等待命令执行完成，返回命令的「退出状态码」（0表示成功，非0表示失败）
r = subprocess.call(['nslookup', 'www.python.org'])

# 打印命令的退出状态码
print('Exit code:', r)
```

运行结果：

```plain
$ nslookup www.python.org
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

非权威应答:
名称:    dualstack.python.map.fastly.net
Addresses:  2a04:4e42::223
          2a04:4e42:600::223
          2a04:4e42:400::223
          2a04:4e42:200::223
          151.101.192.223
          151.101.128.223
          151.101.0.223
          151.101.64.223
Aliases:  www.python.org

Exit code: 0
```

如果子进程还需要输入，则可以通过`communicate()`方法输入：

```python
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
```

上面的代码相当于在命令行执行命令`nslookup`，然后手动输入：

```plain
set q=mx
python.org
exit
```

运行结果如下：

```plain
$ nslookup
Server:		192.168.19.4
Address:	192.168.19.4#53

Non-authoritative answer:
python.org	mail exchanger = 50 mail.python.org.

Authoritative answers can be found from:
mail.python.org	internet address = 82.94.164.166
mail.python.org	has AAAA address 2001:888:2000:d::a6


Exit code: 0
```

### 进程间通信

`Process`之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的`multiprocessing`模块包装了底层的机制，提供了`Queue`、`Pipes`等多种方式来交换数据。

我们以`Queue`为例，在父进程中创建两个子进程，一个往`Queue`里写数据，一个从`Queue`里读数据：

```python
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
```

运行结果如下：

```plain
Process to write: 50563
Put A to queue...
Process to read: 50564
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.
```

在Unix/Linux下，`multiprocessing`模块封装了`fork()`调用，使我们不需要关注`fork()`的细节。由于Windows没有`fork`调用，因此，`multiprocessing`需要“模拟”出`fork`的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，如果`multiprocessing`在Windows下调用失败了，要先考虑是不是pickle失败了。

- 小结

在Unix/Linux下，可以使用`fork()`调用实现多进程。

要实现跨平台的多进程，可以使用`multiprocessing`模块。

进程间通信是通过`Queue`、`Pipes`等实现的。

## 14.2 多线程

多任务可以由多进程完成，也可以由一个进程内的多线程完成。

我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。

由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：`_thread`和`threading`，`_thread`是低级模块，`threading`是高级模块，对`_thread`进行了封装。绝大多数情况下，我们只需要使用`threading`这个高级模块。

启动一个线程就是把一个函数传入并创建`Thread`实例，然后调用`start()`开始执行：

```python
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
```

执行结果如下：

```plain
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
```

由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的`threading`模块有个`current_thread()`函数，它永远返回当前线程的实例。主线程实例的名字叫`MainThread`，子线程的名字在创建时指定，我们用`LoopThread`命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为`Thread-1`，`Thread-2`……

### Lock 锁

多线程和多进程最大的不同在于：

- 多进程中，同一个变量，各自有一份**拷贝**存在于每个进程中，互不影响；

- 多线程中，所有变量都由所有线程共享；

所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

来看看多个线程同时操作一个变量怎么把内容给改乱了：

```python
# multithread
import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))  
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
```

我们定义了一个共享变量`balance`，初始值为`0`，并且启动两个线程，先存后取，理论上结果应该为`0`，但是，由于线程的调度是由操作系统决定的，当`t1`、`t2`交替执行时，只要循环次数足够多，`balance`的结果就不一定是`0`了。

原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：

```python
balance = balance + n
```

也**分两步**：

1. 计算`balance + n`，**存入临时变量**中；
2. **将临时变量的值赋**给`balance`。

也就是可以看成：

```python
x = balance + n
balance = x
```

由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：

```plain
初始值 balance = 0

t1: x1 = balance + 5 # x1 = 0 + 5 = 5
t1: balance = x1     # balance = 5
t1: x1 = balance - 5 # x1 = 5 - 5 = 0
t1: balance = x1     # balance = 0

t2: x2 = balance + 8 # x2 = 0 + 8 = 8
t2: balance = x2     # balance = 8
t2: x2 = balance - 8 # x2 = 8 - 8 = 0
t2: balance = x2     # balance = 0
    
结果 balance = 0
```

但是**t1和t2是交替运行的**，如果操作系统以下面的顺序执行t1、t2：

```plain
初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2      # balance = -8

结果 balance = -8
```

究其原因，是因为==**修改`balance`需要多条语句，而执行这几条语句时，线程可能中断，从而导致*<u>多个线程把同一个对象的内容改乱</u>*了**==。

两个线程同时一存一取，就可能导致余额不对，所以，我们必须确保一个线程在修改`balance`的时候，别的线程一定不能改。

如果我们要确保`balance`计算正确，就要给`change_it()`上一把锁，当某个线程开始执行`change_it()`时，该线程因为获得了锁，因此其他线程不能同时执行`change_it()`，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过`threading.Lock()`来实现：

```python
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
```

当多个线程同时执行`lock.acquire()`时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用`try...finally`来确保锁一定会被释放。

**锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行**，**坏处首先是阻止了多线程并发执行**，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，**不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束**，只能靠操作系统强制终止。

### 多核CPU

多核应该可以同时执行多个线程？

如果写一个死循环的话，会出现什么情况呢？

打开Mac OS X的Activity Monitor，或者Windows的Task Manager，都可以监控某个进程的CPU使用率。

我们可以监控到一个死循环线程会100%占用一个CPU。

如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。

要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。

试试用Python写个死循环：

```python
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
```

启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。

但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？

因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，**多线程在Python中只能交替执行**，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

- 小结

多线程编程，模型复杂，容易发生冲突，必须**用锁加以隔离**，同时，又要**小心死锁**的发生。

Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

## 14.3 ThreadLocal  解决参数在一个线程各个函数间相互传递

在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。

但是局部变量在函数调用的时候，传递起来很麻烦：

```python
def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
```

每个函数一层一层调用都这么传参数那还得了？用全局变量？也不行，因为每个线程处理不同的`Student`对象，不能共享。

如果用一个全局`dict`存放所有的`Student`对象，然后以`thread`自身作为`key`获得线程对应的`Student`对象如何？

```python
global_dict = {}

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    ...
```

这种方式理论上是可行的，它最大的优点是消除了`std`对象在每层函数中的传递问题，但是，每个函数获取`std`的代码有点丑。

有没有更简单的方式？

`ThreadLocal`应运而生，不用查找`dict`，`ThreadLocal`帮你自动做这件事：

```python
import threading
    
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
```

执行结果：

```plain
Hello, Alice (in Thread-A)
Hello, Bob (in Thread-B)
```

全局变量`local_school`就是一个`ThreadLocal`对象，每个`Thread`对它都可以读写`student`属性，但互不影响。你可以把`local_school`看成全局变量，但每个属性如`local_school.student`都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，`ThreadLocal`内部会处理。

可以理解为全局变量`local_school`是一个`dict`，不但可以用`local_school.student`，还可以绑定其他变量，如`local_school.teacher`等等。

`ThreadLocal`最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

- 小结

一个`ThreadLocal`变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。`ThreadLocal`==解决了参数在一个线程中各个函数之间互相传递的问题。==

## 14.4 进程 VS 线程

多进程和多线程是实现多任务最常用的两种方式。现在，讨论一下这两种方式的优缺点。

首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。

如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。

如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。

多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用`fork`调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。

多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。

在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂。

### 线程切换

无论是多进程还是多线程，只要数量一多，效率肯定上不去，为什么呢？

我们打个比方，假设你不幸正在准备中考，每天晚上需要做语文、数学、英语、物理、化学这5科的作业，每项作业耗时1小时。

如果你先花1小时做语文作业，做完了，再花1小时做数学作业，这样，依次全部做完，一共花5小时，这种方式称为单任务模型，或者批处理任务模型。

假设你打算切换到多任务模型，可以先做1分钟语文，再切换到数学作业，做1分钟，再切换到英语，以此类推，只要切换速度足够快，这种方式就和单核CPU执行多任务是一样的了，以幼儿园小朋友的眼光来看，你就正在同时写5科作业。

但是，切换作业是有代价的，比如从语文切到数学，要先收拾桌子上的语文书本、钢笔（这叫保存现场），然后，打开数学课本、找出圆规直尺（这叫准备新环境），才能开始做数学作业。**操作系统在切换进程或者线程时也是一样的，它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态**。

所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。

### 计算密集型 vs. IO密集型

是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。

计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。

计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。

IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，几乎无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言开发效率最差。

### 异步IO

考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法并行执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。

现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。

对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。我们会在后面讨论如何编写协程。

## 14.5 分布式进程

在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

Python的`multiprocessing`模块不但支持多进程，其中`managers`子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于`managers`模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

举个例子：如果我们已经有一个通过`Queue`通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

原有的`Queue`可以继续使用，但是，通过`managers`模块把`Queue`通过网络暴露出去，就可以让其他机器的进程访问`Queue`了。

我们先看服务进程，服务进程负责启动`Queue`，把`Queue`注册到网络上，然后往`Queue`里面写入任务：

```python
# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')
```

请注意，当我们在一台机器上写多进程程序时，创建的`Queue`可以直接拿来用，但是，在分布式多进程环境下，添加任务到`Queue`不可以直接对原始的`task_queue`进行操作，那样就绕过了`QueueManager`的封装，必须通过`manager.get_task_queue()`获得的`Queue`接口添加。

然后，在另一台机器上启动任务进程（本机上启动也可以）：

```python
# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')
```

任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。

现在，可以试试分布式进程的工作效果了。先启动`task_master.py`服务进程：

```plain
$ python3 task_master.py 
Put task 3411...
Put task 1605...
Put task 1398...
Put task 4729...
Put task 5300...
Put task 7471...
Put task 68...
Put task 4219...
Put task 339...
Put task 7866...
Try get results...
```

`task_master.py`进程发送完任务后，开始等待`result`队列的结果。现在启动`task_worker.py`进程：

```plain
$ python3 task_worker.py
Connect to server 127.0.0.1...
run task 3411 * 3411...
run task 1605 * 1605...
run task 1398 * 1398...
run task 4729 * 4729...
run task 5300 * 5300...
run task 7471 * 7471...
run task 68 * 68...
run task 4219 * 4219...
run task 339 * 339...
run task 7866 * 7866...
worker exit.
```

`task_worker.py`进程结束，在`task_master.py`进程中会继续打印出结果：

```plain
Result: 3411 * 3411 = 11634921
Result: 1605 * 1605 = 2576025
Result: 1398 * 1398 = 1954404
Result: 4729 * 4729 = 22363441
Result: 5300 * 5300 = 28090000
Result: 7471 * 7471 = 55815841
Result: 68 * 68 = 4624
Result: 4219 * 4219 = 17799961
Result: 339 * 339 = 114921
Result: 7866 * 7866 = 61873956
```

这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上，比如把计算`n*n`的代码换成发送邮件，就实现了邮件队列的异步发送。

Queue对象存储在哪？注意到`task_worker.py`中根本没有创建Queue的代码，所以，Queue对象存储在`task_master.py`进程中：

```
                                             │
┌─────────────────────────────────────────┐     ┌──────────────────────────────────────┐
│task_master.py                           │  │  │task_worker.py                        │
│                                         │     │                                      │
│  task = manager.get_task_queue()        │  │  │  task = manager.get_task_queue()     │
│  result = manager.get_result_queue()    │     │  result = manager.get_result_queue() │
│              │                          │  │  │              │                       │
│              │                          │     │              │                       │
│              ▼                          │  │  │              │                       │
│  ┌─────────────────────────────────┐    │     │              │                       │
│  │QueueManager                     │    │  │  │              │                       │
│  │ ┌────────────┐ ┌──────────────┐ │    │     │              │                       │
│  │ │ task_queue │ │ result_queue │ │◀───┼──┼──┼──────────────┘                       │
│  │ └────────────┘ └──────────────┘ │    │     │                                      │
│  └─────────────────────────────────┘    │  │  │                                      │
└─────────────────────────────────────────┘     └──────────────────────────────────────┘
                                             │

                                          Network
```

而`Queue`之所以能通过网络访问，就是通过`QueueManager`实现的。由于`QueueManager`管理的不止一个`Queue`，所以，要给每个`Queue`的网络调用接口起个名字，比如`get_task_queue`。

`authkey`有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果`task_worker.py`的`authkey`和`task_master.py`的`authkey`不一致，肯定连接不上。

- 小结

Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。

注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。

---

# 第十五章 正则表达式

字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。比如判断一个字符串是否是合法的Email地址，虽然可以编程提取`@`前后的子串，再分别判断是否是单词和域名，但这样做不但麻烦，而且代码难以复用。

**正则表达式是一种用来匹配字符串的强有力的武器**。它的设计思想是用一种**描述性的语言**来给字符串定义一个规则，凡是**符合规则的字符串**，我们就认为它**“匹配”**了，否则，该字符串就是不合法的。

所以我们判断一个字符串是否是合法的Email的方法是：

1. **创建**一个匹配Email的正则表达式；
2. 用该正则表达式去**匹配**用户的输入来判断是否合法。

因为正则表达式也是用字符串表示的，所以，我们要首先了解如何用字符来描述字符。

在正则表达式中，如果直接给出字符，就是精确匹配。用**`\d`可以匹配一个数字**，**`\w`可以匹配一个字母或数字**，所以：

- `'00\d'`可以匹配`'007'`，但无法匹配`'00A'`；
- `'\d\d\d'`可以匹配`'010'`；
- `'\w\w\d'`可以匹配`'py3'`；

**`.`可以匹配任意字符**，所以：

- `'py.'`可以匹配`'pyc'`、`'pyo'`、`'py!'`等等。

要匹配变长的字符，在正则表达式中，**用`*`表示任意个字符（包括0个）**，**用`+`表示至少一个字符，==用`?`表示0个或1个字符==，用`{n}`表示n个字符，用`{n,m}`表示n-m个字符**：

来看一个复杂的例子：`\d{3}\s+\d{3,8}`。

我们来从左到右解读一下：

1. `\d{3}`表示匹配3个数字，例如`'010'`；
2. **`\s`可以匹配一个空格**（也包括Tab等空白符），所以`\s+`表示至少有一个空格，例如匹配`' '`，`' '`等；
3. `\d{3,8}`表示3-8个数字，例如`'1234567'`。

综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。

如果要匹配`'010-12345'`这样的号码呢？由于`'-'`是特殊字符，在正则表达式中，要用`'\'`转义，所以，上面的正则是`\d{3}\-\d{3,8}`。

但是，仍然无法匹配`'010 - 12345'`，因为带有空格。所以我们需要更复杂的匹配方式。

### 进阶

要做更精确地匹配，**可以用`[]`表示范围**，比如：

- `[0-9a-zA-Z\_]`可以匹配一个数字、字母或者下划线；
- `[0-9a-zA-Z\_]+`可以匹配至少由一个数字、字母或者下划线组成的字符串，比如`'a100'`，`'0_Z'`，`'Py3000'`等等；
- `[a-zA-Z\_][0-9a-zA-Z\_]*`可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
- `[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}`更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

`A|B`可以匹配A或B，所以`(P|p)ython`可以匹配`'Python'`或者`'python'`。

**`^`表示行的开头**，`^\d`表示必须以数字开头。

**`$`表示行的结束**，`\d$`表示必须以数字结束。

你可能注意到了，`py`也可以匹配`'python'`，但是加上`^py$`就变成了整行匹配，就只能匹配`'py'`了。

### re模块

有了准备知识，我们就可以在Python中使用正则表达式了。Python提供`re`模块，包含所有正则表达式的功能。由于Python的字符串本身也用`\`转义，所以要特别注意：

```python
s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成 'ABC\-001'
```

因此我们强烈建议使用Python的`r`前缀，就不用考虑转义的问题了：

```python
s = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：'ABC\-001'
```

先看看如何判断正则表达式是否匹配：

```plain
>>> import re
>>> re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>> re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
>>>
```

`match()`方法判断是否匹配，如果匹配成功，返回一个`Match`对象，否则返回`None`。常见的判断方法就是：

```python
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
```

### 切分字符串

用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：

```plain
>>> 'a b   c'.split(' ')
['a', 'b', '', '', 'c']
```

嗯，无法识别连续的空格，用正则表达式试试：

```plain
>>> re.split(r'\s+', 'a b   c')
['a', 'b', 'c']
```

无论多少个空格都可以正常分割。加入`,`试试：

```plain
>>> re.split(r'[\s\,]+', 'a,b, c  d')
['a', 'b', 'c', 'd']
```

再加入`;`试试：

```plain
>>> re.split(r'[\s\,\;]+', 'a,b;; c  d')
['a', 'b', 'c', 'd']
```

如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组。

### 分组

除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用`()`表示的就是要提取的分组（Group）。比如：

`^(\d{3})-(\d{3,8})$`分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：

```plain
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'
```

==**如果正则表达式中定义了组，就可以在`Match`对象上用`group()`方法提取出子串来。**==

注意到`group(0)`永远是与整个正则表达式相匹配的字符串，`group(1)`、`group(2)`……表示第1、2、……个子串。

提取子串非常有用。来看一个更凶残的例子：

```plain
>>> t = '19:05:30'
>>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
#这里第一个分组表示00-09,10-19,20-23,[0-9]是冗余匹配，\:也是冗余匹配，可以直接写成：
>>> m.groups()
('19', '05', '30')
```

这个正则表达式可以直接识别合法的时间。但是有些时候，用正则表达式也无法做到完全验证，比如识别日期：

```plain
'^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'
```

对于`'2-30'`，`'4-31'`这样的非法日期，用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了。

### 贪婪匹配

最后需要特别指出的是，==**<u>正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符</u>**==。举例如下，匹配出数字后面的`0`：

```plain
>>> re.match(r'^(\d+)(0*)$', '102300').groups()
('102300', '')
```

由于`\d+`采用贪婪匹配，直接把后面的`0`全部匹配了，结果`0*`只能匹配空字符串了。

必须让`\d+`采用非贪婪匹配（也就是尽可能少匹配），才能把后面的`0`匹配出来，==加个`?`就可以让`\d+`采用非贪婪匹配==：

```plain
>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')
```

### 编译

当我们在Python中使用正则表达式时，re模块内部会干两件事情：

1. **编译正则表达式**，如果正则表达式的字符串本身不合法，会报错；
2. **用编译后的正则表达式去匹配字符串**。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

```plain
>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
```

编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。

---

# 第十六章 常用内建模块

## 16.1 datetime

`datetime`是Python处理日期和时间的标准库。

### 获取当前日期和时间

我们先看如何获取当前日期和时间：

```plain
>>> from datetime import datetime
>>> now = datetime.now() # 获取当前datetime
>>> print(now)
2015-05-18 16:28:07.198690
>>> print(type(now))
<class 'datetime.datetime'>
```

注意到`datetime`是模块，`datetime`模块还包含一个`datetime`类，通过`from datetime import datetime`导入的才是`datetime`这个类。

如果仅导入`import datetime`，则必须引用全名`datetime.datetime`。

`datetime.now()`返回当前日期和时间，其类型是`datetime`。

### 获取指定日期和时间

要指定某个日期和时间，我们直接用参数构造一个`datetime`：

```plain
>>> from datetime import datetime
>>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
>>> print(dt)
2015-04-19 12:20:00
```

### datetime转换为timestamp

在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为`0`（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

你可以认为：

```plain
timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
```

对应的北京时间是：

```plain
timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
```

可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。

把一个`datetime`类型转换为timestamp只需要简单调用`timestamp()`方法：

```plain
>>> from datetime import datetime
>>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
>>> dt.timestamp() # 把datetime转换为timestamp
1429417200.0
```



注意Python的timestamp是一个浮点数，整数位表示秒。

某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

### timestamp转换为datetime

要把timestamp转换为`datetime`，使用`datetime`提供的`fromtimestamp()`方法：

```plain
>>> from datetime import datetime
>>> t = 1429417200.0
>>> print(datetime.fromtimestamp(t))
2015-04-19 12:20:00
```



注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。

本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：

```plain
2015-04-19 12:20:00
```



实际上就是UTC+8:00时区的时间：

```plain
2015-04-19 12:20:00 UTC+8:00
```



而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：

```plain
2015-04-19 04:20:00 UTC+0:00
```



timestamp也可以直接被转换到UTC标准时区的时间：

```plain
>>> from datetime import datetime
>>> t = 1429417200.0
>>> print(datetime.fromtimestamp(t)) # 本地时间
2015-04-19 12:20:00
>>> print(datetime.utcfromtimestamp(t)) # UTC时间
2015-04-19 04:20:00
```



### str转换为datetime

很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过`datetime.strptime()`实现，需要一个日期和时间的格式化字符串：

```plain
>>> from datetime import datetime
>>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
>>> print(cday)
2015-06-01 18:19:59
```



字符串`'%Y-%m-%d %H:%M:%S'`规定了日期和时间部分的格式。详细的说明请参考[Python文档](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)。

注意转换后的datetime是没有时区信息的。

### datetime转换为str

如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过`strftime()`实现的，同样需要一个日期和时间的格式化字符串：

```plain
>>> from datetime import datetime
>>> now = datetime.now()
>>> print(now.strftime('%a, %b %d %H:%M'))
Mon, May 05 16:28
```



### datetime加减

对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用`+`和`-`运算符，不过需要导入`timedelta`这个类：

```plain
>>> from datetime import datetime, timedelta
>>> now = datetime.now()
>>> now
datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
>>> now + timedelta(hours=10)
datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
>>> now - timedelta(days=1)
datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
>>> now + timedelta(days=2, hours=12)
datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)
```



可见，使用`timedelta`你可以很容易地算出前几天和后几天的时刻。

### 本地时间转换为UTC时间

本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

一个`datetime`类型有一个时区属性`tzinfo`，但是默认为`None`，所以无法区分这个`datetime`到底是哪个时区，除非强行给`datetime`设置一个时区：

```plain
>>> from datetime import datetime, timedelta, timezone
>>> tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
>>> now = datetime.now()
>>> now
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012)
>>> dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
>>> dt
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))
```



如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

### 时区转换

我们可以先通过`utcnow()`拿到当前的UTC时间，再转换为任意时区的时间：

```plain
# 拿到UTC时间，并强制设置时区为UTC+0:00:
>>> utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
>>> print(utc_dt)
2015-05-18 09:05:12.377316+00:00
# astimezone()将转换时区为北京时间:
>>> bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
>>> print(bj_dt)
2015-05-18 17:05:12.377316+08:00
# astimezone()将转换时区为东京时间:
>>> tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
>>> print(tokyo_dt)
2015-05-18 18:05:12.377316+09:00
# astimezone()将bj_dt转换时区为东京时间:
>>> tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
>>> print(tokyo_dt2)
2015-05-18 18:05:12.377316+09:00
```



时区转换的关键在于，拿到一个`datetime`时，要获知其正确的时区，然后强制设置时区，作为基准时间。

利用带时区的`datetime`，通过`astimezone()`方法，可以转换到任意时区。

注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的`datetime`都可以正确转换，例如上述`bj_dt`到`tokyo_dt`的转换。

### 小结

`datetime`表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储`datetime`，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

## 16.2 collections

`collections`是Python内建的一个集合模块，提供了许多有用的集合类。

### namedtuple

我们知道`tuple`可以表示不变集合，例如，一个点的二维坐标就可以表示成：

```plain
>>> p = (1, 2)
```



但是，看到`(1, 2)`，很难看出这个`tuple`是用来表示一个坐标的。

定义一个`class`又小题大做了，这时，`namedtuple`就派上了用场：

```plain
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.y
2
```



`namedtuple`是一个函数，它用来创建一个自定义的`tuple`对象，并且规定了`tuple`元素的个数，并可以用属性而不是索引来引用`tuple`的某个元素。

这样一来，我们用`namedtuple`可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

可以验证创建的`Point`对象是`tuple`的一种子类：

```plain
>>> isinstance(p, Point)
True
>>> isinstance(p, tuple)
True
```



类似的，如果要用坐标和半径表示一个圆，也可以用`namedtuple`定义：

```python
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])
```



### deque

使用`list`存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为`list`是线性存储，数据量大的时候，插入和删除效率很低。

`deque`是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

```plain
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
```



`deque`除了实现list的`append()`和`pop()`外，还支持`appendleft()`和`popleft()`，这样就可以非常高效地往头部添加或删除元素。

### defaultdict

使用`dict`时，如果引用的Key不存在，就会抛出`KeyError`。如果希望key不存在时，返回一个默认值，就可以用`defaultdict`：

```plain
>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1'] # key1存在
'abc'
>>> dd['key2'] # key2不存在，返回默认值
'N/A'
```



注意默认值是调用函数返回的，而函数在创建`defaultdict`对象时传入。

除了在Key不存在时返回默认值，`defaultdict`的其他行为跟`dict`是完全一样的。

### OrderedDict

使用`dict`时，Key是无序的。在对`dict`做迭代时，我们无法确定Key的顺序。

如果要保持Key的顺序，可以用`OrderedDict`：

```plain
>>> from collections import OrderedDict
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
>>> d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
>>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```



注意，`OrderedDict`的Key会按照插入的顺序排列，不是Key本身排序：

```plain
>>> od = OrderedDict()
>>> od['z'] = 1
>>> od['y'] = 2
>>> od['x'] = 3
>>> list(od.keys()) # 按照插入的Key的顺序返回
['z', 'y', 'x']
```



`OrderedDict`可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

```python
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
```



### ChainMap

`ChainMap`可以把一组`dict`串起来并组成一个逻辑上的`dict`。`ChainMap`本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。

什么时候使用`ChainMap`最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。我们可以用`ChainMap`实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。

下面的代码演示了如何查找`user`和`color`这两个参数：

```python
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
```



没有任何参数时，打印出默认参数：

```plain
$ python3 use_chainmap.py 
color=red
user=guest
```



当传入命令行参数时，优先使用命令行参数：

```plain
$ python3 use_chainmap.py -u bob
color=red
user=bob
```



同时传入命令行参数和环境变量，命令行参数的优先级较高：

```plain
$ user=admin color=green python3 use_chainmap.py -u bob
color=green
user=bob
```



### Counter

`Counter`是一个简单的计数器，例如，统计字符出现的个数：

```plain
>>> from collections import Counter
>>> c = Counter('programming')
>>> for ch in 'programming':
...     c[ch] = c[ch] + 1
...
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
>>> c.update('hello') # 也可以一次性update
>>> c
Counter({'r': 2, 'o': 2, 'g': 2, 'm': 2, 'l': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1})
```



`Counter`实际上也是`dict`的一个子类，上面的结果可以看出每个字符出现的次数。

### 小结

`collections`模块提供了一些有用的集合类，可以根据需要选用。

## 16.3



---

# 第十七章 常用第三方模块

Pass

---

# 第十八章 图形界面

Python支持多种图形界面的第三方库，包括：

- Tk
- wxWidgets
- Qt
- GTK

但是Python自带的库是支持Tk的Tkinter，无需安装任何包，就可以直接使用。本章简单介绍如何使用Tkinter进行**GUI编程**。

---

### GUI介绍

==这里解释一下什么是GUI==:Graphical User Interface(**图形化用户界面**),是用户与计算机程序系统交互的一种方式——**通过图形元素**来操作程序
具有如下特点:

- 可视化:用图形代替纯文字,直观易懂;
- 交互性:通过键鼠等方式操作;
- 所见即所得:操作结果实时可视化反馈

GUI编程是**开发具备图形用户界面的程序的过程**,通过编程语言+GUI框架,将**图形元素,用户操作,程序逻辑**三者结合,最终实现可视化交互

GUI程序是**通过GUI编程实现的、具有图形交互界面的==可执行程序==**,是相对于“命令行程序”的概念

**<u>*==总结:==*</u>**

- **GUI**：是一种 “图形化的交互方式”（界面形式）；
- **GUI 编程**：是 “开发这种图形界面程序的过程 / 技术”；
- **GUI 程序**：是 “最终产出的、可运行的图形界面应用”

### Tkinter

我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；

Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；

Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。

所以，我们的代码只需要调用Tkinter提供的接口就可以了。

### 第一个GUI程序

使用Tkinter十分简单，我们来编写一个GUI版本的“Hello, world!”。

第一步是导入Tkinter包的所有内容：

```python
from tkinter import *  
#导入Tkinter模块的所有内容,*表示“导入模块里的所有类、函数、变量”
```

第二步是从`Frame`派生一个`Application`类，这是所有Widget(组件/控件)的父容器：

> Widget是GUI界面中所有可显示、可交互元素的统称——小到显示文字的标签、可点击的按钮,大到容纳其他元素的容器,都市Widget.一句话,GUI界面上能看到、能操作的每一个“部件”都是Widget.

```python
class Application(Frame):
    def __init__(self, master=None):
    #self是类实例本身,master是类的父容器,默认值为None表示暂时未指定父容器
        Frame.__init__(self, master)
        #调用父类Frame的构造方法,,把当前Application实例作为Frame的实例初始化,并指定它的父容器为master
        self.pack()
        #pack()是Tkinter的布局管理器方法之一,作用是把当前Widget添加到它的父容器里,并完成排版
        self.createWidgets()
        #调用类里自定义的creatWidgets()方法,用来创建具体的界面组件(按钮、标签……)
	#以下是自定义的方法creatWidgets,用来创建并布局具体的功能型Widget
    def createWidgets(self):
        #创建一个Label组件,self表示这个Lable的父容器是当前的Application,text用于设置Lable			显示的文本内容,创建好的Label赋值给self.hellloLabel
        self.helloLabel = Label(self, text='Hello, world!')
        #调用Label的pack()方法,把这个显示Hello的Label添加到它的父容器中并完成排版
        self.helloLabel.pack()
        #self.quit()是Frame类继承来的方法，作用是退出当前GUI程序
        self.quitButton = Button(self, text='Quit', command=self.quit)
        #调用Button的pack()方法，把 “Quit 按钮” 添加到Application容器中并排版
        self.quitButton.pack()
```

- `Frame`是 Tkinter 中的一种**容器型 Widget**—— 它本身不直接显示内容，而是用来 “装其他 Widget”，相当于一个 “界面容器盒子”。
- 所以`Application`作为`Frame`的子类，本身也是一个 “容器 Widget”，用来组织后续的界面元素。

在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。

`pack()`方法把Widget加入到父容器中，并实现布局。`pack()`是最简单的布局，`grid()`可以实现更复杂的布局。

在`createWidgets()`方法中，我们创建一个`Label`和一个`Button`，当Button被点击时，触发`self.quit()`使程序退出。

第三步，实例化`Application`，并启动消息循环：

```python
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 启动GUI主循环：监听用户操作（比如点击按钮）、保持窗口显示:
app.mainloop()
```

**这里对mainloop()解释**:启动GUI的主消息循环,保持窗口一直显示、监听用户的操作(输入文本、点击按钮)、监听到操作就立即出发对应的逻辑.

GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理。

运行这个GUI程序，可以看到下面的窗口：

![tk-hello-world](https://liaoxuefeng.com/books/python/gui/hello.png)

点击“Quit”按钮或者窗口的“x”结束程序。

### 输入文本

我们再对这个GUI程序改进一下，加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。

```python
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #Entry组件,输入型Widget,用于让用户输入文本
        self.nameInput = Entry(self)
        self.nameInput.pack()
        #command=self.hello指定了点击按钮时要执行的函数,这里绑定了下面定义的hello方法
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
	
    #hello方法是按钮点击后的逻辑,获取输入+弹出提示框
    def hello(self):
        #self.nameInput.get()调用Entry的get()方法,获取用户在输入框中输入的内容
        name = self.nameInput.get() or 'world'
        #调用messagebox的showinfo()方法，弹出一个信息提示框,第一个参数Message是提示框的标题,第二个参数是提示框的内容
        messagebox.showinfo('Message', 'Hello, %s' % name)

#创建Application类的实例（此时它的父容器master默认是None，Tkinter 会自动为它创建一个主窗口作为父容器）
app = Application()
# 设置窗口标题:
#app.master表示Application实例的父容器（即自动创建的主窗口）；
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
```

当用户点击按钮时，触发`hello()`，通过`self.nameInput.get()`获得用户输入的文本后，使用`tkMessageBox.showinfo()`可以弹出消息对话框。

程序运行结果如下：

![tk-say-hello](https://liaoxuefeng.com/books/python/gui/message.png)

- 小结

Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。

## 18.1 海龟绘图

在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——[LOGO语言](https://baike.baidu.com/item/LOGO语言/5881905)，它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图。

海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，Python内置了`turtle`库，基本上100%复制了原始的Turtle Graphics的所有功能。

我们来看一个指挥小海龟绘制一个长方形的简单代码：

```python
# 导入turtle包的所有内容:
from turtle import *

# 设置笔刷宽度:
width(4)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
```

在命令行运行上述代码，会自动弹出一个绘图窗口，然后绘制出一个长方形：

![rect](https://liaoxuefeng.com/books/python/gui/turtle/rect.jpg)

从程序代码可以看出，海龟绘图就是指挥海龟前进、转向，海龟移动的轨迹就是绘制的线条。要绘制一个长方形，只需要让海龟前进、右转90度，反复4次。

调用`width()`函数可以设置笔刷宽度，调用`pencolor()`函数可以设置颜色。更多操作请参考[turtle库](https://docs.python.org/3.3/library/turtle.html#turtle-methods)的说明。

绘图完成后，记得==调用`done()`函数，让窗口进入消息循环，等待被关闭==。否则，由于Python进程会立刻结束，将导致窗口被立刻关闭。

`turtle`包本身只是一个绘图库，但是配合Python代码，就可以绘制各种复杂的图形。例如，通过循环绘制5个五角星：

```python
from turtle import *

#定义画五角星的函数,在指定坐标(x,y)画一个边长为40的五角星
def drawStar(x, y):
    pu()#抬起画笔pen up,移动是时不画线
    goto(x, y)#移动海龟到坐标(x,y)
    pd()#放下画笔pen down,移动时开始画线
    # set heading: 0
    seth(0)#设置海龟朝向,0表示朝右
    for i in range(5):#循环五次
        fd(40)
        rt(144)#向右转144度

for x in range(0, 250, 50):
    drawStar(x, 0)

done()
```

程序执行效果如下：

![stars](https://liaoxuefeng.com/books/python/gui/turtle/stars.jpg)

使用递归，可以绘制出非常复杂的图形。例如，下面的代码可以绘制一棵分型树：

> 核心是利用 “自相似” 的递归逻辑生成层层分叉的树枝，同时动态调整画笔颜色和宽度，让树的视觉效果更贴近真实树木（主干粗、分支细，颜色渐变）

```python
from turtle import *

# 设置色彩模式是RGB:
colormode(255)

lt(90)#向左转90度,turtle初始朝右,转后朝上

#核心参数,可以修改调整数的形态
lv = 14#树的递归最大层数,数值越大分支越多
l = 120#初始主干长度
s = 45#分支的转角角度,控制树枝分叉的张开程度

width(lv)#初始画笔宽度

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

# 移动画笔到绘图起点（让树干从画布下方开始画）
penup()
bk(l)#向后退
pendown()
fd(l)

#核心递归函数,函数会重复调用自身生成层层分支，直到达到最大递归层数
def draw_tree(l, level):
    global r, g, b
    # save the current pen width,后续修改宽度后要恢复,保证上层分支宽度不变
    w = width()

    # narrow the pen width  调整画笔
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    # 取模200：避免RGB值超过255（也可%255），让颜色循环渐变
    pencolor(r % 200, g % 200, b % 200)
	
    # 缩短当前分支长度（分支越细，长度也越短）
    l = 3.0 / 4.0 * l

    #画左分支
    lt(s)#左转45度
    fd(l)#向前走缩短后的长度

    if level < lv:# 递归终止条件：没到最大层数就继续画
        draw_tree(l, level + 1) # 递归调用，画左分支的下一层子分支
    bk(l)# 后退l像素（回到分支的分叉点）
    
    #画右分支
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    
    #恢复状态
    lt(s)
    # restore the previous pen width
    width(w)

speed("slow")
# 调用递归函数：初始长度l=120，初始层数4（从第4层开始递归到第14层）
draw_tree(l, 4)
done()
```

执行上述程序需要花费一定的时间，最后的效果如下：

![tree](https://liaoxuefeng.com/books/python/gui/turtle/tree.jpg)

---

# 第十九章 网络编程

计算机网络就是把各个计算机连接到一起,让网络中的计算机可以互相通信.网络编程就是如何在程序中实现两台计算机的通信

==**eg.**== 当你使用浏览器访问新浪网时，你的计算机就和新浪的某台服务器通过互联网连接起来了，然后，新浪的服务器把网页内容作为数据通过互联网传输到你的电脑上。

更确切地说,网络通信是两台计算机上的两个进程之间的通信。比如,浏览器进程和新浪服务器上的某个Web服务进程在通信,而QQ进程和腾讯的某个服务器上的某个进程在通信。        **==网络通信是两个进程之间在通信==**

网络编程对所有开发语言都是一样的，Python也不例外。用Python进行网络编程，就是在Python程序本身这个进程内，连接别的服务器进程的通信端口进行通信。

## 19.1 TCP/IP简介

计算机网络的出现比互联网要早很多。

计算机为了联网，就必须规定**通信协议**，早期的计算机网络，都是由各厂商自己规定一套协议，IBM、Apple和Microsoft都有各自的网络协议，互不兼容，这就好比一群人有的说英语，有的说中文，有的说德语，说同一种语言的人可以交流，不同的语言之间就不行了。

为了把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，为了实现互联网这个目标，互联网协议簇（Internet Protocol Suite）就是通用协议标准。Internet是由inter和net两个单词组合起来的，原意就是连接“网络”的网络，有了Internet，任何私有网络，只要支持这个协议，就可以联入互联网。

因为互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，所以，大家把互联网的协议简称TCP/IP协议。

==**通信的时候，双方必须知道对方的标识**==，好比发邮件必须知道对方的邮件地址。**<u>互联网上每个计算机的唯一标识就是IP地址</u>**，类似`123.123.123.123`。如果一台计算机同时接入到两个或更多的网络，比如路由器，它就会有两个或多个IP地址，所以，**<u>IP地址对应的实际上是计算机的网络接口，通常是网卡</u>**。

**==IP协议负责把数据从一台计算机通过网络发送到另一台计算机==**。数据被分割成一小块一小块，然后通过IP包发送出去。由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。<u>***IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达***</u>。

![internet-computers](https://liaoxuefeng.com/books/python/network/tcp-ip/net.png)

IP地址实际上是一个32位整数（称为IPv4），以字符串表示的IP地址如`192.168.0.1`实际上是把32位整数按8位分组后的数字表示，目的是便于阅读。

IPv6地址实际上是一个128位整数，它是目前使用的IPv4的升级版，以字符串表示类似于`2001:0db8:85a3:0042:1000:8a2e:0370:7334`。

TCP协议则是建立在IP协议之上的。**TCP协议负责在两台计算机之间==建立可靠连接，保证数据包按顺序到达==**。TCP协议会**通过握手建立连接**，然后，**对每个IP包编号**，**确保对方按顺序收到**，**丢包则自动重发**。

许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。

一个TCP报文除了包含要传输的数据外，还包含**源IP地址和目标IP地址**，**源端口和目标端口**。

**端口**有什么作用？在两台计算机通信时，**只发IP地址是不够的**，因为同一台计算机上跑着多个网络程序。一个TCP报文来了之后，到底是交给浏览器还是QQ，就**需要端口号来区分**。<u>每个网络程序都向操作系统申请唯一的端口号</u>，这样，==**两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号**==。     **<u>IP地址和端口号确保两个进程顺利建立网络连接</u>**

一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。

## 19.2 TCP编程

Socket(插座)是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。

### 客户端

大多数连接都是可靠的TCP连接。**创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。**

举个例子，当我们在浏览器中访问新浪时，我们自己的计算机就是客户端，浏览器会主动向新浪的服务器发起连接。如果一切顺利，新浪的服务器接受了我们的连接，一个TCP连接就建立起来的，后面的通信就是发送网页内容了。

所以，我们要创建一个基于TCP连接的Socket，可以这样做：

```python
# 导入socket库:
import socket

# 创建一个socket,指定通信协议类型:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
```

创建`Socket`时，`AF_INET`全称`Address Family Internet Protocol v4`，指定使用**IPv4 地址协议**，如果要用更先进的IPv6，就指定为`AF_INET6`。`SOCK_STREAM`指定使用面向流的**TCP协议(传输控制协议)**，这样，一个`Socket`对象就创建成功，但是还没有建立连接。

**==补充==**:socket 默认是阻塞模式（比如`connect`、`recv`会等待服务器响应，不会立即返回），这也是代码中能 “循环接收数据” 的基础。

**客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。**新浪网站的IP地址可以用域名`www.sina.com.cn`自动转换到IP地址，但是怎么知道新浪服务器的端口号呢？

答案是**作为服务器，提供什么样的服务，端口号就必须固定下来。**由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在`80`端口，因为`80`端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是`25`端口，FTP服务是`21`端口，等等。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

因此，我们连接新浪服务器的代码如下：

```python
s.connect(('www.sina.com.cn', 80))
```

注意参数是一个`tuple`，包含地址和端口号。

建立TCP连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容：

```python
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
```

`Connection: close`:告诉服务器：响应完成后关闭 TCP 连接（避免长连接占用资源）

`\r\n\r\n`:HTTP 请求头的结束标志（空行，分隔请求头和请求体；GET 请求无请求体，所以用空行收尾）

**TCP连接创建的是双向通道，双方都可以同时给对方发数据**。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。例如，**HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。**

发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了：

```python
# 接收数据:
buffer = []#空列表，用于临时存储分段接收的字节数据
while True:#无限循环,直到接受完所有数据
    # 每次最多接收1k字节:
    d = s.recv(1024)
    #从 socket 的接收缓冲区读取最多 1024 字节（1KB）的数据，返回字节类型（bytes）；阻塞特性：如果服务器还没返回数据，recv()会阻塞（等待），直到有数据或连接关闭；
    if d:#如果接收到数据（d非空），就添加到buffer列表
        buffer.append(d)
    else:#如果d为空，说明服务器已关闭 TCP 连接（数据接收完毕），跳出循环
        break
data = b''.join(buffer)
```

接收数据时，调用`recv(max)`方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到`recv()`返回空数据，表示接收完毕，退出循环。

当我们接收完数据后，调用`close()`方法关闭Socket，这样，一次完整的网络通信就结束了：

```python
# 关闭连接:
s.close()
```

接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：

```python
#拆分响应头和响应体,按 HTTP 响应的格式拆分 “响应头” 和 “响应体”（HTML 内容）
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))#打印响应头（解码为字符串）
# 把接收的数据写入文件:
#with open(...) as f：上下文管理器，自动管理文件的打开 / 关闭 —— 即使写入过程中出错，也会保证文件正常关闭，避免资源泄漏
with open('sina.html', 'wb') as f:
    f.write(html)
```

- `header`：字节类型的 HTTP 响应头（包含状态码、服务器信息、重定向地址等）；
- `html`：字节类型的 HTTP 响应体（新浪首页的 HTML 代码，也是最终要保存的内容）
- `'wb'`：文件打开模式 ——`w`是 “写入模式”（**覆盖已有文件，无则创建**），`b`是 “二进制模式”（因为`html`是字节类型，必须用二进制模式写入，不能用`w`（文本模式））；

现在，只需要在浏览器中打开这个`sina.html`文件，就可以看到新浪的首页了。

在py交互环境下,文件被保存到了交互环境的默认工作目录中，在我的mac电脑上

```python
import os
print(os.getcwd())  # 打印当前工作目录路径
```

在py交互环境下,输出结果为`/Users/ipromise'`

若是想把文件保存到桌面,需要修改`open()`的路径为桌面的绝对路径：

```python
# Mac/Linux（替换“你的用户名”为实际用户名）
desktop_path = '/Users/ipromise/Desktop/sina.html'
with open(desktop_path, 'wb') as f:
    f.write(html)
```

或者有方法二,自动获取桌面路径,适用于跨平台

```python
import os
import os.path

# 自动获取桌面路径
if os.name == 'nt':  # Windows系统
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
else:  # Mac/Linux
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')

# 拼接文件路径
file_path = os.path.join(desktop, 'sina.html')

# 保存到桌面
with open(file_path, 'wb') as f:
    f.write(html)
```

**==注意==**:上述操作形成的`.html`文件打开后会出现`302 Found`,302是HTTP的状态码之一,表示为`你请求的资源被临时转移到了另一个URL`,因为现在几乎所有主流网站都会把`http://`开头的请求（默认 80 端口），强制重定向到`https://`开头的加密地址（默认 443 端口）—— 这是为了安全。

### 服务器

和客户端编程相比，服务器编程就要复杂一些。

==**服务器进程首先要绑定一个端口并监听来自其他客户端的连接**==。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。

所以，**服务器会打开固定端口（比如80）监听**，**每来一个客户端连接，就创建该Socket连接**。由于服务器会有大量来自客户端的连接，所以，**服务器要能够区分一个Socket连接是和哪个客户端绑定的**。一个Socket依赖4项：**服务器地址、服务器端口、客户端地址、客户端端口**来唯一确定一个Socket。

但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。

我们来编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上`Hello`再发回去。

首先，**创建一个基于IPv4和TCP协议的Socket**：

```python
import socket#网络通信
import threading#多线程
import time#延时
#创建 TCP Socket 对象,用于监听和接收客户端连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#
```

然后，**我们要绑定监听的地址和端口**。服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用`0.0.0.0`绑定到所有的网络地址，还可以用`127.0.0.1`绑定到本机地址。`127.0.0.1`是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，也就是说，外部的计算机无法连接进来。

端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用`9999`这个端口号。请注意，小于`1024`的端口号必须要有管理员权限才能绑定：

```python
# 监听端口:
s.bind(('127.0.0.1', 9999))
```

`bind()`是服务器端专属操作，客户端用`connect()`，服务器用`bind()`固定通信地址。

紧接着，调用`listen()`方法开始**监听端口**，**传入的参数指定等待连接的最大数量**：

```python
s.listen(5)#5是监听队列大小,表示服务器最多同时刮起5个未处理的连接请求
#控制台输出提示，告知服务器已启动并等待客户端连接
print('Waiting for connection...')
```

- **注意**：`listen()`仅开启监听，不会阻塞，真正阻塞的是后续的`accept()`。

接下来，服务器程序通过一个**永久循环**来接受来自客户端的连接，`accept()`会等待并返回一个客户端的连接:

```python
#主循环：无限等待客户端连接
while True:#无限循环，服务器持续运行，永不退出（除非手动终止）
    # 接受一个新连接:
    sock, addr = s.accept()#阻塞等待客户端的连接请求，有客户端连接成功才返回
    # 创建新线程来处理TCP连接:
    #创建新线程，指定线程要执行的函数是tcplink，并传入参数(sock, addr)（即和当前客户端通信的Socket、客户端地址）
    t = threading.Thread(target=tcplink, args=(sock, addr))
    #启动新线程，tcplink函数会在新线程中执行，主循环立即回到accept()继续等待下一个客户端
    t.start()
```

- `sock`：新的 Socket 对象 —— 专门用于和当前连接的客户端通信（服务器原有`s`仍继续监听新连接）；
- `addr`：元组`(客户端IP, 客户端端口)`，标识连接的客户端身份。
- `accept()`是阻塞函数，没有客户端连接时，代码会卡在这一行，不会执行后续逻辑。
- **为什么用多线程**：如果不用线程，服务器处理一个客户端连接时（比如循环接收数据），会阻塞`accept()`，无法响应其他客户端；多线程让每个客户端连接独立处理，主循环能继续监听新连接。

**每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接**：

```python
#定义处理单个客户端连接的函数tcplink,这个函数运行在独立线程中,处理和单个客户端的通信
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    #向客户端发送欢迎消息（字节类型）,b''用于将字符串转为字节
    sock.send(b'Welcome!')
    while True:#循环和客户端通信，直到客户端断开或发送exit
        data = sock.recv(1024)#阻塞接收客户端发送的数据，最多接收1024字节
        time.sleep(1)#延时1秒,模拟服务器处理数据的耗时
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    #关闭和当前客户端通信的Socket，释放资源
    sock.close()
    #控制台打印，告知该客户端连接已关闭
    print('Connection from %s:%s closed.' % addr)
```

- `not data`：客户端断开连接（`recv()`返回空字节`b''`）；
- `data.decode('utf-8') == 'exit'`：客户端发送的内容**解码**为字符串后是`exit`；
- `break`：满足任一条件，跳出通信循环，准备关闭连接;
- `.encode('utf-8')`：转回字节类型，通过 Socket 发送;

连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上`Hello`再发送给客户端。如果客户端发送了`exit`字符串，就直接关闭连接。

==**概念补充**==:

1. **服务器的 “双 Socket” 设计**：

   - 主 Socket `s`：仅用于绑定、监听、接受连接，不参与和客户端的具体通信；
   - 子 Socket `sock`：`accept()`返回的新 Socket，专门和单个客户端通信，每个客户端对应一个独立的`sock`。

2. **多线程的必要性**：

   单线程服务器的问题：处理 A 客户端时，会卡在`recv()`/`send()`，无法响应 B 客户端的连接请求；

   多线程解决：每个客户端连接用独立线程处理，主线程始终在`accept()`等待新连接，实现 “同时” 处理多个客户端。

3. **阻塞特性总结**：

   - `accept()`：阻塞等待客户端连接；
   - `recv()`：阻塞等待客户端发送数据；
   - 这些阻塞仅影响当前线程，不影响其他线程（比如处理 B 客户端的线程阻塞，不影响处理 A 客户端的线程）

要测试这个服务器程序，我们还需要编写一个客户端程序：

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```

需要打开两个命令行窗口，一个运行服务器程序，一个运行客户端程序，就可以看到效果：

> 图一为服务器,图二为客户端

![截屏2025-12-15 22.54.40](../../截屏2025-12-15 22.54.40.png)

![截屏2025-12-15 22.54.48](../../截屏2025-12-15 22.54.48.png)

需要注意的是，客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序。

注:要想运行测试客户端和服务器的连接,要将客户端和服务器代码保存为`.py`文件,在终端中直接调用`python3 文件名.py`(**不要进入交互环境**),先运行服务器绑定端口保持监听状态再运行客户端才能连接

- 小结

用TCP协议进行Socket编程在Python中十分简单
对于客户端，要主动连接服务器的IP和指定端口
对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。

同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。

## 19.3 UDP编程

TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，**UDP则是面向无连接的协议。**

使用UDP协议时，不需要建立连接，**只需要知道对方的IP地址和端口号**，**就可以直接发数据包**。但是，能不能到达就不知道了。

虽然**用UDP传输数据不可靠**，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。

我们来看看如何通过UDP协议传输数据。和TCP类似，使用UDP的通信双方也分为客户端和服务器。服务器首先需要绑定端口：

```python
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
```

创建Socket时，`SOCK_DGRAM`指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用`listen()`方法，而是直接接收来自任何客户端的数据：

```python
print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
```

`recvfrom()`方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用`sendto()`就可以把数据用UDP发给客户端。

注意这里省掉了多线程，因为这个例子很简单。

客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用`connect()`，直接通过`sendto()`给服务器发数据：

```python
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
```

从服务器接收数据仍然调用`recv()`方法。

仍然用两个命令行分别启动服务器和客户端测试，结果如下：

```
┌────────────────────────────────────────────────────────┐
│Windows PowerShell                                - □ x │
├────────────────────────────────────────────────────────┤
│PS C:\Users\liaoxuefeng> python udp_server.py           │
│Bind UDP on 9999...                                     │
│Received from 127.0.0.1:63823...                        │
│Received from 127.0.0.1:63823...                        │
│Received from 127.0.0.1:63823...                        │
│       ┌────────────────────────────────────────────────┴───────┐
│       │Windows PowerShell                                - □ x │
│       ├────────────────────────────────────────────────────────┤
│       │PS C:\Users\liaoxuefeng> python udp_client.py           │
└───────┤Welcome!                                                │
        │Hello, Michael!                                         │
        │Hello, Tracy!                                           │
        │Hello, Sarah!                                           │
        │PS C:\Users\liaoxuefeng>                                │
        │                                                        │
        │                                                        │
        └────────────────────────────────────────────────────────┘
```

- 小结

UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的`9999`端口与TCP的`9999`端口可以各自绑定。

---

# 第二十章 电子邮件

Email的历史比Web还要久远，直到现在，Email也是互联网上应用非常广泛的服务。

几乎所有的编程语言都支持发送和接收电子邮件，在开始编写代码之前，有必要搞清楚电子邮件是如何在互联网上运作的。

传统邮件是如何运作的?假设你现在在北京，要给一个香港的朋友发一封信，怎么做呢？

首先你得写好信，装进信封，写上地址，贴上邮票，然后就近找个邮局，把信仍进去。

信件会从就近的小邮局转运到大邮局，再从大邮局往别的城市发，比如先发到天津，再走海运到达香港，也可能走京九线到香港，但是你不用关心具体路线，你只需要知道一件事，就是信件走得很慢，至少要几天时间。

信件到达香港的某个邮局，也不会直接送到朋友的家里，因为邮局的叔叔是很聪明的，他怕你的朋友不在家，一趟一趟地白跑，所以，信件会投递到你的朋友的邮箱里，邮箱可能在公寓的一层，直到你的朋友回家的时候检查邮箱，发现信件后，就可以取到邮件了。

电子邮件的流程基本上也是按上面的方式运作的，只不过速度不是按天算，而是按秒算。

现在我们回到电子邮件，假设我们自己的电子邮件地址是`me@163.com`，对方的电子邮件地址是`friend@sina.com`，现在我们用`Outlook`或者`Foxmail`之类的软件写好邮件，填上对方的Email地址，点“发送”，电子邮件就发出去了。这些**电子邮件软件被称为MUA**：Mail User Agent——**邮件用户代理**。

Email从MUA发出去，不是直接到达对方电脑，而是发到**MTA**：Mail Transfer Agent——**邮件传输代理**，就是那些**Email服务提供商**，比如网易、新浪等等。由于我们自己的电子邮件是`163.com`，所以，Email首先被投递到网易提供的MTA，再由网易的MTA发到对方服务商，也就是新浪的MTA。这个过程中间可能还会经过别的MTA，但是我们不关心具体路线，我们只关心速度。

Email到达新浪的MTA后，由于对方使用的是`@sina.com`的邮箱，因此，新浪的MTA会把Email投递到邮件的最终目的地**MDA**：Mail Delivery Agent——**邮件投递代理**。Email到达MDA后，就静静地躺在新浪的某个服务器上，存放在某个文件或特殊的数据库里，将这个**长期保存邮件的地方称为电子邮箱**。

同普通邮件类似，Email不会直接到达对方的电脑，因为对方电脑不一定开机，开机也不一定联网。**对方要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上。**

所以，一封电子邮件的旅程就是：

==**邮件软件MUA(邮件用户代理)	Email服务提供商MTA(邮件传输代理)	邮件最终目的地MDA(邮件投递代理)**==

```plain
发件人 -> MUA -> MTA(自己的) -> MTA(对方的) -> 若干个MTA -> MDA <- MUA <- 收件人
```

有了上述基本概念，要编写程序来发送和接收邮件，本质上就是：

1. 编写MUA把邮件发到MTA；
2. 编写MUA从MDA上收邮件。

发邮件时，MUA和MTA使用的协议就是**SMTP**：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议。

收邮件时，MUA和MDA使用的协议有两种：

- **POP**：Post Office Protocol，目前版本是3，俗称POP3；
- **IMAP**：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。

邮件客户端软件在发邮件时，会让你先配置SMTP服务器，也就是你要发到哪个MTA上。假设你正在使用163的邮箱，你就不能直接发到新浪的MTA上，因为它只服务新浪的用户，所以，你得填**163提供的SMTP服务器地址：`smtp.163.com`**，为了证明你是163的用户，SMTP服务器还要求你填写邮箱地址和邮箱口令，这样，MUA才能正常地把Email通过SMTP协议发送到MTA。

类似的，从MDA收邮件时，MDA服务器也要求验证你的邮箱口令，确保不会有人冒充你收取你的邮件，所以，Outlook之类的邮件客户端会要求你填写POP3或IMAP服务器地址、邮箱地址和口令，这样，MUA才能顺利地通过POP或IMAP协议从MDA取到邮件。

在使用Python收发邮件前，请先准备好至少两个电子邮件，如`xxx@163.com`，`xxx@sina.com`，`xxx@qq.com`等，注意两个邮箱不要用同一家邮件服务商。

最后*特别注意*，目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能，否则只允许在网页登录：

![qqmail-setting](https://liaoxuefeng.com/books/python/email/setting.png)

## 20.1 SMTP发送邮件

**SMTP是发送邮件的协议**，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

Python对SMTP支持有`smtplib`和`email`两个模块，**`email`负责构造邮件，`smtplib`负责发送邮件**。

### 发送文本

首先，我们来构造一个最简单的纯文本邮件：

```python
#用email负责构造邮件
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
```

注意到构造`MIMEText`对象时，**第一个参数就是邮件正文**，**第二个参数是MIME的subtype**，**传入`'plain'`表示纯文本**，最终的MIME就是`'text/plain'`，最后一定**要用`utf-8`编码保证多语言兼容性**。

然后，通过SMTP发出去：

```python
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

#用smtplib负责发送邮件
import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)#登陆SMTP服务器
#发邮件,一次可以发给多个人,所以传入list,as_string()把MTMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
```

我们用`set_debuglevel(1)`就可以**打印出和SMTP服务器交互的所有信息**。**SMTP协议就是简单的文本命令和响应**。`login()`方法用来**登录SMTP服务器**，`sendmail()`方法就是**发邮件**，由于**可以一次发给多个人**，**所以传入一个`list`**，邮件正文是一个`str`，`as_string()`把`MIMEText`对象变成`str`。

如果一切顺利，就可以在收件人信箱中收到我们刚发送的Email：

![send-mail](https://liaoxuefeng.com/books/python/email/smtp/email-1.png)

仔细观察，发现如下问题：

1. 邮件没有主题；
2. 收件人的名字没有显示为友好的名字，比如`Mr Green <green@example.com>`；
3. 明明收到了邮件，却提示不在收件人中。

这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，所以，我们必须把`From`、`To`和`Subject`添加到`MIMEText`中，才是一封完整的邮件：

```python
from email import encoders
from email.header import Header#处理邮件头（发件人、收件人、主题）的编码（解决中文乱码问题）
from email.mime.text import MIMEText#构造纯文本格式的邮件内容
from email.utils import parseaddr, formataddr#解析、格式化邮件地址（处理“名称 < 邮箱>”格式）

import smtplib#实现 SMTP 协议，连接邮件服务器并发送邮件
 
#`_format_addr()`函数用于格式化一个邮件地址	format——样式、版式   
def _format_addr(s):
    name, addr = parseaddr(s)#把“名称<邮箱>”拆分成name（名称）和addr（邮箱）
    return formataddr((Header(name, 'utf-8').encode(), addr))
	#名称用UTF-8编码（支持中文名称）,formataddr()用于重新组合成标准的邮件地址格式

#输入邮件信息
from_addr = input('From: ')
password = input('Password: ')#这里password不是邮箱密码,是授权码
to_addr = input('To: ')#收件人邮箱,多个收件人用逗号分隔
smtp_server = input('SMTP server: ')#发件人邮箱对应的服务商提供的服务器地址,形如smtp.qq.com

#构造邮件内容与邮件头
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')#创建纯文本邮件
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)#设置发件人显示（名称 + 邮箱）
msg['To'] = _format_addr('管理员 <%s>' % to_addr)#设置收件人显示
#设置邮件标题（同样用 Header 编码支持中文）
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    
#连接 SMTP 服务器并发送
server = smtplib.SMTP_SSL(smtp_server, 465)#这里要改成465端口,smtplib用于连接SMTP服务器
server.set_debuglevel(1)#开启调试模式，显示发送过程的日志
server.login(from_addr, password)#用发件人邮箱和密码/授权码登录服务器
server.sendmail(from_addr, [to_addr], msg.as_string())#发送邮件
server.quit()#关闭连接
```

我们编写了一个函数`_format_addr()`来格式化一个邮件地址。注意不能简单地传入`name <addr@example.com>`，因为如果包含中文，需要通过`Header`对象进行编码。

`msg['To']`接收的是字符串而不是list，如果有多个邮件地址，用`,`分隔即可。

再发送一遍邮件，就可以在收件人邮箱中看到正确的标题、发件人和收件人：

![mail-with-header](../../../Library/Application Support/typora-user-images/截屏2025-12-16 19.28.01.png)你看到的收件人的名字很可能不是我们传入的`管理员`，因为很多邮件服务商在显示邮件时，会把收件人名字自动替换为用户注册的名字，但是其他收件人名字的显示不受影响。

如果我们查看Email的原始内容，可以看到如下经过编码的邮件头：

```plain
From: =?utf-8?b?UHl0aG9u54ix5aW96ICF?= <xxxxxx@163.com>
To: =?utf-8?b?566h55CG5ZGY?= <xxxxxx@qq.com>
Subject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmeKApuKApg==?=
```

这就是经过`Header`对象编码的文本，包含utf-8编码信息和Base64编码的文本。如果我们自己来手动构造这样的编码文本，显然比较复杂。

### 发送HTML邮件

如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造`MIMEText`对象时，把HTML字符串传进去，再把**第二个参数由`plain`变为`html`就可以**了：

```python
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
```

再发送一遍邮件，你将看到以HTML显示的邮件：

![html-mail](https://liaoxuefeng.com/books/python/email/smtp/email-3.png)

### 发送附件

带附件的邮件可以看做包含若干部分的邮件：**文本和各个附件本身**，所以，可以构造一个`MIMEMultipart`对象代表邮件本身，然后往里面加上一个`MIMEText`作为邮件正文，再继续往里面加上表示附件的`MIMEBase`对象即可：

```python
# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/ipromise/Desktop/测试图片.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
```

给出完整代码:

```python
from email import encoders
from email.header import Header#处理邮件头（发件人、收件人、主题）的编码（解决中文乱码问题）
from email.mime.text import MIMEText#构造纯文本格式的邮件内容
from email.mime.multipart import MIMEMultipart  # 新增：导入多部分邮件类
from email.mime.base import MIMEBase            # 新增：导入附件基类
from email.utils import parseaddr, formataddr#解析、格式化邮件地址（处理“名称 < 邮箱>”格式）

import smtplib#实现 SMTP 协议，连接邮件服务器并发送邮件
 
#`_format_addr()`函数用于格式化一个邮件地址	format——样式、版式   
def _format_addr(s):
    name, addr = parseaddr(s)#把“名称<邮箱>”拆分成name（名称）和addr（邮箱）
    return formataddr((Header(name, 'utf-8').encode(), addr))
	#名称用UTF-8编码（支持中文名称）,formataddr()用于重新组合成标准的邮件地址格式

#输入邮件信息
from_addr = input('From: ')
password = input('Password: ')#这里password不是邮箱密码,是授权码
to_addr = input('To: ')#收件人邮箱,多个收件人用逗号分隔
smtp_server = input('SMTP server: ')#发件人邮箱对应的服务商提供的服务器地址,形如smtp.qq.com

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/ipromise/Desktop/测试图片.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

#连接 SMTP 服务器并发送
server = smtplib.SMTP_SSL(smtp_server, 465)#这里要改成465端口,smtplib用于连接SMTP服务器
server.set_debuglevel(1)#开启调试模式，显示发送过程的日志
server.login(from_addr, password)#用发件人邮箱和密码/授权码登录服务器
server.sendmail(from_addr, [to_addr], msg.as_string())#发送邮件
server.quit()#关闭连接
```

然后，按正常发送流程把`msg`（注意类型已变为`MIMEMultipart`）发送出去，就可以收到如下带附件的邮件：

![mimemultipart](../../../Library/Application Support/typora-user-images/截屏2025-12-16 19.48.28.png)

### 发送图片

大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。

要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用`src="cid:0"`就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的`cid:x`即可。

把上面代码加入`MIMEMultipart`的`MIMEText`从`plain`改为`html`，然后在适当的位置引用图片：

```python
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
```

**==完整代码==**:

```python
from email import encoders
from email.header import Header#处理邮件头（发件人、收件人、主题）的编码（解决中文乱码问题）
from email.mime.text import MIMEText#构造纯文本格式的邮件内容
from email.mime.multipart import MIMEMultipart  # 新增：导入多部分邮件类
from email.mime.base import MIMEBase            # 新增：导入附件基类
from email.utils import parseaddr, formataddr#解析、格式化邮件地址（处理“名称 < 邮箱>”格式）

import smtplib#实现 SMTP 协议，连接邮件服务器并发送邮件
 
#`_format_addr()`函数用于格式化一个邮件地址	format——样式、版式   
def _format_addr(s):
    name, addr = parseaddr(s)#把“名称<邮箱>”拆分成name（名称）和addr（邮箱）
    return formataddr((Header(name, 'utf-8').encode(), addr))
	#名称用UTF-8编码（支持中文名称）,formataddr()用于重新组合成标准的邮件地址格式

#输入邮件信息
from_addr = input('From: ')
password = input('Password: ')#这里password不是邮箱密码,是授权码
to_addr = input('To: ')#收件人邮箱,多个收件人用逗号分隔
smtp_server = input('SMTP server: ')#发件人邮箱对应的服务商提供的服务器地址,形如smtp.qq.com

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/ipromise/Desktop/测试图片.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIME15867Base('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

#连接 SMTP 服务器并发送
server = smtplib.SMTP_SSL(smtp_server, 465)#这里要改成465端口,smtplib用于连接SMTP服务器
server.set_debuglevel(1)#开启调试模式，显示发送过程的日志
server.login(from_addr, password)#用发件人邮箱和密码/授权码登录服务器
server.sendmail(from_addr, [to_addr], msg.as_string())#发送邮件
server.quit()#关闭连接
```

再次发送，就可以看到图片直接嵌入到邮件正文的效果(**图片自己去看163邮箱**)

### 同时支持HTML和Plain格式

如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？

办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。

利用`MIMEMultipart`就可以组合一个HTML和Plain，要注意指定`subtype`是`alternative`：

```python
msg = MIMEMultipart('alternative')
msg['From'] = ...
msg['To'] = ...
msg['Subject'] = ...

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象...
```

### 加密SMTP

**使用标准的25端口连接SMTP服务器时，使用的是明文传输**，**发送邮件的整个过程可能会被窃听**。要更安全地发送邮件，可以**加密SMTP会话，就是先创建SSL安全连接，然后再使用SMTP协议发送邮件**。

某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。

必须知道，**Gmail的SMTP端口是587**，因此，修改代码如下：

```python
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
...
```

只需要在创建`SMTP`对象后，立刻调用`starttls()`方法，就创建了安全连接。后面的代码和前面的发送邮件代码完全一样。

如果因为网络问题无法连接Gmail的SMTP服务器，请相信我们的代码是没有问题的，你需要对你的网络设置做必要的调整。(==**需要科学上网啦**==)

- 小结

使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。

构造一个邮件对象就是一个`Messag`对象，如果构造一个`MIMEText`对象，就表示一个文本邮件对象，如果构造一个`MIMEImage`对象，就表示一个作为附件的图片，要把多个对象组合起来，就用`MIMEMultipart`对象，而`MIMEBase`可以表示任何对象。它们的继承关系如下：

```plain
Message#邮件
+- MIMEBase#任意对象
   +- MIMEMultipart#多对象组合
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText#纯文本
      +- MIMEImage#纯图片
```

这种嵌套关系就可以构造出任意复杂的邮件。你可以通过[email.mime文档](https://docs.python.org/3/library/email.mime.html)查看它们所在的包以及详细的用法。

## 20.2 POP3收取邮件

SMTP用于发送邮件，如果要收取邮件呢？

收取邮件就是编写一个**MUA**作为客户端，从**MDA**把邮件获取到用户的电脑或者手机上。收取邮件最常用的协议是**POP**协议，目前版本号是3，俗称**POP3**。

Python内置一个`poplib`模块，实现了POP3协议，可以直接用来收邮件。

注意到**POP3协议收取的不是一个可以阅读的邮件本身**，**而是邮件的原始文本**，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。

要把POP3收取的文本变成可以阅读的邮件，还需要用`email`模块提供的各种类来解析原始文本，变成可阅读的邮件对象。

所以，收取邮件分两步：

1. 用`poplib`把**邮件的原始文本下载到本地**；
2. 用`email`**解析原始文本，还原为邮件对象**。

### 通过POP3下载邮件

POP3协议本身很简单，以下面的代码为例，我们来获取最新的一封邮件内容：

```python
import poplib

# 输入邮件地址, 口令和POP3服务器地址:
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()
```

用POP3获取邮件其实很简单，要获取所有邮件，只需要循环使用`retr()`把每一封邮件内容拿到即可。真正麻烦的是把邮件的原始内容解析为可以阅读的邮件对象。

### 解析邮件

解析邮件的过程和上一节构造邮件正好相反，因此，先导入必要的模块：

```python
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib
```

只需要一行代码就可以把邮件内容解析为`Message`对象：

```python
msg = Parser().parsestr(msg_content)
```

但是这个`Message`对象本身可能是一个`MIMEMultipart`对象，即包含嵌套的其他`MIMEBase`对象，嵌套可能还不止一层。

所以我们要递归地打印出`Message`对象的层次结构：

```python
# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))
```

邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：

```python
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
```

`decode_header()`返回一个list，因为像`Cc`、`Bcc`这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。

文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：

```python
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
```

把上面的代码整理好，我们就可以来试试收取一封邮件。先往自己的邮箱发一封邮件，然后用浏览器登录邮箱，看看邮件收到没，如果收到了，我们就来用Python程序把它收到本地：

![pop3-sample-mail](https://liaoxuefeng.com/books/python/email/pop3/exist.png)

运行程序，结果如下：

```plain
+OK Welcome to coremail Mail Pop3 Server (163coms[...])
Messages: 126. Size: 27228317

From: Test <xxxxxx@qq.com>
To: Python爱好者 <xxxxxx@163.com>
Subject: 用POP3收取邮件
part 0
--------------------
  part 0
  --------------------
    Text: Python可以使用POP3收取邮件……...
  part 1
  --------------------
    Text: Python可以<a href="...">使用POP3</a>收取邮件……...
part 1
--------------------
  Attachment: application/octet-stream
```

我们从打印的结构可以看出，这封邮件是一个`MIMEMultipart`，它包含两部分：第一部分又是一个`MIMEMultipart`，第二部分是一个附件。而内嵌的`MIMEMultipart`是一个`alternative`类型，它包含一个纯文本格式的`MIMEText`和一个HTML格式的`MIMEText`。

- 小结

用Python的`poplib`模块收取邮件分两步：第一步是用POP3协议把邮件获取到本地，第二步是用`email`模块把原始邮件解析为`Message`对象，然后，用适当的形式把邮件内容展示给用户即可。

---

# 第二十一章 访问数据库

程序运行的时候，数据都是在内存中的。当程序终止的时候，通常都需要将数据保存到磁盘上，无论是保存到本地磁盘，还是通过网络保存到服务器上，最终都会将数据写入磁盘文件。

而如何定义数据的存储格式就是一个大问题。如果我们自己来定义存储格式，比如保存一个班级所有学生的成绩单：

| 名字    | 成绩 |
| ------- | ---- |
| Michael | 99   |
| Bob     | 85   |
| Bart    | 59   |
| Lisa    | 87   |

我们可以用一个文本文件保存，一行保存一个学生，用`,`隔开：

```csv
Michael,99
Bob,85
Bart,59
Lisa,87
```

还可以用JSON格式保存，也是文本文件：

```json
[
    {"name":"Michael","score":99},
    {"name":"Bob","score":85},
    {"name":"Bart","score":59},
    {"name":"Lisa","score":87}
]
```

还可以定义各种保存格式，但是问题来了：

存储和读取需要自己实现，JSON还是标准，自己定义的格式就各式各样了；

不能做快速查询，只有把数据全部读到内存中才能自己遍历，但有时候数据的大小远远超过了内存，根本无法全部读入内存。

为了便于**程序保存和读取数据**，而且，能直接通过条件快速查询到指定的数据，就出现了数据库（Database）这种<u>专门用于集中存储和查询</u>的软件。

数据库软件诞生的历史非常久远，早在1950年数据库就诞生了。经历了网状数据库，层次数据库，我们现在广泛使用的关系数据库是20世纪70年代基于关系模型的基础上诞生的。

**==关系模型==**有一套复杂的数学理论，但是从概念上是十分容易理解的。举个学校的例子：

假设某个XX省YY市ZZ县第一实验小学有3个年级，要表示出这3个年级，可以在Excel中用一个表格画出来：

![grade](https://liaoxuefeng.com/books/python/database/table_grade.jpg)

每个年级又有若干个班级，要把所有班级表示出来，可以在Excel中再画一个表格：

![class](https://liaoxuefeng.com/books/python/database/table_class.jpg)

这两个表格有个**映射关系**，就是根据Grade_ID可以在班级表中查找到对应的所有班级：

![grade-classes](https://liaoxuefeng.com/books/python/database/table_relationship.jpg)

也就是Grade表的每一行对应Class表的多行，==在关系数据库中，这种基于表（Table）的**一对多**的关系就是关系数据库的基础。==

根据某个年级的ID就可以查找所有班级的行，这种**查询语句在关系数据库中称为SQL语句**，可以写成：

```sql
SELECT * FROM classes WHERE grade_id = '1';
```

结果也是一个表：

| grade_id | class_id | name       |
| -------- | -------- | ---------- |
| 1        | 11       | 一年级一班 |
| 1        | 12       | 一年级二班 |
| 1        | 13       | 一年级三班 |

类似的，Class表的一行记录又可以关联到Student表的多行记录：

![class-students](https://liaoxuefeng.com/books/python/database/table_relationship2.jpg)

想从零学习关系数据库和基本的SQL语句，请参考[SQL教程](SQL教程.md)。

### 数据库类别

既然我们要使用关系数据库，就必须选择一个关系数据库。目前广泛使用的关系数据库也就这么几种：

付费的商用数据库：

- Oracle，典型的高富帅；
- SQL Server，微软自家产品，Windows定制专款；
- DB2，IBM的产品，听起来挺高端；
- Sybase，曾经跟微软是好基友，后来关系破裂，现在家境惨淡。

这些数据库都是不开源而且付费的，最大的好处是花了钱出了问题可以找厂家解决，不过在Web的世界里，常常需要部署成千上万的数据库服务器，当然不能把大把大把的银子扔给厂家，所以，无论是Google、Facebook，还是国内的BAT，无一例外都选择了免费的开源数据库：

- MySQL，大家都在用，一般错不了；
- PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；
- SQLite，嵌入式数据库，适合桌面和移动应用。

作为一个Python工程师，选择哪个免费数据库呢？这里我们会介绍SQLite和MySQL，SQLite适合作为嵌入式数据库，优点是不用安装任何软件，直接能用。生产环境下，应当选择MySQL或者PostgreSQL。

## 21.1 使用SQLite

SQLite是一种**嵌入式数据库**，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。

Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。

在使用SQLite前，我们先要搞清楚几个概念：

**表是数据库中存放关系数据的集合**，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。**表和表之间通过外键关联**。

要**操作关系数据库**，首先需要**连接到数据库**，一个数据库连接称为`Connection`；

连接到数据库后，需要**打开游标**，称之为`Cursor`，**通过`Cursor`执行SQL语句**，然后，获得执行结果。

Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。

由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。

我们在Python交互式命令行实践一下：

```text
# 导入SQLite驱动:
>>> import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
>>> conn = sqlite3.connect('test.db')
# 创建一个Cursor:
>>> cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
<sqlite3.Cursor object at 0x10f8aa260>
# 继续执行一条SQL语句，插入一条记录:
>>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
<sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数:
>>> cursor.rowcount
1
# 提交事务:
>>> conn.commit()
# 关闭Cursor:
>>> cursor.close()
# 关闭Connection:
>>> conn.close()
```

我们再试试查询记录：

```text
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
# 执行查询语句:
>>> cursor.execute('select * from user where id=?', ('1',))
<sqlite3.Cursor object at 0x10f8aa340>
# 获得查询结果集:
>>> values = cursor.fetchall()
>>> values
[('1', 'Michael')]
>>> cursor.close()
>>> conn.close()
```

使用Python的DB-API时，只要搞清楚`Connection`和`Cursor`对象，**打开后一定记得关闭，就可以放心地使用**。

**使用`Cursor`对象执行`insert`，`update`，`delete`语句时，执行结果由`rowcount`返回影响的行数，就可以拿到执行结果**。

**使用`Cursor`对象执行`select`语句时，通过`fetchall()`可以拿到结果集。结果集是一个`list`，每个元素都是一个`tuple`，对应一行记录**。

如果SQL语句带有参数，那么需要**把参数按照位置传递**给`execute()`方法，**有几个`?`占位符就必须对应几个参数**，例如：

```text
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
```

SQLite支持常见的标准SQL语句以及几种常见的数据类型。具体文档请参阅SQLite官方网站。

- 小结

在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过`Connection`对象和`Cursor`对象操作数据。

要确保打开的`Connection`对象和`Cursor`对象都正确地被关闭，否则，资源就会泄露。

如何才能确保出错的情况下也关闭掉`Connection`对象和`Cursor`对象呢？请回忆`try:...except:...finally:...`的用法。

## 21.2 使用MySQL

**MySQL是Web世界中使用最广泛的数据库服务器**。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。而**MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite**。

此外，**MySQL内部有多种数据库引擎**，最常用的引擎是支持数据库事务的InnoDB。

### 安装MySQL

可以直接从MySQL官方网站下载最新的[Community Server 8.x](https://dev.mysql.com/downloads/mysql/)版本。MySQL是跨平台的，选择对应的平台下载安装文件，安装即可。

安装时，MySQL会提示输入`root`用户的口令，请务必记清楚。如果怕记不住，就把口令设置为`password`。

在Windows上，安装时请选择`UTF-8`编码，以便正确地处理中文。

在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在`/etc/my.cnf`或者`/etc/mysql/my.cnf`：

```text
[client]
default-character-set = utf8mb4

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8mb4
collation-server = utf8_general_ci
```

重启MySQL后，可以通过MySQL的客户端命令行检查编码：

```text
$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor...
...

mysql> show variables like '%char%';
+--------------------------+--------------------------------------+
| Variable_name            | Value                                |
+--------------------------+--------------------------------------+
| character_set_client     | utf8mb4                              |
| character_set_connection | utf8mb4                              |
| character_set_database   | utf8mb4                              |
| character_set_filesystem | binary                               |
| character_set_results    | utf8mb4                              |
| character_set_server     | utf8mb4                              |
| character_set_system     | utf8mb3                              |
| character_sets_dir       | /usr/local/mysql-8.x/share/charsets/ |
+--------------------------+--------------------------------------+
8 rows in set (0.00 sec)
```

看到`utf8mb4`字样就表示编码设置正确。

 注意

如果MySQL的版本<5.5.3，则只能把编码设置为`utf8`，`utf8mb4`支持最新的Unicode标准，可以显示emoji字符，但`utf8`无法显示emoji字符。

### 用Docker启动MySQL

如果不想安装MySQL，还可以以Docker的方式快速启动MySQL。

首先安装[Docker Desktop](https://www.docker.com/products/docker-desktop/)，然后在命令行输入：

```plain
$ docker run -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 --name mysql-latest -v ./mysql-data:/var/lib/mysql mysql:latest --mysql-native-password=ON --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

上述命令详细参数如下：

- `$`:终端提示 “可以输入命令” 的标识，不是命令的一部分

- `-e MYSQL_ROOT_PASSWORD=password`：Docker启动MySQL容器的核心环境变量,给MySQL的最高权限用户root设置登录密码,可以自定义；
- `-p 3306:3306`：在本机`3306`端口监听；
- `--name mysql-latest`：启动后容器的名称为`mysql-latest`，可任意设置；
- `-v ./mysql-data:/var/lib/mysql`：把当前目录`./mysql-data`映射到容器目录`/var/lib/mysql`，此目录存放MySQL数据库文件，避免容器停止后数据丢失；
- `mysql:latest`：启动镜像名称为`mysql:latest`；
- `--mysql-native-password=ON`：表示启用明文口令；
- `--character-set-server=utf8mb4`：表示启用`utf8mb4`作为字符集；
- `--collation-server=utf8mb4_unicode_ci`：表示启用`utf8mb4`作为排序规则。

运行命令后可看到如下输出：

```plain
2024-07-11 02:44:05+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.4.1-1.el9 started.
...
2024-07-11T02:44:16.874162Z 0 [System] [MY-015015] [Server] MySQL Server - start.
...
2024-07-11T02:44:17.120017Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2024-07-11T02:44:17.561242Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
...
2024-07-11T02:44:17.868691Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.4.1'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
```

看到最后一行`ready for connections`表示启动成功。

### 安装MySQL驱动

由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动：

```text
$ pip install mysql-connector-python 
```

我们演示如何连接到MySQL服务器的test数据库：

```text
# 导入MySQL驱动:
>>> import mysql.connector
# 注意把password设为你的root口令:
>>> conn = mysql.connector.connect(user='root', password='password', database='test')
>>> cursor = conn.cursor()
# 创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
>>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
>>> cursor.rowcount
1
# 提交事务:
>>> conn.commit()
>>> cursor.close()
# 运行查询:
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id = %s', ('1',))
>>> values = cursor.fetchall()
>>> values
[('1', 'Michael')]
# 关闭Cursor和Connection:
>>> cursor.close()
True
>>> conn.close()
```

由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。

- 小结

- 执行INSERT等操作后要调用`commit()`提交事务；
- MySQL的SQL占位符是`%s`。

## 21.3 使用SQLAlchemy

数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，可以用一个`list`表示多行，`list`的每一个元素是`tuple`，表示一行记录，比如，包含`id`和`name`的`user`表：

```python
[
    ('1', 'Michael'),
    ('2', 'Bob'),
    ('3', 'Adam')
]
```

Python的DB-API返回的数据结构就是像上面这样表示的。

但是用`tuple`表示一行很难看出表的结构。如果把一个`tuple`用`class`实例来表示，就可以更容易地看出表的结构来：

```python
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]
```

这就是传说中的**ORM**：Object-Relational Mapping，**把关系数据库的表结构映射到对象上**。

但是由谁来做这个转换呢？所以**ORM框架**应运而生。

在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法。

首先通过pip安装SQLAlchemy：

```plain
$ pip install sqlalchemy
```

然后，利用上次我们在MySQL的test数据库中创建的`user`表，用SQLAlchemy来试试：

第一步，导入SQLAlchemy，并初始化DBSession：

```python
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:LBJ2306sqd%40@localhost:3306/test')#这里%40表示符号@,URL中@是分隔符,密码中有@需要用%40表示,否则报错
# 先创建表（如果表不存在，需手动创建，否则插入会报错）
Base.metadata.create_all(engine)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
```

 URL 中 `@` 是**分隔符**（格式：`用户名:密码@主机:端口/数据库`），密码里的 `@` 会被当成分隔符，导致：

- 解析后：用户名 = root，密码 = LB23sqd，主机 =@[localhost](https://localhost/)（错误）
- 正确期望：用户名 = root，密码 = LB23sqd@，主机 =[localhost](https://localhost/)

以上代码完成SQLAlchemy的初始化和具体每个表的`class`定义。如果有多个表，就继续定义其他`class`，例如School：

```python
class School(Base):
    __tablename__ = 'school'
    id = ...
    name = ...
```

`create_engine()`用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：

```plain
'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
```

**你只需要根据需要替换掉用户名、口令等信息即可。**

下面，我们看看如何向数据库表中添加一行记录。

由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个`User`对象：

```python
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
```

可见，关键是获取session，然后把对象添加到session，最后提交并关闭。`DBSession`对象可视为当前数据库连接。

如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是`tuple`，而是`User`对象。SQLAlchemy提供的查询接口如下：

```python
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
```

运行结果如下：

```plain
type: <class '__main__.User'>
name: Bob
```

可见，**ORM就是把数据库表的行与相应的对象建立关联，互相转换**。

由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。

例如，如果一个User拥有多个Book，就可以定义一对多关系如下：

```python
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
```

当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。

- 小结

ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。

正确使用ORM的前提是了解关系数据库的原理。

---

# 第二十二章 Web开发

最早的软件都是运行在大型机上的，软件使用者通过“哑终端”登陆到大型机上去运行软件。后来随着PC机的兴起，软件开始主要运行在桌面上，而数据库这样的软件运行在服务器端，这种Client/Server模式简称==**CS架构。	客户端/服务器**==

随着互联网的兴起，人们发现，CS架构不适合Web，最大的原因是Web应用程序的修改和升级非常迅速，而CS架构需要每个客户端逐个升级桌面App，因此，Browser/Server模式开始流行，简称==**BS架构。	浏览器/服务器**==

在BS架构下，**客户端只需要浏览器，应用程序的==逻辑==和==数据==都存储在服务器端**。**浏览器只需要==请求服务器==，获取Web页面，并把Web页面展示给用户即可**。

当然，**Web页面也具有极强的交互性**。由于Web页面是用HTML编写的，而HTML具备超强的表现力，并且，服务器端升级后，客户端无需任何部署就可以使用到新的版本，因此，BS架构迅速流行起来。

今天，除了重量级的软件如Office，Photoshop等，大部分软件都以Web形式提供。比如，新浪提供的新闻、博客、微博等服务，均是Web应用。

Web应用开发可以说是目前软件开发中最重要的部分。Web开发也经历了好几个阶段：

1. 静态Web页面：由文本编辑器直接编辑并生成静态的HTML页面，如果要修改Web页面的内容，就需要再次编辑HTML源文件，早期的互联网Web页面就是静态的；
2. CGI：由于静态Web页面无法与用户交互，比如用户填写了一个注册表单，静态Web页面就无法处理。要处理用户发送的动态数据，出现了Common Gateway Interface，简称CGI，用C/C++编写。
3. ASP/JSP/PHP：由于Web应用特点是修改频繁，用C/C++这样的低级语言非常不适合Web开发，而脚本语言由于开发效率高，与HTML结合紧密，因此，迅速取代了CGI模式。ASP是微软推出的用VBScript脚本编程的Web开发技术，而JSP用Java来编写脚本，PHP本身则是开源的脚本语言。
4. MVC：为了解决直接用脚本语言嵌入HTML导致的可维护性差的问题，Web应用也引入了Model-View-Controller的模式，来简化Web开发。ASP发展为ASP.Net，JSP和PHP也有一大堆MVC框架。

目前，Web开发技术仍在快速发展中，异步开发、新的MVVM前端技术层出不穷。

Python的诞生历史比Web还要早，由于Python是一种解释型的脚本语言，开发效率高，所以非常适合用来做Web开发。

Python有上百种Web开发框架，有很多成熟的模板技术，选择Python开发Web应用，不但开发效率高，而且运行速度快。

本章我们会详细讨论Python Web开发技术。

## 22.1 HTTP协议

在Web应用中，**服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示出来**。而**浏览器和服务器之间的传输协议是HTTP**，所以：

- HTML是一种用来定义网页的文本，会HTML，就可以编写网页；
- HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。

在举例子之前，我们需要安装Google的[Chrome浏览器](https://www.google.com/intl/zh-CN/chrome/)。

为什么要使用Chrome浏览器而不是IE呢？因为我们需要在浏览器很方便地调试我们的Web应用，而Chrome提供了一套完整地调试工具，非常适合Web开发。

安装好Chrome浏览器后，打开Chrome，在菜单中选择“视图”，“开发者”，“开发者工具”，就可以显示开发者工具(右上角三个点---“更多工具”---“开发者工具)：

![chrome-dev-tools](https://liaoxuefeng.com/books/python/web/http-basic/dev-tools.jpg)

**==`Elements`显示网页的结构，`Network`显示浏览器和服务器的通信。我们点`Network`，确保第一个小红灯亮着，Chrome就会记录所有浏览器和服务器之间的通信：==**

![chrome-devtools-network](https://liaoxuefeng.com/books/python/web/http-basic/record.jpg)

当我们在地址栏输入`www.sina.com.cn`时，浏览器将显示新浪的首页。在这个过程中，通过`Network`的记录，我们就可以知道浏览器干了什么事情。在`Network`中，定位到第一条记录，点击，右侧将显示`Request Headers`，点击右侧的`view source`，我们就可以看到浏览器发给新浪服务器的请求：

![sina-http-request](https://liaoxuefeng.com/books/python/web/http-basic/http-request.jpg)

最主要的头两行分析如下，第一行：

```plain
GET / HTTP/1.1
```

`GET`表示一个读取请求，将从服务器获得网页数据，`/`表示URL的路径，URL总是以`/`开头，`/`就表示首页，最后的`HTTP/1.1`指示采用的HTTP协议版本是1.1。目前HTTP协议的版本就是1.1，但是大部分服务器也支持1.0版本，主要区别在于1.1版本允许多个HTTP请求复用一个TCP连接，以加快传输速度。

从第二行开始，每一行都类似于`Xxx: abcdefg`：

```plain
Host: www.sina.com.cn
```

表示请求的域名是`www.sina.com.cn`。如果一台服务器有多个网站，服务器就需要通过`Host`来区分浏览器请求的是哪个网站。

继续往下找到`Response Headers`，点击`view source`，显示服务器返回的原始响应数据：

![sina-http-response](https://liaoxuefeng.com/books/python/web/http-basic/http-response.jpg)

HTTP响应分为Header和Body两部分（Body是可选项），我们在`Network`中看到的Header最重要的几行如下：

```plain
200 OK
```

`200`表示一个成功的响应，后面的`OK`是说明。失败的响应有`404 Not Found`：网页不存在，`500 Internal Server Error`：服务器内部出错，等等。

```plain
Content-Type: text/html
```

`Content-Type`指示响应的内容，这里是`text/html`表示HTML网页。请注意，浏览器就是依靠`Content-Type`来判断响应的内容是网页还是图片，是视频还是音乐。浏览器并不靠URL来判断响应的内容，所以，即使URL是`http://example.com/abc.jpg`，它也不一定就是图片。

HTTP响应的Body就是HTML源码，我们在菜单栏选择“视图”，“开发者”，“查看网页源码”就可以在浏览器中直接查看HTML源码：

![sina-http-source](https://liaoxuefeng.com/books/python/web/http-basic/source.jpg)

当浏览器读取到新浪首页的HTML源码后，它会解析HTML，显示页面，然后，根据HTML里面的各种链接，再发送HTTP请求给新浪服务器，拿到相应的图片、视频、Flash、JavaScript脚本、CSS等各种资源，最终显示出一个完整的页面。所以我们在`Network`下面能看到很多额外的HTTP请求。

### HTTP请求的流程

跟踪了新浪的首页，我们来总结一下**HTTP请求的流程**：

**步骤1：浏览器首先向服务器发送HTTP请求**，请求包括：

方法：`GET`还是`POST`，**`GET`仅请求资源，`POST`会附带用户数据**；

路径：`/full/url/path`；

域名：由Host头指定：`Host: www.sina.com.cn`

以及其他相关的Header；

如果是POST，那么请求还包括一个Body，包含用户数据。

**步骤2：服务器向浏览器返回HTTP响应**，响应包括：

响应代码：**`200`表示成功，`3xx`表示重定向，`4xx`表示客户端发送的请求有错误，`5xx`表示服务器端处理时发生了错误**；

**响应类型：由`Content-Type`指定**，例如：`Content-Type: text/html;charset=utf-8`表示响应类型是HTML文本，并且编码是`UTF-8`，`Content-Type: image/jpeg`表示响应类型是JPEG格式的图片；

以及其他相关的Header；

通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。

**步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2**。

**Web采用的HTTP协议采用了非常简单的请求-响应模式**，从而大大简化了开发。当我们编写一个页面时，我们只需要在HTTP响应中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，因此，**一个HTTP请求只处理一个资源**。

**HTTP协议同时具备极强的扩展性**，虽然浏览器请求的是`http://www.sina.com.cn/`的首页，但是新浪在HTML中可以链入其他服务器的资源，比如`<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png">`，从而将请求压力分散到各个服务器上，并且，**一个站点可以链接到其他站点，无数个站点互相链接起来，就形成了World Wide Web**，简称“三达不溜”（WWW）。

### HTTP格式

**每个HTTP请求和响应都遵循相同的格式**，**一个HTTP包含==Header和Body==两部分**，其中Body是可选的。

HTTP协议是一种文本协议，所以，它的格式也非常简单。HTTP GET请求的格式：

```plain
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3
```

每个Header一行一个，换行符是`\r\n`。

HTTP POST请求的格式：

```plain
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
```

当遇到连续两个`\r\n`时，Header部分结束，后面的数据全部是Body。

HTTP响应的格式：

```plain
200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
```

HTTP响应如果包含body，也是通过`\r\n\r\n`来分隔的。请再次注意，Body的数据类型由`Content-Type`头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。

当存在`Content-Encoding`时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到`Content-Encoding: gzip`时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。

要详细了解HTTP协议，推荐“[HTTP: The Definitive Guide](https://book.douban.com/subject/1440226/)”一书，非常不错，有中文译本《[HTTP权威指南](https://book.douban.com/subject/10746113/)》。

## 22.2 HTML简介

网页就是HTML？这么理解大概没错。因为网页中不但包含文字，还有图片、视频、HTML5小游戏，有复杂的排版、动画效果，所以，**==HTML定义了一套语法规则，来告诉浏览器如何把一个丰富多彩的页面显示出来==**。

HTML长什么样？上次我们看了新浪首页的HTML源码，如果仔细数数，竟然有6000多行！

所以，学HTML，就不要指望从新浪入手了。我们来看看最简单的HTML长什么样：

```html
<html>
<head>
  <title>Hello</title>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>
```

可以用文本编辑器编写HTML，然后保存为`hello.html`，双击或者把文件拖到浏览器中，就可以看到效果：

![hello.html](https://liaoxuefeng.com/books/python/web/html-basic/html.jpg)

**HTML文档就是一系列的Tag组成**，最外层的Tag是`<html>`。规范的HTML也包含`<head>...</head>`和`<body>...</body>`（注意不要和HTTP的Header、Body搞混了），由于HTML是富文档模型，所以，还有一系列的Tag用来表示链接、图片、表格、表单等等。

### CSS简介

CSS是Cascading Style Sheets（层叠样式表）的简称，CSS用来控制HTML里的所有元素如何展现，比如，给标题元素`<h1>`加一个样式，变成48号字体，灰色，带阴影：

```html
<html>
<head>
  <title>Hello</title>
  <style>
    h1 {
      color: #333333;
      font-size: 48px;
      text-shadow: 3px 3px 3px #666666;
    }
  </style>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>
```

效果如下：

![hello-css](https://liaoxuefeng.com/books/python/web/html-basic/css.jpg)

### JavaScript简介

**JavaScript虽然名称有个Java，但它和Java真的一点关系没有**。**JavaScript是为了让HTML具有==交互性==而作为脚本语言添加的**，JavaScript既可以**内嵌**到HTML中，也可以从**外部链接**到HTML中。如果我们希望当用户点击标题时把标题变成红色，就必须通过JavaScript来实现：

```html
<html>
<head>
  <title>Hello</title>
  <style>
    h1 {
      color: #333333;
      font-size: 48px;
      text-shadow: 3px 3px 3px #666666;
    }
  </style>
  <script>
    function change() {
      document.getElementsByTagName('h1')[0].style.color = '#ff0000';
    }
  </script>
</head>
<body>
  <h1 onclick="change()">Hello, world!</h1>
</body>
</html>
```

点击标题后效果如下：

![hello-js-change-color](https://liaoxuefeng.com/books/python/web/html-basic/js.jpg)

- 小结

如果要学习Web开发，首先要对HTML、CSS和JavaScript作一定的了解。HTML定义了页面的内容，CSS来控制页面元素的样式，而JavaScript负责页面的交互逻辑。

讲解HTML、CSS和JavaScript就可以写3本书，对于优秀的Web开发人员来说，精通HTML、CSS和JavaScript是必须的，这里推荐一个在线学习网站[w3schools](https://www.w3schools.com/)，以及一个对应的[中文版本](https://www.w3school.com.cn/)。

当我们用Python或者其他语言开发Web应用时，我们就是要在服务器端动态创建出HTML，这样，浏览器就会向不同的用户显示出不同的Web页面。

## 22.3 WSGI接口

了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：

1. 浏览器发送一个HTTP请求；
2. 服务器收到请求，生成一个HTML文档；
3. 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
4. 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

所以，**最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回**。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。

正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。

这个接口就是WSGI：Web Server Gateway Interface。

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：

```python
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
```

上面的`application()`函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

- `environ`：一个包含所有HTTP请求信息的`dict`对象；
- `start_response`：一个发送HTTP响应的函数。

在`application()`函数中，调用：

```python
start_response('200 OK', [('Content-Type', 'text/html')])
```

就发送了HTTP响应的Header，注意**Header只能发送一次，也就是只能调用一次`start_response()`函数**。`start_response()`函数**接收两个参数，一个是HTTP响应码，一个是一组`list`表示的HTTP Header**，**每个Header用一个包含两个`str`的`tuple`表示。**

通常情况下，都应该把`Content-Type`头发送给浏览器。其他很多常用的HTTP Header也应该发送。

然后，**函数的返回值`b'<h1>Hello, web!</h1>'`将作为HTTP响应的Body发送给浏览器**。

有了WSGI，我们关心的就是如何从`environ`这个`dict`对象拿到HTTP请求信息，然后构造HTML，通过`start_response()`发送Header，最后返回Body。

整个`application()`函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了。

不过，这个`application()`函数怎么调用？如果我们自己调用，两个参数`environ`和`start_response`我们没法提供，返回的`bytes`也没法发给浏览器。

所以`application()`函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。但是现在，我们只想尽快测试一下我们编写的`application()`函数真的可以把HTML输出到浏览器，所以，要赶紧找一个最简单的WSGI服务器，把我们的Web应用程序跑起来。

好消息是Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

### 运行WSGI服务

我们先编写`hello.py`，实现Web应用程序的WSGI处理函数：

```python
# hello.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
```

然后，再编写一个`server.py`，负责启动WSGI服务器，加载`application()`函数：

```python
# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
```

确保以上两个文件在同一个目录下，然后在命令行输入`python server.py`来启动WSGI服务器：

![wsgiref-start](https://liaoxuefeng.com/books/python/web/wsgi/server.jpg)

注意：如果`8000`端口已被其他程序占用，启动将失败，请修改成其他端口。

启动成功后，打开浏览器，输入`http://localhost:8000/`，就可以看到结果了：

![hello-web](https://liaoxuefeng.com/books/python/web/wsgi/result.jpg)

在命令行可以看到wsgiref打印的log信息：

![wsgiref-log](https://liaoxuefeng.com/books/python/web/wsgi/log.jpg)

按`Ctrl+C`终止服务器。

如果你觉得这个Web应用太简单了，可以稍微改造一下，从`environ`里读取`PATH_INFO`，这样可以显示更加动态的内容：

```python
# hello.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
```

你可以在地址栏输入用户名作为URL的一部分，将返回`Hello, xxx!`：

![hello-michael](https://liaoxuefeng.com/books/python/web/wsgi/hello.jpg)

- 小结

无论多么复杂的**Web应用程序，入口都是一个WSGI处理函数**。HTTP请求的所有输入信息都可以通过`environ`获得，HTTP响应的输出都可以通过`start_response()`加上函数返回值作为Body。

复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。

## 22.4 使用Web框架

了解了WSGI框架，我们发现：其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。

但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL。

每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。

一个最简单的想法是从`environ`变量里取出HTTP请求的信息，然后逐个判断：

```python
def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method=='GET' and path=='/':
        return handle_home(environ, start_response)
    if method=='POST' and path='/signin':
        return handle_signin(environ, start_response)
    ...
```

只是这么写下去代码是肯定没法维护了。

代码这么写没法维护的原因是因为WSGI提供的接口虽然比HTTP接口高级了不少，但和Web App的处理逻辑比，还是比较低级，我们需要在WSGI接口之上能进一步抽象，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做。

**==介绍一下URL:==**统一资源定位符（Uniform Resource Locator）,是web网页的地址.URL由**资源类型、存放资源的主机域名、资源文件名构成**

```plain
protocol :// hostname[:port] / path / [;parameters][?query]#fragment
```

URL的一般语法格式如上所示.其中:

- protocol:协议,指定使用的传输协议,常用HTTP协议

```plain
http 通过 HTTP 访问该资源。 格式 HTTP://
https 通过安全的 HTTPS 访问该资源。 格式 HTTPS://
ftp 通过 FTP访问资源。格式 FTP://
```

- hostname:主机名,是指存放资源的服务器的域名系统DNS主机名或IP地址
- port:端口号HTTP工作在TCP协议80端口,HTTPS工作在TCP协议443端口
- path:路径,由若干个‘/’符号隔开的字符串,一般用来表示主机上的一个目录或文件地址
- parameters:参数,用于指定特殊参数的**可选项**
- query:查询,**可选**,用于给动态网页传递参数,可有多个参数,用符号“&”隔开,每个参数的值和名用“=”连接
- fragment:信息片段,字符串,用于指定网络资源中的片段

由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，直接选择一个比较流行的Web框架——[Flask](https://flask.palletsprojects.com/)来使用。

用Flask编写Web App比WSGI接口简单，我们先用`pip`安装Flask：

```plain
$ pip install flask
```

然后写一个`app.py`，处理3个URL，分别是：

- `GET /`：首页，返回`Home`；
- `GET /signin`：登录页，显示登录表单；
- `POST /signin`：处理登录表单，显示登录结果。

注意噢，同一个URL`/signin`分别有GET和POST两种请求，映射到两个处理函数中。

Flask通过Python的[装饰器](https://liaoxuefeng.com/books/python/functional/decorator/index.html)在内部自动地把URL和函数给关联起来，所以，我们写出来的代码就像这样：

```python
from flask import Flask  #Flask框架的核心类,用于创建Web应用实例
from flask import request#requestFlask封装的请求对象,用来获取客户端发送的请求数据(比如表单、URL参数)

app = Flask(__name__)#创建应用实例,初始化Flask应用

#用装饰器绑定URL路径和视图函数
@app.route('/', methods=['GET', 'POST'])#允许该路径接收GE（默认）和POST两种请求方法
def home():#视图函数，处理访问/的请求，返回一段HTML代码
    return '<h1>Home</h1>'

#登录表单页
@app.route('/signin', methods=['GET'])#绑定/signin路径，仅允许GET请求（浏览器直接输入URL访问就是GET请求）；
def signin_form():#视图函数，返回一段HTML表单代码：
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

#登录验证：表单提交后触发
@app.route('/signin', methods=['POST'])#同样绑定/signin路径，但仅处理POST请求（即表单提交的请求）
def signin():#视图函数，处理登录验证
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
```

- `action="/signin"`：表单提交后，会向 `/signin` 路径发送请求；
- `method="post"`：表单提交方式为 `POST`（避免密码暴露在 URL 中）；
- 表单包含：用户名输入框（`name="username"`）、密码输入框（`type="password"` 隐藏输入内容）、提交按钮。
- `request.form['username']`：从 POST 请求的表单数据中获取「用户名」（`request.form` 专门解析表单提交的键值对）；
- `request.form['password']`：从表单数据中获取「密码」；
- `if __name__ == '__main__'`：Python 入口判断 —— 只有当这个脚本**被直接运行**（比如 `python server.py`）时，才执行下面的代码；如果脚本被导入为模块（比如 `import server`），则不执行。
- app.run()：启动 Flask 内置的开发服务器,默认运行在：
  - 地址：`127.0.0.1`（本地回环地址，即 `localhost`）；
  - 端口：`5000`。

运行`python app.py`，Flask自带的Server在端口`5000`上监听：

```plain
$ python app.py 
 * Running on http://127.0.0.1:5000/
```

打开浏览器，输入首页地址`http://localhost:5000/`：

![flask-home](https://liaoxuefeng.com/books/python/web/web-framework/home.png)

首页显示正确！

再在浏览器地址栏输入`http://localhost:5000/signin`，会显示登录表单：

![flask-signin-form](https://liaoxuefeng.com/books/python/web/web-framework/signin.png)

输入预设的用户名`admin`和口令`password`，登录成功：

![flask-signin-ok](https://liaoxuefeng.com/books/python/web/web-framework/signin-ok.png)

输入其他错误的用户名和口令，登录失败：

![flask-signin-failed](https://liaoxuefeng.com/books/python/web/web-framework/signin-failed.png)

实际的Web App应该拿到用户名和口令后，去数据库查询再比对，来判断用户是否能登录成功。

除了Flask，常见的Python Web框架还有：

- [Django](https://www.djangoproject.com/)：全能型Web框架；
- [web.py](https://webpy.org/)：一个小巧的Web框架；
- [Bottle](https://bottlepy.org/)：和Flask类似的Web框架；
- [Tornado](https://www.tornadoweb.org/)：Facebook的开源异步Web框架。

当然了，因为开发Python的Web框架也不是什么难事，我们后面也会讲到开发Web框架的内容。

- 小结

有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。

在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。Flask通过`request.form['name']`来获取表单的内容。

## 22.5 使用模版

Web框架把我们从WSGI中拯救出来了。现在，我们只需要不断地编写函数，带上URL，就可以继续Web App的开发了。

但是，**Web App不仅仅是处理逻辑，展示给用户的页面也非常重要**。在函数中返回一个包含HTML的字符串，简单的页面还可以，但是，想想新浪首页的6000多行的HTML，你确信能在Python的字符串中正确地写出来么？

俗话说得好，不懂前端的Python工程师不是好的产品经理。有Web开发经验的同学都明白，Web App最复杂的部分就在HTML页面。HTML不仅要正确，还要通过CSS美化，再加上复杂的JavaScript脚本来实现各种交互和动画效果。总之，生成HTML页面的难度很大。

由于在Python代码里拼字符串是不现实的，所以，模板技术出现了。

使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户：

![mvc-seq](https://liaoxuefeng.com/books/python/web/template/mvc.png)

这就是传说中的MVC：Model-View-Controller，中文名“模型-视图-控制器”。

Python**处理URL的函数就是C**：**Controller，Controller负责业务逻辑**，比如检查用户名是否存在，取出用户信息等等；

包含变量`{{ name }}`的**模板是V**：**View，View负责显示逻辑**，通过简单地**替换一些变量**，**View最终输出的就是用户看到的HTML**。

**Model是用来传给View的**，这样View在**替换变量的时候**，就**可以从Model中取出相应的数据**。

上面的例子中，Model就是一个`dict`：

```python
{ 'name': 'Michael' }
```

只是因为Python支持关键字参数，很多Web框架允许传入关键字参数，然后，在框架内部组装出一个`dict`作为Model。

现在，我们把上次直接输出字符串作为HTML的例子用高端大气上档次的MVC模式改写一下：

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
```

Flask通过`render_template()`函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是[jinja2](https://jinja.palletsprojects.com/)，所以我们先直接安装jinja2：

```plain
$ pip install jinja2
```

然后，开始编写jinja2模板：

### home.html

用来显示首页的模板：

```html
<html>
<head>
  <title>Home</title>
</head>
<body>
  <h1 style="font-style:italic">Home</h1>
</body>
</html>
```

### form.html

用来显示登录表单的模板：

```html
<html>
<head>
  <title>Please Sign In</title>
</head>
<body>
  {% if message %}
  <p style="color:red">{{ message }}</p>
  {% endif %}
  <form action="/signin" method="post">
    <legend>Please sign in:</legend>
    <p><input name="username" placeholder="Username" value="{{ username }}"></p>
    <p><input name="password" placeholder="Password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
  </form>
</body>
</html>
```

### signin-ok.html

登录成功的模板：

```html
<html>
<head>
  <title>Welcome, {{ username }}</title>
</head>
<body>
  <p>Welcome, {{ username }}!</p>
</body>
</html>
```

登录失败的模板呢？我们在`form.html`中加了一点条件判断，把`form.html`重用为登录失败的模板。

最后，一定要把模板放到正确的`templates`目录下，`templates`和`app.py`在同级目录下：

![mvc-dir](https://liaoxuefeng.com/books/python/web/template/dir.png)

启动`python app.py`，看看使用模板的页面效果：

![mvc-form](https://liaoxuefeng.com/books/python/web/template/result.png)

通过MVC，我们在Python代码中处理M：Model和C：Controller，而V：View是通过模板处理的，这样，我们就成功地把Python代码和HTML代码最大限度地分离了。

使用模板的另一大好处是，模板改起来很方便，而且，改完保存后，刷新浏览器就能看到最新的效果，这对于调试HTML、CSS和JavaScript的前端工程师来说实在是太重要了。

在Jinja2模板中，我们用`{{ name }}`表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用`{% ... %}`表示指令。

比如循环输出页码：

```jinja
{% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}
```

如果`page_list`是一个list：`[1, 2, 3, 4, 5]`，上面的模板将输出5个超链接。

除了Jinja2，常见的模板还有：

- [Mako](https://www.makotemplates.org/)：用`<% ... %>`和`${xxx}`的一个模板；
- [Cheetah](https://cheetahtemplate.org/)：也是用`<% ... %>`和`${xxx}`的一个模板；
- [Django](https://www.djangoproject.com/)：Django是一站式框架，内置一个用`{% ... %}`和`{{ xxx }}`的模板。

- 小结

有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。

---

# 第二十三章 异步IO

在IO编程一节中，我们已经知道，CPU的速度远远快于磁盘、网络等IO。在一个线程中，CPU执行代码的速度极快，然而，一旦遇到IO操作，如读写文件、发送网络数据时，就需要等待IO操作完成，才能继续进行下一步操作。这种情况称为同步IO。

在IO操作的过程中，当前线程被挂起，而其他需要CPU执行的代码就无法被当前线程执行了。

因为一个IO操作就阻塞了当前线程，导致其他代码无法执行，所以我们必须使用多线程或者多进程来并发执行代码，为多个用户服务。每个用户都会分配一个线程，如果遇到IO导致线程被挂起，其他用户的线程不受影响。

多线程和多进程的模型虽然解决了并发问题，但是系统不能无上限地增加线程。由于系统切换线程的开销也很大，所以，一旦线程数量过多，CPU的时间就花在线程切换上了，真正运行代码的时间就少了，结果导致性能严重下降。

由于我们要解决的问题是CPU高速执行能力和IO设备的龟速严重不匹配，多线程和多进程只是解决这一问题的一种方法。

另一种解决IO问题的方法是异步IO。当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。

可以想象如果按普通顺序写出的代码实际上是没法完成异步IO的：

```python
do_some_code()
f = open('/path/to/file', 'r')
r = f.read() # <== 线程停在此处等待IO操作结果
# IO操作完成后线程才能继续执行:
do_some_code(r)
```

所以，同步IO模型的代码是无法实现异步IO模型的。

异步IO模型需要一个**消息循环**，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：

```python
loop = get_event_loop()
while True:
    event = loop.get_event()
    process_event(event)
```

消息模型其实早在应用在桌面应用程序中了。一个GUI程序的主线程就负责不停地读取消息并处理消息。所有的键盘、鼠标等消息都被发送到GUI程序的消息队列中，然后由GUI程序的主线程处理。

由于GUI线程处理键盘、鼠标等消息的速度非常快，所以用户感觉不到延迟。某些时候，GUI线程在一个消息处理的过程中遇到问题导致一次消息处理时间过长，此时，用户会感觉到整个GUI程序停止响应了，敲键盘、点鼠标都没有反应。这种情况说明在消息模型中，处理一个消息必须非常迅速，否则，主线程将无法及时处理消息队列中的其他消息，导致程序看上去停止响应。

消息模型是如何解决同步IO必须等待IO操作这一问题的呢？当遇到IO操作时，代码只负责发出IO请求，不等待IO结果，然后直接结束本轮消息处理，进入下一轮消息处理过程。当IO操作完成后，将收到一条“IO完成”的消息，处理该消息时就可以直接获取IO操作结果。

在“发出IO请求”到收到“IO完成”的这段时间里，同步IO模型下，主线程只能挂起，但异步IO模型下，主线程并没有休息，而是在消息循环中继续处理其他消息。这样，在异步IO模型下，一个线程就可以同时处理多个IO请求，并且没有切换线程的操作。对于大多数IO密集型的应用程序，使用异步IO将大大提升系统的多任务处理能力。

- `小故事`

  老张爱喝茶，废话不说，煮开水。 出场人物：老张，水壶两把（普通水壶，简称水壶；会响的水壶，简称响水壶）。 1 老张把水壶放到火上，立等水开。（同步阻塞） 老张觉得自己有点傻 2 老张把水壶放到火上，去客厅看电视，时不时去厨房看看水开没有。（同步非阻塞） 老张还是觉得自己有点傻，于是变高端了，买了把会响笛的那种水壶。水开之后，能大声发出嘀~~~~的噪音。 3 老张把响水壶放到火上，立等水开。（异步阻塞） 老张觉得这样傻等意义不大 4 老张把响水壶放到火上，去客厅看电视，水壶响之前不再去看它了，响了再去拿壶。（异步非阻塞） 老张觉得自己聪明了。

  所谓同步异步，只是对于水壶而言。 普通水壶，同步；响水壶，异步。 虽然都能干活，但响水壶可以在自己完工之后，提示老张水开了。这是普通水壶所不能及的。 同步只能让调用者去轮询自己（情况2中），造成老张效率的低下。

  所谓阻塞非阻塞，仅仅对于老张而言。 立等的老张，阻塞；看电视的老张，非阻塞。 情况1和情况3中老张就是阻塞的，媳妇喊他都不知道。虽然3中响水壶是异步的，可对于立等的老张没有太大的意义。所以一般异步是配合非阻塞使用的，这样才能发挥异步的效用。

## 23.1 协程

在学习异步IO模型前，我们先来了解协程。

协程，又称微线程，纤程。英文名Coroutine。

协程的概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。

子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。

所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。

子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：

```python
def A():
    print('1')
    print('2')
    print('3')

def B():
    print('x')
    print('y')
    print('z')
```



假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：

```plain
1
2
x
y
3
z
```



但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。

看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？

最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

Python对协程的支持是通过generator实现的。

在generator中，我们不但可以通过`for`循环来迭代，还可以不断调用`next()`函数获取由`yield`语句返回的下一个值。

但是Python的`yield`不但可以返回一个值，它还可以接收调用者发出的参数。

来看例子：

传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。

如果改用协程，生产者生产消息后，直接通过`yield`跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

```python
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
```



执行结果：

```plain
[PRODUCER] Producing 1...
[CONSUMER] Consuming 1...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 2...
[CONSUMER] Consuming 2...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 3...
[CONSUMER] Consuming 3...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 4...
[CONSUMER] Consuming 4...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 5...
[CONSUMER] Consuming 5...
[PRODUCER] Consumer return: 200 OK
```



注意到`consumer`函数是一个`generator`，把一个`consumer`传入`produce`后：

1. 首先调用`c.send(None)`启动生成器；
2. 然后，一旦生产了东西，通过`c.send(n)`切换到`consumer`执行；
3. `consumer`通过`yield`拿到消息，处理，又通过`yield`把结果传回；
4. `produce`拿到`consumer`处理的结果，继续生产下一条消息；
5. `produce`决定不生产了，通过`c.close()`关闭`consumer`，整个过程结束。

整个流程无锁，由一个线程执行，`produce`和`consumer`协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

最后套用Donald Knuth的一句话总结协程的特点：

“子程序就是协程的一种特例。”

## 23.2 使用asyncio

`asyncio`是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

`asyncio`的编程模型就是一个消息循环。`asyncio`模块内部实现了`EventLoop`，把需要执行的协程扔到`EventLoop`中执行，就实现了异步IO。

用`asyncio`提供的`@asyncio.coroutine`可以把一个`generator`标记为`coroutine`类型，然后在`coroutine`内部用`yield from`调用另一个`coroutine`实现异步操作。

为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法`async`和`await`，可以让`coroutine`的代码更简洁易读。

用`asyncio`实现`Hello world`代码如下：

```python
import asyncio

async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    await asyncio.sleep(1)
    print("Hello again!")

asyncio.run(hello())
```



`async`把一个函数变成`coroutine`类型，然后，我们就把这个`async`函数扔到`asyncio.run()`中执行。执行结果如下：

```plain
Hello!
(等待约1秒)
Hello again!
```



`hello()`会首先打印出`Hello world!`，然后，`await`语法可以让我们方便地调用另一个`async`函数。由于`asyncio.sleep()`也是一个`async`函数，所以线程不会等待`asyncio.sleep()`，而是直接中断并执行下一个消息循环。当`asyncio.sleep()`返回时，就接着执行下一行语句。

把`asyncio.sleep(1)`看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行`EventLoop`中其他可以执行的`async`函数了，因此可以实现并发执行。

上述`hello()`还没有看出并发执行的特点，我们改写一下，让两个`hello()`同时并发执行：

```python
# 传入name参数:
async def hello(name):
    # 打印name和当前线程:
    print("Hello %s! (%s)" % (name, threading.current_thread))
    # 异步调用asyncio.sleep(1):
    await asyncio.sleep(1)
    print("Hello %s again! (%s)" % (name, threading.current_thread))
    return name
```



用`asyncio.gather()`同时调度多个`async`函数：

```python
async def main():
    L = await asyncio.gather(hello("Bob"), hello("Alice"))
    print(L)

asyncio.run(main())
```



执行结果如下：

```plain
Hello Bob! (<function current_thread at 0x10387d260>)
Hello Alice! (<function current_thread at 0x10387d260>)
(等待约1秒)
Hello Bob again! (<function current_thread at 0x10387d260>)
Hello Alice again! (<function current_thread at 0x10387d260>)
['Bob', 'Alice']
```



从结果可知，用`asyncio.run()`执行`async`函数，所有函数均由同一个线程执行。两个`hello()`是并发执行的，并且可以拿到`async`函数执行的结果（即`return`的返回值）。

如果把`asyncio.sleep()`换成真正的IO操作，则多个并发的IO操作实际上可以由一个线程并发执行。

我们用`asyncio`的异步网络连接来获取sina、sohu和163的网站首页：

```python
import asyncio

async def wget(host):
    print(f"wget {host}...")
    # 连接80端口:
    reader, writer = await asyncio.open_connection(host, 80)
    # 发送HTTP请求:
    header = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    writer.write(header.encode("utf-8"))
    await writer.drain()

    # 读取HTTP响应:
    while True:
        line = await reader.readline()
        if line == b"\r\n":
            break
        print("%s header > %s" % (host, line.decode("utf-8").rstrip()))
    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()
    print(f"Done {host}.")

async def main():
    await asyncio.gather(wget("www.sina.com.cn"), wget("www.sohu.com"), wget("www.163.com"))

asyncio.run(main())
```



执行结果如下：

```plain
wget www.sohu.com...
wget www.sina.com.cn...
wget www.163.com...
(等待一段时间)
(打印出sohu的header)
www.sohu.com header > HTTP/1.1 200 OK
www.sohu.com header > Content-Type: text/html
...
(打印出sina的header)
www.sina.com.cn header > HTTP/1.1 200 OK
www.sina.com.cn header > Date: Wed, 20 May 2015 04:56:33 GMT
...
(打印出163的header)
www.163.com header > HTTP/1.0 302 Moved Temporarily
www.163.com header > Server: Cdn Cache Server V2.0
...
```



可见3个连接由一个线程并发执行3个`async`函数完成。

### 小结

`asyncio`提供了完善的异步IO支持，用`asyncio.run()`调度一个`coroutine`；

在一个`async`函数内部，通过`await`可以调用另一个`async`函数，这个调用看起来是串行执行的，但实际上是由`asyncio`内部的消息循环控制；

在一个`async`函数内部，通过`await asyncio.gather()`可以并发执行若干个`async`函数。

## 23.3 使用aiohttp

`asyncio`可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把`asyncio`用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+`async`函数实现多用户的高并发支持。

`asyncio`实现了TCP、UDP、SSL等协议，`aiohttp`则是基于`asyncio`实现的HTTP框架。

我们先安装`aiohttp`：

```plain
$ pip install aiohttp
```



然后编写一个HTTP服务器，分别处理以下URL：

- `/` - 首页返回`Index Page`；
- `/{name}` - 根据URL参数返回文本`Hello, {name}!`。

代码如下：

```python
# app.py
from aiohttp import web

async def index(request):
    text = "<h1>Index Page</h1>"
    return web.Response(text=text, content_type="text/html")

async def hello(request):
    name = request.match_info.get("name", "World")
    text = f"<h1>Hello, {name}</h1>"
    return web.Response(text=text, content_type="text/html")

app = web.Application()

# 添加路由:
app.add_routes([web.get("/", index), web.get("/{name}", hello)])

if __name__ == "__main__":
    web.run_app(app)
```



直接运行`app.py`，访问首页：

![Index](https://liaoxuefeng.com/books/python/async-io/aiohttp/index.png)

访问`http://localhost:8080/Bob`：

![Hello](https://liaoxuefeng.com/books/python/async-io/aiohttp/hello.png)

使用aiohttp时，定义处理不同URL的`async`函数，然后通过`app.add_routes()`添加映射，最后通过`run_app()`以asyncio的机制启动整个处理流程。

---

学完全部课程，[点此](#开头)返回开头处