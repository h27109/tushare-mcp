import os

# 导入tushare
import tushare as ts

tushare_api_key = os.environ.get('TUSHARE_API_KEY')
# 初始化pro接口
pro = ts.pro_api(tushare_api_key)