import time
import sys
import requests

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf

if(__name__=="__main__"):
    stdin_values = get_stdin()
    res = requests.post("http://gateway:8080/function/func_star", json={})
    print(res)
