// 예외처리
// 아래의 코드를 예로 했을때 배열의 범위를 벗어나게 입력했다는 것을 알 수 있지만, 컴퓨터는 실행하기 전까지 오류가 있다는 것을 알 수 없습니다.
public class trycatchTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        int [] num = new int[4];
        
        System.out.println("num 배열의 최대 길이는 4입니다.");
		
        num[5] = 0;
        System.out.println("num[5]에 값을 입력했습니다.");
       	
	}
}
// 위 코드는 정상적으로 컴파일 및 num[5]까지 실행되다가 num[5]에서 배열이 벗어났다는 오류를 인지한 후 ArrayIndexOutOfBoundsException 에러를 반환합니다.

// 위와 같은 상황을 대비하기 위해 자바는 예외처리문인 try catch문을 제공합니다.
// try >> try문 안에 있는 코드들이 에러가 발생하는 경우 catch문으로 전달합니다.
// catch >> try문에서 발생한 예외처리를 진행합니다. (catch문에서 모든 예외처리를 할 수 있는것은 아닙니다.)


// try catch문
// 맨 위에 있는 코드를 try catch문으로 예외처리한 코드
public class trycatchTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
      try {
    	 int [] num = new int[4];  
         
         System.out.println("num 배열의 최대 길이는 4입니다.");
      
         num[5] = 0;
         System.out.println("num[5]에 값을 입력했습니다.");
     
      } catch (ArrayIndexOutOfBoundsException e) {
    	  System.out.println("배열 길이가 맞지 않습니다.");
      }
       	
	}
}
// try문 내의 num[5]에서 ArrayIndexOutOfBoundsException 에러가 발생했고 catch문에서 예외처리를 진행하였다.


// finally구문
// finally구문은 예외처리가 발생여부를 떠나서 무조건 실행되도록 하는 구문
public class trycatchTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
       try {
    	 int [] num = new int[4];  
         
         System.out.println("num 배열의 최대 길이는 4입니다.");
      
         num[5] = 0;
         System.out.println("num[5]에 값을 입력했습니다.");
      
      } catch (ArrayIndexOutOfBoundsException e) {
    	  System.out.println("배열 길이가 맞지 않습니다.");
      
      } finally {
    	  System.out.println("배열을 다시 선언합니다.");
    	  int [] num = new int[6];
    	  
    	  num[5] = 0;
    	  System.out.println(num[5]);
      }
       
       System.out.println("배열 프로그램을 종료합니다.");
	}
}







