from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import requests
import re
import logging
import configparser

logger = logging.getLogger('django')
conf = configparser.ConfigParser()
conf.read('conf/lark.config')


def ding(tos, content):
    mtos = tos.split(",")
    for to in mtos:
        p1 = re.compile(r"^(.*)/(true|false)$")
        p2 = re.compile(r"^(.*)/((\d{11}/)*\d{11}/?)$")
        p3 = re.compile(r"^[^/]*")
        m1 = p1.fullmatch(to)
        m2 = p2.fullmatch(to)
        if m1:
            token = m1.group(1)
            at_all = m1.group(2)
            at = []
        elif m2:
            token = m2.group(1)
            at_all = "false"
            at = m2.group(2).split(",")
        else:
            token = p3.match(to).group()
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


def phone(tos, content):
    client = AcsClient(conf['phone']['ali.key'], conf['phone']['ali.secret'], 'default')
    ali_number = conf['phone']['ali.number']
    voice_template = conf['phone']['ali.voice.template']

    m = re.search(r'OK|PROBLEM', content)
    if m:
        message = m.group()
    else:
        message = ''

    def call(name):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dyvmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')
        request.set_version('2017-05-25')
        request.set_action_name('SingleCallByTts')

        request.add_query_param('RegionId', "default")
        request.add_query_param('CalledShowNumber', ali_number)
        request.add_query_param('CalledNumber', name)
        request.add_query_param('TtsCode', voice_template)
        request.add_query_param('TtsParam', {'name': '', 'message': message})

        response = client.do_action(request)
        logger.info("Call {!s}, msg={!s}, return={!s}".format(name, content, response))

    tos = tos.split(',')
    for number in tos:
        call(number)


# TODO
def mail(args):
    pass
