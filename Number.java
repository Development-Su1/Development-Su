
public class Number {

	public static void main(String[] args) {
		//이런것을 연산자 영어로 Operator라고 함
		System.out.println(6 + 2);  //8
        System.out.println(6 - 2);  //4
        System.out.println(6 * 2);  //12
        System.out.println(6 / 2);  //3
        
//Math는 많은 기능들이 잘 정리가 안되어 있으면 찾기가 어려워서 수학과 관련된 아주 유명하고 자주 사용하는 그룹핑 한 일종의 캐비넷이다.       
//Math.은 Math라고 하는 캐비넷 안에 수학과 관련된 여러 명령어들을 보여준다.
        System.out.println(Math.PI);   //3.14
        System.out.println(Math.floor(Math.PI));   //Math.floor을 하게 되면 소수점을 없애줌(반올림). 따라서 3.0이됨.
        System.out.println(Math.ceil(Math.PI));   //ceil은 올림이라는 뜻. 그럼 3.14의 뒤에 1이 있으면 그 앞의 값을 1을 올려버림. 4.0
        
	}

}
