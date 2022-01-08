import os

from requests.sessions import session
from todayLoginService import TodayLoginService
from login.Utils import Utils
from liteTools import *
import time
import json
import htmlLib
import requests
from requests import utils as ru


def loadConfig():
    user = DT.loadYml('config.yml')

    # 用户代理
    user['proxy'] = user.get('proxy')
    requestsProxies = dict()
    if not user['proxy']:  # 如果用户代理设置为空，则不设置代理。
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


def getQrcode(loginInSession):
    # 初始化
    result = {"status": "", "qrcode": "", "currentTime": "",
              "cookies": "", "headers": "", "url": ""}
    session = loginInSession['session']
    headers = loginInSession['headers']
    host = loginInSession['host']
    # 开始获取签到列表
    url = f"{host}campusphere.net/wec-counselor-leave-apps/leave/home/index.html?v={int(time.time())}"
    session.get(url, headers=headers, verify=False)
    headers['Content-Type'] = 'application/json;charset=UTF-8'
    url = f"{host}wec-counselor-leave-apps/leave/checkApplyCondition"
    session.post(url, headers=headers, data=json.dumps(
        {"type": 1}), verify=False)
    # 正式获取签到列表
    url = f"{host}wec-counselor-leave-apps/leave/stu/list"
    session.post(url, headers=headers, data=json.dumps(
        {"pageNumber": 1, "pageSize": 20, "needApproval": 1}), verify=False)
    url = f"{host}wec-counselor-leave-apps/leave/stu/list"
    res = session.post(url, headers=headers, data=json.dumps(
        {"pageNumber": 1, "pageSize": 20, "needApproval": 1}), verify=False)
    res = DT.resJsonEncode(res)
    # 寻找正在休假中的任务
    vacationList = res['datas']['rows']
    vacationList = list(filter(lambda x: x['status'] == "6", vacationList))
    if len(vacationList) == 0:
        # 如果没有找到正在休假中的任务
        result["status"] = "没有找到已经请假的任务"
        return result
    vacation = vacationList[0]
    result["status"] = vacation['leaveReason']
    # 获取请假详情
    url = f"{host}wec-counselor-leave-apps/leave/stu/detail"
    session.post(url, headers=headers, data=json.dumps(
        {"id": vacation['id'], "needApproval": 1}), verify=False)
    # 获取qrCode
    url = f"{host}wec-counselor-leave-apps/leave/stu/getLeaveQr"
    res = session.post(url, headers=headers, data=json.dumps(
        {"leaveId": vacation['id'], "needApproval": 1}), verify=False)
    res = DT.resJsonEncode(res)
    result['qrcode'] = res['datas']['qr']+"&1"
    result['currentTime'] = res['datas']['currentTime']
    # 刷新二维码用的数据
    result['url'] = url
    result['cookies'] = ru.dict_from_cookiejar(session.cookies)
    result['headers'] = session.headers
    result['leaveId'] = vacation['id']
    return result

def reflashQrCode(result):
    # 初始化
    session = requests.session()
    session.cookies.update(result['cookies'])
    session.headers = result['headers']
    url = result['url']
    leaveId = result['leaveId']
    # 获取二维码
    res = session.post(url, data=json.dumps(
        {"leaveId": leaveId, "needApproval": 1}), verify=False)
    res = DT.resJsonEncode(res)
    # 更新数据
    result['qrcode'] = res['datas']['qr']+"&1"
    result['currentTime'] = res['datas']['currentTime']
    result['cookies'] = ru.dict_from_cookiejar(session.cookies)
    result['headers'] = session.headers
    return result


def login(user):
    # 开始登录
    today = TodayLoginService(user)
    today.login()
    return {"session": today.session, "host": today.host, "headers": today.session.headers}


def main_handler(event, context):
    '''腾讯云入口函数'''
    # 初始化参数
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 将工作路径设置为脚本位置
    user = loadConfig()
    apiUrl = "https://" + event['headers']['host'] + event['requestContext']['path']
    urlParams = event['queryString']
    key = bytes(user['key'].encode())
    
    if "reflash" in urlParams: # 如果是刷新二维码
        reflashSession = json.loads(CT.decrypt_QrString(urlParams["reflash"], key = key))
        # 刷新Qrcode
        result = reflashQrCode(reflashSession)
        # 封装刷新二维码用的会话
        reflashSession = CT.encrypt_QString(json.dumps(result), key = key)
        reflashUrl = apiUrl + f"?reflash={reflashSession}"

    else:
        user['username'] = urlParams['account']
        user['password'] = urlParams['key']
        user['schoolName'] = urlParams['school']
        # 开始登录
        loginInSession = login(user)
        # 获取QrCode
        result = getQrcode(loginInSession)
        # 封装刷新二维码用的会话
        reflashSession = CT.encrypt_QString(json.dumps(result), key = key)
        reflashUrl = apiUrl + f"?reflash={reflashSession}"



    body = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ko" lang="ko">
<head>
<title>{result['status']}</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no" />
<meta http-equiv="refresh" content="10;url={reflashUrl}">
<script type="text/javascript" src="//static.runoob.com/assets/qrcode/qrcode.min.js"></script>
{htmlLib.flowCss}
{htmlLib.flowCss_2}
{htmlLib.css}
</head>
<body>
{htmlLib.div_1}
</br>
</br>
</br>
</br>
<div id="qrcode" align="center"></div>
<p><font color="lightgray">{result['status']}</font></p>
<p><font color="lightgray">{result['currentTime']}</font></p>
<script type="text/javascript">
new QRCode(document.getElementById("qrcode"), {'{'}
    text: "{result['qrcode']}",
    width: 200,
    height: 200,
    colorDark : "#000000",
    colorLight : "#ffffff",
    correctLevel : QRCode.CorrectLevel.H
{'}'});  // 设置要生成二维码的链接
</script>
{htmlLib.timeJs}
</body>
</html>
"""

    resp = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text/html;charset=utf-8"},
        "body": body
    }
    return resp
