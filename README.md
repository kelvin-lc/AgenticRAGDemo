# AgenticRAGDemo

一个展示Agentic RAG（检索增强生成）架构的演示项目，通过多智能体协作实现增强的信息检索和推理能力。

## 项目概述

本项目实现了一个先进的RAG系统，通过多个专业智能体的协调工作，相比传统的单智能体RAG方法，能够提供更准确、全面和上下文相关的响应。

## 系统架构

### 高层流程

```
客户端应用 → FastAPI接口层 → Agentic RAG核心层 → 知识存储层
      ↓              ↓              ↓              ↓
  Web/移动应用  →  RESTful API  →  智能体协调   →  向量数据库
      ↓              ↓              ↓              ↓
  请求/响应   →  异步处理机制  →  多跳推理链构建 →  Mock知识库
```

### Agent Coordination Pipeline

```
用户http query → query agent → 并行多个retriaval agent → extraction agent → leader agent validation  → finally answer
                ↓                ↓                          ↓                    ↓
            实体识别            向量检索                    关系推理              答案验证
            查询分类            扩展检索                    推理链构建            置信度评估  
```

## 各个Agent介绍

目前系统采用基于Teams的`Coordinate`模式，由leader来统一控制。也可以使用范式的Workflow模式。包含以下专业智能体：

### 0. leader agent
    
**职责：**
- 协调多个retriaval agent 和 extraction agent
- 返回最终答案给用户


### 1. 查询分析智能体 (QueryAnalysisAgent)

**职责：**
- 解析和理解用户查询
- 识别关键实体和关系
- 分类查询意图和预期答案类型

**输出：** 结构化的查询意图，包含主要实体、查询类型和预期响应格式

### 2. 多个检索智能体 (RetrievalAgent)
因为Agentic RAG 中的knowledge可能来个多个实例，多个无法一次retrieval得到的chunk，所以需要并行多个retriaval agent。
- 单个retriaval agent 可以循环调用。
- 多个retriaval agent 可以并行调用。

**职责：** 基于查询分析结果进行多轮信息检索

**能力：**
- **初始检索：** 搜索与主要实体相关的文档
- **扩展检索：** 基于初始结果查找相关实体信息
- **迭代检索：** 持续检索直到建立完整的推理链

### 3. 提取智能体 (ExtractionAgent)

**职责：** 提取分析检索到的信息片段，组合成一个完整的知识

**能力：**
- 信息关联分析，构建推理链
- 推理路径构建，候选答案生成

### 4. 验证智能体 (ValidationAgent)

**职责：** 验证推理结果的正确性和一致性

**能力：**
- 逻辑一致性验证
- 信息完整性检查
- 答案置信度评估

## 知识库结构

### Mock知识库设计

系统包含两个用于演示的Mock知识库：

- **`project_csv_knowledge.csv`：** 团队成员的项目分配和贡献情况
- **`relationships_csv_knowledge.csv`：** 人际关系和团队动态  

### 查询处理示例

**查询：** "李四做了哪些项目？"

**处理流程：**
1. 查询分析智能体识别"李四"为主要实体，"项目"为目标信息
2. 检索智能体在`project_csv_knowledge.csv`中搜索李四的项目分配
3. 提取智能体可能根据需要扩展搜索到相关团队成员
4. 验证智能体确保响应的完整性和准确性
5. 返回最终答案给用户

### 模块化设计优势

系统设计具有清晰的关注点分离，便于：
- **可扩展性：** 轻松添加新的智能体和功能
- **可维护性：** 隔离的模块便于调试和更新
- **协作开发：** 多个开发者可以同时专注于不同模块
- **测试：** 每个组件的独立测试

## 快速开始

### 环境要求
- Python 3.12+
- uv包管理器
- OpenAI API密钥。Model也可以使用其他模型，环境变量均在 config.py 中配置。

### 安装步骤
```bash
# 克隆项目
git clone git@github.com:kelvin-lc/AgenticRAGDemo.git
cd AgenticRAGDemo

# 安装依赖
uv sync

### 启动服务
```bash
# 方式1: 使用启动脚本（推荐）
uv run python start_server.py

# 方式2: 直接启动
uv run python src/main.py

# 服务将在 http://localhost:8001 启动
# API文档: http://localhost:8001/docs
# 健康检查: http://localhost:8001/ping
```

### 发送请求

```bash
curl -X POST http://localhost:8001/api/v1/agent/completions -H "Content-Type: application/json" -d '{"message": "李四在哪里项目", "user_id": "test_user", "session_id": "test_session", "stream": false}'
```

## 开发路线图

### 计划功能
- [ ] Docker容器化
- [ ] 多轮对话支持
- [ ] 数据持久化层
- [ ] 性能、评估等框架
- [ ] 综合日志系统
- [ ] 指标监控和告警
- [ ] 单元和集成测试
- [ ] CI/CD流水线实现

## 贡献指南

[待实现：贡献指南]

## 许可证

[待实现：许可证信息]