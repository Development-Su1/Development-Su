// import는 불러오는 것인데 뒤에 오는 클래스를 불러오는 것이다.    
// 이것을 써주면 구지 길게 써주지 않아도 된다. ( Elevator = org.opentutorials.iot.Elevator;)
import javax.swing.JOptionPane;  // >> 이것은 javax의 swing에 속해있는 JOptionPane이라고 하는 클래스가 로드되었다라는 것이다. 

import org.opentutorials.iot.Elevator;   
import org.opentutorials.iot.Security;
import org.opentutorials.iot.Lighting;
import org.opentutorials.iot.DimmingLights;

public class OkJavaGoInHomeinput {

	public static void main(String[] args) {
		
//		String id = "Anyang APT 203";로 하면 밑에 "Anyang APT 203"부분을 id(id+)로 바꾸면 똑같이 출력됨
		
		String id = JOptionPane.showInputDialog("Enter a ID");
//		>> 위에 있는 JOptionPane.showInputDialog("Enter a ID");에 의해서 자바가 swing이라는 기술에 
//		   JOptionPane이라고 하는 기능에 .showInputDialog라는 기능을 켜주면 작은 상자가 뜨고 거기에 입력값을 입력할 때까지 
//		   자바는 실행을 멈춰있다가 입력값을 입력하면  JOptionPane.showInputDialog("Enter a ID");의 값이 입력값의 텍스트로 바뀐다.
//		>> ex) 작은 상자에 Anyang APT 203이라고 입력하면 바로 위 코드의 값이 Anyang APT라고 하는 텍스트로 바뀐다. 
		
		String bright = JOptionPane.showInputDialog("Enter a bright level");
		
		// Elevator Call
		Elevator myElevator = new Elevator(id);   
		myElevator.callForUp(1);
		
		// Security off   (보안 해제)
		Security mySecurity = new Security(id);
		mySecurity.off();
		
		//Light on
		Lighting hallLamp = new Lighting(id+" / Hall Lamp");  // Anynag APT 203의 Hall Lamp를 의미
		hallLamp.on();
		
		//DimmingLights on (밝기 조절 램프 켜기)
		DimmingLights moodLamp = new DimmingLights(id+" moodLamp");
		moodLamp.setBright(Double.parseDouble(bright));
//		>> 23번인 String bright라는 곳에 가져온 값은 정수인데 바로 위에 넣어야 할 값은 실수(double)이다. << 에러
//      >> 에러 해결방법은?
//		   Double.parseDouble(text[=입력값]);을 써줌. 이것은 입력값으로 들어온 문자를 실수(double)로 바꿔준다.
//		>> moodLamp는 Lighting이라는 다르게 setBright라는 메소드를 가지고 있다.
		moodLamp.on();
		
	}

}
