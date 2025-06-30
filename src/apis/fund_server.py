from .secure_mcp import SecureFastMCP

from .fund import *

mcp = SecureFastMCP('tushare_fund_server')

@mcp.tool(name = 'fund_basic', description = fund_basic_wrapper.__doc__)
def fund_basic(ts_code, market='',status=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fund_basic_wrapper(params)

@mcp.tool(name = 'fund_company', description = fund_company_wrapper.__doc__)
def fund_company():
    return fund_company_wrapper()

@mcp.tool(name = 'fund_manager', description = fund_manager_wrapper.__doc__)
def fund_manager(ts_code, ann_date='', name='', offset=0, limit=5000):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fund_manager_wrapper(params)

@mcp.tool(name = 'fund_share', description = fund_share_wrapper.__doc__)
def fund_share(ts_code, trade_date='', start_date='', end_date='', market=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fund_share_wrapper(params)

@mcp.tool(name = 'fund_nav', description = fund_nav_wrapper.__doc__)
def fund_nav(ts_code, nav_date='', market='', start_date='', end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fund_nav_wrapper(params)

@mcp.tool(name = 'fund_div', description = fund_div_wrapper.__doc__)
def fund_div(ts_code, ann_date='', ex_date='', pay_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fund_div_wrapper(params)


@mcp.tool(name = 'fund_portfolio', description = fund_portfolio_wrapper.__doc__)
def fund_portfolio(ts_code, symbol='', ann_date='', period='', start_date='', end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fund_portfolio_wrapper(params)

@mcp.tool(name = 'fund_daily', description = fund_daily_wrapper.__doc__)
def fund_daily(ts_code, trade_date='', start_date='', end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fund_daily_wrapper(params)

@mcp.tool(name = 'fund_adj', description = fund_adj_wrapper.__doc__)
def fund_adj(ts_code, trade_date='', start_date='', end_date='', offset=0, limit=2000):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fund_adj_wrapper(params)





