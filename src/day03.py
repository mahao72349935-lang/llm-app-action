from transformers import pipeline

def analyze_chinese_sentiment():
    # 重点：通过 model 参数，指定 Hugging Face 上一个专门做中文正负面评价的模型
    # 第一次运行依然会自动去 HF 下载这个中文模型
    print("正在加载中文情感分析模型...")
    classifier = pipeline("sentiment-analysis", model="uer/roberta-base-finetuned-jd-binary-chinese")
    
    weibo_comments = [
        "这家餐厅太难吃了，服务态度还极差，再也不会来了！",
        "今天天气真好，和朋友出去玩得很开心~",
        "这件衣服质量一般般吧，习惯性好评。"
    ]
    
    print("\n--- 中文社交媒体情感分析 ---")
    results = classifier(weibo_comments)
    
    for text, result in zip(weibo_comments, results):
        # 不同的模型输出的 label 可能不同，比如这个中文模型输出 'positive (星级较高)' 等
        print(f"评论: {text}")
        print(f"判断结果: {result['label']}, 置信度: {result['score']:.4f}\n")

if __name__ == "__main__":
    analyze_chinese_sentiment()
