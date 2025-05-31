from mcp.server.fastmcp import FastMCP

from .macro_international import *

mcp = FastMCP('tushare_macro_international_server')

@mcp.tool(name = 'us_tycr', description = us_tycr_wrapper.__doc__)
def us_tycr(date='',start_date='',end_date='',fields=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return us_tycr_wrapper(params)

@mcp.tool(name = 'us_trycr', description = us_trycr_wrapper.__doc__)
def us_trycr(date='',start_date='',end_date='',fields=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return us_trycr_wrapper(params)

@mcp.tool(name = 'us_tbr', description = us_tbr_wrapper.__doc__)
def us_tbr(date='',start_date='',end_date='',fields=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return us_tbr_wrapper(params)

@mcp.tool(name = 'us_tltr', description = us_tltr_wrapper.__doc__)
def us_tltr(date='',start_date='',end_date='',fields=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return us_tltr_wrapper(params)

@mcp.tool(name = 'us_trltr', description = us_trltr_wrapper.__doc__)
def us_trltr(date='',start_date='',end_date='',fields=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return us_trltr_wrapper(params)