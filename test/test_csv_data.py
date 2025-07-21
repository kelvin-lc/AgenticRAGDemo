#!/usr/bin/env python3
"""
测试CSV文件数据读取
"""

import pandas as pd
from pathlib import Path


def test_csv_reading():
    """测试CSV文件读取"""
    current_dir = Path(__file__).parent.parent / "src" / "knowledges"

    print("=== 测试项目数据CSV ===")
    try:
        projects_df = pd.read_csv(current_dir / "projects_data.csv")
        print(f"项目数据形状: {projects_df.shape}")
        print("列名:", list(projects_df.columns))

        # 查找李四的数据
        lisi_data = projects_df[projects_df["name"] == "李四"]
        print(f"\n找到李四的记录数: {len(lisi_data)}")
        if len(lisi_data) > 0:
            print("李四的项目信息:")
            for _, row in lisi_data.iterrows():
                print(
                    f"  - {row['项目名称']} ({row['project_id']}) - {row['role_in_project']}"
                )
        else:
            print("未找到李四的数据")

    except Exception as e:
        print(f"读取项目数据出错: {e}")

    print("\n=== 测试关系数据CSV ===")
    try:
        relationships_df = pd.read_csv(current_dir / "relationships_data.csv")
        print(f"关系数据形状: {relationships_df.shape}")
        print("列名:", list(relationships_df.columns))

        # 查找李四的关系
        lisi_relations = relationships_df[
            (relationships_df["person_a_name"] == "李四")
            | (relationships_df["person_b_name"] == "李四")
        ]
        print(f"\n找到李四的关系记录数: {len(lisi_relations)}")
        if len(lisi_relations) > 0:
            print("李四的关系信息:")
            for _, row in lisi_relations.iterrows():
                if row["person_a_name"] == "李四":
                    other_person = row["person_b_name"]
                else:
                    other_person = row["person_a_name"]
                print(f"  - 与{other_person}的关系: {row['是否相同的项目']}")
        else:
            print("未找到李四的关系数据")

    except Exception as e:
        print(f"读取关系数据出错: {e}")


if __name__ == "__main__":
    test_csv_reading()
