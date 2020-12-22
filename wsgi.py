'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-08 16:24:10 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-09 00:17:20
 */
'''
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from app import create_app

app = create_app('production')