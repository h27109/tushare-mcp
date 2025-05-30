from mcp.server.fastmcp import FastMCP

from .stock_index import *

mcp = FastMCP('tushare_stock_index_server')

@mcp.tool(name = 'index_basic', description = index_basic_wrapper.__doc__)
def index_basic(ts_code,name='',market='',publisher='',category=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return index_basic_wrapper(params)

@mcp.tool(name = 'index_daily', description = index_daily_wrapper.__doc__)
def index_daily(ts_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return index_daily_wrapper(params)

@mcp.tool(name = 'index_weekly', description = index_weekly_wrapper.__doc__)
def index_weekly(ts_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return index_weekly_wrapper(params)

@mcp.tool(name = 'index_monthly', description = index_monthly_wrapper.__doc__)
def index_monthly(ts_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return index_monthly_wrapper(params)

@mcp.tool(name = 'index_weight', description = index_weight_wrapper.__doc__)
def index_weight(index_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return index_weight_wrapper(params)

@mcp.tool(name = 'index_daily_basic', description = index_daily_basic_wrapper.__doc__)
def index_daily_basic(ts_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return index_daily_basic_wrapper(params)

@mcp.tool(name = 'index_global', description = index_global_wrapper.__doc__)
def index_global(ts_code,trade_date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return index_global_wrapper(params)

@mcp.tool(name = 'index_daily_info', description = index_daily_info_wrapper.__doc__)
def index_daily_info(trade_date='',ts_code='',exchange='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return index_daily_info_wrapper(params)

@mcp.tool(name = 'sz_daily_info', description = sz_daily_info_wrapper.__doc__)
def sz_daily_info(trade_date='',ts_code='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return sz_daily_info_wrapper(params)



