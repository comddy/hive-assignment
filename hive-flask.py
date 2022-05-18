# 导入连接工具
from impala.dbapi import connect
# 导入as_pandas工具，可以将获取到的数据转化为 dataframe或者 Series
from impala.util import as_pandas
import pandas as pd
import numpy as np
from flask import Flask,jsonify,current_app
from flask_cors import CORS
import re
# 得到连接，
conn = connect(host='192.168.142.110', port=10000, auth_mechanism='NOSASL', user='root', 
password='***',  database='hive1')
# 得到句柄
cursor = conn.cursor()

# 总收入统计和每日收入统计
daily_amount, total_amount = {}, 1
def order():
    global daily_amount, total_amount
    sql = "select * from dwd_daily_order"
    cursor.execute(sql)
    res = as_pandas(cursor)
    daily_amount = {
        'name': res.iloc[:,0].to_list(),
        'value': res.iloc[:,1].to_list()
    }
    sql = "select * from dws_total_profit"
    cursor.execute(sql)
    res = as_pandas(cursor)
    total_amount = res.iloc[0,0]

# topN
top10_amount,top10_time = {}, {}
def topN():
    global top10_amount,top10_time
    sql = "select * from dws_game_user_top10_amount"
    cursor.execute(sql)
    res = as_pandas(cursor)
    top10_amount = {
        'name': res.iloc[:,1].to_list(),
        'value': res.iloc[:,2].to_list()
    }
    sql = "select * from dws_game_user_top10_played_time"
    cursor.execute(sql)
    res = as_pandas(cursor)
    time = res.iloc[:,2].to_list()
    time = [round(int(i)/3600,1) for i in time]
    top10_time = {
        'name': res.iloc[:,1].to_list(),
        'value': time
    }

# 用户每日数据分析
daily_start_info = {}
def daily_start(): 
    global daily_start_info
    sql = "select * from dws_daily_start_info"
    cursor.execute(sql)
    res = as_pandas(cursor)
    daily_start_info = {
        'new': res.iloc[:,0].to_list(),
        'old': res.iloc[:,1].to_list(),
        'name': res.iloc[:,2].to_list(),
    }

#每日留存率
retention_rate = {}
def daily_retention():
    global retention_rate
    sql = "select * from dwd_game_user_retention_info"
    cursor.execute(sql)
    res = as_pandas(cursor)
    f = lambda i:re.findall('"(.*?)"', res.iloc[i,0].decode())
    start_device = f(0)
    device_num = f(0)
    retention_rate_info = []
    for i in range(1,7):
        start_device = list(set(start_device) & set(f(i)))
        device_num = list(set(device_num) | set(f(i)))
        retention_rate_info.append(round(len(start_device) / len(device_num),2))
    retention_rate = {
        'name': ["2日留存率","3日留存率","4日留存率","5日留存率","6日留存率","7日留存率"],
        'value': retention_rate_info
    }

#用户概况
summary_user = {}
def summary_info():
    global summary_user
    sql = "select * from dws_game_user_per_played_time"
    cursor.execute(sql)
    res = as_pandas(cursor)
    summary_user = {
        'value': [round(float(res.iloc[0,0]) / 3600, 2), round(float(res.iloc[0,1]) / 3600, 2)]
    }

# 地区分布
myArea = {}
def area_info():
    global myArea
    sql = "select * from dws_game_user_area"
    cursor.execute(sql)
    res = as_pandas(cursor)
    value = res.iloc[:,1].to_list()
    value[0] += value[9]
    value.pop()
    myArea = {
        'name': res.iloc[:9,0].to_list(),
        'value': value
    }

def init_data():
    order()
    topN()
    daily_start()
    daily_retention()
    summary_info()
    area_info()



app = Flask(__name__)
with app.app_context():
    a = current_app
    b = current_app.config['DEBUG']
CORS(app, resources=r'/*')  # 注册CORS, "/*" 允许访问所有api

# @cross_origin(supports_credentials=True)  #配置单一指定路由
@app.route("/topN/amount", methods=["GET","POST"])
def topN_amount():
    return jsonify(top10_amount)

@app.route("/topN/time", methods=["GET","POST"])
def topN_time():
    return jsonify(top10_time)

@app.route("/amount/total", methods=["GET","POST"])
def amount_total():
    return str(total_amount)

@app.route("/amount")
def amount():
    return jsonify(daily_amount)

@app.route("/dailyLogin")
def dailyLogin():
    return jsonify(daily_start_info)

@app.route("/retention")
def retention():
    return jsonify(retention_rate)

@app.route("/summary")
def summary():
    return jsonify(summary_user)
 
@app.route("/area")
def area():
    return jsonify(myArea)

if __name__ == '__main__':
    init_data()
    app.run(host="0.0.0.0")
