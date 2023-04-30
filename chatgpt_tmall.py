import openai
import requests
from flask import Flask, request, jsonify

# 配置OpenAI API密钥
openai.api_key = "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"
openai.api_base = "https://api.181999.xyz"

app = Flask(__name__)

# 定义与ChatGPT交互的函数
def tmall_genie_chat(user_input):
    prompt = f"与天猫精灵用户的对话：\n用户：{user_input}\n天猫精灵："
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5
    )

    chat_response = response.choices[0].text.strip()
    return chat_response

# 定义一个路由处理天猫精灵发来的POST请求
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data["user_input"]
    chat_response = tmall_genie_chat(user_input)
    return jsonify({"response": chat_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
