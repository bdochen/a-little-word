这一刻，准备仗剑走天涯，攻克所有难关
用忙碌将某些事项遗忘
奋勇向前，不再思考任何东西了


from flask import Flask, render_template_string,  session, request, redirect, url_for,render_template

app = Flask(__name__)

app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'

# 设置过期时间，30秒后失效
app.permanent_session_lifetime =50


@app.route('/')
def index():
    return 'hello mixc'



@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username =request.form.get('username')
        password = request.form.get('password')
        print(username,' ',password)
        if username=='abc' and password=='chen':
            session.permanent = True
            session['username']=username
            return 'login sucess'
        else:
            return render_template('login.html')

@app.route('/home/', methods=['GET', 'POST'])
def home():
    if session['username']=='abc':
        return session['username']
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)


<head><meta charSet="utf-8"/></head>
<body>
    <form action="" method="post">
        账号：<input type="text" name="username">
        密码：<input type="password" name="password">
        <input type="submit" value="登录">
    </form>
</body>



class student(object):
    # 定义构造方法
    def __init__(self, n, a):  # __init__() 是类的初始化方法；它在类的实例化操作后 会自动调用，不需要手动调用；
        # 设置属性
        self.name = n
        self.age = a

    # 定义普通方法
    def tell(self):
        print("%s 说：我今年%s岁" % (self.name, self.age))

    def __str__(self):
        return "名字：%s 年龄：%d" % (self.name, self.age)
#__str__为专有用法
#https://www.cnblogs.com/an-wen/p/11582222.html
#https://blog.csdn.net/pdstar/article/details/90900944
# 类student 实例化一个对象john
john = student("约翰", 19)

# 调用类中的 speak()方法
john.tell()
print(john)



