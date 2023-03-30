import openai
openai.api_key = "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"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="你知道网络小说吗？",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)

print(response)