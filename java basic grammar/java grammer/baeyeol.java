// 배열 생성
// String[] classGroup에서 classGroup은 배열이 담길 변수의 이름이다. 
// String[]은 classGroup에 담을 배열에 담길 데이터의 타입이 문자열의 배열이라는 의미다. 
// 배열을 선언할 때는 데이터 타입 뒤에 []를 붙여야 한다. []가 없다면 classGroup는 배열이 아니라 문자열 데이터 타입을 갖는 변수가 된다. 
// 배열에 소속될 데이터들은 중괄호 안에 위치한다. 
public class baeyeol {

	public static void main(String[] args) {
		
      String [] classGroup = {"조현수", "윤승희", "최운주", "양희진", "노다민"}; 
	}

}

// 배열에 담겨있는 데이터를 꺼내오는 방법
// classGroup[0]처럼 배열이 담겨있는 변수의 이름 뒤에 대괄호를 붙이고 그 안에 0부터 시작하는 숫자를 입력하면 순차적으로 값을 가져올 수 있다.
public class GetDemo {
	
	public static void main(String[] args) {
		String [] classGroup = {"조현수", "윤승희", "최윤주", "양희진", "노다민"};
		System.out.println(classGroup[0]);   // 조현수
		System.out.println(classGroup[1]);   // 윤승희
		System.out.println(classGroup[2]);   // 최윤주
		System.out.println(classGroup[3]);   // 양희진
		System.out.println(classGroup[4]);   // 노다민
	}
}

// 배열을 정의하는 다른 방법과 배열에 담겨 있는 값의 수를 알아내는 방법
// .length는 배열에 실제 담긴 데이터의 숫자를 의미하는 것이 아니라 배열을 처음 생성할 때 지정한 배열의 크기를 의미한다는 점을 주의
//  length는 배열에 담긴 원소의 숫자가 아니라 배열을 선언할 때 지정한 배열이 담을 수 있는 값의 크기를 의미한다.
public class LengthDemo {
	
	public static void main(String[] args) {
		String[] classGroup = new String[5];   // 새로운 문자열을 만드는 방법 (배열[]을 정의할 떈 new사용)
		classGroup[0] = "조현수";
		System.out.println(classGroup.length);
		classGroup[1] = "윤승희";
		System.out.println(classGroup.length);
		classGroup[2] = "최윤주";
		System.out.println(classGroup.length);
		classGroup[3] = "양희진";
		System.out.println(classGroup.length);
		classGroup[4] = "노다민";
		System.out.println(classGroup.length);
		
	}
}

// 학교 비유를 조금만 더 활용해보자. 1반 학생들이 상담을 받는다고 했을 때
// 반복문과 배열은 매우 밀접한 관계에 있다고 할 수 있다.
public class ArrayLoopDemo {
	
    public static void main(String[] args) {
    	
    	String[] members = {"조현수", "윤승희", "최윤주", "양희진", "노다민"};
    	for (int i = 0; i < members.length; i++) {     // members.length는 3이다.
    		String member = members [i];   // String member라는 변수인데 이것의 데이터 타입은 String이다. 즉, 문자를 담는 변수이다.
    		System.out.println(member + "가 상담을 받았습니다.");
    	}
    }
}


// for - each
// 배열의 내용을 탐색할 때 for 문을 좀 더 간편하게 사용할 수 있는 방법
// 위의 예제는 이전 예제와 정확하게 동일하게 동작한다.
public class ForeachDemo {
	
    public static void main(String[] args) {
    	String[] members = {"조현수", "윤승희", "최윤주", "양희진", "노다민"};
    	for (String e : members) {     // 배열 members의 값을 변수 e에 담아서 중괄호 구간 안으로 전달해준다.
    		System.out.println(e + "가 상담을 받았습니다.");
    	}
    	
    }
}
	 











