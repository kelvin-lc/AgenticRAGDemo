#!/usr/bin/env python3
"""
测试完整的团队流程
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.teams.leader import get_agentic_rag_team


def test_team_flow():
    """测试团队流程"""
    print("🚀 开始团队流程测试...")

    try:
        # 创建团队
        print("\n🤖 创建Agentic RAG团队...")
        team = get_agentic_rag_team(user_id="test_user", session_id="test_session")
        print(f"团队创建成功: {team.name}")
        print(f"团队成员数量: {len(team.members)}")

        # 测试查询
        query = "李四的项目名称是什么"
        print(f"\n🔍 测试查询: {query}")

        # 运行团队
        print("\n⚡ 开始团队协作...")
        response = team.run(query)

        print(f"\n📝 团队响应:")
        print(f"响应内容: {response.content}")
        print(f"响应类型: {type(response)}")

        # 检查是否包含具体答案
        if "李四" in response.content and (
            "项目" in response.content
            or "智能客服系统" in response.content
            or "移动端应用" in response.content
        ):
            print("\n✅ 测试成功！团队返回了关于李四项目的具体信息")
        else:
            print("\n❌ 测试失败！团队没有返回关于李四项目的具体信息")
            print(f"实际响应: {response.content}")

    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback

        traceback.print_exc()


def test_simple_query():
    """测试简单查询"""
    print("\n🔍 测试简单查询...")

    try:
        team = get_agentic_rag_team()

        # 测试多个查询
        queries = ["李四在哪里项目", "张三参与了哪些项目", "王五的项目信息"]

        for i, query in enumerate(queries, 1):
            print(f"\n--- 查询 {i}: {query} ---")
            response = team.run(query)
            print(f"响应: {response.content[:200]}...")

    except Exception as e:
        print(f"❌ 简单查询测试失败: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_team_flow()
    test_simple_query()
    print("\n✅ 所有测试完成!")
