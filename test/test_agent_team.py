#!/usr/bin/env python3
"""
测试Agent团队功能
"""

from src.teams.leader import get_agentic_rag_team


def test_agent_team():
    """测试Agent团队功能"""
    print("=== 测试Agent团队创建 ===")

    try:
        # 创建Agent团队
        team = get_agentic_rag_team()
        print("✅ Agent团队创建成功")
        print(f"团队名称: {team.name}")
        print(f"团队模式: {team.mode}")
        print(f"团队成员数量: {len(team.members)}")

        # 列出团队成员
        print("\n团队成员:")
        for i, member in enumerate(team.members):
            print(f"  {i+1}. {member.name} ({member.agent_id})")

    except Exception as e:
        print(f"❌ Agent团队创建失败: {e}")


def test_team_query():
    """测试团队查询功能"""
    print("\n=== 测试团队查询 ===")

    try:
        # 创建Agent团队
        team = get_agentic_rag_team()

        # 测试查询
        query = "李四在哪里项目"
        print(f"查询: {query}")

        # 运行查询
        response = team.run(query)
        print(f"响应: {response.content}")

    except Exception as e:
        print(f"❌ 团队查询失败: {e}")


if __name__ == "__main__":
    test_agent_team()
    test_team_query()
