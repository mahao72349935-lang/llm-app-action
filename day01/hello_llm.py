# day01/hello_llm.py

# 引入类型提示 (类似 TypeScript 中的类型声明，增强代码可读性)
from typing import Dict

# def 相当于 JS 的 function。 
# -> str 表示这个函数预期返回一个字符串 (类似 TS 的返回类型)
def generate_greeting(user_info: Dict) -> str:
    """
    这是一个函数的文档字符串（Docstring），企业规范中必须要有。
    用于说明函数的作用。
    """
    # 提取字典中的数据，类似 JS 的 user_info.name，但 Python 用中括号取值
    name = user_info["name"]
    role = user_info["role"]
    target = user_info["target"]
    
    # f-string 语法，相当于 JS 的 `你好 ${name}`
    greeting_msg = f"你好，{name}！欢迎踏上【{role}】的征途。你的目标是：{target}。"
    
    return greeting_msg

# 这一行相当于 JS 中的： if (require.main === module)
# 意思是：只有当直接运行这个脚本时，才执行下面的代码；如果是被别的模块 import，则不执行。
if __name__ == "__main__":
    # 定义一个字典，类似 JS 的对象
    programmer_profile = {
        "name": "未来架构师",
        "role": "LLM应用工程师",
        "target": "3个月内掌握 RAG、Agent 与微调，成功上岸！"
    }
    
    # 调用函数
    result = generate_greeting(programmer_profile)
    
    # 打印结果 (相当于 console.log)
    print("=" * 40)
    print(result)
    print("=" * 40)