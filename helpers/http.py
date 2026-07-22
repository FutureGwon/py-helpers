import urllib.request,json
def get_json(url):
      with urllib.request.urlopen(url) as r: return json.loads(r.read())
        
