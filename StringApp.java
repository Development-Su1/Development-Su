
public class StringApp {

	public static void main(String[] args) {
		
		System.out.println("Hello World");  // 문자가 모여있는 것[문자열] (String)
	 // System.out.println('Hello World');  에러>> 자바에서 ''은 특수한 데이터 타입을 가리킴 
	    System.out.println('H');  // ''은 한 글자를 나타냄[문자] (Character)
	    
		System.out.println("Hello "   // >> Hello와 Word 사이에서 엔터를 누르면 저렇게 됨
				+ "World");       // >> 즉, Hello라는 문자열과 word 문바열을 + 합쳐준것임
		
		// new line
		System.out.println("Hello \nWorld");  // \n으로 줄바꿈 해줌
	
		// escape >> 문자를 탈출시키는 것
		System.out.println("Hello \"World\"");   // Hello "World"
		
		
	}

}
