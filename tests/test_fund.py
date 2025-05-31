import sys
sys.path.append('..')
from src.apis.fund_server import *

if __name__ == "__main__":
    test_fund_code = '510300.SH'  # 沪深300ETF
    
    # 测试 fund_basic 接口
    print("测试 fund_basic 接口:")
    print(fund_basic(ts_code=test_fund_code, market='E'))  # E表示场内基金
    
    # 测试 fund_company 接口
    print("\n测试 fund_company 接口:")
    print(fund_company())  # 获取所有基金公司信息
    
    # 测试 fund_manager 接口
    print("\n测试 fund_manager 接口:")
    print(fund_manager(ts_code=test_fund_code))
    
    # 测试 fund_share 接口
    print("\n测试 fund_share 接口:")
    print(fund_share(ts_code=test_fund_code, 
                    start_date='20250101', 
                    end_date='20250516',
                    market='SH'))
    
    # 测试 fund_nav 接口
    print("\n测试 fund_nav 接口:")
    print(fund_nav(ts_code=test_fund_code, 
                  start_date='20250101',
                  end_date='20250516',
                  market='E'))
    
    # 测试 fund_div 接口
    print("\n测试 fund_div 接口:")
    print(fund_div(ts_code=test_fund_code))
    
    # 测试 fund_portfolio 接口
    print("\n测试 fund_portfolio 接口:")
    print(fund_portfolio(ts_code=test_fund_code,
                        period='20250331'))  # 测试2025年一季度的持仓
    
    # 测试 fund_daily 接口
    print("\n测试 fund_daily 接口:")
    print(fund_daily(ts_code=test_fund_code,
                    start_date='20250101',
                    end_date='20250516'))
    
    # 测试 fund_adj 接口
    print("\n测试 fund_adj 接口:")
    print(fund_adj(ts_code=test_fund_code,
                  start_date='20250101',
                  end_date='20250516')) 