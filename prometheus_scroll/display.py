import sys
import time
import urllib

import requests

from pixel_display import output_display

output_display1 = output_display()
promServer = sys.argv[1]
ql = {"query": 'increase(gateway_function_invocation_total{code="200",function_name="func_star",instance="gateway:8080",job="gateway"}[30m])'}
promQL = promServer + "/api/v1/query?" + urllib.urlencode(ql)
print(promQL)
def get_total(url):
    res = requests.get(url)
    value = 0
    if res.status_code == 200:
        body = res.json()
        result = body["data"]["result"][0]
        value = int(float(result["value"][1]))
    return value
# {"status":"success","data":{"resultType":"vector","result":[{"metric":{"code":"200","function_name":"func_star","instance":"gateway:8080","job":"gateway"},"value":[1490905920.588,"7.027828387096775"]}]}}
# {"status":"success","data":{"resultType":"vector","result":[{"metric":{"code":"200","function_name":"func_github_redis_updater","instance":"gateway:8080","job":"gateway"},"value":[1490903389.818,"1.0027855153203342"]}]}}
while(True):
    total = get_total(promQL)
    output_display1.display(total)
    time.sleep(5)
