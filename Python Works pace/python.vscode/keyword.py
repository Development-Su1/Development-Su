# 키워드 인자
# 함수를 호출하는 방법 중에 키워드 인자를 이용하는 방법도 있습니다.
def profile(name, age, main_lang):   # 키워드 인자 : name, age, main_lang
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬" ,age=34)
profile(age=32, name="김태호" ,main_lang="자바")    
# 키워드 인자는 무엇보다 순서에 구애받지 않는다.

# (예)
# 반드시 일반 전달값들을 순서대로 먼저 적고 나서 키워드 인자들을 적어야 합니다. 
# profile("유재석", age=20, main_lang="파이썬") >> (O) 올바른 함수 호출 방법 (일반 전달값을 먼저 작성)
# profile(name="김태호", 25, "파이썬") >> (X) 잘못된 함수 호출 방법 (키워드 인자 먼저 작성 후 일반 전달값 작성)

# [방법1]
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(age=23, main_lang="파이썬", name="조현수") 
profile(main_lang="자바", name="윤승희", age=22)   

# [방법2]
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile("양희진", age=22, main_lang="파이썬")
profile(main_lang="자바", name="조현수", age=23)