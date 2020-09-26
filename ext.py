from bs4 import BeautifulSoup as bsoap
import re
import os
from os import path
import shutil
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from nsepy import get_history
from datetime import date
import pandas as pd
import numpy as np
import pickle as pck
import os
import re
import os
k=[]
os.chdir('/home/sahil/fundamentals8')
with open('key_financial_ratios','rb') as f:
  try:
      while True:
        k.append(pck.load(f))
  except EOFError:
        pass

