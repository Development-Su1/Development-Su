# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
#       보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 

# 이름 : 

# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
# 1주차.txt
# 2주차.txt
# 3주차.txt
# ...
# 50주차.txt

# (예 : 35주차.txt 파일 내용)
# - 35 주차 주간보고 -

# 부서 : 

# 이름 : 

# 업무 요약 : 


#  1주차 파일을 만드는 코드를 작성
with open("1주차.txt", "w", encoding="utf8") as report_file:
    report_file.write("-1주차 주간 보고-")
    report_file.write("\n부서 : ")    # 줄바꿈을 해주는 탈출문자(\n)로 줄바꿈을 해줌
    report_file.write("\n이름 : ")
    report_file.write("\n업무 요약 : ")

# 만약 줄바꿈을 하지 않는다면 파일에는 이런 식으로 내용이 적히게 됩니다.
# - 1 주차 주간보고 -부서 : 이름 : 업무 요약 : 

# 이제 다음으로 이 작업을 50번 반복
for i in range(1, 51):
     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
         report_file.write("-{0}주차 주간 보고-" .format(i))
         report_file.write("\n부서 : ")  
         report_file.write("\n이름 : ")
         report_file.write("\n업무 요약 : ")

# 보고서 본문 중 첫 번째 줄에도 몇 주차인지 정보가 필요하므로 format()을 이용하여 i 값을 넣어주면 됩니다.
# 1~50 까지의 숫자 정보를 가지는 i 변수와 합치는 방식으로 하겠습니다. 
# 문자열 여러개를 합칠 때 + 기호를 쓸 수 있는데 i 는 정수이므로 str(i)를 통해 문자열로 변환해준 다음 둘을 더하도록 합니다.
          