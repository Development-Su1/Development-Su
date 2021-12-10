// abstract
// 상속을 강제하는 일종의 규제
// 즉, 클래스나 메소드를 사용하기 위해서는 반드시 상속해서 사용하도록 강제하는 것이다.

// 추상 메소드 (메소드의 시그니처만 정의된 비어있는 메소드를 의미한다.)
abstract class A {
	public abstract int b();
    // 본체가 있는 메소드는 abstract 키워드를 가질 수 없다.
    // public abstract int c(){System.out.println("Hello")}
    // 오류를 발생시키는데 본체인 {System.out.println("Hello")}가 존재하는데 추상 메소드를 의미하는 abstract를 사용하고 있기 때문이다. 
		
	public void d() {
		System.out.println("world");    // 추상 클래스에는 추상 메소드가 아닌 메소드가 존재할 수 있다.
	}
}
public class AbstractDemo {
	
	public static void main(String[] args) {
		A obj = new A ();    // 추상 클래스는 구체적인 메소드의 내용이 존재하지 않기 때문에 인스턴스화시켜서 사용할 수 없다.
		
	}
}
// 메소드 b의 선언 부분에는 abstract라는 키워드가 등장하고 있다. 
// 이 키워드는 메소드 b는 메소드의 시그니처만 정의 되어 있고 이 메소드의 구체적인 구현은 하위 클래스에서 오버라이딩 해야 한다는 의미다. 
// 이렇게 내용이 비어있는 메소드를 추상 메소드라고 부른다. 
// 추상 메소드를 하나라도 포함하고 있는 클래스는 추상 클래스가 되고, 자연스럽게 클래스의 이름 앞에 abstract가 붙는다. 

// 위의 문제들을 해결하기 위한 코드
// 클래스 A를 상속한 하위 클래스를 만들고 추상 메소드를 오버라이딩해서 내용있는 메소드를 만들어야 한다.
abstract class A {
	public abstract int b();
	public void d() {
	   System.out.println("world");
	}	
} 
class B extends A {    // 클래스 B는 클래스 A를 상속했다. 
	public int b () {return 1;}   // 클래스 A의 추상 메소드인 메소드 b를 오버리이딩 하고 있다. 그 결과 클래스 A를 사용할 수 있다.
}
public class AbstractDemo {
	
	public static void main(String[] args) {
		B odj = new B();
		System.out.println(obj.b());
	}
}
// 부모 클래스에는 메소드의 시그니처만 정의해놓고(31행처럼) 그 메소드의 실제 동작 방법은 이 메소드를 상속 받은 하위 클래스의 책임으로 위임하고 있다.(37행처럼)


// 계산기 예제에 추상 클래스 개념을 도입한 코드
abstract class Calculator {
	int left, right;
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public abstract void sum();
	public abstract void avg();
	public void run() {
		sum();
		avg();
	}
}

class CalculatorDecoPlus extends Calculator {
	public void sum() {
		System.out.println("+ sum :" + (this.left + this.right));
	}
	
	public void avg() {
		System.out.println("+ avg :"+(this.left+this.right)/2);

	}
}

class CalculatorDecoMinus extends Calculator {
	public void sum() {
		System.out.println("- sum :" + (this.left + this.right));
	}
	
	public void avg() {
		System.out.println("- avg :" + (this.left - this.right)/2);
	}
}

public class CalculatorDemo {
	
	public static void main(String[] args) {
		CalculatorDecoPlus c1 = new CalculatorDecoPlus();
		c1.setoprands(10, 20);
		c1.run();
		
		CalculatorDecoMinus c2 = new CalculatorDecoMinus();
		c2.setoprands(10, 20); 
		c2.run();
	}
}
// 실행결과
// + sum : 30
// + avg : 15
// - sum : 30
// - avg : 15
// 위의 예제는 합계(sum)를 실행하고 평균(avg)을 실행하는 절차를 메소드 run을 통해서 한 번에 실행되도록 한 코드이다. 

















