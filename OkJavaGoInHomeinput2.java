// run 맨 밑에 Organize Favorites는 즐겨찾기다. 저기서 Add를 클릭하여 내가 자주 찾는 목록을 선택하면 된다.

// import는 불러오는 것인데 뒤에 오는 클래스를 불러오는 것이다.   
// 이것을 써주면 구지 길게 써주지 않아도 된다. ( Elevator = org.opentutorials.iot.Elevator;)
import javax.swing.JOptionPane;  // >> 이것은 javax의 swing에 속해있는 JOptionPane이라고 하는 클래스가 로드되었다라는 것이다. 

import org.opentutorials.iot.Elevator;   
import org.opentutorials.iot.Security;
import org.opentutorials.iot.Lighting;
import org.opentutorials.iot.DimmingLights;

public class OkJavaGoInHomeinput2 {

//	paramter, 매개변수(args도 매개변수다.)
//	>> {} 안에서는 args가 사용자가 입력한 값이다.
	public static void main(String[] args) {
		
//		String id = "JAVA APT 203";로 하면 밑에 "JAVA APT 203"부분을 id(id+)로 바꾸면 똑같이 출력됨
		
		String id = args[0];
		String bright = args[1];
//		>> args 라는 parameter(매개변수)를 이용해서 받는다.
//		   값이 여러가지일때는 배열을 이용하여 args[0], args[1] 이런식으로 0번째 1번째 등 순서를 매겨준다. 
//		   이클립에서만 해당되는 것중 하나는 run configuration에 들어가서 arguments 탭에서 그일을 할 수 있다. 
//		   여기서 순서를 구분하는 것은 ' ' 이다. >> ex) 'pusan' '14.0' --> 첫번째 인자는 pusan 두번째 인자는 14.0이 되는것이다.
//		번외) 이유는 모르겠지만 작은따옴표로 인자값을 구분하면 숫자형식오류가 발생해서 큰따옴표로 인자를 구분해주었더니 정상실행이되었다.
		
		
		// Elevator Call
		Elevator myElevator = new Elevator(id);   
		myElevator.callForUp(1);
		
		// Security off   (보안 해제)
		Security mySecurity = new Security(id);
		mySecurity.off();
		
		//Light on
		Lighting hallLamp = new Lighting(id+" / Hall Lamp");  // JAVA APT 203의 Hall Lamp를 의미
		hallLamp.on();
		
		//DimmingLights on
		DimmingLights moodLamp = new DimmingLights(id+" moodLamp");
		moodLamp.setBright(Double.parseDouble(bright));
//		>> 23번인 String bright라는 곳에 가져온 값은 정수인데 바로 위에 넣어야 할 값은 실수(double)이다. << 에러
//      >> 에러 해결방법은?
//		   Double.parseDouble(text[=입력값]);을 써줌. 이것은 입력값으로 들어온 문자를 실수(double)로 바꿔준다.
		moodLamp.on();
		
	}

}
