// 접근 제어자

// 클래스의 맴버(변수와 메소드)들의 접근 권한을 지정한다.
// 클래스 맴버에 대한 접근 제어자
class A {
	public String y() {
		return "public void y()";
	}
	
	private String z() {    
		return "public void z()";
		
	}
	
	public String x() {    // 접근 제어자가 public이기 때문에 호출 할 수 있다. 
		return z();
	}
	
}
public class AccessDemo1 {
	public static void main(String[] args) {
		A a = new A();
		System.out.println(a.y());
     // System.out.println(a.z());  >> 이 코드는 오류가 발생한다. 즉, 메소드 z에 접근 할 수 없다는 의미
	    System.out.println(a.x());	
	}
}
// 위 코드의 결과
// 8행에 private은 클래스(A) 밖에서는 접근 할 수 없다는 의미다.
// 이 private의 자리에 오는 것들을 접근 제어자(access modifier)라고 한다.
// 이것 때문에 22행에서 출력할 때 오류가 나는 것이다.
// 그러나 13행은 잘 출력된다. 그 이유는 접근 제어자가 public이기 때문이다.
// 그리고 메소드의 내용을 보면 내부적으로 메소드 z를 호출하고 있다. 메소드 z는 정상적으로 호출된다.
// 왜냐하면 메소드 x와 메소드 z는 같은 클래스의 소속이기 때문이다. 따라서 메소드 x에서 z를 호출 할 수 있는 것이다.

// 예제
class Calculator {
	private int left, right;   
// 인스턴스 필드인 left와 right가 private으로 지정되었다.
// 이 두개의 변수는 객체 외부에서 호출될 필요가 없다. 따라서 외부로부터 이 변수를 숨기기 위해서 접근 제어자로 private을 지정했다.
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	private int _sum () {
		return this.left + this.right;
		
	}
	
	public void sumDecoplus() {
		System.out.println("++++" + _sum() + "++++");
	}
	
	public void sumDecoMinus() {
		System.out.println("----" + _sum() + "----");
	}
}
public class CalculatorDemo {
	
	public static void main(String[] args) {
	    Calculator c1 = new Calculator();
	    c1.setoprands(10, 20);
	    c1.sumDecoplus();
	    c1.sumDecoMinus();	
	}
}
// 실행결과 << ++++30++++     ----30----
// 메소드 _sum이 추가 되었는데 실제 계산은 이 메소드가 내부적으로 처리하고, 
// 계산된 결과를 외부에 출력해주는 메소드는 sumDecoPlus, sumDecoMinus에서 처리한다.


// 클래스의 접근 제어자
// 클래스의 접근 제어자는 총 2개로 public과 default이다. default는 접근 제어자를 붙이지 않은 경우 default가 된다.
// 접근 제어자가 public인 클래스는 다른 패키지의 클래스에서도 사용할 수 있고, default인 경우는 같은 패키지에서만 사용 가능하다.

























