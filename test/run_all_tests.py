#!/usr/bin/env python3
"""
运行所有测试
"""

import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def run_all_tests():
    """运行所有测试"""
    print("🚀 开始运行所有测试...\n")

    # 测试CSV数据
    print("=" * 50)
    print("📊 测试CSV数据")
    print("=" * 50)
    try:
        from test_csv_data import test_csv_reading

        test_csv_reading()
        print("✅ CSV数据测试通过\n")
    except Exception as e:
        print(f"❌ CSV数据测试失败: {e}\n")

    # 测试知识库
    print("=" * 50)
    print("🧠 测试知识库")
    print("=" * 50)
    try:
        from test_knowledge import test_knowledge_base

        test_knowledge_base()
        print("✅ 知识库测试通过\n")
    except Exception as e:
        print(f"❌ 知识库测试失败: {e}\n")

    # 测试Agent团队
    print("=" * 50)
    print("🤖 测试Agent团队")
    print("=" * 50)
    try:
        from test_agent_team import test_agent_team

        test_agent_team()
        print("✅ Agent团队测试通过\n")
    except Exception as e:
        print(f"❌ Agent团队测试失败: {e}\n")

    print("🎉 所有测试完成!")


if __name__ == "__main__":
    run_all_tests()
