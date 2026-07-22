import hashlib,secrets
def sha256(d): return hashlib.sha256(d.encode()).hexdigest()
  def token(n=32): return secrets.token_hex(n)
    
