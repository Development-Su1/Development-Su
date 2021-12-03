
public class and {

	public static void main(String[] args) {
		if (true && true) {       // &&(and)은 좌항과 우항의 값이 모두 참일때 참이 된다.
      	   System.out.println(1);  // 결과는 1이다. and의 좌우항이 모두 true인 것은 첫 번째 조건문 밖에 없기 때문이다. 
      	   
		}

		if (true && false) {         // 둘 중에 하나라도 true가 아니면 false가 되기 때문에 출력되지 않음
			System.out.println(2);
		
		}
		
		if (false && true) {
			System.out.println(3);   // 출력되지 않음
		
		}
		
		if (false && false) {
			System.out.println(4);   // 출력되지 않음
		
		}
		
	}

}

//   논리 연산자를 이용한 사례를 살펴보자. 
//   "id의 값이 egoing이고 password의 값이 111111이면 참이다"
//   즉, and 연산자의 좌항과 우항이 모두 참일 때 전체가 참이 되는 것이다.
public class LoginDemo3 {
    public static void main(String[] args) {
        String id = args[0];
        String password = args[1];
        if (id.equals("egoing") && password.equals("111111")) {
            System.out.println("right");
        } else {
            System.out.println("wrong");
        }
    }
}


//   ||(or)는 좌우항 중에 하나라도 true라면 전체가 true가 되는 논리 연산자다. 
public class OrDemo {
	
	public static void main(String[] args) {
		if (true || true) {          // true가 되어 1이 출력된다.
			System.out.println(1);
		}
		if (true || false) {         // 둘 중에 하나만 true면 저거 전체가 true가 되기 때문에 2가 출력됨.
			System.out.println(2);
		}
		if (false || true) {         // 이것도 마찬가지다.
			System.out.println(3);
		}
		if (false || false) {        // 둘다 false이기 때문에 4는 출력이 안됨.
			System.out.println(4);
		}
		
      }
  }

//    다음 예제는 id 값으로 egoing, k8805, sorialgi 중의 하나를 사용하고 
//    비밀번호는 111111을 입력하면 right 외의 경우에는 wrong를 출력하는 예다.
public class LoginDemo4 {
    public static void main(String[] args) {
        String id = args[0];
        String password = args[1];
        if ((id.equals("egoing") || id.equals("k8805") || id.equals("sorialgi"))
                && password.equals("111111")) {
            System.out.println("right");
        } else {
            System.out.println("wrong");
        }
    }
}


//    !는 부정의 의미로 not이라고 읽는다.
//    Boolean의 값을 역전시키는 역할을 한다.
//    true에 !를 붙으면 false가 되고 false에 !을 붙이면 true가 된다. 아래의 결과는 2다.
public class NotDemo {
	 
    public static void main(String[] args) {
        if (!true) {
            System.out.println(1);
        }
        if (!false) {
            System.out.println(2);
        }
 
    }
 
}




