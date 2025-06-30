from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取API密钥，如果环境变量不存在，则使用默认值
API_KEY = os.getenv("MCP_API_KEY", "default_api_key")

# 创建HTTP Bearer安全方案
security = HTTPBearer()

async def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    验证Bearer令牌是否有效
    """
    print(f"收到认证请求，完整HTTP头域:")
    for header_name, header_value in credentials.scheme.items():
        print(f"  {header_name}: {header_value}")
    print(f"Bearer令牌: {credentials.credentials}")
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的认证凭据",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials 