#!/usr/bin/env python3
# sensor.py : 各センサー取得プログラム
# coding: UTF-8
import ds18b20
import hc_sr04
import dht22

# 各センサー取得処理
def get_value():
    # 水温取得
    waterTemp = ds18b20.get_temperature()
    # 距離取得
    distance = hc_sr04.get_distance()
    # 室内温湿度取得
    roomHum, roomTemp = dht22.get_humidity_temperature()

    return waterTemp, distance, roomTemp, roomHum

#-- main --
def main():
    w, d, t, h = get_value()
    resultStr = 'W:{}, D:{}, T:{}, H:{}'.format(
        round(w, 1),
        round(d, 1),
        round(t, 1),
        round(h, 1))
    print(resultStr)

if __name__ == '__main__' :
    main()