"""
转义字符
    ' 在python中代表 字符串的数据的标识符
    当我们在程序中 引号相互嵌套时,解释器把'解析成特殊意义的字符,程序会报错
    我们可以通过转义符号  \  将'  转变成  普通字符

    准仪符号  \
            格式 :  \特殊意义的字符


"""

str1 = '他说:\'你干嘛这样子\''
print(str1)

str2 = '你好啊小\n,你吃了吗?'
print(str2)
print("======================")
str3 = "你好啊小伙子\r\n,你最近是不是腰疼?"
print(str3)

str4 = "你好\\n小伙子"
print(str4)

str5 = "as衣服\为一个覅我佛文件佛文件" \
       "我就怕我看见;mfblm为己任"
print(str5)

str6 = r"uyfiwugv\nwyefgt\newy"
print(str6)

# print('\你好')

""""
\d
\D
\w
\W
\s
\S
\n
\r
\t
"""
