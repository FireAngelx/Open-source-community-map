import requests
# 令牌（待更新操作）
access_token = '5662eb1cc0adf5cdfb2a627128e1e8c6'
# 存放用户信息的数组
# member_info = []
# 获取成员信息的格式化字符串
format_get_member_info = 'https://gitee.com/api/v5/orgs/%s/members?access_token=%s&page=%d&per_page=100&role=all'
# 目标组织
organization = 'OpenHarmony'


# 获取组织内全部成员信息至member_info，并将成员信息输出至data.txt
def get_member_info(member_info):
    page = 1
    while 1:
        r = requests.get(format_get_member_info % (organization, access_token, page))
        r = eval(r.text)
        if len(r) == 0:
            break
        else:
            member_info += r
        page += 1
    print(len(member_info))
    f = open("data.txt", 'w')
    for member in member_info:
        f.write(str(member))
    f.close()