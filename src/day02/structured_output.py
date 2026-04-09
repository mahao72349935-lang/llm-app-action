# src/day02/structured_output.py

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def get_json(prompt: str, schema_desc: str) -> dict:
    """
    让 LLM 返回稳定的 JSON 格式
    schema_desc：告诉 LLM 需要什么结构
    """
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": f"""你是一个数据提取助手。
用户给你一段描述，你需要提取信息并以 JSON 格式返回。
返回格式要求：{schema_desc}
重要：只返回 JSON，不要有任何其他文字，不要有 markdown 代码块。"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,  # JSON输出必须用0，保证稳定性
    )

    raw = response.choices[0].message.content.strip()

    # 安全解析：防止 LLM 偷偷加了 ```json ``` 包裹
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    return json.loads(raw)


# ── 测试1：提取简历信息 ──
resume_text = """
张三，男，28岁，5年前端开发经验。
熟悉 Vue3、React、TypeScript。
曾就职于阿里巴巴、字节跳动。
期望薪资 35k，坐标上海。
"""

result = get_json(
    prompt=resume_text,
    schema_desc='{"name": "姓名", "age": 年龄数字, "skills": ["技能列表"], "companies": ["公司列表"], "salary": 期望薪资数字, "city": "城市"}'
)

print("提取结果：")
print(json.dumps(result, ensure_ascii=False, indent=2))
print(f"\n姓名：{result['name']}")
print(f"技能数量：{len(result['skills'])}")
print(f"期望薪资：{result['salary']}k")


# ── 测试2：批量处理 + 错误保护 ──

def safe_get_json(prompt: str, schema_desc: str) -> dict | None:
    """加了异常保护的版本，生产环境必须用这个"""
    try:
        return get_json(prompt, schema_desc)
    except json.JSONDecodeError as e:
        print(f"JSON 解析失败：{e}")
        print(f"原始输出：{prompt}")
        return None

# 批量提取商品信息
products = [
    "iPhone 15 Pro，售价 7999 元，库存 328 件，分类：手机",
    "MacBook Air M3，售价 8999 元，库存 56 件，分类：电脑",
    "AirPods Pro 2，售价 1899 元，库存 0 件，分类：耳机",
]

schema = '{"name": "商品名", "price": 价格数字, "stock": 库存数字, "category": "分类", "in_stock": 是否有货布尔值}'

print("\n批量商品提取：")
results = []
for p in products:
    item = safe_get_json(p, schema)
    if item:
        results.append(item)
        print(f"  {item['name']} | {item['price']}元 | 有货:{item['in_stock']}")

# 统计有货商品
in_stock = [r for r in results if r["in_stock"]]
print(f"\n共 {len(results)} 件商品，{len(in_stock)} 件有货")