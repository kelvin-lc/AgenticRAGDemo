# 测试文档

本目录包含Agentic RAG Demo项目的所有测试文件。

## 测试文件说明

### 1. `test_csv_data.py`
- **功能**: 测试CSV文件数据读取
- **测试内容**: 
  - 项目数据CSV文件读取
  - 关系数据CSV文件读取
  - 李四相关数据的验证

### 2. `test_knowledge.py`
- **功能**: 测试知识库功能
- **测试内容**:
  - 项目知识库检索
  - 关系知识库检索
  - 向量数据库功能

### 3. `test_agent_team.py`
- **功能**: 测试Agent团队功能
- **测试内容**:
  - Agent团队创建
  - 团队成员配置
  - 团队查询功能

### 4. `run_all_tests.py`
- **功能**: 运行所有测试
- **使用**: 一键运行所有测试用例

## 运行测试

### 运行单个测试
```bash
# 测试CSV数据
uv run python test/test_csv_data.py

# 测试知识库
uv run python test/test_knowledge.py

# 测试Agent团队
uv run python test/test_agent_team.py
```

### 运行所有测试
```bash
uv run python test/run_all_tests.py
```

## 测试环境要求

- Python 3.12+
- uv包管理器
- 已安装项目依赖
- 有效的OpenAI API密钥

## 注意事项

1. 确保在项目根目录下运行测试
2. 测试会使用真实的API调用，请注意API使用量
3. 知识库测试会创建临时向量数据库
4. 所有测试都是独立的，可以单独运行 