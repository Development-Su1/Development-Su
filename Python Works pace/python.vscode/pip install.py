# 파이썬 패키지를 어떻게 찾아볼 수 있는지 방법을 알아보겠습니다.  
# 브라우저를 열고 구글에서 pypi 라고 검색을 하면 첫 페이지에 나오는 pypi.org를 확인할 수 있는데 이 곳을 방문합니다. 
# 또는 주소창에 바로 https://pypi.org 라고 입력을 하는 방법도 있습니다.

# 페이지 중간에 보시면 이 글을 쓰는 시점에서 벌써 29 만개를 초과하는 프로젝트가 있는 것을 확인할 수 있는데요. 
# 조금 윗쪽에 browse projects 링크를 클릭하여 프로젝트를 살펴보겠습니다.

# 좌측에서 Topic 부분을 클릭하여 확대를 해보면 주제별로 어떤 프로젝트가 있는지를 확인할 수 있습니다. 
# 스크롤을 내려보면 Email, Database, Game, Internet 등 다양한 주제가 있는데 
# 원하는 주제를 선택하면 주제에 맞는 프로젝트 목록이 우측에 나타나게 됩니다.

# 실습을 위해서 웹 스크래핑에 아주 유명한 BeautifulSoup4 라는 패키지를 설치하기 위해서 
# 우선 검색어 입력부분에 beautifulsoup 까지만 입력 후 Enter 를 누릅니다.

# 이 중에서 윗쪽에 있는 beautifulsoup4 와 버전 정보로 이어지는 프로젝트를 클릭해보겠습니다.

# BeautifulSoup4 패키지 설치를 직접 해보겠습니다. 
# 프로젝트 페이지 좌측 상단의 버튼을 클릭하면 패키지 설치 명령을 복사할 수 있습니다.

# 실습을 위해 Quick start 부분의 처음 세 문장을 복사하여 Visual Studio Code 에 붙여넣기 합니다.
# 이 때 각 문장 앞의 >>> 부분은 제외하도록 합니다.
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


# install = 패키지 설치   >> pip install [패키지]
# install upgrade = 패키지 업그레이드	>> pip install upgrade [패키지]
# uninstall = 패키지 삭제	>> pip uninstall [패키지]
# list = 설치 패키지 목록	>> pip list
# show = 패키지 상세 정보	>> pip show [패키지]