from .secure_mcp import SecureFastMCP

from .macro_china import *

mcp = SecureFastMCP('tushare_macro_china_server')

@mcp.tool(name = 'shibor', description = shibor_wrapper.__doc__)
def shibor(date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return shibor_wrapper(params)

@mcp.tool(name = 'shibor_quote', description = shibor_quote_wrapper.__doc__)
def shibor_quote(date='',start_date='',end_date='',bank=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return shibor_quote_wrapper(params)

@mcp.tool(name = 'shibor_lpr', description = shibor_lpr_wrapper.__doc__)
def shibor_lpr(date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return shibor_lpr_wrapper(params)

@mcp.tool(name = 'libor', description = libor_wrapper.__doc__)
def libor(date='',start_date='',end_date='',curr_type=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return libor_wrapper(params)

@mcp.tool(name = 'hibor', description = hibor_wrapper.__doc__)
def hibor(date='',start_date='',end_date=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return hibor_wrapper(params)

@mcp.tool(name = 'cn_gdp', description = cn_gdp_wrapper.__doc__)
def cn_gdp(q='',start_q='',end_q='',fields=''):
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return cn_gdp_wrapper(params)

@mcp.tool(name = 'cn_cpi', description = cpi_wrapper.__doc__)
def cn_cpi(m='',start_m='',end_m=''):  
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return cpi_wrapper(params)

@mcp.tool(name = 'cn_ppi', description = ppi_wrapper.__doc__)
def cn_ppi(m='',start_m='',end_m=''):  
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return ppi_wrapper(params)

@mcp.tool(name = 'cn_m', description = cn_m_wrapper.__doc__)
def cn_m(m='',start_m='',end_m='',fields=''):  
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return cn_m_wrapper(params)

@mcp.tool(name = 'sf_month', description = sf_month_wrapper.__doc__)
def sf_month(m='',start_m='',end_m=''):  
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return sf_month_wrapper(params)

@mcp.tool(name = 'cn_pmi', description = cn_pmi_wrapper.__doc__)
def cn_pmi(m='',start_m='',end_m='',fields=''):  
    params = {k: v for k, v in locals().items() if k != '__doc__' and v != ''}
    return cn_pmi_wrapper(params)

