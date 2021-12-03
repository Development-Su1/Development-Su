//  while (반복문)
//  while (조건) {
//    반복 실행 영역
//  }
//    >>>  Ctrl+C (dnls 나 Cmd+.) 단축키를 이용해서 무한 반복을 중지할 수 있다.

public class java_while {

	public static void main(String[] args) {
		while (true) {                         // 무한 반복을 발생시킨다.  
			System.out.println("Coding Everybody");
		}

	}

}


//   true를 false로 바꾼 아래의 예제를 실행해보자. 
//   반복조건이 false이기 때문에 반복문이 한 번도 실행되지 않을 것이기 때문에 컴파일러가 오류를 발생시키는 것이다.
public class java_while {
	
	public static void main(String[] args) {     
		while (false) {
			System.out.println("Coding Everybody");
		}
	}
	
}

//    아래의 반복문은 i의 값을 1씩 순차적으로 증가시킴으로써 반복의 지속 여부를 결정하고 있다. 
//    변수 i는 관습적으로 반복의 조건으로 사용하는 임의의 변수다. 변수 이름으로 다른 것을 사용해도 무방하다. 
int i = 0;   //  언제까지 반복할 것이냐에 대한 기준점으로 사용이 됨.
// i의 값이 10보다 작다면 true, 크다면 false가 된다. 현재 i의 값은 0이기 때문에 이 반복문은 실행된다.  
 while (i <10) {
	 System.out.println("Coding Everybody"+i);
// Coding Everybody에 i의 값을 더한다. 반복문의 중괄호의 마지막 라인에 도달하면 반복문은 반복문을 재호출한다.
	    i++;   // i=i+1;과 같다. 즉 여기의 값이 위에 +i에 대입되는 것이다.
	}
	 

//     for문
//     for문은 특정한 횟수만큼 반복 실행을 하는 경우에 자주 사용된다. 
//     for (초기화; 종료조건; 반복실행) {
//          반복적으로 실행될 구문
//      }
//   >>  초기화 : 반복문이 실행될 때 1회 실행된다.
 
 public class ForDemo {
	 
	    public static void main(String[] args) {
	        for (int i = 0; i < 10; i++) {
	            System.out.println("Coding Everybody " + i);
	        }
	 
	    }
	 
	}
 
// coding everybody 뒤에 붙는 숫자를 2의 배수하고 싶다면 어떻게 해야 할까? 
int = 0;
 while (i < 10) {
	System.out.println("Coding Everybody"+(i+1)*2);
	i++;
}


//   break
//   반복작업을 중간에 중단시키고 싶다면 어떻게 해야 할까?  break를 사용하면 된다. 
//   종료조건에 따르면 10행이 출력돼야 하는데 5행만 출력되었다. 
//   if(i == 5) 에 의해서 i의 값이 5일 때 break 문이 실행되면서 반복문이 완전히 종료된 것이다. 
//   반복문 안에서 break가 실행되면 반복문을 즉시 종료시킨다. 
 public class BreakDemo {
	 
	    public static void main(String[] args) {
	        for (int i = 0; i < 10; i++) {
	            if (i == 5)
	                break;
	            System.out.println("Coding Everybody " + i);
	        }
	 
	    }
	 
	}


//    continue
//    실행을 즉시 중단하면서 반복은 지속해가게 하려면 어떻게 해야 할까?   
//    숫자 5가 보이지 않는다. i의 값이 5가 되었을 때 실행이 중단됐기 때문이다. 
//    continue 구문은 이 명령이 나타나는 이후의 로직을 실행하지 않도록 한다. 하지만 반복문 자체를 중단하는 것이 아니고 다시 반복문이 실행된다.
public class ContinueDemo {
	 
	    public static void main(String[] args) {
	        for (int i = 0; i < 10; i++) {
	            if (i == 5)
	                continue;
	            System.out.println("Coding Everybody " + i);
	        }
	 
	    }
	 
	}
 
 
 
 
 
 
 
 
 
 

