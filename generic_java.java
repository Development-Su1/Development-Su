// 제네릭
// 클래스 내부에서 사용할 데이터 타입을 외부에서 지정하는 기법
class Person<T> {  
	public T info;  // Person의 필드 info의 데이터 타입은 T로 되어있다. 그런데 T라는 데이터 타입은 존재하지 않는다.
}

public class GenericDemo {
	
	public static void main(String[] args) {
		Person<String> p1 = new Person<String>();  // 3행의 T는 <>안에 지정된 데이터 타입에 의해서 결정된다.
		Person<StringBuilder> p2 = new Person<StringBuilder>();	
	}
}
// 데이터 타입 결과
// 이것은 각각의 인스턴스를 생성할 때 사용한 <> 사이에 어떤 데이터 타입을 사용했느냐에 달려있다.
// p1.info : String
// p2.info : StringBuilder

// 제네릭 
// 클래스를 정의할 때는 info의 데이터 타입을 확정하지 않고 인스턴스를 생성할 때 데이터 타입을 지정하는 기능


// 타입의 안정성
class StudentInfo {
	public int grade;
	StudentInfo(int grade){ this.grade = grade; }	
}

class StudentPerson {
    public StudentInfo info;
    StudentPerson(StudentInfo info) { this.info = info; } 	
}

class EmployeeInfo {
	public int rank;
	EmployeeInfo(int rank) { this.rank = rank; }
}

class EmployeePerson {
	public EmployeeInfo info;
	EmployeePerson(EmployeeInfo info) { this.info = info; }
}

public class GenericDemo {
	public static void main(String[] args) {
		StudentInfo si = new StudentInfo(2);
		StudentPerson sp = new StudentPerson(si);
		 System.out.println(sp.info.grade);   // 2
		
		EmployeeInfo ei = new EmployeeInfo(1);
		EmployeePerson ep = new EmployeePerson(ei);
		 System.out.println(ep.info.rank);  // 1
		
	}
}
// StudentPerson과 EmployeePerson가 사실상 같은 구조를 가지고 있다. 
// 중복이 발생하고 있는 것이다. 중복을 제거해보자.
class StudentInfo {
	public int grade;
	StudentInfo(int grade) { this.grade = grade; }  	
}

class EmployeeInfo {
	public int rank;
	EmployeeInfo(int rank) { this.rank = rank; }
}

class Person {  
	public Object info;  
	// StudentInfo와 EmployeeInfo의 공통의 조상을 데이터 타입으로 지정을 하면 되는 것이다.
	// 그런데 현재 저 두개의 공통 조상이 없다.
	// 그래서 모든 클래스들의 조상인 Object를 사용했다. 따라서 어떠한 클래스의 인스턴스도 올 수 있다.
	Person(Object info) { this.info = info; }
}

class GenericDemo {
	public static void main(String[] args) {
		person p1 = new Person("부장");
		EmployeeInfo ei = (EmployeeInfo)p1.info;
	 // p1에 있는 info는 Object라는 일반적인 데이터 타입이다.
	 // 그런데 ei에 담길 데이터는 EmployeeInfo라고 하는 매우 구체적인 데이터 타입이기 때문에 형변환을 해주어야 한다.
	 // 형변환을 해줄 때는 ()를 써주고 그안에 구체적인 데이터 타입을 써주면 된다.
		System.out.println(ei.rank);
		
	}
}
// 위의 코드는 컴파일이 성공적이지만 실행을 하면 에러가 발생한다.
// 클래스 person의 생성자는 매개변수 info의 데이터 타입이 object이기 때문인데 이는 다시말해 모든 객체가 될 수 있는 것이다.
// 그렇기 때문에 위와 EmployeeInfo의 객체가 아니라 String이 와도 컴파일 에러가 발생하지 않는다. 대신 런타임 에러가 발생할 수 있다.
// 컴파일의 기본은 모든 에러는 컴파일이 발생할 수 있도록 유도하는 것이다.
// 런타임은 실제로 애플리케이션이 동작하고 있는 상황이기 때문에 런타임에 발생하는 에러는 항상 심각한 문제를 초해할 수 있다.
// 즉, 모든 타입이 올 수 있기 때문에 타입을 엄격하게 제한할 수 없게 된다.


// 제네릭화
// intValue();를 호출 >> Int 타입의 데이터타입으로 돌려주는 메소드이다.(원래값가져오기)
class StudentInfo {
	public int grade;
	StudentInfo(int grade) { this.grade= grade; }
}

class EmployeeInfo {
	public int rank;
	EmployeeInfo(int rank) { this.rank = rank; }
}

class Person<T> {
	public T info;
	Person(T info) { this.info = info; }
}

public class GenericDemon {
	public static void main(String[] args) {
	Person<EmployeeInfo> p1 = new Person<EmployeeInfo>(new EmployeeInfo(1));	
	EmployeeInfo ei1 = p1.info;	
	System.out.println(ei1.rank);   // 성공
	
	Person<String> p2 = new Person<Stirng>("부장");
	String si2 = p2.info;
	System.out.println(si2.rank);  // 컴파일 실패
	
	Person<StudentInfo> p3 = new Person<StudentInfo>(new StudentInfo(2));
	StudentInfo si = p3.info;
	System.out.println(si.grade);
	
	
	}
}
// p1은 잘 동작한다. 
// p2는 컴파일 오류가 발생한다. p2.info가 String이고 String은 rank 필드가 없는데 이를 호출하고 있기 때문이다.


// 복수의 제네릭 (클래스 내에서 여러개의 제네릭을 필요로 하는 경우)
class EmployeeInfo {
	public int rank;
	EmployeeInfo(inr rank) { this.rank = rank; }
}

class Person<T, S> {
	public T info;
	public S id;
	Person(T info, S id) {
	this.info = info;
	this.id =id;
	}
}

public class GenericDemo{
	public static void main(Stirng[] args) {
	Person<EmployeeInfo, int> p1 = new Person<EmployeeInfo, int>(new EmployeeInfo(1), 1); 	
	}
}
// 위와 같이 복수 즉 여러개를 해줄 때에는 콤마(,)로 해주면 된다.
// 위의 예제는 에러가 발생하는 것이기에 형태만 본다.


// 위 예제의 오류를 해결해보자
// 기본 데이터 타입과 제네릭
// 제네릭은 참조 데이터 타입(클래스, 인터페이스, 배열)에 대해서만 사용할 수 있다. 기본 데이터 타입에서는 사용할 수 없다.
class EmployeeInfo {
	public int rank;
	EmployeeInfo(int rank) { this.rank = rank; }
}

class Person<T, S> {
	public T info;
	public S id;
	Person(T info, S id) {
	this.info = info;
	this.id = id;
	
	}
}

public class GenericDemo{
	public static void main(Stirng[] args) {
	EmployeeInfo e = new EmployeeInfo(1);
	Integer i = new Integer(10);
	Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(e, i);
	System.out.println(p1.id.Integer);

	}
}
// Integer은 기본 데이터 타입인 int를 참조 데이터 타입으로 변환해주는 역할을 한다.
// 이러한 클래스를 Wrapper 클래스라고 한다.
// 덕분에 기본 데이터 타입을 사용할 수 없는 제네릭에서 int를 사용할 수 있었다.
// 제네릭은 생략이 가능하다.


// 메소드에 적용
class EmployeeInfo {
	public int rank;
	EmployeeInfo(int rank) { this.rank = rank; }
}

class Person<T, S> {
	public T info;
	public S id;
	Person(T info, S id) {
		this.info = info;
		this.id = id;
		
	}
	
	public <U> void printInfo(U info) {   
	// 메소드 안에서 info라고 하는 매개변수를 사용하는데 이 매개변수의 데이터 타입을 아직 확정하고 싶지 않을 때 <U>로 써준다.
		System.out.println(info);
    }
}

public class GenericDemo {
	public static vodi main(String[] args) {
		EmployeeInfo e = new EmployeeInfo(1);
		Integer i = new Integer(10);
		Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(e, i);
		p1.<EmployeeInfo>printInfo(e);
	//	<EmployeeInfo>은 205행에 <U>이다.
		p1.printInfo(e);
	//  216행의 코드를 생략하면 된다. 왜냐하면 <EmployeeInfo>은 생략이 가능하기 때문이다.
	}
}


// 제네릭의 제한
// extends
// 제네릭으로 올 수 있는 데이터 타입을 특정 클래스으 자식으로 제한할 수 있다.
abstract class Info {  // EmployeeInfo의 부모 클래스를 Info라고 정의하였다.
	public abstract int getLevel();  
}

class EmployeeInfo extends Info {  // 그 자식인 EmployeeInfo가 getLevel이라고 하는 메소드를 구현하고 있다.
	public int rank;
	EmployeeInfo(int rank) { this.rank = rank; }
	public int getLevel() {
		return this.rank;	
		
	}
}

class Person<T extends Info> {   // Person의 T는 info 클래스나 그 자식 외에는 올 수 없다.
	public T info;
	Person(T info) { this.info = info; }
}

public class GenericDemo{
	public static void main(String[] args) {
		Person p1 = new Person(EmployeeInfo(1));
		Person<String> p2 = new PersonInfo<String>("부장");
	}
}

// extends은 상속뿐만 아니라 구현에서도 사용할 수 있다.
interface Info {
	int getLevel;
}

class EmployeeInfo implements Info{
	public int rank;
	EmployeeInfo(int rank) { this.rank = rank; }
	public int getLevel() {
		return this.rank;
	}
}

class Person<T extends Info> {  // 여기서 extends는 Info의 부모가 누구냐를 묻는 것이기 때문에 써도 된다.
	public T info;
	Person(T info) { this.info = info; }
}

public class GenericDemo{
	public static void main(String[] args) {
		Person p1 = new Person (new EmployeeInfo(1));
		person<String> ps = new Person<String>("부장");
	}
}




















