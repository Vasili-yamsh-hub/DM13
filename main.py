from PyQt5 import QtWidgets,uic
from PyQt5.QtSerialPort import QSerialPort,QSerialPortInfo
from PyQt5.QtCore import QIODevice
app = QtWidgets.QApplication([])
ui  = uic.loadUi("main_design.ui")
ui.setWindowTitle("Serial GUI")

serial = QSerialPort()
serial.setBaudRate(115200)
portlst = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portlst.append(port.portName())

ui.COM_List.addItems(portlst)

def open_port():
    serial.setPortName(ui.COM_List.currentText())
    serial.open(QIODevice.ReadWrite)
    print("on port")

def close_port():
    serial.close()
    print("close")

def on_read():
    rx = serial.readLine()
    print(rx)


serial.readyRead.connect(on_read)
ui.OpenCOM.clicked.connect(open_port)
ui.CloseCOM.clicked.connect(close_port)


ui.show()
app.exec()