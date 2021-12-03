import java.io.BufferedWriter;
import java.sql.SQLOutput;

import javax.sql.rowset.serial.SQLOutputImpl;

import org.jcp.xml.dsig.internal.SignerOutputStream;

// 메소드 (코드를 재사용할 수 있게 해준다.)
// void main(String[] args) {  << 이것이 메소드이다.
// 메소드를 만들 때 public static이라고 적어야 한다.

// 메소드의 정의와 호출
// 직접 메소드를 만드는 것을 정의, 만들어진 메소드를 실행하는 것을 호출
// 결과값은 0 1 2 3 4 5 6 7 8 9
public class method {

	public static void numbering() {
		int i = 0;
		while (i < 10) {
			System.out.println(i);
			i++;
		}
		
	}

	public static void main(String[] args) {
		numbering();
	}
}

//  37행처럼 numbering();이라고하면 26행인 메소드 numbering의 로직이 실행된다.
//  [정의]
//	public static void numbering() {
//		int i = 0;
//		while (i < 10) {
//			System.out.println(i);
//			i++;
//		}
//		
//	}

//   [호출]
//   public static void main(String[] args) {
//	    numbering();
//  }
//  }

 
// 1. 재활용
//  결과값이 5번 실행된다.
public class MethodDemo3 {
    public static void numbering() {
        int i = 0;
        while (i < 10) {
            System.out.println(i);
            i++;
        }
    }
 
    public static void main(String[] args) {
        numbering();
        numbering();
        numbering();
        numbering();
        numbering();
    }
}

 
// 입력값
// 매개변수(int limit)와 인자(5)
// [방법 1]
// 필요에 따라서 0부터 4까지 출력하고 싶거나 0부터 8까지 출력하고 싶다면 어떻게 해야 할까?
// 입력 값에 따라서 다른 출력 값을 갖도록 메소드를 정의하면 된다. 
// 결과는 0부터 4까지 출력한다. 
// 메소드 numbering의 괄호 안에 위치한 숫자 5는 이 메소드가 호출될 때 limit이라는 변수의 값이 된다. 
public class MethodDemo4 {
    public static void numbering(int limit) {
        int i = 0;
        while (i < limit) {
            System.out.println(i);
            i++;
        }
    }
 
    public static void main(String[] args) {
        numbering(5);
    }
}

// [방법 2]
// 위의 코드는 아래의 코드와 동일한 의미를 갖는다. 
public static void numbering() {
    int limit = 5;
    int i = 0;
    while (i < limit) {
        System.out.println(i);
        i++;
    }
}

// 복수의 인자
// 메소드로 여러개의 입력값을 전달하고 싶다면 어떻게 해야 할까?
// 출력할 숫자의 시작 값과 마지막 값을 입력값으로 전달하면 됨.
// 결과는 1부터 4까지가 출력된다.

public class MethodDemo5 {
	 
    public static void numbering(int init, int limit) {
        int i = init;
        while (i < limit) {
            System.out.println(i);
            i++;
        }
    }
 
    public static void main(String[] args) {
        numbering(1, 5);
    }
 
}


// 출력값 1
// return
// return 뒤에 따라오는 값을 메소드의 결과로 반환한다. 동시에 메소드를 종료시킨다.
// String numbering은 numbering라는 변수는 반드시 문자열을 받는 즉 return하는 변수라는 뜻이다.
public class MethodDemo6 {
	
	// return을 통해서 반환할 값의 데이터 형식을 메소드의 이름 옆에 명시해주어야 한다.
	// 만약 반환 값이 없다면 아래와 같이 void를 적어준다.
	public static String numbering(int init, int limit) {  
        int i = init;
        String output = "";    // 만들어지는 숫자들을 output이라는 변수에 담기 위해서 변수에 빈 값을 주었다.
        while (i < limit) {
            output += i;     // 숫자를 화면에 출력하는 대신 변수 output에 담았다.
            i++; 
        }
        // 중요!!! output에 담겨 있는 문자열을 메소드 외부로 반환하려면 아래와 같이 return 키워드 뒤에 반환하려는 값을 배치하면 된다.
        return output;
    }
 
    public static void main(String[] args) {   // 반환 값이 없다면 void를 적어준다.
        String result = numbering(1, 5);    // 메소드 numbering이 리턴한 값이 변수 result에 담긴다.
        System.out.println(result);     // 변수 result의 값을 화면에 출력한다.
    }
}

// 출력값 2
// FileWriter은 파일에 기록한다는 것
public class MethodDemo7 {
	public static String numbering(int init, int limit) {
		int i = init;
		String output = "";
		while (i < limit) {
			output += i;
			i++;		
		}
		return output;
	}
	
	public static void main (String[] args) {
		String result = numbering (1, 5);
		System.out.println(result);
		   BufferedWriter out = new BufferedWriter(new FileWriter("out.txt"));
		   out.write(result);
		   out.close();
	   // 165~167행 코드는 out.txt라는 파일을 만들고 그 파일에 result라는 값을 기록하는 방법의 코드다.  

	}


// return은 값을 반환하는 동작을 한다. 그런데 return은 메소드를 중단시키는 역할도 한다. 
// 위의 코드는 컴파일조차 되지 않는다.
// 왜냐하면, return 은 메소드를 종료시키는 역할을 하므로 return 1이 처음 등장한 이후의 구문인 2,3은 실행되지 않기때문이다.	
public class returnDemo {
	public static int one() {
		return 1;
		return 2;
		return 3;
	}
	
	public static void main (String[] args) {
		System.out.println(one());
	}
}

// 하지만 아래의 예제는 문제가 전혀 없다.
// return이 여러 번 등장하지만 return이 중복적으로 실행될 가능성이 없기 때문이다. 
// return "none";를 제거하면 컴파일이 되지 않을 것이다. 
public class returnDemo2 {
	public static String num(int i) {
		if (i == 0) {
			return "Zero";
		} else if (i==1) {    // true이기 떄문에 출력됨. 이 이후에는 출력안됨
			return "one";
		} else if (i == 2) {
			return "two";
		}
		return "none";
	}
	
	public static void main (String[] args) {
		System.out.println(num(1));   // i에 1 대입
	}
	
	
}


// 복수의 return
// 메소드는 여러 개의 입력 값을 가질 수 있다. 그렇다면 여러 개의 값을 출력하고 싶다면? 
// 자바는 문법적으로 그런 기능을 제공하지 않는다. 하나의 변수에 여러개의 값을 담아서 출력하면 된다.
// 하나의 메소드는 하나의 값만을 반환할 수 있기 때문에 각각의 회원정보를 반환하는 메소드를 만들었다.
public class returnDemo3 {
	public static String getMember1() {
		return "최진혁";
	}
	
	public static String getMember2() {
		return "최유빈";
	}
	
	public static String getMember3() {
		return "한이람";
	}
	
	public static void main (String[] args) {
		System.out.println(getMember1());
		System.out.println(getMember2());
		System.out.println(getMember3());
	}
}


// 맴버를 담고 있는 배열을 반환하고 있다. 메소드 getMembers가 리턴한 배열을 members 변수에 담았다. 
// 이 변수를 이용해서 여러 개의 데이터를 처리 할 수 있게 된다. 
// String[] getMembers()의 뜻은 getMembers()가 return한 return값이 문자열의 데이터를 담을 수 있는 배열이다.  
public class returnDemo4 {
	public static String[] getMembers() {
		String[] members = {"최진혁", "최유빈", "한이람"};
		return members;
	}
	
	public static void main (String[] args) {
		String[] members = getMembers();
	}
}









