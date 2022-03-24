from PyQt5 import QtWidgets,uic
from PyQt5.QtSerialPort import QSerialPort,QSerialPortInfo
from PyQt5.QtCore import QIODevice
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys


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

list_X = []
list_Y = []

for i in range(500):
    list_X.append(i)
for i in range(500):
    list_Y.append(0)
def on_read():
    rx = serial.readLine()
    data = eval(str(rx, "utf-8").strip())

    print(data)
    global list_X, list_Y

    list_Y = list_Y[1:]
    list_Y.append(data)
    ui.graph.clear()
    ui.graph.plot(list_X, list_Y)


serial.readyRead.connect(on_read)
ui.OpenCOM.clicked.connect(open_port)
ui.CloseCOM.clicked.connect(close_port)


ui.show()
app.exec()