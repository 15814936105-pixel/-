from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QMessageBox
from PySide6.QtCore import QTimer
from dataclasses import dataclass
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Kky2395312733@",
    database = "timer"
)
cursor = conn.cursor()
cursor.execute(
    """
    create table if not exists users(
    username varchar(50),
    account varchar(50),
    password varchar(50)
    )
    """
)
class signin_window(QWidget):
    def __init__(self):
        super().__init__()
        self.signup_window = signup_window()  # 创建注册窗口实例，存为属性
        self.mainwindow = mainwindow() # 创建主窗口实例，存为属性
        #账号输入
        self.Layout_account = QHBoxLayout()
        self.Label_account = QLabel("account  ")
        self.LineEdit_account = QLineEdit()
        self.Layout_account.addWidget(self.Label_account)
        self.Layout_account.addWidget(self.LineEdit_account)
        #密码输入
        self.Layout_password = QHBoxLayout()
        self.Label_password = QLabel("password")
        self.LineEdit_password = QLineEdit()
        self.Layout_password.addWidget(self.Label_password)
        self.Layout_password.addWidget(self.LineEdit_password)
        #密码错误提示
        self.Label_error = QLabel("")
        self.Label_error.setStyleSheet("color: red; font-size: 12px;")
        #登录按钮
        self.btn_signin = QPushButton("sign in")
        self.btn_signin.clicked.connect(self.signin)
        #注册按钮
        self.btn_signup = QPushButton("sign up")
        self.btn_signup.clicked.connect(self.signup)
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.Layout_account)
        self.layout.addLayout(self.Layout_password)
        self.layout.addWidget(self.Label_error)
        self.layout.addWidget(self.btn_signin)
        self.layout.addWidget(self.btn_signup)
        self.setLayout(self.layout)
    def signin(self):
        # for i in users:
        #     if i.user_account==self.LineEdit_account.text() and i.user_password==self.LineEdit_password.text():
        #         QMessageBox.warning(self, "state", "successfully sign in")
        #         self.close()
        #         self.mainwindow.show()
        #         return
        #循环结束没有return， 说明没有找到
        self.input_account = self.LineEdit_account.text()
        self.input_password = self.LineEdit_password.text()
        cursor.execute(
        """
        select * from users where account=%s and password=%s
        """,(self.input_account, self.input_password)
        )
        self.result = cursor.fetchone()
        if self.result:
            QMessageBox.warning(self, "state", "successfully sign in")
            self.close()
            self.mainwindow.show()
            return
            #循环结束没有return， 说明没有找到
        self.Label_error.setText("password incorrect")
        self.LineEdit_account.clear()
        self.LineEdit_password.clear()
        QTimer.singleShot(2000, lambda:self.Label_error.setText(""))
    def signup(self):
        self.hide()
        self.signup_window.show()
# 注册窗口
class signup_window(QWidget):
    def __init__(self):
        super().__init__()
        #输入用户名
        self.Layout1 = QHBoxLayout()
        self.Label_username = QLabel("please enter your username")
        self.LineEdit_username = QLineEdit()
        self.Layout1.addWidget(self.Label_username)
        self.Layout1.addWidget(self.LineEdit_username)
        #输入账号
        self.Layout2 = QHBoxLayout()
        self.Label_account = QLabel("please enter your account")
        self.LineEdit_account = QLineEdit()
        self.Layout2.addWidget(self.Label_account)
        self.Layout2.addWidget(self.LineEdit_account)
        #输入密码
        self.Layout3 = QHBoxLayout()
        self.Label_password = QLabel("please enter your password")
        self.LineEdit_password = QLineEdit()
        self.Layout3.addWidget(self.Label_password)
        self.Layout3.addWidget(self.LineEdit_password)
        #确认按钮
        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.add_information_to_mysql)
        #
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addLayout(self.Layout1)
        self.mainlayout.addWidget(QLabel(""))
        self.mainlayout.addLayout(self.Layout2)
        self.mainlayout.addWidget(QLabel(""))
        self.mainlayout.addLayout(self.Layout3)
        self.mainlayout.addWidget(QLabel(""))
        self.mainlayout.addWidget(self.btn)
        self.setLayout(self.mainlayout)
    def add_information_to_mysql(self):
        self.input_username = self.LineEdit_username.text()
        self.input_account = self.LineEdit_account.text()
        self.input_password = self.LineEdit_password.text()
        cursor.execute(
            """
            insert into users (username,account,password) values (%s,%s,%s)
            """,(self.input_username,self.input_account,self.input_password)
        )
        conn.commit()
        self.close()
        window.show()

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        label = QLabel("hello")
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = signin_window()
    window.show()
    app.exec()
