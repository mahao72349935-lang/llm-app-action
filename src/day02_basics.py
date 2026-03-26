# 1. 导入模块 (相当于 JS 的 import)
import os

# 2. 定义函数 (def 相当于 JS 的 function 或 const name = () => {})
def greet_user(name: str):
    """
    这是一个简单的问候函数
    :param name: 字符串类型 (相当于 TS 中的 name: string)
    """
    # f-string 相当于 JS 的模板字符串 `Hello, ${name}`
    message = f"Hello, {name}! 欢迎来到 LLM 应用开发世界。"
    return message

# 3. 列表与字典 (相当于 JS 的 Array 和 Object)
def show_data_structures():
    # List (JS Array)
    tech_stack = ["Python", "LangChain", "VectorDB"]
    tech_stack.append("React") # 相当于 push
    
    # Dictionary (JS Object/JSON)
    course_info = {
        "duration": "3 months",
        "goal": "Job offer"
    }
    
    print(f"技术栈: {tech_stack}")
    print(f"目标: {course_info['goal']}") # 访问 key 必须用引号

# 4. 程序入口 (相当于 JS 脚本直接执行，但在 Python 中习惯用这个判断)
if __name__ == "__main__":
    user_name = "前端转 AI 的开发者"
    result = greet_user(user_name)
    print(result)
    show_data_structures()