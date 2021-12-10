import javax.sql.rowset.serial.SQLOutputImpl;

// final
// 상속 / 변경을 금지하는 규제이다.


// final필드
// 필드와 변수는 같은 의미이다. 
// 실행되는 과정에서 한번 값이 정해진 이후에는 변수 내의 값이 바뀌지 않도록 규제한다.

// 예제
class Calculator {
	static final double PI = 3.14;
	int left, right;
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;	
//      Calculator.PI = 3.14;
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
		System.out.println(c1.PI);
//      Calculator.PI = 10;			
	}
}
// 변수 앞에 final이 붙어있다는 점이다. 
// 그리고 19행과 37행에 Calculator.PI를 통해서 클래스 변수 PI의 값을 변경하려고 하고 있지만 자바는 이것을 허용하지 않는다. 
// final로 지정된 변수에는 한번 값이 할당되면 그 값을 바꿀 수 없기 때문이다.
// 이러한 특징은 클래스 변수의 예를 들었지만 인스턴스 변수에도 적용된다.



































