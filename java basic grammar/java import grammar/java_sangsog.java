// 상속 (물려준다는 의미)
// 어떤 객체가 있을 때 그 객체의 필드(변수)와 메소드를 다른 객체가 물려 받을 수 있는 기능
// 상속은 기존 객체를 그대로 유지하면서 어떤 기능을 추가할 때 쓰이는 방법

// 예제
// 객체 Calculator는 더하기와 평균에 해당하는 sum과 avg 메소드를 가지고 있다.
// 그런데 이 객체가 가지고 있는 기능에 빼기(substract)를 추가하고 싶다.
// 기존의 객체는 기능을 물려준다는 의미에서 부모 객체가 되고 새로운 객체는 기존 객체의 기능을 물려받는다는 의미에서 자식 객체가 된다. 
class Calculator {
	int left, right;
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;	
	}
	
	public void sum() {
		System.out.println(this.left + this.right );
	}
	
	public void avg() {
		System.out.println((this.left + this.right) / 2);
	}
}

class SubstractionableCalculator extends Calculator {  // 새로운 클래스인 SubstractionableCalculator을 정의
	public void substract() { 
		System.out.println(this.left - this.right);
	}
}

public class CalculatorDemo1 {
	
	public static void main(String[] args) {
		
		SubstractionableCalculator c1 = new SubstractionableCalculator();
		c1.setoprands(10, 20);
		c1.sum();
		c1.avg();
		c1.substract();
	}
}
// 실행결과 >> 30  15  -10
// extends Calculator은 클래스 Calculator를 상속 받는다는 의미다.
// 따라서 SubstaractableCalculator는 Calculator에서 정의한 메소드 setOprands, sub, avg를 사용할 수 있게 된다. 

// Calculator을 상속 받는 클래스를 하나 더 만들어보자. 이 클래스는 곱하기를 할 수 있는 클래스다.
class MultiplicationableCalculator extends Calculator {
	
	public void multiplication() {
		System.out.println(this.left * this.right);
	}
}

public class CalculatorDemo2 {
	
	public static void main(String[] args) {
		
		MultiplicationableCalculator c1 = new MultiplicationableCalculator();
		c1.setoprands(10, 20);
		c1.sum();
		c1.avg();
		c1.multiplication();
	}
}
// 실행결과 >> 30   15    200

// 상속한 클래스를 다시 상속할 수 있을까? 가능하다. 
// 아래의 예제는 곱하기가 가능한 클래스인 MultiplicationableCalculator을 상속받고 있다.
// 나누기(division) 추가, 새로운 클래스인 DivisionableCalculator 생성
class DivisionableCalculator extends MultiplicationableCalculator {
	
	public void division() {
		System.out.println(this.left / this.right);
	}
}

public class CalculatorDemo3 {
	
	public static void main(String[] args) {
		
		DivisionableCalculator c1 = new DivisionableCalculator();
		c1.setoprands(10, 20);
		c1.sum();
		c1.avg();
		c1.multiplication();
		c1.division();
	}
}





























