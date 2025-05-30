import sys
sys.path.append('..')
from src.apis.finance_server import *

if __name__ == '__main__':
    # 测试 income 接口  
    print("测试 income 接口:")
    print(income(ts_code='300130.SZ', ann_date='', f_ann_date='', start_date='', end_date='', report_type='', period='', comp_type=''))
    
    # 测试 balancesheet 接口
    print("\n测试 balancesheet 接口:")
    print(balancesheet(ts_code='300130.SZ', ann_date='', f_ann_date='', start_date='', end_date='', report_type='', period='', comp_type=''))
    
    # 测试 cashflow 接口
    print("\n测试 cashflow 接口:")
    print(cashflow(ts_code='300130.SZ', ann_date='', f_ann_date='', start_date='', end_date='', report_type='', period='', comp_type='', is_calc=''))
    
    # 测试 forecast 接口
    print("\n测试 forecast 接口:")
    print(forecast(ts_code='300130.SZ', ann_date='', start_date='', end_date='', period=''))
    
    # 测试 express 接口
    print("\n测试 express 接口:")
    print(express(ts_code='300130.SZ', ann_date='', start_date='', end_date='', period=''))
    
    # 测试 dividend 接口
    print("\n测试 dividend 接口:")  
    print(dividend(ts_code='300130.SZ', ann_date='', record_date='', ex_date='', imp_ann_date=''))
    
    # 测试 fina_indicator 接口
    print("\n测试 fina_indicator 接口:")
    print(fina_indicator(ts_code='300130.SZ', ann_date='', start_date='', end_date='', period=''))
    
    # 测试 fina_mainbz 接口
    print("\n测试 fina_mainbz 接口:")
    print(fina_mainbz(ts_code='300130.SZ', period='', type='', start_date='', end_date=''))
    
    # 测试 disclosure_date 接口
    print("\n测试 disclosure_date 接口:")
    print(disclosure_date(ts_code='300130.SZ', end_date='', pre_date='', actual_date=''))