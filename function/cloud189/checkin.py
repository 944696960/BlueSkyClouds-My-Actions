import requests

cookies = {
    'apm_ct': '20210811223811619',
    'apm_ip': '84C6C75AF24B2DA68BFE666EA2616A41',
    'apm_sid': 'E77AFC9AD0263B7DF408A9CF33750721',
    'apm_ua': 'CB1E39D6CD2B969C34B0A2CC0B0B2008',
    'apm_uid': 'D728053A4B076A72E2837D5FBA212891',
    'COOKIE_LOGIN_USER': '66DF1CAA089B94B92D7BC259C3D09366019B3B10F9A6A8D595E4900B81D6B05966FD77478A6211D8CB7E51D5F69C8B8D379FFA3DA5C7E099416909A7',
    'JSESSIONID': 'aaacYOjAL0WA75SxppaMx',
}

headers = {
    'Host': 'm.cloud.189.cn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Ecloud/8.9.4 iOS/14.2 clientId/AFEDEC7B-5907-4320-9FDA-B1A1C100D959 clientModel/iPhone proVersion/1.0.5',
    'Referer': 'https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=0',
    'Accept-Language': 'zh-cn',
    'X-Requested-With': 'XMLHttpRequest',
}

params = (
    ('taskId', 'TASK_SIGNIN'),
    ('activityId', 'ACT_SIGNIN'),
    ('noCache', '0.20524460452901994'),
)

response = requests.get('https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action', headers=headers, params=params, cookies=cookies)

