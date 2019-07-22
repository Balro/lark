import requests
import re
import logging

logger = logging.getLogger('django')


def dingding(tos, content):
    p1 = re.compile(r"^(.*)/(true|false)$")
    p2 = re.compile(r"^(.*)/((\d{11},)*\d{11},?)$")
    p3 = re.compile(r"^[^/]*")
    m1 = p1.fullmatch(tos)
    m2 = p2.fullmatch(tos)
    if m1:
        token = m1.group(1)
        at_all = m1.group(2)
        at = []
    elif m2:
        token = m2.group(1)
        at_all = "false"
        at = m2.group(2).split(",")
    else:
        token = p3.match(tos).group()
        at_all = "false"
        at = ""
    url = "https://oapi.dingtalk.com/robot/send?access_token=" + token
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": at,
            "isAtAll": at_all,
        }
    }
    req = requests.post(url, headers=headers, json=data)
    logger.info("Send to ding: data={!s}, return={!s}".format(data, req.text))


# TODO
def phone(args):
    pass


# TODO
def mail(args):
    pass
