"""
字符串操作
"""
pwd = "20200901"  #--->"2o2oo9ol"

data = {
    "a":"A",
    "0":""
}
#  生成字符表
table = str.maketrans(data)

pwd = "abc2020"
res = pwd.translate(table)
print(res)


#  字符串的格式化
# 字符串的拼接
# +
name = "张三"
age = 18
gender = "女"
length = 30.55
# 以字符串的形式输出用户信息
print("姓名:"+name+",年龄:"+str(age)+",性别:"+gender)
# 使用print 输出多个值
print("姓名:",name,",年龄:",age)
# %
str1 = "姓名:%s,年龄:%i,性别:%s"%(name,age,gender)
print(str1)
str2 = "姓名:%s"%(name,)
print(str2)

str3 = "姓名:%s,头发的长度:%.1f"%(name,length)
print(str3)

# 格式化对齐方式(了解)
str4 = "姓名:%5s,"%name # 默认右对齐
print(str4)

str5 = "姓名:%-5s,"%name
print(str5)

# 左对齐时,填充不生效, 右对齐可以生效的
str6 = "年龄:%05d"%age
print(str6)

print("=================")
# format()
name = "三儿"
age = 18
gender = "女"
length = 35.55

# 基本使用
res = "姓名:{},性别:{},年龄:{}".format(name,gender,age)
print(res)
# 通过索引来去使用,一个值可以多次使用
res2 = "年龄:{2},姓名:{0},性别:{1},年龄:{2}".format(name,gender,age)
print(res2)

# 直接通过变量名字设置
res3 = "姓名:{name},性别:{gender},年龄:{age},性别:{gender}".format(gender="男",name="小白",age=22)
print(res3)

info = {
    "name":"小六",
    "age":18.0808
}
# 直接传递字典
res4 = "你做个自我介绍吧:{name},{age},{name}".format(**info)
print(res4)

# 保留小数
res4 = "你的身高有多高{length:.1f}".format(length=178.6603)
print(res4)


# f-string
name = "彩飘飘"
age = 18

res5 = f"我叫:{name},芳龄:{age+2}"
print(res5)

res6 = f"我叫:{name:0>10},芳龄:{age+2}"
print(res6)

weight = 80.055

res7 = f"我的体重是:{weight:.2f}"
print(res7)
