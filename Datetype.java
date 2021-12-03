//Sout를 쓰고 컨트롤 스페이스를 누른뒤 엔터를 누르면 System.out.println(); 한번에 쓸 수 있음


public class Datetype {
	public static void main(String[] args) {
		System.out.println(6);      //숫자(Number)를 표현하고 싶을 때 이렇게 표현함
        System.out.println("six");   //문자 즉 문자열(String)
        System.out.println("6");   //문자 즉 문자열 6이다. >> (String 6)

	    System.out.println(6+6);   //12
	    System.out.println("6"+"6");   //66 즉, 양 옆에 문자열이 있을 때 +는 더하기가 아니라 결합연산자이다.(문자열을 위한것)
	    
	    System.out.println(6*6);   //36
//	    System.out.println("6"*"6");  >> 에러가 발생함 즉, 문자열은 곱하기라는 연산을 할수가 없다.
	    
	    System.out.println("1111".length());    //4 >> 길이(.length)를 나타냄 (문자열만"")
	    System.out.println(1111);    // 숫자 1111이다.
//	    System.out.println(1111.length());  >> 숫자는 그 숫자의 길이를 알려주는 연산같은 것은 없다.
	    
	    System.out.println("HelloWord");   //문자열(String)
	    System.out.println('H');   //char 문자
	}
}