// object 클래스

// toString
// toString은 객체를 문자로 표현하는 메소드이다. 
// 기본 예졔 (계산기 코드)
class Calculator {
	int left, right;
	
	public void setOprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void sum() {
		System.out.println(this.left + this.right);
		
	}
	
	public void avg() {
		System.out.println((this.left + this.right)/2);
	
	}
}
public class CalculatorDemo {
	
	public static void main(String[] args) {
		Calculator c1 = new Calculator();
		c1.setOprands(10, 20);
        System.out.println(c1);   // 클래스 Calculator의 인스턴스 c1을 화면에 출력하고 있다.
	}	
}
// 예를들어 계산기 인스턴스의 left, right 값을 알 수 있다면 개발을 좀 더 편하게 할 수 있을 것이다.
class Calculator {
	int left, right;
	
	public void setOprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void sum() {
		System.out.println(this.left + this.right);
	}
	
	public void avg() {
		System.out.println((this.left + this.right)/2);
    }
	
	public String toString() {
		return "left :" + this.left + "right :" + this.right;	
	}
}

public class CalculatorDemo {
	
	public static void main(String[] args) {
		Calculator c1 = new Calculator();
		c1.setOprands(10, 20);
		System.out.println(c1);
		System.out.println(c1.toString());
	}
}
// 실행결과
// left : 10, right : 20
// left : 10, right : 20
// 클래스 Calculator에 toString을 재정의(overriding)했다.
// toString을 직접 호출하지 않아도 어떤 객체를 System.out.print로 호출하면 자동으로 toString이 호출되도록 약속되어 있다.































