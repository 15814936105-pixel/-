from PySide6.QtWidgets import QApplication,QPushButton,QLabel,QLineEdit,QHBoxLayout,QVBoxLayout,QWidget,QGroupBox
from PySide6.QtCore import QDateTime
from PySide6.QtGui import QIcon
import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
def getweather(city):
    url = f"https://api.seniverse.com/v3/weather/now.json?key={API_KEY}&location={city}&language=zh-Hans&unit=c"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data
class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("天气检测器")
        #输入城市
        self.Layout_city = QHBoxLayout()
        self.Label_city = QLabel("请输入您要查询的城市")
        self.LineEdit_city = QLineEdit()
        self.Layout_city.addWidget(self.Label_city)
        self.Layout_city.addWidget(self.LineEdit_city)
        #查询按钮
        self.btn = QPushButton("查询")
        self.btn.setIcon(QIcon("search.png"))
        self.btn.clicked.connect(self.func)
        #显示时间
        self.Layout_time = QHBoxLayout()
        self.Label_time1 = QLabel("现在时间:")
        self.Label_time2 = QLabel()
        self.Layout_time.addWidget(self.Label_time1)
        self.Layout_time.addWidget(self.Label_time2)
        #显示温度
        self.Layout_temperature = QHBoxLayout()
        self.Label_temperature1 = QLabel("温度:")
        self.Label_temperature2 = QLabel()
        self.Layout_temperature.addWidget(self.Label_temperature1)
        self.Layout_temperature.addWidget(self.Label_temperature2)
        #显示天气
        self.Layout_weather = QHBoxLayout()
        self.Label_weather1 = QLabel("天气:")
        self.Label_weather2 = QLabel()
        self.Layout_weather.addWidget(self.Label_weather1)
        self.Layout_weather.addWidget(self.Label_weather2)
        #Groupbox
        self.groupbox = QGroupBox("查询结果")
        self.groupbox.setStyleSheet("""
            QGroupBox {
                border: 1px solid #dcdde1;
                border-radius: 10px;
                margin-top: 10px;
                background: white;
                font-weight: bold;
                color: #2c3e50;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 5px;
            }
        """)
        self.Layout_groupbox = QVBoxLayout()
        self.Layout_groupbox.addLayout(self.Layout_time)
        self.Layout_groupbox.addLayout(self.Layout_temperature)
        self.Layout_groupbox.addLayout(self.Layout_weather)
        self.groupbox.setLayout(self.Layout_groupbox)

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addLayout(self.Layout_city)
        self.mainlayout.addWidget(self.btn)
        # self.mainlayout.addLayout(self.Layout_time)
        # self.mainlayout.addLayout(self.Layout_temperature)
        # self.mainlayout.addLayout(self.Layout_weather)
        self.mainlayout.addWidget(self.groupbox)
        self.mainlayout.setSpacing(15)
        self.mainlayout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(self.mainlayout)
    def func(self):
        self.city = self.LineEdit_city.text()
        self.data = getweather(self.city)
        self.temperature = self.data["results"][0]["now"]["temperature"]
        self.text = self.data["results"][0]["now"]["text"]
        self.Label_temperature2.setText("   "+self.temperature+"℃")
        self.Label_weather2.setText("   "+self.text)
        self.dt = QDateTime.currentDateTime()
        self.Label_time2.setText(self.dt.toString("yyyy年MM月dd日HH时mm分"))

if __name__ == "__main__":
    app = QApplication([])
    window = mainwindow()
    window.show()
    app.exec()