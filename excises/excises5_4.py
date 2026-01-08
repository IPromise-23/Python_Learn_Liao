# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）
# 帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# 用if-elif判断并打印结果：
H=input('请输入你的身高（米）：')
W=input('请输入你的体重（公斤）：')
bmi=float(W)/float(H)**2
if bmi<18.5:
    print('你的bmi指数为：%.1f，体重过轻' %bmi)
elif 18.5<=bmi<25:
    print('你的bmi指数为：%.1f，体重正常' %bmi)
elif 25<=bmi<28:
    print('你的bmi指数为：%.1f，体重过重' %bmi)
elif 28<=bmi<32:
    print('你的bmi指数为：%.1f，肥胖' %bmi)
else:
    print('你的bmi指数为：%.1f，严重肥胖' %bmi)