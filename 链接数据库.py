from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QMessageBox
import mysql.connector
from PySide6.QtCore import QTimer


class mywindow(QWidget):
    def __init__(self):
        super().__init__()

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kky2395312733@",
            database="hello"
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            create table if not exists users(
            username varchar(50),
            account varchar(50),
            password varchar(50)
            )
            """
        )

        self.mainlayout = QVBoxLayout()
        self.btn = QPushButton("button")

        self.layout1 = QHBoxLayout()
        self.label_username = QLabel("username:")
        self.LineEdit_username = QLineEdit()
        self.layout1.addWidget(self.label_username)
        self.layout1.addWidget(self.LineEdit_username)

        self.layout2 = QHBoxLayout()
        self.label_account = QLabel("account:   ")
        self.LineEdit_account = QLineEdit()
        self.layout2.addWidget(self.label_account)
        self.layout2.addWidget(self.LineEdit_account)

        self.layout3 = QHBoxLayout()
        self.label_password = QLabel("password:")
        self.LineEdit_password = QLineEdit()
        self.layout3.addWidget(self.label_password)
        self.layout3.addWidget(self.LineEdit_password)

        self.label_error = QLabel("")
        self.label_error.setStyleSheet("color: red; font-size: 12px;")

        self.mainlayout.addLayout(self.layout1)
        self.mainlayout.addLayout(self.layout2)
        self.mainlayout.addLayout(self.layout3)
        self.mainlayout.addWidget(self.btn)
        self.mainlayout.addWidget(self.label_error)
        self.setLayout(self.mainlayout)

        self.btn.clicked.connect(self.func)
    def func(self):
        input_account = self.LineEdit_account.text()
        input_password = self.LineEdit_password.text()
        input_username = self.LineEdit_username.text()
        if not input_account or not input_password or not input_username:
            self.label_error.setText("用户名，账号和密码不能为空")
            QTimer.singleShot(2000, lambda: self.label_error.setText(""))
            return
        self.cursor.execute(
             """
             insert into users (username,account,password) values (%s,%s,%s)
             """,
             (input_username, input_account, input_password)
        )
        self.conn.commit()

    def closeEvent(self, event):
        print("closeEvent被执行，正在关闭数据库连接")
        self.cursor.close()
        self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = mywindow()
    window.show()
    app.exec()