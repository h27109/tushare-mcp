# Tushare MCP 服务器

这是一个基于MCP (Model Context Protocol)协议的Tushare数据服务器，提供股票、基金、宏观经济等金融数据查询服务。

## 功能

- 股票数据查询服务
- 公司财务数据查询服务
- 股票指数数据查询服务
- 基金数据查询服务
- 中国宏观数据查询服务
- 国际宏观数据查询服务

## 安装

```bash
# 安装依赖
pip install -r requirements.txt
```

## 配置

在项目根目录创建`.env`文件，设置以下环境变量：

```
# MCP服务器API密钥
MCP_API_KEY=your_secret_api_key_here
```

## 运行

```bash
# 运行SSE服务器
python src/main-sse.py
```

## API认证

所有API请求都需要使用Bearer认证。在请求头中添加以下内容：

```
Authorization: Bearer your_secret_api_key_here
```

## 示例

使用curl发送请求：

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_secret_api_key_here" \
  -d '{"method":"stock_basic","params":{"ts_code":"000001.SZ"}}'
```

## 服务列表

- 股票数据查询服务: http://localhost:8000
- 公司财务数据查询服务: http://localhost:8001
- 股票指数数据查询服务: http://localhost:8002
- 基金数据查询服务: http://localhost:8003
- 中国宏观数据查询服务: http://localhost:8004
- 国际宏观数据查询服务: http://localhost:8005
