def padovan_r(in_,out_= ""):
  rules = {"A": "B", "B": "C", "C": "AB"}
  if (in_ == ""):
    return out_
  else:    
    out_ = rules[ in_[-1] ] + out_
    in_ = in_[:-1]
    return padovan_r(in_, out_)

def f_r(n, c=0, s="A"):
  if c == n:
    return s
  else:
    s = padovan_r(s)
    c = c + 1
    return f_r(n, c, s)
















def padovan_i(in_):
  out_ = ""
  rules = {"A": "B", "B": "C", "C": "AB"}
  while not(in_ == ""):
    out_ = rules[in_[-1]] + out_
    in_ = in_[:-1]
  return out_

def f_i(n):
  c = 0
  s = "A"
  while not(c == n):
    s = padovan_i(s)
    c = c + 1
  return s
