# 외장 함수
# 외장 함수를 사용하기 위해서는 반드시 해당 모듈을 import 해야 합니다.

# 처음 사용할 모듈은 glob 입니다. 
# glob은 어떤 경로 내의 폴더 또는 파일의 목록을 조회할 때 사용하며 윈도우에서는 dir 명령과 비슷합니다. 
# glob 모듈에는 glob()이라는 함수가 있는데 파일 이름 또는 형태를 넘기면 그에 해당하는 파일이 조회됩니다.
# import를 통해 glob 모듈을 가져다 쓰도록 하고 glob() 함수에는 모든 것을 의미하는 * 와 
# 파이썬 파일 확장자를 의미하는 .py를 합친 *.py를 전달함으로써 확장자가 py인 모든 파일의 목록을 출력해보도록 하겠습니다.
import glob
print(glob.glob("*.py"))

# >> 실행을 해보면 현재 작업 공간에 존재하는 .py로 끝나는 모든 파일이 출력되는 것을 확인할 수 있습니다.
# ['helloworld.py', 'practice.py', 'theater_module.py']


# 다음으로 사용할 모듈은 os 입니다. os 는 운영체제에서 제공하는 기본 기능 정도로 생각하시면 됩니다.
# 폴더를 만들거나 삭제하는 기능을 수행할 수 있습니다. 
# os모듈을 import 하고 getcwd()함수를 호출하는데
# 이 때 cwd는 current working directory로 현재 작업 디렉토리를 의미합니다.
import os
print(os.getcwd())


# 이번에는 폴더를 하나 만들어보겠습니다. 
# folder 변수에 "sample_dir" 이란 값을 지정하고, os 모듈이 제공하는 기능 중 주어진 경로에 해당하는 
# 폴더 또는 파일이 존재하는지 여부를 알려주는 os.path.exists()함수를 통해서 
# folder 변수와 동일한 이름의 폴더가 존재하는지를 확인합니다. 
# 확인 결과 폴더가 존재하지 않는 경우에만 makedirs() 함수를 통해서 새로운 폴더를 생성하도록 하겠습니다.
import os

folder = "sample_dir"

if  os.path.exists(folder):
    print("이미 존재하는 파일입니다.")

else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

# 프로그램을 실행시켜보면 Visual Studio Code 좌측 EXPLORER 탭에 sample_dir 이라는 폴더가 새로 생기고 
# 다음 문장이 출력되는 것을 확인할 수 있습니다. >> [sample_dir 폴더를 생성하였습니다.]
# 다시 한 번 프로그램을 실행시키면 이미 sample_dir 폴더가 존재하기 때문에 출력 결과는 달라집니다.
# >> [이미 존재하는 폴더입니다.]


