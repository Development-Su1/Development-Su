// 상수와 enum
// 상수는 변하지 않는 값이다. 아래에서 좌항이 변수이고 우항이 상수이다.
// int x = 1;

// 상수의 이런 특성을 이용해서 아래와 같은 로직을 작성할 수 있다.
public class ConstantDemo {
	public static void main(String[] args) {
	/*
     * 1. 사과
     * 2. 복숭아
     * 3. 바나나
     */
	int type = 1;   //  1이다.(1로 지정)
	switch (type) {    // 위에 type가 1이기 때문에 switch(type)에서 case1만 실행된다.
	case 1:
		System.out.println(57);
	    break;
	    
	case 2:
		System.out.println(34);
		break;
		
	case 3:
		System.out.println(93);
		break;
     	}		
	}
}
// 위와 같은 로직에서 숫자 1에 해당하는 과일은 언제나 사과여야 한다. 그러므로 변하지 않는 값인 상수값에 따라서 그 값에 해당하는 과일의 의미를 고정하고 있다
// 인스턴스형 상수는 switch문의 조건값으로 사용될 수 없다.


// 그런데 주석으로 상수의 의미를 전달하고 있지만 주석이 없어졌거나, 주석이 상수를 사용하는 코드와 멀어진다면 
// 각 숫자에 해당하는 과일이 무엇을 나타내는지 알아보기거 어렵거나 불가능해질 수 있다.
// 이런 때는 이름이 있다면 더 좋을 것이다. 변수도 상수가 될 수 있다. 
// 변수를 지정하고 그 변수를 final로 처리하면 한번 설정된 변수의 값은 더 이상 바뀌지 않는다. 
// 또한 바뀌지 않는 값이라면 인스턴스 변수가 아니라 클래스 변수(static)로 지정하는 것이 더 좋을 것이다.
// private: 자기 자신의 클래스 내에서만 접근이 가능
public class ConstantDemo {
	private final static int APPLE = 1;
	private final static int PEACH = 2;
	private final static int BANANA = 3;

	public static void main(String[] args) {
		
		int type = APPLE;
		switch(type) {
		case APPLE:
			System.out.println(57 + "kcal");	
		    break;
		    
		case PEACH:
			System.out.println(34 + "kcal");	
		    break;
		    
		case BANANA:
			System.out.println(93 + "kcal");	
		    break;
		}
	}	
}

// 프로그램이 커지면서 누군가 기업에 대한 상수가 필요해졌다.
public class ConstantDemo {
	
	// fruit
	private final static int APPLE = 1;
	private final static int PEACH = 2;
	private final static int BANANA = 3;
	
	// company
	private final static int GOOGLE = 1;
//  private final static int APPLE = 2;	 // 과일 APPLE과 기업 APPLE이 서로 같은 이름을 가진다. 이렇게 되면 APPLE 값이 2에서 1로 바뀐다.
	private final static int ORACLE = 3;
	
	public static void main(String[] args) {
		
		int type = 1;
		switch(type) {
		case APPLE:
		   System.out.println(57 + "kcal");	
		   break;	
		    
		case PEACH:
			System.out.println(34 + "kcal");	
		    break;
				    
		case BANANA:
			System.out.println(93 + "kcal");	
		    break;  
		    
		}	
	}
}
// 과일 APPLE과 기업 APPLE이 서로 같은 이름을 가진다. 이렇게 되면 APPLE 값이 2에서 1로 바뀐다.
// 다행인 것은 final로 선언했기 때문에 컴파일이 되지 않고 이름이 중복되는 문제를 방지할 수 있다.

// 그러나 기업에 대한 상수를 작성했고 이것이 이미 다양한 영역에서 사용되고 있는 상태에서 APPLE을 추가하려면 낭패가 될것이다.
// 이러한 문제를 해결하기 위해 접두사를 붙여 코드를 작성하였다.
public class ConstantDemo {
	
	// fruit
	private final static int FRUIT_APPLE = 1;
	private final static int FRUIT_PEACH = 2;
	private final static int FRUIT_BANANA = 3;
	
	// company
	private final static int COMPANY_GOOGLE = 1;
    private final static int COMPANY_APPLE = 2;	 
	private final static int COMPANY_ORACLE = 3;
	
	public static void main(String[] args) {
		
		int type = FRUIT_APPLE;
		switch(type) {
		case FRUIT_APPLE:
		   System.out.println(57 + "kcal");	
		   break;	
		    
		case FRUIT_PEACH:
			System.out.println(34 + "kcal");	
		    break;
				    
		case FRUIT_BANANA:
			System.out.println(93 + "kcal");	
		    break;  
		    
		}	
	}
}


// 네임스페이스
// 이것은 중복될 확률을 낮출 수 있다.
// 그런데 상수가 너무 지저분하다. 이것을 깔끔하게 바꿀 수 있는데 이때에는 인터페이스를 사용하면 된다.
interface FRUIT {
	int APPLE=1, PEACH=2, BANANA=3;
}

interface COMPANY {
	int COOGLE=1, APPLE=2, ORACLE=3;
}

public class ConstantDemo {
	
	public static void main(String[] args) {
		
		int type = FRUIT.APPLE;
		switch(type) {
		case FRUIT.APPLE:
			System.out.println(57 + "kcal");	
			   break;	
		
		case FEUIT.PEACH:
			System.out.println(34 + "kcal");	
			   break;	
			   
		case FRUIT.BANANA:
			System.out.println(93 + "kcal");	
			   break;	
		}	
	}
}
// 접미사(FRUIT_, COMPANY_)로 이름을 구분했던 부분이 인터페이스로 구분되기 때문에 언어의 특성을 보다 잘 살린 구조가 되었다. 
// 인터페이스를 이렇게 사용할 수 있는 것은 인터페이스에서 선언된 변수는 무조건 public static final의 속성을 갖기 때문이다.


// 우리 코드는 과일과 기업이라는 두 개의 상수 그룹이 존재한다. 
// 서로 다른 상수그룹의 비교를 시도했고 양쪽 모두 값이 정수 1이기 때문에 오류를 사전에 찾아주지 못하고 있다. 
// 컴파일러가 이런 실수를 사전에 찾아줄 수 있게 하려면 어떻게 해야 할까?
class Fruit {
	public static final Fruit APPLE = new Fruit();
	public static final Fruit PEACH = new Fruit();
	public static final Fruit BANANA = new Fruit();
}
class company {
	public static final company COOGLE = new company();
	public static final company APPLE = new company();
	public static final company ORACLE = new company();
}

public class ConstantDemo {
	public static void main(String[] args) {
		
		if(Fruit.APPLE == company.APPLE) {   // 에러 발생
			System.out.println("과일 애플과 회사 애플이 같다.");	
				
		}	
	}
}
// Fruit와 Company 클래스를 만들고 클래스 변수로 해당 클래스의 인스턴스를 사용하고 있다. 
// 각각의 변수가 final이기 때문에 불변이고, Static이므로 인스턴스로 만들지 않아도 된다.
// 결과는 17행에서 에러가 발생한다. 이것이 우리가 바라던 것이다. 서로 다른 카테고리의 상수에 대해서는 비교조차 금지하게 된 것이다. 
// 언제나 오류는 컴파일 시에 나타나도록 하는 것이 바람직하다. 실행 중에 발생하는 오류는 찾아내기가 더욱 어렵다.
// 위의 코드는 두 가지 문제점이 있는데 하나는 switch 문에서 사용할 수 없고 또 하나는 선언이 너무 복잡하다는 것이다. 이것을 해결할 방법은 enum이다.


// enum
// enum의 생성자가 접근 제어자 private만을 허용하기 때문이다.
// enum은 열거형(enumerated type)이라고 부른다. 열거형은 서로 연관된 상수들의 집합이라고 할 수 있다. 
// 위의 예제에서는 Fruit와 Company가 말하자면 열거인 셈이다. 이전 코드를 enum으로 바꿔보자.
enum fruit {
	APPLE, PEACH, BANANA;		
}

enum Company {      // enum은 class, interface와 동급의 형식을 가지는 단위다. 하지만 enum은 사실상 class이다. 
	COOGLE, APPLE, ORACLE;
}

public class ConstantDemo {
	
	public static void main(String[] args) {
//		if(Fruit.APPLE == Company.APPLE){    >> 컴파일 에러가 발생한 것이다. 밑에 부분포함
//            System.out.println("과일 애플과 회사 애플이 같다.");
//	    }  	
//  enum이 서로 다른 상수 그룹에 대한 비교를 컴파일 시점에서 차단할 수 있다는 것을 의미한다.	
		
		Fruit type = Fruit.APPLE;
		switch(type) {
		case APPLE:    // APPLE는 레이블이라고 함.
			System.out.println(57 + "kcal");
			break;
			
		case PEACH:   //
			System.out.println(34 + "kcal");
	        break;
	        
		case BANANA:   //
			System.out.println(93 + "kcal");
			break;
		}	
	}
}

//   enum fruit {
//      APPLE, PEACH, BANANA;		
//   }

//  위의 코드는 아래의 코드와 같다.

//    class Fruit{
//    public static final Fruit APPLE  = new Fruit();
//    public static final Fruit PEACH  = new Fruit();
//    public static final Fruit BANANA = new Fruit();
//    private Fruit(){}
//    }
// 생성자의 접근 제어자가 private이다. 그것이 클래스 Fruit를 인스턴스로 만들 수 없다는 것을 의미한다. 다른 용도로 사용하는 것을 금지하고 있는 것이다.


// enum은 사실 클래스다. 그렇기 때문에 생성자를 가질 수 있다.
enum Fruit {
	APPLE, PEACH, BANANA;   // 상수 열거
	Fruit() {    // 생성자 
		System.out.println("Call Constructor "+this);
	}
}

enum Company {      
	COOGLE, APPLE, ORACLE;
}

public class ConstantDemo {
	
	public static void main(String[] args) {
		
//		if(Fruit.APPLE == Company.APPLE){
//            System.out.println("과일 애플과 회사 애플이 같다.");
//        }
	
		Fruit type = Fruit.APPLE;
		switch(type) {
		case APPLE:
			System.out.println(57 + "kcal");
			break;
			
		case PEACH:
			System.out.println(34 + "kcal");
			break;
		
		case BANANA:
			System.out.println(93 + "kcal");
			break;
			
		}	
	}
}
// 실행결과
//  Call Constructor APPLE
//  Call Constructor PEACH
//  Call Constructor BANANA
//  57kcal
// >> Call Constructor가 출력된 것은 생성자 Fruit가 호출되었음을 의미한다. 
//    이것이 3번 호출되었다는 것은 필드의 숫자만큼 호출되었다는 뜻이다. 즉 enum은 생성자를 가질 수 있다.


// 생성자의 매개변수를 통해서 필드(APPLE..)의 인스턴스 변수 값을 부여할 수 있다. 
enum Fruit {
	APPLE("red"), PEACH("pink"), BANANA("yellow"); //  Fruit의 상수를 선언하면서 동시에 생성자를 호출하고 있다.
	
//	아래 코드는 생성자다. 생성자의 매개변수로 전달된 값은 this.color를 통해서 301행의 인스턴스 변수의 값으로 할당된다.
	public String color;   // 전역변수
	Fruit(Stirng color) {    // 매개변수(= 지역변수)
		System.out.println("Call Construtor" +this);
		this.color = color;   // this가 있는 것은 전역변수를 의미하고, 없는 것은 매개변수 즉 지역변수를 의미한다.
	}
}

enum Company {
	COOGLE, APPLE, ORACLE;
}

public class ConstantDemo {
	
	public static void mian(Stirng[] args) {
		
//		if(Fruit.APPLE == Company.APPLE){
//            System.out.println("과일 애플과 회사 애플이 같다.");
//        }
		
	Fruit type = Fruit.APPLE;
	switch(type) {
	case APPLE:
		System.out.println(57 + "kcal,"+Fruit.APPLE.color);  // APPLE에 할당된 Fruit 인스턴스의 color 필드를 반환하게 된다.
		break;
		
	case PEACH:
		System.out.println(34 + "kcal"+Fruit.PEACH.color);
		break;
	
	case BANANA:
		System.out.println(93 + "kcal"+Fruit.BANANA.color);
		break;
	}	
  }
}


// 열거형은 메소드를 가질수도 있다. 아래 코드는 위의 예제와 동일한 결과를 출력한다.
enum Fruit {
	APPLE("red"), PEACH("pink"), BANANA("yellow");
	
	public String color;
	Fruit(String color) {
		System.out.println("Call Construtor" +this);
		this.color = color;

	}
	
	String getcolor() {
		return this.color;
		
	}
}

enum Company {
	COOGLE, APPLE, ORACLE;
}

public class ConstantDemo {
	
	public static void main(String[] args) {
	    Fruit type = Fruit.APPLE;
	    switch(type) {
	    case APPLE:
	    	System.out.println(57 + "kcal,"+Fruit.APPLE.getcolor());  
			break;
	    
	    case PEACH:
	    	System.out.println(34 + "kcal"+Fruit.PEACH.getcolor());  
			break;
	    
	    case BANANA:	
			System.out.println(93 + "kcal"+Fruit.BANANA.getcolor());  
			break;	
			
	    }		
	}
}


// enum은 맴버 전체를 열거 할 수 있는 기능도 제공한다.
// 열거형은 연관된 값들을 저장한다. 또 그 값들이 변경되지 않도록 보장한다. 
// 뿐만 아니라 열거형 자체가 클래스이기 때문에 열거형 내부에 생성자, 필드, 메소드를 가질 수 있다.
enum Fruit {
	APPLE("red"), PEACH("pink"), BANANA("yellow")
	
	private String color;
	Fruit(String color) {
		System.out.println("Call Constructor "+this);
        this.color = color;
		
	}
	
	String getcolor() {
		return this.color;
			
	}
}

enum Company {
	COOGLE, APPLE, ORACLE;
}

public class ConstantDemo {
	
	public static void main(Stirng[] args) {
		for(Fruit f : Fruit.valuse()) {    // valuse()가 호출되면서 Fruit이 가지고 있는 데이터들이 f에 담기게 됨.
//			:뒤에는 어떠한 집합이 오는 것이고 앞에는 그 데이터 집합의 소속되어 있는 것을 하나하나 꺼내서 변수(f)에 담아주는 것이다.
			
			System.out.println(f+ " , " +f.getcolor());
			
		}
	}
}
//    .valuse()라는 메소드
// >> 열거형의 어떠한 데이터가 있는지 몰라도 마치 배열처럼 그 안에 들어있는 열거형이 갖고 있는 데이터를 하나씩 꺼내서 처리할 수 있는 기능










 






















