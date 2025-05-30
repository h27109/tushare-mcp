import sys

import uvicorn
sys.path.append('..')
from src.apis.stock_server import *

if __name__ == "__main__":
    #测试 stock_basic 接口
    print("测试 stock_basic 接口:")
    print(stock_basic(ts_code='300130.SZ'))
    

    # 测试 stock_company 接口
    print("\n测试 stock_company 接口:")
    print(stock_company(ts_code='300130.SZ'))
    
    # 测试 stk_managers 接口
    print("\n测试 stk_managers 接口:")
    print(stk_managers(ts_code='300130.SZ'))
    
    # 测试 daily 接口
    print("\n测试 daily 接口:")
    print(daily(ts_code='300130.SZ', trade_date='20250516'))
    
    # 测试 rt_k 接口
    print("\n测试 rt_k 接口:")
    print(rt_k(ts_code='300130.SZ'))
    
    # 测试 weekly 接口
    print("\n测试 weekly 接口:")
    print(weekly(ts_code='300130.SZ', start_date='20250101', end_date='20250516'))
    
    # 测试 monthly 接口
    print("\n测试 monthly 接口:")
    print(monthly(ts_code='300130.SZ', start_date='20250101', end_date='20250516'))

    # 测试 daily_basic 接口
    print("\n测试 daily_basic 接口:")
    print(daily_basic_data(ts_code='300130.SZ', trade_date='20250516'))

    # 测试 top10_holders 接口
    print("\n测试 top10_holders 接口:")
    print(top10_holders(ts_code='300130.SZ'))

    # 测试 top10_floatholders 接口
    print("\n测试 top10_floatholders 接口:")
    print(top10_floatholders(ts_code='300130.SZ'))

    # 测试 stk_holdernumber 接口
    print("\n测试 stk_holdernumber 接口:")
    print(stk_holdernumber(ts_code='300130.SZ'))

    # 测试 moneyflow 接口
    print("\n测试 moneyflow 接口:")
    print(stock_moneyflow(ts_code='300130.SZ'))

        
