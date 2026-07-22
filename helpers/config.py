import os,json
def load(p='config.json'):
      if os.path.exists(p):
                with open(p) as f: return json.load(f)
                      return {}
        
