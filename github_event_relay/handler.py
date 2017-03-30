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
    
    # stdin_values includes the event from Github, you can inspect it and decide what to do.
    # - the event could be a new subscriber (watcher), fork or a star, so you may want to break this down
    
    # Here we're calling into another function called "star" which exists to help us track which events were stars
    # later on.
    res = requests.post("http://gateway:8080/function/func_star", json={})
    
    print(res)
