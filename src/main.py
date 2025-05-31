import uvicorn
from dotenv import load_dotenv
import contextlib
from fastapi import FastAPI
import logging
load_dotenv(override=True)

from apis import stock_mcp, finance_mcp, stock_index_mcp, fund_mcp, macro_china_mcp, macro_international_mcp, time_utils_mcp

from youtebe_subtitles import youtebe_subtitles_mcp

def main():
    services = [
        {"name":"stock",                "mcp": stock_mcp, "description": "股票数据查询服务"},
        {"name":"finance",              "mcp": finance_mcp, "description": "公司财务数据查询服务"},
        {"name":"stock_index",          "mcp": stock_index_mcp, "description": "股票指数数据查询服务"},
        {"name":"fund",                 "mcp": fund_mcp, "description": "基金数据查询服务"},
        {"name":"macro_china",          "mcp": macro_china_mcp, "description": "中国宏观数据查询服务"},
        {"name":"macro_international",  "mcp": macro_international_mcp, "description": "国际宏观数据查询服务"},
        {"name":"time",                 "mcp": time_utils_mcp, "description": "时间工具"},
        {"name":"youtebe_subtitles",    "mcp": youtebe_subtitles_mcp, "description": "youtebe视频字幕查询服务"}
    ]
    @contextlib.asynccontextmanager
    async def lifespan(app: FastAPI):
        async with contextlib.AsyncExitStack() as stack:
            for service in services:
                await stack.enter_async_context(service['mcp'].session_manager.run())
            yield

    app = FastAPI(lifespan=lifespan)

    # 添加各个server的路由。
    # 客户端配置的时候，url=http://ip:8000/{name}/mcp，如http://127.0.0.1:8000/stock/mcp
    for service in services:
        app.mount(f"/{service['name']}", service['mcp'].streamable_http_app())

    logging.basicConfig(
        level=logging.DEBUG,  # 设置日志级别
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),  # 输出到控制台
            logging.FileHandler('mcp.log')  # 输出到文件
        ]
    )
    #logger = logging.getLogger("mcp")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == '__main__':
    print("MCP app启动")
    main()

