'''
Created on 2018年5月14日

@author: Administrator
'''
import csv
def getCsvData():
    #读取CSV文件
    value_rows=[]
    with open('testcsv.csv',encoding='UTF-8') as f:
        f_csv= csv.reader(f)
        next(f_csv)
        for r in f_csv:
            value_rows.append(r)
    return value_rows