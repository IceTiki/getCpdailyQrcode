import os
from todayLoginService import TodayLoginService
from login.Utils import Utils
from liteTools import *
import time
import json

def loadConfig():
    user = DT.loadYml('config.yml')
    
    # 用户代理
    user['proxy'] = user.get('proxy')
    requestsProxies = dict()
    if not user['proxy']: # 如果用户代理设置为空，则不设置代理。
        requestsProxies = dict()
    elif type(user['proxy']) == str:
        if "http://" in user['proxy'][0:7]:
            requestsProxies['http'] = user['proxy']
        elif "https://" == user['proxy'][0:8]:
            requestsProxies['https'] = user['proxy']
        else:
            raise Exception("代理应以http://或https://为开头")
    elif type(user['proxy']) == dict:
        requestsProxies = user['proxy']
    user['proxy'] = requestsProxies

    return user

def getQrcode(user):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 将工作路径设置为脚本位置
    result = {"status":"","qrcode":"","currentTime":""}
    # 开始登录
    today = TodayLoginService(user)
    today.login()
    session = today.session
    host = today.host
    headers = session.headers
    # 开始获取签到列表
    url = f"{host}campusphere.net/wec-counselor-leave-apps/leave/home/index.html?v={int(time.time())}"
    session.get(url, headers=headers, verify=False)
    headers['Content-Type'] = 'application/json;charset=UTF-8'
    url = f"{host}wec-counselor-leave-apps/leave/checkApplyCondition"
    session.post(url, headers=headers,data=json.dumps({"type":1}), verify=False)
    # 正式获取签到列表
    url = f"{host}wec-counselor-leave-apps/leave/stu/list"
    session.post(url, headers=headers,data=json.dumps({"pageNumber":1,"pageSize":20,"needApproval":1}), verify=False)
    url = f"{host}wec-counselor-leave-apps/leave/stu/list"
    res = session.post(url, headers=headers,data=json.dumps({"pageNumber":1,"pageSize":20,"needApproval":1}), verify=False)
    res = DT.resJsonEncode(res)
    # 寻找正在休假中的任务
    vacationList = res['datas']['rows']
    vacationList = list(filter(lambda x:x['status']=="6",vacationList))
    if len(vacationList) == 0:
        # 如果没有找到正在休假中的任务
        result["status"] = "没有找到已经请假的任务"
        return result
    vacation=vacationList[0]
    result["status"] = vacation['leaveReason']
    # 获取请假详情
    url = f"{host}wec-counselor-leave-apps/leave/stu/detail"
    session.post(url, headers=headers,data=json.dumps({"id":vacation['id'],"needApproval":1}), verify=False)
    # 获取qrCode
    url = f"{host}wec-counselor-leave-apps/leave/stu/getLeaveQr"
    res = session.post(url, headers=headers,data=json.dumps({"leaveId":vacation['id'],"needApproval":1}), verify=False)
    res = DT.resJsonEncode(res)
    result['qrcode'] = res['datas']['qr']+"&1"
    result['currentTime'] = res['datas']['currentTime']
    return result


def main_handler(event, context):
    '''腾讯云入口函数'''
    # 初始化参数
    user = loadConfig()
    user['username'] = event['queryString']['account']
    user['password'] = event['queryString']['key']
    user['schoolName'] = event['queryString']['school']
    # 获取QrCode
    result = getQrcode(user)

    body=f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ko" lang="ko">
<head>
<title>{result['status']}</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no" />
<script type="text/javascript" src="//static.runoob.com/assets/qrcode/qrcode.min.js"></script>
</head>
<body>
<h1>{result['status']}</h1>
<h1>{result['currentTime']}</h1>
<div id="qrcode"></div>
<script type="text/javascript">
new QRCode(document.getElementById("qrcode"), "{result['qrcode']}");  // 设置要生成二维码的链接
</script>
</body>
</html>
"""

    resp = {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {"Content-Type":"text/html;charset=utf-8"},
    "body": body
    }
    return resp
