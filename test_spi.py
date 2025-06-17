import sys
import signal
import os
import time

# 导入spidev模块
import spidev

def signal_handler(signal, frame):
    sys.exit(0)

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

def spidevTest():
    # 设置spi的bus号（0, 1, 2）和片选(0, 1)
    spi_bus = input("Please input SPI bus num:")
    spi_device = input("Please input SPI cs num:")
    # 创建spidev类的对象以访问基于spidev的Python函数。
    spi=spidev.SpiDev()
    # 打开spi总线句柄
    spi.open(int(spi_bus), int(spi_device))

    # 设置 spi 频率为 12MHz
    spi.max_speed_hz = 12000000

    print("Starting demo now! Press CTRL+C to exit")

    # 发送 [0x55, 0xAA], 接收的数据应该也是 [0x55, 0xAA]
    try:
        while True:
            resp = spi.xfer2([0x55, 0xAA])
            print(BytesToHex(resp))
            time.sleep(1)

    except KeyboardInterrupt:
        spi.close()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    print("List of enabled spi controllers:")
    os.system('ls /dev/spidev*')

    spidevTest()
