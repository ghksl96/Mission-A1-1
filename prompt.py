prompt = input("저장할 프롬프트를 입력하세요: ")

with open("prompts.txt", "a", encoding="utf-8") as f:
    f.write(prompt + "\n")

print("저장 완료! 프롬프트:", prompt)

