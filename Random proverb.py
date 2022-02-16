quotes = ["Convictions are more dangerous enemies of truth than lies.", "Rather be dead than cool.", "Accept challenges, so that you may feel the exhilaration of victory.",
"Nothing great in the world has been accomplished without passion.", "If you don't risk anything you risk even more.", "The biggest adventure you can ever take is to live the life of your dreams."]
meaning = ["강한 신념이야말로 거짓보다 더 위험한 진리의 적이다.", "열정없이 사느니 차라리 죽는게 낫다.", "도전을 받아들여라. 그러면 승리의 쾌감을 맛볼 지도 모른다.",
"이 세상에 열정없이 이루어진 위대한 것은 없다.", "아무런 위험을 감수하지 않는다면 더 큰 위험을 감수하게 될 것이다.", "여러분이 할 수 있는 가장 큰 모험은 바로 여러분이 꿈꿔오던 삶을 사는 것입니다"]

from tkinter import *
import random

def click_button():
    random_quote = random.randint(0, 6)   # 0 ~ 6 까지
    canvas.itemconfig(eng, text=quotes[random_quote])
    canvas.itemconfig(kor, text=meaning[random_quote])

window = Tk()
window.title("오늘의 명언")
window.resizable(False, False)    # 윈도우 크리 고정할 경우

canvas = Canvas(window, width=700, height=500, bg="black")
canvas.pack()    

img = PhotoImage(file="night.png")
canvas.create_image(350, 250, image=img)

eng = canvas.create_text(350, 200, text="오늘의 명언", fill="white", \
                   font=("나눔바른펜", 30, "bold"))

kor =  canvas.create_text(350, 250, text="", fill="white", \
                   font=("나눔바른펜", 20, "bold"))


button = Button(window, text="보기", font=("나눔바른펜", 20, "bold"), bg="white", command=click_button)
button.place(x=320, y=400)


