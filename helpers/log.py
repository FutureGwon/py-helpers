import logging
def get_logger(n):
      l=logging.getLogger(n);l.setLevel(logging.INFO)
      return l
  
