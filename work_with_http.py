import requests as req
import re

result = False
first_link = input()
get_link = req.get(first_link)


if get_link.status_code == 200:
    get_scnd_link = input()
    for link in re.findall(r"<a href=\"(.*)\"", get_link.text):
        res = req.get(link)
        if res.status_code == 200:
            for url in re.findall(r"<a href=\"(.*)\"", res.text):
                if get_scnd_link == url:
                    result = True
                    break
                if result:
                    break
else:
    result = False

if result:
    print('Yes')
else:
    print('No')