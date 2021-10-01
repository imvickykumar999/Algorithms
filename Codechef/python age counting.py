import requests
import numpy as np
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
l = (r.json()['data']).split(',')

count = 0
for i in l:
  if 'age' in i:
    if int(i.split('=')[1]) >= 50:
      count += 1
print(count)

# -------------------------------------

# https://coderbyte.com/editor/languagespecific:Python%20Age%20Counting/:candidate#useritphm1to7

# Python Age Counting
# In the Python file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/age-counting which contains a data key and the value is a string which contains items in the format: key=STRING, age=INTEGER. Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value.
#
# Example Input
# {"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}
#
# Example Output
# 2
