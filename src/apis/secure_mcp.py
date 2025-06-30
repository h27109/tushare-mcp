from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from .auth import verify_api_key, API_KEY

class SecureFastMCP(FastMCP):
    """
    带有Bearer认证的FastMCP服务器
    """
    
    def __init__(self, name: str):
        """
        初始化带有认证的MCP服务器
        
        Args:
            name: 服务器名称
        """
        super().__init__(name)
    
    def sse_app(self) -> FastAPI:
        """
        创建带有Bearer认证的SSE应用
        
        Returns:
            FastAPI: 带有认证的FastAPI应用
        """
        # 获取原始的SSE应用
        app = super().sse_app()
        
        # 为所有路由添加认证依赖
        for route in app.routes:
            if hasattr(route, "dependant"):
                route.dependant.dependencies.append(
                    {"callable": verify_api_key}
                )
        
        return app
    
    def streamable_http_app(self) -> FastAPI:
        """
        创建带有Bearer认证的Streamable HTTP应用
        
        Returns:
            FastAPI: 带有认证的FastAPI应用
        """
        # 获取原始的Streamable HTTP应用
        app = super().streamable_http_app()
        
        # 添加认证中间件
        @app.middleware("http")
        async def auth_middleware(request: Request, call_next):
            # 检查Authorization头
            auth_header = request.headers.get("Authorization")
            
            if not auth_header or not auth_header.startswith("Bearer "):
                return JSONResponse(
                    status_code=401,
                    content={"detail": "无效的认证凭据"},
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
            # 提取令牌
            token = auth_header.split(" ")[1]
            
            # 验证令牌
            if token != API_KEY:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "无效的认证凭据"},
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
            # 继续处理请求
            return await call_next(request)
        
        return app 