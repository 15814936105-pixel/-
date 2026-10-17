from PySide6.QtCore import QDateTime,QDate,QTime
print(QDate.currentDate())
print(QTime.currentTime())
print(QDateTime.currentDateTime())
print(QDate)
dt = QDateTime.currentDateTime()
print(dt.toString("yyyy年MM月dd日HH时mm分"))