import chromadb
# 1. 导入 Chroma 提供的 Embedding 函数工具 (相当于按需引入特定的 Loader)
from chromadb.utils import embedding_functions

def run_vector_search():
    print("🚀 正在初始化本地 Chroma 向量数据库...")
    client = chromadb.Client()

    print("🧠 正在加载【支持中文】的 Embedding 模型，这需要一点时间下载...")
    # 2. 核心修复：指定一个多语言模型 paraphrase-multilingual-MiniLM-L12-v2
    # 这个模型支持 50+ 种语言，中文理解能力不错，且足够轻量
    chinese_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )

    # 3. 创建集合时，把我们指定的中文 Embedding 函数传进去
    # 注意：换了模型，集合名字最好也换一下，避免和之前存入的乱码数据冲突
    collection = client.create_collection(
        name="frontend_ai_docs_chinese", 
        embedding_function=chinese_ef
    )

    documents = [
        "Vue 是一款用于构建用户界面的渐进式 JavaScript 框架。",
        "React 是一个用于构建 Web 和原生交互界面的库。",
        "Hugging Face 是一个提供海量开源机器学习模型的社区。",
        "向量数据库被广泛用于大语言模型的长期记忆存储。",
        "今天中午我吃了一顿非常美味的红烧肉。"
    ]

    ids = [f"doc_{i+1}" for i in range(len(documents))]

    print(f"📥 正在将 {len(documents)} 条文档存入数据库...")
    collection.add(
        documents=documents,
        ids=ids
    )
    print("✅ 数据存储完毕！\n")

    # 查询
    query_text = "我想学前端开发，有什么推荐的技术？"
    
    print(f"🔍 用户的提问是: '{query_text}'")
    print("⏳ 正在向量数据库中进行语义相似度搜索...")
    
    results = collection.query(
        query_texts=[query_text],
        n_results=2
    )

    print("\n🎉 搜索到的最相关文档是：")
    for idx, doc in enumerate(results['documents'][0]):
        print(f"TOP {idx + 1}: {doc}")

if __name__ == "__main__":
    run_vector_search()