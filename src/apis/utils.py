from mcp.server.fastmcp import FastMCP
from datetime import datetime

"""
时间工具
"""
mcp = FastMCP('time_utils')

@mcp.tool(name = 'get_current_time', description = "获取当前时间")
def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
