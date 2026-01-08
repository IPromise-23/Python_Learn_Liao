#练习一:利用os模块编写一个能实现dir -l输出的程序。
#dir -l的效果是显示文件权限、链接数、所有者、组、大小、修改时间、文件名

import os #内置的os模块可以直接调用操作系统提供的接口函数
import time
import pwd  # 用于获取文件所有者
import grp  # 用于获取文件所属组

def get_file_permission(mode):
    """把文件的st_mode转换成rwx格式的权限字符串（比如-rw-r--r--）"""
    perm = []
    # 第一位：d=目录，-=普通文件
    perm.append('d' if os.path.isdir(mode) else '-')
    # 所有者权限（r=读、w=写、x=执行）
    perm.append('r' if (mode & 0o400) else '-')
    perm.append('w' if (mode & 0o200) else '-')
    perm.append('x' if (mode & 0o100) else '-')
    # 组权限
    perm.append('r' if (mode & 0o040) else '-')
    perm.append('w' if (mode & 0o020) else '-')
    perm.append('x' if (mode & 0o010) else '-')
    # 其他用户权限
    perm.append('r' if (mode & 0o004) else '-')
    perm.append('w' if (mode & 0o002) else '-')
    perm.append('x' if (mode & 0o001) else '-')
    return ''.join(perm)


# 遍历当前目录的所有文件/文件夹
for entry in os.scandir('.'):
    stat_info = entry.stat()  # 获取文件的详细状态
    # 1. 文件权限（比如-rw-r--r--）
    permission = get_file_permission(stat_info.st_mode)
    # 2. 链接数
    link_count = stat_info.st_nlink
    # 3. 文件所有者（用户名）
    owner = pwd.getpwuid(stat_info.st_uid).pw_name
    # 4. 文件所属组（组名）
    group = grp.getgrgid(stat_info.st_gid).gr_name
    # 5. 文件大小（字节）
    file_size = stat_info.st_size
    # 6. 最后修改时间（转成可读字符串）
    modify_time = time.ctime(stat_info.st_mtime)
    # 7. 文件名（目录名后加/区分）
    file_name = entry.name + ('/' if entry.is_dir() else '')
    
    # 按dir -l的格式对齐输出
    print(f"{permission} {link_count:2d} {owner:8} {group:8} {file_size:8d} {modify_time} {file_name}")



#练习二:编写一个程序，能在当前目录以及当前目录的所有子目录下
#查找文件名包含指定字符串的文件，并打印出相对路径

import os

def find_target_files(keyword):
    """在当前目录及子目录中，查找文件名包含keyword的文件，打印相对路径"""
    # os.walk('.')会遍历：当前目录（.）→ 所有子目录
    # root：当前遍历的目录路径（相对路径）
    # dirs：当前目录下的子目录列表
    # files：当前目录下的文件列表
    for root, dirs, files in os.walk('.'):
        for file in files:
            if keyword in file:  # 判断文件名是否包含指定字符串
                # 拼接相对路径（root + 文件名）
                relative_path = os.path.join(root, file)
                print(relative_path)


# 获取用户输入的目标字符串
target_keyword = input("请输入要查找的文件名包含的字符串：")
find_target_files(target_keyword)