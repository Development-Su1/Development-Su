// 아래 예제는 간단한 더하기 프로그램이이다.
// 아주 간단한 예제지만 상당히 복잡한 작업을 실행하고 있는 로직이라고 가정하자.
public class ClaculatorDemo1 {

	public static void main(String[] args) {
		// 아래의 로직이 1000줄 짜리의 복잡한 로직이라고 가정하자.
		System.out.println(10 + 20);
		System.out.println(20 + 40);

	}

}

// 메소드화
// 실행 결과는 30과 60이다. 프로그래밍의 기본은 중복을 제거하는 것이다. 위의 로직은 두개의 값을 더한다는 중복이 존재한다. 
// 이 중복을 제거하기 위한 방법으로 고려해볼 수 있는 기능이 메소드다.
// 아래의 코드는 위의 코드를 메소드화시킨 예제다.
public class ClaculatorDemo2 {
	public static void sum(int left, int right) {   // sum은 합계라는 뜻
		System.out.println(left + right);
	}
	
	public static void main (String[] args) {
		sum(10, 20);
		sum(20, 40);
	}
	
}

// 똑같은 수를 이용해서 더하기 뿐 아니라 평균도 구해야 한다면 어떻게 해야할까?
// 입력값(left, right)을 변수화시키고 메소드들(sum, avg)가 이 값을 사용하면 코드의 양을 줄일 수 있게 된다.
public class ClaculatorDemo3 {
	public static void avg(int left, int right) {
		System.out.println((left + right) / 2);
	}
	
	public static void sum (int left, int right) {
		System.out.println(left + right);
	}
	
	public static void main (String[] args) {
		int left, right;
		
		left = 10;
		right = 20;
		
		sum(left, right);
		avg(left, right);
		
		left = 20;
		right = 40;
		
		sum(left, right);
		avg(left, right);
	}
}


// 객체화
// 아래의 예제는 의미적으로 연관된 로직들을 물리적으로 응집된 하나의 객체로 만드는 법을 설명하는 예제다. 

// 클래스는 연관되어 있는 변수와 메소드의 집합이다. << 변수 left와 right, 메소드 sum과 avg
// 이것들을 Calculator이라는 이름으로 그룹핑하고 싶다. 이럴 때 사용하는 키워드가 class이다. 
// class 키워드 뒤에는 클래스 이름이 오고 그 뒤의 중괄호는 클래스의 시작과 끝의 경계를 의미한다. 
// 이렇게 해서 더하기(sum)와 평균(avg)를 계산 할 수 있는 클래스가 만들어졌다.
class Calculator {     // 이 로직들을 대표하는 이름을 계산기라는 의미의 Calculator라고 정했음.
	int left, right;
	
	public void setoprands(int left, int right) {
		this.left = left;      // this는 클래스를 통해서 만들어진 인스턴스 자신을 가리킨다.
		this.right = right;
		
	}
	
	public void sum() {
		System.out.println(this.left + this.right);
	}
	
	public void avg() {
		System.out.println((this.left + this.right) / 2);
	}
}

// 설계도를 구체적인 제품으로 만들어야 한다. 그 때 사용하는 키워드가 new이다. 구체적인 제품을 인스턴스(instance)라고 부른다. 
// 클래스 : 설계도, 인스턴스 : 제품
// new Calculator()은 Calculator를 구체적인 제품으로 만드는 명령이다.

// Calculator c1은 Calculator라는 의미다. 즉 클래스를 만든다는 것은 사용자 정의 데이터 타입을 만드는 것과 같은 의미다. 
// 클래스를 인스턴스화 할 때는 변수에 담아야 한다는 것과 이 때 사용하는 변수의 데이터 타입은 그 클래스가 된다는 점이다.
// 각각의 인스턴스는 메소드 setOprands를 통해서 변수 left, right의 값을 설정하고 있다.
public class ClaculatorDemo4 {
	
	public static void main (String[] args) {
		
		Calculator c1 = new Calculator();   //  new를 이용해서 만든 인스턴스를 변수 c1에 담고 있다. 
		c1.setoprands(10, 20);
		c1.sum();
		c1.avg();
		
		Calculator c2 = new Calculator();
		c2.setoprands(20, 40);
		c2.sum();
		c2.avg();
		
	}
}

























