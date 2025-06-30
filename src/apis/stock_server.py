from .secure_mcp import SecureFastMCP
from pandas import DataFrame
from .stock import *

"""
股票数据查询服务器
"""
mcp = SecureFastMCP('tushare_stock_server')

@mcp.tool(name = 'stock_basic', description = stock_basic_wrapper.__doc__)
def stock_basic(ts_code,name='',exchange='',market='',is_hs='',list_status='') -> DataFrame:
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return stock_basic_wrapper(params)

@mcp.tool(name = 'stock_company', description = stock_company_wrapper.__doc__)
def stock_company(ts_code='',exchange=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return stock_company_wrapper(params)

@mcp.tool(name = 'stk_managers', description = stk_managers_wrapper.__doc__)
def stk_managers(ts_code='',ann_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return stk_managers_wrapper(params)

@mcp.tool(name = 'daily', description = daily_wrapper.__doc__)
def daily(ts_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return daily_wrapper(params)

@mcp.tool(name = 'rt_k', description = rt_k_wrapper.__doc__)
def rt_k(ts_code):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return rt_k_wrapper(params)

@mcp.tool(name = 'weekly', description = weekly_wrapper.__doc__)
def weekly(ts_code='',trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return weekly_wrapper(params)

@mcp.tool(name = 'monthly', description = monthly_wrapper.__doc__)
def monthly(ts_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return monthly_wrapper(params)

@mcp.tool(name = 'daily_basic', description = daily_basic_data_wrapper.__doc__)
def daily_basic_data(ts_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return daily_basic_data_wrapper(params)

@mcp.tool(name = 'top10_holders', description = top10_holders_wrapper.__doc__)
def top10_holders(ts_code ,period='',ann_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return top10_holders_wrapper(params)

@mcp.tool(name = 'top10_floatholders', description = top10_floatholders_wrapper.__doc__)
def top10_floatholders(ts_code='',period='',ann_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return top10_floatholders_wrapper(params)

@mcp.tool(name = 'stk_holdernumber', description = stk_holdernumber_wrapper.__doc__)
def stk_holdernumber(ts_code,ann_date='',enddate='',startdate=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return stk_holdernumber_wrapper(params)

@mcp.tool(name = 'stock_moneyflow', description = stock_moneyflow_wrapper.__doc__)
def stock_moneyflow(ts_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return stock_moneyflow_wrapper(params)
