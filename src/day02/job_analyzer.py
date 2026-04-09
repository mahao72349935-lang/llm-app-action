# src/day02/job_analyzer.py
# 实战工具：分析职位描述，提取关键信息 + 判断匹配度

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def analyze_job(jd_text: str, my_skills: list[str]) -> dict:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": """你是一个职位分析助手。分析职位描述，返回 JSON，只返回 JSON 不要其他文字。
格式：
{
  "title": "职位名称",
  "required_skills": ["必须技能列表"],
  "bonus_skills": ["加分技能列表"],
  "salary_range": "薪资范围字符串，没有则填null",
  "match_score": 匹配度0到100的整数,
  "missing_skills": ["候选人缺少的关键技能"],
  "suggestion": "一句话建议"
}"""
            },
            {
                "role": "user",
                "content": f"职位描述：{jd_text}\n\n我的技能：{', '.join(my_skills)}"
            }
        ],
        temperature=0,
    )

    raw = response.choices[0].message.content.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw)


# 模拟一条真实 JD
jd = """
职位：LLM应用工程师
职责：
- 基于 LangChain / LlamaIndex 开发 RAG 知识库系统
- 设计和优化 Prompt，提升模型输出质量
- 对接 OpenAI / 国内大模型 API
- 与前端协作完成 AI 产品功能

要求：
- Python 熟练，有 FastAPI 或 Flask 经验
- 了解 LangChain、向量数据库（Chroma/Pinecone）
- 有 LLM 应用开发经验优先
- 加分：有 Vue/React 前端经验，了解 RAG 原理

薪资：25k-40k，上海
"""

my_skills = ["Vue3", "React", "TypeScript", "Python基础", "OpenAI API调用", "LangChain入门"]

result = analyze_job(jd, my_skills)

print("=" * 40)
print(f"职位：{result['title']}")
print(f"匹配度：{result['match_score']} / 100")
print(f"薪资：{result['salary_range']}")
print(f"必须技能：{', '.join(result['required_skills'])}")
print(f"缺少技能：{', '.join(result['missing_skills']) or '无'}")
print(f"建议：{result['suggestion']}")
print("=" * 40)