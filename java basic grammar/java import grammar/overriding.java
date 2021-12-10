// overriding

class Calculator {
	int left, right;
	
	public void setoprands (int left, int right) {
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
	
	public void sum() {      // 메소드 sum이 SubstractionableCalculator에 추가
		System.out.println("실행 결과는" + (this.left + this.right) + "입니다.");
	    // 부모가 이미 갖고 있는 sum을 재정의 즉 overriding한 것이다.
	}
	
	public void substract() {
		System.out.println(this.left - this.right);
	}
}

public class CalculatorDemo {
	public static void main(String[] args) {
		
		SubstractionableCalculator c1 = new SubstractionableCalculator();
		c1.setoprands(10, 20);
		c1.sum();
		c1.avg();
		c1.substract();
	}
}
// 실행결과   <<    실행결과는 30입니다.   15    -10
// 메소드 sum이 SubstractionableCalculator에 추가 되었다. 실행결과는 c1.sum이 상위 클래스의 메소드가 아닌 하위 클래스의 메소드 sum을 실행하고 있는 것을 보여준다.
// 하위 클래스에서 상의 클래스와 동일한 메소드를 정의하면 부모 클래스로부터 물려 받은 기본 동작 방법을 변경하는 효과를 갖게 된다. 
// 기본동작은 폭넓게 적용되고, 예외적인 동작은 더 높은 우선순위를 갖게하고 있다. 이것이 바로 overriding이다.


// 상위 클래스에서 정의하고 있는 메소드 avg는 계산 결과를 화면에 출력하고 있다. 
// 그런데 계산 결과를 좀 더 다양하게 사용하기 위해서 메소드 avg가 화면에 결과를 출력하는 대신 계산 결과를 리턴해주면 좋겠다.
// 이 조건에 만족하는 코드
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

class SubstractionableCalculator extends Calculator {
	
	public void sum() {
		System.out.println("실행 결과는" + (this.left + this.right) + "입니다.");
	}
	
	public void avg() {
		return (this.left + this.right) / 2;
	}
	
	public void substract() {
		System.out.println(this.left - this.right);
	}
	
}

public class CalculatorDemo {
	
	public static void main(String[] args) {
		SubstractionableCalculator c1 = new SubstractionableCalculator();
		c1. setoprands(10, 20);
		c1.sum();
		c1.avg();
		c1.substract();
	}
	
}
// 위와 같이 화면 에러가 발생한다.
// overriding을 하기 위해서는 메소드의 리턴 형식이 같아야 한다. 즉 클래스 Calculator의 메소드 avg는 리턴 타입이 void이다. 
// 그런데 이것을 상속한 클래스 SubstractionableCalculator의 리턴 타입은 int이다.
// 오버라이딩을 하기 위해서는 메소드 이름, 메소드 매개변수의 숫자와 데이터 타입 그리고 순서, 메소드 리턴 타입을 충족시켜야 한다.
// 메소드 매개변수 예시 >> public void avg(int a, int b)에서 int a, int b가 매개변수이다.

// 따라서 아래 코드와 같이 변경해야 한다.
class Calculator {
	int left, right;
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void sum() {
		System.out.println(this.left + this.right);
		
	}
	
	public int avg() {
		return ((this.left + this.right) / 2);
		
	}
}
  
class SubstractionableCalculator extends Calculator {
    
   public void sum() {
       System.out.println("실행 결과는 " +(this.left + this.right)+ "입니다.");
   }
    
   public int avg() {
       return ((this.left + this.right) / 2);
   }
    
   public void substract() {
       System.out.println(this.left - this.right);
   }
}

public class CalculatorDemo {
   public static void main(String[] args) {
       SubstractionableCalculator c1 = new SubstractionableCalculator();
       c1.setOprands(10, 20);
       c1.sum();
       c1.avg();
       c1.substract();
   }
}
// 상위 클래스와 하위 클래스의 서명이 같기 때문에 메소드 오버라이딩을 할 수 있었다. 
// 그런데 위의 코드를 보면 중복이 발생했다. 메소드 avg의 부모와 자식 클래스가 같은 로직을 가지고 있다. 
// 중복은 제거 되어야 한다. 생성자와 마찬가지로 super를 사용하면 이 문제를 해결 할 수 있다.
class Calculator {
	int left, right;
	
	public void setoprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void sum() {
		System.out.println(this.left + this.right);
		
	}
	
	public int avg() {
		return ((this.left + this.right) / 2);
	}
}

class SubstractionableCalculator extends Calculator {
	
	public void sum() {
		System.out.println("실행 결과는" +(this.left + this.right)+ "입니다.");
		
	}
	
	public void avg() {
		return super.avg();
	}
	
	public void substract() {
        System.out.println(this.left - this.right);
    }
}

public class CalculatorDemo {
    public static void main(String[] args) {
        SubstractionableCalculator c1 = new SubstractionableCalculator();
        c1.setOprands(10, 20);
        c1.sum();
        System.out.println("실행 결과는" + c1.avg());
        c1.substract();
    }
}














