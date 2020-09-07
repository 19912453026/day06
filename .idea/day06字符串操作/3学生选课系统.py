"""
选课系统:
"""
# 定义数据
#  level: 0  管理员   1 学员
#  del_f: 0  正常    1  被删除
user_info = {
    "admin":{"pwd":"123456","checked_cou":[],"nikname":"老孙","level":0,"del_f":0},
    "zs":{"pwd":"123456","checked_cou":[],"nikname":"张三","level":1,"del_f":0},
}
course = ["微机原理","网络原理","毛概"]

# 系统的界面
while True:
    print("===================")
    print("   1.登录")
    print("   2.退出")
    print("===================")

    # 判断要干什么事情
    msg = input("请输入您的选项:")
    if msg == "1":
        while True:
            print("==========用户登录===========")
            # 提示输入账号或密码
            user = input("请输入您的账号:")
            pwd = input("请输入您的密码:")
            # 判断用户名和密码
            if user not in user_info or pwd != user_info[user]["pwd"]:
                input("账号或密码有误:按回车请重新输入:")
                continue
            # 判断身份:
            if user_info[user]['level'] == 0:
                print("========管理员个人首页===========")
                print("   1.个人中心")
                print("   2.查看所有的课程")
                print("   3.添加课程")
                print("   4.添加学生")
                print("   5.退出系统")
                print("   6返回登录界面")

            else:
                print("========普通用户个人首页=======")
                print("   1.个人中心")
                print("   2.查看已选的课程")
                print("   3.选课")
                print("   5.退出系统")
                print("   6返回登录界面")
    elif msg == "2":
        print("正在退出系统....")
        print("退出成功!!!!")
        exit()
    else:
        input("您输入的选项有误,按回车后重新输入:")