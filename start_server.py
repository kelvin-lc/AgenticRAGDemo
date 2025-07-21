#!/usr/bin/env python3
"""
启动Agentic RAG Demo服务器
"""

import uvicorn
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

if __name__ == "__main__":
    print("🚀 启动Agentic RAG Demo服务器...")
    print("📍 服务地址: http://localhost:8001")
    print("📚 API文档: http://localhost:8001/docs")
    print("🏥 健康检查: http://localhost:8001/ping")
    print("=" * 50)

    uvicorn.run(
        "src.main:app", host="0.0.0.0", port=8001, reload=True, log_level="info"
    )
