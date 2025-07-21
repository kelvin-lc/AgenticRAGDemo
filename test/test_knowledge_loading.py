#!/usr/bin/env python3
"""
测试知识库加载和搜索功能
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.knowledges.projects_csv_knowledge import project_knowledge_base
from src.knowledges.relationships_csv_knowledge import relationships_knowledge_base


def test_knowledge_loading():
    """测试知识库加载"""
    print("🔍 测试知识库加载...")

    try:
        # 测试项目知识库
        print("\n📊 项目知识库测试:")
        print(f"知识库类型: {type(project_knowledge_base)}")

        # 测试搜索功能
        print("\n🔎 搜索项目知识库中的'李四':")
        results = project_knowledge_base.search("李四")
        print(f"搜索结果数量: {len(results)}")

        if results:
            print("搜索结果:")
            for i, result in enumerate(results, 1):
                print(f"  {i}. {result}")
        else:
            print("  未找到相关结果")

        # 测试关系知识库
        print("\n🔗 关系知识库测试:")
        print(f"知识库类型: {type(relationships_knowledge_base)}")

        print("\n🔎 搜索关系知识库中的'李四':")
        results = relationships_knowledge_base.search("李四")
        print(f"搜索结果数量: {len(results)}")

        if results:
            print("搜索结果:")
            for i, result in enumerate(results, 1):
                print(f"  {i}. {result}")
        else:
            print("  未找到相关结果")

    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback

        traceback.print_exc()


def test_agent_knowledge_access():
    """测试智能体是否能访问知识库"""
    print("\n🤖 测试智能体知识库访问...")

    try:
        from src.agents.project_retrival_agent import get_project_agent

        # 创建项目智能体
        project_agent = get_project_agent()
        print(f"项目智能体创建成功: {project_agent.name}")
        print(f"知识库已附加: {project_agent.knowledge is not None}")

        if project_agent.knowledge:
            print(f"知识库类型: {type(project_agent.knowledge)}")
            print(f"搜索功能已启用: {project_agent.search_knowledge}")

    except Exception as e:
        print(f"❌ 智能体测试失败: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    print("🚀 开始知识库测试...")
    test_knowledge_loading()
    test_agent_knowledge_access()
    print("\n✅ 测试完成!")
