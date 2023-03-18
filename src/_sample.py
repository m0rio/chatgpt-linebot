import os
import openai
from dotenv import load_dotenv

# .env ファイルを読み込む
load_dotenv()

# APIキーの設定
openai.api_key = os.environ.get("OPENAI_API_KEY")


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "keplerについて教えて"},
    ],
)
print(response.choices[0]["message"]["content"].strip())