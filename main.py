while True:
    print("1. 프롬프트 저장하기")
    print("2. 프롬프트 목록 보기")
    print("3. 종료하기")
    print("4. 프롬프트 삭제하기")
    print("5. 프롬프트 검색하기")

    선택 = input("번호를 선택하세요: ")

    if 선택 == "1":
        prompt = input("저장할 프롬프트를 입력하세요: ")
        with open("prompts.txt", "a", encoding="utf-8") as f:
            f.write(prompt + "\n")
        print("저장 완료!")

    elif 선택 == "2":
        with open("prompts.txt", "r", encoding="utf-8") as f:
            줄목록 = f.readlines()

        if 줄목록 == []:                          # ← 새로 추가! 비었는지 확인
            print("📭 아직 저장된 프롬프트가 없어요!")
        else:                                     # ← 안 비었으면 목록 출력
            print("저장된 프롬프트 목록:")
            번호 = 1
            for 줄 in 줄목록:
                print(번호, ".", 줄.strip())
                번호 = 번호 + 1

    elif 선택 == "3":
        print("프로그램을 종료합니다. 안녕! 👋")
        break

    elif 선택 == "4":
        with open("prompts.txt", "r", encoding="utf-8") as f:
            줄목록 = f.readlines()

        if 줄목록 == []:
            print("📭 삭제할 프롬프트가 없어요!")
        else:
            # 1. 먼저 목록을 번호 붙여 보여주기
            print("삭제할 프롬프트 목록:")
            번호 = 1
            for 줄 in 줄목록:
                print(번호, ".", 줄.strip())
                번호 = 번호 + 1

            # 2. 몇 번 지울지 물어보기
            지울번호 = int(input("몇 번을 삭제할까요? "))

            # 3. 그 번호만 빼고 다시 저장
            del 줄목록[지울번호 - 1]
            with open("prompts.txt", "w", encoding="utf-8") as f:
                f.writelines(줄목록)

            print("🗑️ 삭제 완료!")

    elif 선택 == "5":
        검색어 = input("검색할 단어를 입력하세요: ")

        with open("prompts.txt", "r", encoding="utf-8") as f:
            줄목록 = f.readlines()

        print("🔍 검색 결과:")
        번호 = 1
        for 줄 in 줄목록:
            if 검색어 in 줄:              # ← 검색어가 들어있으면!
                print(번호, ".", 줄.strip())
                번호 = 번호 + 1

    else:
        print("⚠️ 잘못된 번호예요! 1~3 중에 골라주세요!")