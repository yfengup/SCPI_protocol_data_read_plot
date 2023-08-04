#VCTOR胜利仪器 4090B LCR数字电桥
#RS485接口，通过SCPI协议串口读取，保存（txt与csv文件），并实时绘制测量曲线图
#copyright Steve Feng 31/07/2023

import serial
import matplotlib.pyplot as plt
import csv

#绘图变量声明
plt.ion()
plt.figure(figsize=(10, 6))
x = []
y = []

# 串口配置
ser = serial.Serial('COM5', 9600, timeout=0.1) #前两个参数分别是串口和波特率，要和仪器对应timeout参数可以修改横坐标的分度值

# txt打开文件
file_path = "D:\新-博士生涯\数字电桥读数\LCR read draw\data.txt"  # 更改为保存数据的文件路径
file = open(file_path, "w")

# csv打开文件
csvfile = open('csv_data.csv', mode='w', newline='')
fieldnames = ['resistance']
csvwrite = csv.DictWriter(csvfile, fieldnames=fieldnames)
csvwrite.writeheader()

# 读取和保存数据，并实时绘图
while True:
        cmd = 'FETCh?\r\n' #SCPI协议中读取实时测量值的命令
        ser.write(cmd.encode('utf-8')) #转成字符型，并写入仪器
        data = ser.readall().decode() #读取仪器的返回测量值

        number_data = data.strip() #去除字符串中的转义符
        float_data = number_data.replace(',', '') #去除字符串中的逗号
        value = float(float_data) #字符型转浮点型

        file.write(data)  # 写入txt文件
        file.flush()  # 刷新文件缓冲区

        csvwrite.writerow({'resistance': value}) #保存csv文件

        #实时绘制曲线图
        x.append(len(x))
        y.append(value)
        plt.clf()
        plt.plot(x, y)
        plt.xlabel("Time (s)")
        plt.ylabel("Value")
        plt.title("Real-time Data Graph")
        plt.pause(0.01)

        print(value)  # 可选，打印读取到的数据

# 关闭文件和串口
file.close()
ser.close()