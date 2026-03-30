# day01/main.py
# 你的第一个大模型应用！

from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载环境变量（类比前端的 import.meta.env）
load_dotenv()

# 初始化客户端（DeepSeek 兼容 OpenAI SDK，只需改 base_url）
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def chat(messages: list) -> str:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        temperature=0.7,
        max_tokens=1000,
        stream=True,  # 开启流式输出
    )
    
    full_reply = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
            full_reply += content
    
    print()  # 换行
    return full_reply

def main():
    print("🤖 AI 助手启动！输入 'quit' 退出\n")
    
    # System prompt：定义 AI 的人格（这是工程中最重要的技巧之一）
    messages = [
        {
            "role": "system",
            "content": "你是一名严格的前端面试官，正在面试一名求职者。你只问前端相关的面试题，每次只问一个问题，根据对方的回答追问或给出点评，语气专业但不失礼貌。先做一个简短的自我介绍，然后开始面试。"
        }
    ]
    
    while True:
        user_input = input("你：").strip()
        
        if user_input.lower() == 'quit':
            print("再见！")
            break
        
        if not user_input:
            continue
        
        # 把用户输入加入对话历史（多轮对话的关键！）
        messages.append({"role": "user", "content": user_input})
        
        print("AI：", end="", flush=True)
        reply = chat(messages)
        
        # 把 AI 回复也存入历史（这样 AI 才有"记忆"）
        messages.append({"role": "assistant", "content": reply})
        print()  # 空行分隔
        # 把对话追加写入 history.txt
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(f"你：{user_input}\n")
            f.write(f"AI：{reply}\n\n")

if __name__ == "__main__":
    main()