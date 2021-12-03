// 1,2,3,4.... >> 자연수
// -4, -3, -2, 0, 1, 2, 3, 4... >> 정수 
// -2.0, -2.4, -1.0, 0, 1.0, 2.0.... >> 실수

public class variable {

	public static void main(String[] args) {
		
	//  a=1;  Number 그러나 정확한 표현으로는 integer(정수)임	
		int a=1;
		System.out.println(a);
		
		
//		int b = 1.1;  >> int는 정수형태만 가능하므로 1.1은 안됨
//		위와 같은 1.1을 실수(real number)라고 하는데 정확한 표현은 double이다.
		double b = 1.1;
		System.out.println(b);
		
		
		String c = "Hello World";   // 문자열이기 때문에
		System.out.println(c);
		
		
		Character e = 'H';    // 문자이기 때문에
		System.out.println(e);
      
	}

}
