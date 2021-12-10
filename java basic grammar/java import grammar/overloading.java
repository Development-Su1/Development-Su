// overloading

// 우리의 계산기는 2개의 값(left, right)에 대한 연산(sum, avg) 만을 수행 할 수 있다.
// 그런데 만약 3개의 값을 대상으로 연산을 해야 한다면 어떻게 해야할까? 우선 아래와 같이 입력값을 3개 받아야 할 것이다. 
// c1.setoprands(10, 20, 30);
class Calculator {
	int left, right;
	int third = 0;   // 변수를 지정해 놓지 않으면 이상 값이 들어가기 떄문에 0으로 지정을 해준것이다.
	                 // 즉 매개변수 2개의 sum을 계산할때 이상한 값이 들어가는것을 방지하기 위해 third를 0으로 초기화했다.
	                  
	public void setoprands(int left, int right) {
		System.out.println("setoprands(int left, int right)");
		this.left = left;
		this.right = right;
	}
	
	public void setoprands(int left, int right, int third) {
		System.out.println("setoprands(int left, int right, int third)");
		this.left = left;
		this.right = right;
		this.third = third;
	}
	
	public void sum() {
		System.out.println(this.left + this.right + this.third);
		
	}
	
	public void avg() {
		System.out.println((this.left + this.right + this.third) / 3);
	}
}

public class CalculatorDemo {
	
	public static void main(String[] args) {
		Calculator c1 = new Calculator();
		c1.setoprands(10, 20);
		c1.sum();
		c1.avg();
		c1.setoprands(10, 20, 30);
		c1.sum();
		c1.avg();
	}
}
// 실행결과
// setoprands(int left, int right)   30    15   setOprands(int left, int right, int third)   60    30
// 이를 통해서 알 수 있는 것은 매개변수의 숫자에 따라서 같은 이름의, 서로 다른 메소드를 호출하고 있다는 것을 알 수 있다.
// 이름은 같지만 시그니처는 다른 메소드를 중복으로 선언 할 수 있는 방법을 메소드 오버로딩(overloading)이라고 한다.

// 위 코드 중 12~13행과 18~19행이 서로 동일한 코드 즉 중복이 발생하였다.
// 먼저 중복되는 18~19행을 제거한다.
// 그리고 this는 자기 자신을 나타내는 특수한 변수이기에 위에 this.setoprands(left, right);를 써준다.
// 결론적으로 중복이 되는 코드를 먼저 호출한 다음에 this.setoprands(left, right);처럼 
// 그리고 메소드에서 추가적으로 필요한 작업인 this.third = third;을 부과한다.
public void setoprands(int left, int right) {
	System.out.println("setoprands(int left, int right)");
	this.left = left;
	this.right = right;
}

public void setoprands(int left, int right, int third) {
	this.setoprands(left, right);
	System.out.println("setoprands(int left, int right, int third)");
	this.third = third;
}


// 메소드 오버로딩은 매개변수를 사용한다. 즉 매개변수가 다르면 이름이 같아도 서로 다른 메소드가 되는 것이다. 
// 반면에 매개변수는 같지만 리턴타입이 다르면 오류가 발생한다. 


// 더 많은 값을 대상으로 연산을 해야 한다면 어떻게 해야할까?
// 아래의 코드는 인자로 배열을 사용하고 있다. 이렇게하면 하나의 인자로 여러개의 값을 받을 수 있다.
class Calculator {
	int[] oprands;
	
	public void setoprands(int[] oprands) {
		this.oprands = oprands;
	}
	 
	public void sum() {
		int total = 0;
		for(int value : this.oprands) {
			total += value;
		}
		System.out.println(total);
	
	}
	
	public void avg() {
		
		int total = 0;
		for(int value : this.oprands) {
			total += value;
		}
		System.out.println(total / this.oprands.length);	
	}
}
public class CalculatorDemo {
	
	public static void main(String[] args) {
		Calculator c1 = new Calculator();
		c1.setoprands(new int[] {10, 20});
		c1.sum();
		c1.avg();
		c1.setoprands(new int[] {10, 20, 30});
		c1.sum();
		c1.avg();
	}
}










