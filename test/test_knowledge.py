#!/usr/bin/env python3
"""
测试知识库是否正确加载和检索
"""

import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.knowledges.projects_csv_knowledge import project_knowledge_base
from src.knowledges.relationships_csv_knowledge import relationships_knowledge_base


def test_knowledge_base():
    """测试知识库功能"""
    print("=== 测试项目知识库 ===")

    # 测试项目知识库
    try:
        # 搜索李四的项目信息
        results = project_knowledge_base.search("李四")
        print(f"找到 {len(results)} 条关于李四的项目记录")

        for i, result in enumerate(results):
            print(f"结果 {i+1}:")
            print(f"  内容: {result.content}")
            print()

    except Exception as e:
        print(f"项目知识库搜索出错: {e}")

    print("\n=== 测试关系知识库 ===")

    # 测试关系知识库
    try:
        # 搜索李四的关系信息
        results = relationships_knowledge_base.search("李四")
        print(f"找到 {len(results)} 条关于李四的关系记录")

        for i, result in enumerate(results):
            print(f"结果 {i+1}:")
            print(f"  内容: {result.content}")
            print()

    except Exception as e:
        print(f"关系知识库搜索出错: {e}")


if __name__ == "__main__":
    test_knowledge_base()
