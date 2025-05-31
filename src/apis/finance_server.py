from mcp.server.fastmcp import FastMCP

from .finance import *

mcp = FastMCP('tushare_finance_server')

@mcp.tool(name = 'income', description = income_wrapper.__doc__)
def income(ts_code,ann_date = '', f_ann_date='',start_date='',end_date='',report_type='',period='',comp_type=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return income_wrapper(params)

@mcp.tool(name = 'balancesheet', description = balancesheet_wrapper.__doc__)
def balancesheet(ts_code,ann_date = '', f_ann_date='',start_date='',end_date='',report_type='',period='',comp_type=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return balancesheet_wrapper(params)


@mcp.tool(name = 'cashflow', description = cashflow_wrapper.__doc__)
def cashflow(ts_code,ann_date = '', f_ann_date='',start_date='',end_date='',report_type='',period='',comp_type='', is_calc=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return cashflow_wrapper(params)


@mcp.tool(name = 'forecast', description = forecast_wrapper.__doc__)
def forecast(ts_code,ann_date = '', start_date='',end_date='',period=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return forecast_wrapper(params)


@mcp.tool(name = 'express', description = express_wrapper.__doc__)
def express(ts_code,ann_date = '',start_date='',end_date='',period=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return express_wrapper(params)


@mcp.tool(name = 'dividend', description = dividend_wrapper.__doc__)
def dividend(ts_code,ann_date = '', record_date='',ex_date='',imp_ann_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return dividend_wrapper(params)


@mcp.tool(name = 'fina_indicator', description = fina_indicator_wrapper.__doc__)
def fina_indicator(ts_code,ann_date = '',start_date='',end_date='',period=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fina_indicator_wrapper(params)


@mcp.tool(name = 'fina_mainbz', description = fina_mainbz_wrapper.__doc__)
def fina_mainbz(ts_code,period='',type='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return fina_mainbz_wrapper(params)


@mcp.tool(name = 'disclosure_date', description = disclosure_date_wrapper.__doc__)
def disclosure_date(ts_code,end_date='',pre_date='',actual_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return disclosure_date_wrapper(params)
