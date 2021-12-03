// 클래스 맴버와 인스턴스 맴버
// 객체를 만들기 위해서 우선 클래스를 정의하고, 클래스에 대한 인스턴스를 만들었다. 

// 클래스 변수
// 우리가 만든 계산기가 원주율의 값을 사용자에게 제공하도록 하고 싶다고 간주해보자. 그런데 원주율인 3.14는 이미 알려져있는 수이다. 
// 따라서 각각의 인스턴스 마다 원주율의 값을 별도로 가지고 있을 필요가 없다. 이런 경우 변수를 클래스의 맴버로 만들면 된다. 
// 아래 코드는 원주율을 담고 있는 변수 PI를 클래스의 소속인 맴버로 만든 예제다. 
class Calculator {
	static double PI = 3.14;  // static을 맴버(변수, 메소드) 앞에 붙이면 클래스의 맴버가 된고 모든 인스턴스에서 같은 값을 가진다.
	int left, right;
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void sum () {
		System.out.println(this.left + this.right);
	}
	
	public void avg () {
		System.out.println((this.left + this.right) / 2);
	}
}

public class CalculatorDemo1 {
	
	public static void main (String[] args) {
		Calculator c1 = new Calculator();
		System.out.println(c1.PI);       // 인스턴스를 통해서 PI에 접근
		
		Calculator c2 = new Calculator();
		System.out.println(c2.PI);
		 
		System.out.println(Calculator.PI);   // // 클래스를 통해서 PI에 접근
}
	
	
// 만약 계산을 할 때 특별한 값을 포함시켜야 한다면 어떻게 해야 할까? 
// sum과 avg를 실행할 때마다 특정한 값을 연산에 포함시키고 싶을 때 시도해볼 수 있는 방법이다. 
class  Calculator2 {
	static double PI = 3.14;
	static int base = 0;   // 클래스 변수인 base가 추가되었다.
	int left, right;
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void sum() {
		System.out.println(this.left + this.right + base);  // 더하기에 base의 값을 포함시킨다.
	}
	
	public void avg() {
		System.out.println((this.left + this.right + base) / 2);  // 평균치에 base의 값을 포함시킨다.
	}
}

class CalculatorDemo2 {
	
	public static void main(String[] args) {
		
		Calculator2 c1 = new Calculator2();
		c1.setoprands(10, 20);
		c1.sum();
		
		Calculator2 c2 = new Calculator2();
		c2.setoprands(20, 40);
		c2.sum();
		
		Calculator2.base = 10;  // 클래스 변수 base의 값을 10으로 지정했다.
		c1.sum();   // 40 출력
		c2.sum();   // 70 출력
	}
}


// 클래스 메소드
// 굳이 인스턴스가 left와 right의 값을 항상 유지하고 있어야 할 이유는 없다. 
// 합계나 평균을 구할 때마다 좌항과 우항의 값을 주는 방식으로 계산을 할 수도 있다. 
class Calculator3 {
	
	public static void sum(int left, int right) {
		  System.out.println(left + right);
	}
	
	public static void avg(int left, int right) {
		System.out.println((left + right) / 2);
	}
}

class CalculatorDemo3 {
	
	public static void main(String[] args) {
		Calculator3.sum(10, 20);
		Calculator3.avg(10, 20);
		
		Calculator3.sum(20, 40);
		Calculator3.avg(20, 40);
	}
}


// 클래스와 인스턴스의 차이점을 보여주기 위한 예제
// 인스턴스 메소드는 클래스 맴버에 접근 할 수 있다.
// 클래스 메소드는 인스턴스 맴버에 접근 할 수 없다.
class c1 {
	static int static_variable = 1;    // 클래스 변수
	int instance_variable = 2;        // 인스턴스 변수
	static void static_static() {    // 클래스 메소드가 클래스 변수를 호출할 때 static_static이다.
		System.out.println(static_variable);
	}
	static void static_instance() {    // 클래스 메소드에서는 인스턴스 변수에 접근 할 수 없다. 
        //System.out.println(instance_variable);
	}
	void instance_static() {   // 인스턴스 메소드에서는 클래스 변수에 접근 할 수 있다.
		System.out.println(static_variable);
	}
	void instance_instance() {
		System.out.println(static_variable);
	}	
}
public class  ClassMemberDemo {  
	
	public static void mian(String[] agrs) {
		c1 c = new c1 ();
		// 인스턴스를 이용해서 정적 메소드에 접근 -> 성공
        // 인스턴스 메소드가 정적 변수에 접근 -> 성공
        c.static_static();             // >> 인스턴스(c)를 통해서 클래스에 접근 가능
        // 인스턴스를 이용해서 정적 메소드에 접근 -> 성공
        // 정적 메소드가 인스턴스 변수에 접근 -> 실패
        c.static_instance();
        // 인스턴스를 이용해서 인스턴스 메소드에 접근 -> 성공
        // 인스턴스 메소드가 클래스 변수에 접근 -> 성공
        c.instance_static();
        // 인스턴스를 이용해서 인스턴스 메소드에 접근 -> 성공 
        // 인스턴스 메소드가 인스턴스 변수에 접근 -> 성공
        c.instance_instance();
        // 클래스를 이용해서 클래스 메소드에 접근 -> 성공
        // 클래스 메소드가 클래스 변수에 접근 -> 성공
        C1.static_static();         // >> 클래스(c1)를 통해서도 직접 클래스 메소드에 접근 가능
        // 클래스를 이용해서 클래스 메소드에 접근 -> 성공
        // 클래스 메소드가 인스턴스 변수에 접근 -> 실패
        C1.static_instance();
        // 클래스를 이용해서 인스턴스 메소드에 접근 -> 실패
        C1.instance_static();
        // 클래스를 이용해서 인스턴스 메소드에 접근 -> 실패
        //C1.instance_instance();
	}
}












