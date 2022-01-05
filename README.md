# getCpdailyQrcode

基于[若离自动签到](https://github.com/thriving123/fuckTodayStudy)的项目，用于通过账号密码获取朋友的请假二维码。

## 声明

本项目为Python学习交流的开源非营利项目，仅作为程序员之间相互学习交流之用。

严禁用于商业用途，禁止使用本项目进行任何盈利活动。

使用者请遵从相关政策。对一切非法使用所产生的后果，我们概不负责。

本项目对您如有困扰请联系我们删除。

## 计划

- [ ] 使用非对称加密，使其可以分享限时而且不泄露密码的请假二维码使用连接
- [ ] 使返回的页面看起来像是今日校园里的页面

## 说明

原理是腾讯云API触发腾讯云函数，通过模拟登录自动寻找已请假的任务以及其核验二维码。

请求格式为

```
URL?account=账号&key=密码&school=学校
```

```bash
pip3 install -r ./src/requirements.txt -t ./src/ -i https://mirrors.aliyun.com/pypi/simple
```

