import os,json,re
def read_json(p):
      with open(p) as f: return json.load(f)
        def slugify(t):
              return re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')
          
