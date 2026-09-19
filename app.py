# 프롬프트 데이터 (리스트 안에 딕셔너리!)
prompts = [
    {"제목": "회의록 작성", "카테고리": "텍스트 생성", "내용": "전문가처럼 회의록 글을 써줘", "즐겨찾기": False},
    {"제목": "판타지 게임", "카테고리": "이미지 생성", "내용": "멋있는 판타지 게임 주인공을 그려줘", "즐겨찾기": False},
    {"제목": "대기업 비서", "카테고리": "텍스트 생성", "내용": "대기업 비서처럼 일정을 관리해줘", "즐겨찾기": False},
]


# 메뉴를 보여주는 함수
def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("================================")

    # 프롬프트를 추가하는 함수
def add_prompt():
    print("\n----- 프롬프트 추가 -----")
    제목 = input("제목: ")
    내용 = input("내용: ")
    카테고리 = input("카테고리: ")

    새프롬프트 = {"제목": 제목, "내용": 내용, "카테고리": 카테고리, "즐겨찾기": False}
    prompts.append(새프롬프트)

    print(f"'{제목}' 프롬프트가 추가되었어요! ✅")

    # 프롬프트 목록을 보여주는 함수
def show_list():
    print("\n----- 프롬프트 목록 -----")
    if prompts == []:
        print("아직 저장된 프롬프트가 없어요! 😅")
    else:
        for i in range(len(prompts)):
            제목 = prompts[i]["제목"]
            카테고리 = prompts[i]["카테고리"]
            print(f"{i+1}. {제목} [{카테고리}]")

                # 프롬프트 상세 보기 함수
def show_detail():
    show_list()  # 먼저 목록을 보여줘서 번호를 고르게 함

    if prompts == []:
        return  # 목록이 비어있으면 여기서 끝!

    번호 = input("\n자세히 볼 번호를 선택하세요: ")

    if 번호.isdigit() and 1 <= int(번호) <= len(prompts):
        선택 = prompts[int(번호) - 1]  # 번호에 맞는 프롬프트 꺼내기
        print("\n----- 상세 정보 -----")
        print(f"📌 제목: {선택['제목']}")
        print(f"📝 내용: {선택['내용']}")
        print(f"📁 카테고리: {선택['카테고리']}")
        print(f"⭐ 즐겨찾기: {'예' if 선택['즐겨찾기'] else '아니오'}")
    else:
        print("잘못된 번호예요! 😅")

            # 카테고리별로 조회하는 함수
def show_category():
    print("\n----- 카테고리별 조회 -----")

    카테고리 = input("조회할 카테고리를 입력하세요: ")

    찾은개수 = 0  # 몇 개 찾았는지 세는 변수
    for i in range(len(prompts)):
        if prompts[i]["카테고리"] == 카테고리:
            제목 = prompts[i]["제목"]
            print(f"{i+1}. {제목} [{카테고리}]")
            찾은개수 = 찾은개수 + 1

    if 찾은개수 == 0:
        print(f"'{카테고리}' 카테고리에 프롬프트가 없어요! 😅")

            # 프롬프트를 검색하는 함수
def search_prompt():
    print("\n----- 프롬프트 검색 -----")

    검색어 = input("검색어를 입력하세요: ")

    찾은개수 = 0
    for i in range(len(prompts)):
        제목 = prompts[i]["제목"]
        if 검색어 in 제목:
            카테고리 = prompts[i]["카테고리"]
            print(f"{i+1}. {제목} [{카테고리}]")
            찾은개수 = 찾은개수 + 1

    if 찾은개수 == 0:
        print(f"'{검색어}'에 대한 검색 결과가 없어요! 😅")

                    # 즐겨찾기 추가/해제 함수
def toggle_favorite():
    show_list()  # 먼저 목록 보여주기

    if prompts == []:
        return  # 비어있으면 끝!

    번호 = input("\n즐겨찾기할 번호를 선택하세요: ")

    if 번호.isdigit() and 1 <= int(번호) <= len(prompts):
        선택 = prompts[int(번호) - 1]  # 번호에 맞는 프롬프트 꺼내기

        if 선택["즐겨찾기"] == False:      # 별표 없으면
            선택["즐겨찾기"] = True        # 별표 붙이기!
            print(f"'{선택['제목']}'을(를) 즐겨찾기에 추가했어요! ⭐")
        else:                             # 별표 있으면
            선택["즐겨찾기"] = False       # 별표 떼기!
            print(f"'{선택['제목']}'을(를) 즐겨찾기에서 해제했어요! ⬜")
    else:
        print("잘못된 번호예요! 😅")

                    # 즐겨찾기 목록만 보여주는 함수
def show_favorites():
    print("\n----- ⭐ 즐겨찾기 목록 -----")

    찾은개수 = 0  # 몇 개 찾았는지 세기
    for i in range(len(prompts)):
        if prompts[i]["즐겨찾기"] == True:   # 별표 있는 것만!
            제목 = prompts[i]["제목"]
            카테고리 = prompts[i]["카테고리"]
            print(f"{i+1}. {제목} [{카테고리}] ⭐")
            찾은개수 = 찾은개수 + 1

    if 찾은개수 == 0:
        print("아직 즐겨찾기한 프롬프트가 없어요! 😅")


# 프로그램 시작!
while True:
    show_menu()
    choice = input("번호를 선택하세요: ")

    if choice == "1":
        add_prompt()
    elif choice == "2":
        show_list()
    elif choice == "3":
        show_category()   
    elif choice == "4":
        search_prompt() 
    elif choice == "5":
        show_detail()    
    elif choice == "6":
        toggle_favorite()
    elif choice == "7":          
        show_favorites() 
    elif choice == "0":
        print("프로그램을 종료합니다. 안녕히 가세요! 👋")
        break
    else:
        print("아직 만들지 않은 기능이에요! 곧 추가할게요 😊")