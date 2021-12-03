// !=  >> 부정을 의미한다. '같다'의 부정은 '같지 않다'이다
// .equals()  >>  문자열을 비교할 때 사용하는 메소드다. 즉, 문자와 문자를 비교하는 방법이다.
// 문자와 문자를 비교할 때는 '=='를 사용하지 않고 .equals를 사용한다.

import java.util.*;
import java.lang.*;
import java.io.*;

public class java_if {

	
	public static void main(String[] args) {
		System.out.println(1==2);  //false
		System.out.println(1==1);  // true
		System.out.println("one"=="two");  //false
		System.out.println("one"=="one");  //true

		System.out.println(1!=2);   //true
		System.out.println(1!=1);   //false
		System.out.println("one"!="two");  //true
		System.out.println("one"!="one");  //false
		
//		String a = "Hello World";
//		String b = new String("Hello World");
//      System.out.println(a==b);
//		System.out.println(a.equals(b));
		
	}
}


//  if문
//       if(true) {
//	           System.out.println("result : true");  //  실행결과는 'result : true'다. if 뒤에 true가 왔기 때문이다.
//	    }


//      if (false) {
//             System.out.println("result : true");  //  아무것도 출력하지 않을 것이다. if절이 false이기 때문이다.
//       } 


//	결과는 12345를 출력할 것이다.

	        if (true) {
	            System.out.println(1);
	            System.out.println(2);
	            System.out.println(3);
	            System.out.println(4);
	        }
	        System.out.println(5);
	        
	        
//   결과는 5만 출력될 것이다.
	        
	        if(false){
	            System.out.println(1);
	            System.out.println(2);
	            System.out.println(3);
	            System.out.println(4);
	        }
	        System.out.println(5);
	    
	        
//   if-else절은 if절의 값이 true일 때 then절이 실행되고, false일 때 else절이 실행된다.    
	        
//	   	 결과는 1이다.
	        public class java_if {
	        	 
	            public static void main(String[] args) {
	                if (true) {
	                    System.out.println(1);
	                } else {
	                    System.out.println(2);  // 실행되지 않는다.
	                }
	         
	            }
	         
	        }    
	 
//		   	 결과는 2이다.
	        if(false){
	            System.out.println(1);  // 실행되지 않는다.
	        } else {
	            System.out.println(2);
	        }
	        

//  else if
//  if절의 값이 true라면 then절이 실행된다. false라면 else if절로 넘어간다.
//	else if절의 값이 true라면 else if then절이 실행된다. false라면 else절이 실행된다.        
//	else if절은 여러 개가 복수로 등장할 수 있고, else는 생략이 가능하다.
//	else절이 else if절보다 먼저 등장할 수 없다.
	        
//	    결과는 2다.    
	        public class java_if {
	        	 
	            public static void main(String[] args) {
	                if (false) {
	                    System.out.println(1);
	                } else if (true) {
	                    System.out.println(2);   // 실행됨
	                } else if (true) {
	                    System.out.println(3);   // true가 처음으로 등장한 구간이 실행되고 if문 else문은 실행되지 않는다.
	                } else {
	                    System.out.println(4);
	                }
	         
	            }
	         
	        }
	
//	     결과는 3이다. 
	        if(false){
	            System.out.println(1);
	        } else if(false) {
	            System.out.println(2);
	        } else if(true) {
	            System.out.println(3);
	        } else {
	            System.out.println(4);
	        }
	        
//	      결과는 4이다.
	        if(false){
	            System.out.println(1);
	        } else if(false) {
	            System.out.println(2);
	        } else if(false) {
	            System.out.println(3);
	        } else {
	            System.out.println(4);
	        }
  
	        
//   	 사용자가 입력한 아이디 값을 체크하는 프로그램을 만들어 볼 것이다. ID의 값으로 egoing을 입력
public class java_Login {
	  public static void main(String[] args) {
	            	String id = args[0];   // 입력값이 들어온다.
	            	if(id.equals("egoing")) {    // id와 egoing의 값이 다르면 false 같으면 true
	            	   System.out.println("right");
	            	}  else {
	            	     system.out.println("wrong");
	            	   }
	            	}
	            }
	
//       위의 예제에서 아이디와 비밀번호를 모두 검증해야 한다면 어떻게 하면 될까? 
//       사용자가 입력한 값과 아이디의 값이 일치하는지를 확인한 후에 일치한다면 비밀번호가 일치하는지 확인한 것이다. 
public class java_Login  {
    public static void main(String[] args) {
        String id = args[0];
        String password = args[1];  
        if (id.equals("egoing")) {
            if (password.equals("111111")) {
                System.out.println("right");    // 비번이 true일 때
            } else {
                System.out.println("wrong");    // 비번이 false일 때
            }
 
        } else {
            System.out.println("wrong");   // id의 값이 false이면 여기서 wrong가 출력된다.
        }
    }
}


//  switch문
//  사용빈도는 적지만 조건이 많다면 switch()문이 로직을 보다 명료하게 보여줄 수 있다. 
//  즉, switch 뒤의 괄호에 숫자로 1이 주어지면 case 1에 해당하는 로직 이후의 모든 case들이 실행된다.
public class java_Switch {
	 
    public static void main(String[] args) {
         
        System.out.println("switch(1)");
        switch(1){
        case 1:
            System.out.println("one");
        case 2:
            System.out.println("two");
        case 3:
            System.out.println("three");
        }
         
        System.out.println("switch(2)");
        switch(2){
        case 1:
            System.out.println("one");
        case 2:
            System.out.println("two");
        case 3:
            System.out.println("three");
        }
         
        System.out.println("switch(3)");
        switch(3){
        case 1:
            System.out.println("one");
        case 2:
            System.out.println("two");
        case 3:
            System.out.println("three");
        }
 
    }
//   결과는 아래와 같다.
//   switch(1)
//   one
//   two
//   three
//   switch(2)
//   two
//   three
//   switch(3)
//   three

//     코드를 바꿔보자.
//     break를 만나면 switch 문의 실행이 즉시 중지된다.
    public class SwitchDemo {
    	 
        public static void main(String[] args) {
             
            System.out.println("switch(1)");
            switch(1){
            case 1:
                System.out.println("one");
                break;
            case 2:
                System.out.println("two");
                break;
            case 3:
                System.out.println("three");
                break;
            }
             
            System.out.println("switch(2)");
            switch(2){
            case 1:
                System.out.println("one");
                break;
            case 2:
                System.out.println("two");
                break;
            case 3:
                System.out.println("three");
                break;
            }
             
            System.out.println("switch(3)");
            switch(3){
            case 1:
                System.out.println("one");
                break;
            case 2:
                System.out.println("two");
                break;
            case 3:
                System.out.println("three");
                break;
            }
     
        }
     
    }
//    결과는 다음과 같다.
//    switch(1)
//    one
//    switch(2)
//    two
//    switch(3)
//    three
    
//    위의 코드는 아래와 같이 if문으로 변경 할 수 있다.
//    if문과 switch문은 서로 대체 가능한 관계다.
    public static void main(String[] args) {
        
        int val = 1;
        if(val == 1){
            System.out.println("one");
        } else if(val == 2){
            System.out.println("two");
        } else if(val == 3){
            System.out.println("three");
        }
 
    }
 
}
    
//     default문
public class SwitchDemo {
	 
    public static void main(String[] args) {
         
        System.out.println("switch(1)");
        switch(1){
        case 1:
            System.out.println("one");
            break;
        case 2:
            System.out.println("two");
            break;
        case 3:
            System.out.println("three");
            break;
        default:
            System.out.println("default");
            break;
        }
         
        System.out.println("switch(2)");
        switch(2){
        case 1:
            System.out.println("one");
            break;
        case 2:
            System.out.println("two");
            break;
        case 3:
            System.out.println("three");
            break;
        default:
            System.out.println("default");
            break;
        }
         
        System.out.println("switch(3)");
        switch(3){
        case 1:
            System.out.println("one");
            break;
        case 2:
            System.out.println("two");
            break;
        case 3:
            System.out.println("three");
            break;
        default:
            System.out.println("default");
            break;
        }
         
        System.out.println("switch(4)");
        switch(4){
        case 1:
            System.out.println("one");
            break;
        case 2:
            System.out.println("two");
            break;
        case 3:
            System.out.println("three");
            break;
        default:
            System.out.println("default");   // switch(4)에서 case4가 없기 때문에 그 값은 default로 출력된다. 
            break;
        }
 
    }
 
}
//  위의 코드는 각 switch 문에 default:가 이끄는 구문을 추가했다. 그 결과는 아래와 같다.
//  가장 마지막은 default로 끝난다. 즉, 주어진 케이스가 없는 경우 default 문이 실행된다는 것을 알 수 있다. 
//  switch(1)
//  one
//  switch(2)
//  two
//  switch(3)
//  three
//  switch(4)
//  default


