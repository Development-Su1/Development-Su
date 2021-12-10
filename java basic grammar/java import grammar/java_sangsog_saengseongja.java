// 상속과 생성자

class Calculator {
	int left, right;
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void sum() {
		System.out.println(this.left + this.right);
	}
	
	public void avg() {
		System.out.println((this.left + this.right) / 2);
	}
}

class SubstractionableCalculator extends Calculator {    // Calculator가 SubstractionableCalculator의 부모클래스이다.
	
	public SubstractionableCalculator(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void substract() {
		System.out.println(this.left - this.right);
	}
}

public class CalculatorConstructorDemo4 {
	
	public static void main(String[] args) {
		
		SubstractionableCalculator c1 = new SubstractionableCalculator(10, 20);
		// SubstractionableCalculator라고 하는 클래스가 생성자로 left(10)와 right(20)의 값을 위처럼 받도록 변경함.
		c1.sum();
        c1.avg();
        c1.substract();
	}
}
// 실행결과 >> 30   15   -10
// SubstractionableCalculator의 생성자로 left와 right의 값을 받아서 초기화시키고 있다.


// 어떻게 하면 상위 클래스의 생성자를 호출할 수 있을까?
// super 
// super 키워드는 부모 클래스를 의미한다. 여기에 ()붙이면 부모 클래스의 생성자를 의미하게 된다. 
// 이렇게 하면 부모 클래스의 기본 생성자가 없어져도 오류가 발생하지 않는다.
// 하위 클래스의 생성자에서 super를 사용할 때 주의할 점은 super가 초기화보다 가장 먼저 나타나야 한다는 점이다. 
// 여기서 초기화는 어떤 일을 시작하기 전에 준비하는 것을 말한다.
class Calculator {
	int left, right;
	
	public Calculator() {}  // 부모클래스의 기본생성자
		
	public Calculator(int left, int right) {    // 꼭 기본생성자가 추가된 뒤에 해야한다.
		this.left = left;
		this.right = right;
	}
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void sum() {
		System.out.println(this.left + this.right);
	}
	
	public void avg() {
		System.out.println((this.left + this.right) / 2);
	}
	
}

class SubstractionableCalculator extends Calculator {   
	
	public SubstractionableCalculator (int left, int right) {
		super(left, right);
	    // 80행에서는 this 대신 super을 사용한 것임.
		// this. -> 클래스 내부의 메서드에서 소속된 클래스 변수를 호출 및 연결
		// super -> 부모클래스 내부의 메서드에서 소속된 클래스 변수를 호출 및 연결
	}
	
	public void substract() {
		System.out.println(this.left - this.right);
	}
}

public class CalculatorConstructorDemo5 {
	
	public static void main(String[] args) {
		
		SubstractionableCalculator c1 = new SubstractionableCalculator(10, 20);  // 생성자를 이용해서 객체 생성
		c1.sum();
		c1.avg();
		c1.substract();
	}
}


















