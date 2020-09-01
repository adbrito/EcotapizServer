import json
import math

def request_todict(request):
    try:
        body = request.body.decode('utf-8')
        body = json.loads(body)
        return body
    except:
        return {}