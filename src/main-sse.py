import multiprocessing
import sys
import os
import uvicorn
from dotenv import load_dotenv
import importlib

# 提前导入所有可能的MCP服务
from apis import *

load_dotenv()

def run_mcp_server(service_name, module_path, instance_name, port):
    """在指定端口运行 MCP 服务的 ASGI 应用"""
    print(f"启动 {service_name} 服务，端口: {port}")
    
    # 动态导入模块
    module = __import__(module_path, fromlist=[instance_name])
    importlib.reload(module)  # 确保重新加载
    
    # 获取实例
    mcp_instance = getattr(module, instance_name)
    
    # 获取 ASGI 应用并运行
    app = mcp_instance.sse_app()
    uvicorn.run(app, host="0.0.0.0", port=port)

def main():
    # 配置服务和端口
    services = [
        {"name": "股票数据查询服务", "module": "apis", "instance": "stock_mcp", "port": 8000},
        {"name": "公司财务数据查询服务", "module": "apis", "instance": "finance_mcp", "port": 8001},
        {"name": "股票指数数据查询服务", "module": "apis", "instance": "stock_index_mcp", "port": 8002},
        {"name": "基金数据查询服务", "module": "apis", "instance": "fund_mcp", "port": 8003},
        {"name": "中国宏观数据查询服务", "module": "apis", "instance": "macro_china_mcp", "port": 8004},
        {"name": "国际宏观数据查询服务", "module": "apis", "instance": "macro_international_mcp", "port": 8005}
    ]
    
    # 为每个服务创建一个进程
    processes = []
    for service in services:
        process = multiprocessing.Process(
            target=run_mcp_server,
            args=(service["name"], service["module"], service["instance"], service["port"]),
            daemon=True
        )
        processes.append(process)
        process.start()
        print(f"已启动 {service['name']} 服务进程")
    
    # 打印服务信息
    print("\n服务已启动，可通过以下地址访问：")
    for service in services:
        print(f"{service['name']}: http://localhost:{service['port']}")
    
    try:
        # 等待所有进程完成
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print("\n接收到中断信号，正在停止...")

if __name__ == '__main__':
    print("MCP多服务启动")
    main()

