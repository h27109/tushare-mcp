import sys
sys.path.append('..')
from src.apis.stock_index_server import *

if __name__ == "__main__":
    # 测试 index_basic 接口
    print("测试 index_basic 接口:")
    print(index_basic(ts_code='000001.SH'))  # 上证指数
    
    # 测试 index_daily 接口
    print("\n测试 index_daily 接口:")
    print(index_daily(ts_code='000001.SH', trade_date='20250516'))
    
    # 测试 index_weekly 接口
    print("\n测试 index_weekly 接口:")
    print(index_weekly(ts_code='000001.SH', start_date='20250101', end_date='20250516'))
    
    # 测试 index_monthly 接口
    print("\n测试 index_monthly 接口:")
    print(index_monthly(ts_code='000001.SH', start_date='20250101', end_date='20250516'))
    
    # 测试 index_weight 接口
    print("\n测试 index_weight 接口:")
    print(index_weight(index_code='000001.SH', trade_date='20250516'))
    
    # 测试 index_daily_basic 接口
    print("\n测试 index_daily_basic 接口:")
    print(index_daily_basic(ts_code='000001.SH', trade_date='20250516'))
    
    # 测试 index_global 接口
    print("\n测试 index_global 接口:")
    print(index_global(ts_code='XIN9', trade_date='20250516'))
    
    # 测试 index_daily_info 接口
    print("\n测试 index_daily_info 接口:")
    print(index_daily_info(trade_date='20250516', ts_code='000001.SH'))
    
    # 测试 sz_daily_info 接口
    print("\n测试 sz_daily_info 接口:")
    print(sz_daily_info(trade_date='20250516', ts_code='主板A股'))  # 深证成指
