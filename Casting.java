// 데이터 타입의 변환(Casting)

public class Casting {

	public static void main(String[] args) {
		
		double a = 1.1;
		double b = 1;
		double b2 = (double) 1;	// 위와 똑같은 코드이다.
		System.out.println(b);   // b의 값은 1,0
//		>> 정수지만 이 정수가 b라고 하는 저 변수에 담길 때 저 변수가 double형이기 때문에 자동으로 1이 double 즉, 실수인 1.0으로 컨버팅됨.
//		즉, 손실이 없기 때문에 자동으로 캐스팅 바꿔준것이다. 이러한 이유로 2번째를 3번째처럼 (double)를 써주지 않은 것이다.
		
		
//		int c = 1.1;  >> 에러 발생
//		>> (double)실수형은 1.1처럼 소수점이 있고 (int)정수형은 소수점이 없기 때문에 자동으로 바꿔주게 되면 0.1을 잃어버리게 됨.
		
		
//		int c = 1.1;
		double d = 1.1;
		int e = (int) 1.1;  
		System.out.println(e);   // 1
//      바로 위에서 Add cast to int는 1.1은 double인데 저것을 int라는 형태로 강제로 바꾸는 코드를 자동으로 추가해주겠다는 것.
//	    즉, 더블인 1.1을 강제로 정수로 바꾸면 소수점 밑에 있는게 완전히 사라지기 때문에 손실이 일어남. 그래서 (int)같은 것을 꼭 명시해야함.
		
		
//		1을 String으로 바꾸고 싶다면? >> 1 toString
		String f = Integer.toString(1);
		System.out.println(f);    // 1이 나왔지만 이 1은 데이터 타입이 더이상 숫자가 아니라 문자열이다.
		
//		문자열인지 숫자인지 즉 데이터 타입이 무엇인지 확인하고 싶다면?
		String g = Integer.toString(1);
		System.out.println(g.getClass());  // .getClass를 붙여주면 됨. 그럼 f라는 변수의 데이터 타입을 알려줌.
//		위 코드 실행결과 >>  class java.lang.String
	}

}
