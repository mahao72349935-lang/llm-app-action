import os
def check_env(): 
  aiList = ['PyTorch', 'LangChain', 'RAG']
  for ai in aiList:
    print(f"正在检查{os.name}环境下的{ai}环境...")
  
if __name__ == "__main__":
  check_env()