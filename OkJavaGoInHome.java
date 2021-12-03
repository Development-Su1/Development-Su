// import는 불러오는 것인데 뒤에 오는 클래스를 불러오는 것이다.  
// 이것을 써주면 구지 길게 써주지 않아도 된다. ( Elevator = org.opentutorials.iot.Elevator;)
import org.opentutorials.iot.Elevator;   
import org.opentutorials.iot.Security;
import org.opentutorials.iot.Lighting;
 
public class OkJavaGoInHome {

	public static void main(String[] args) {
		
//		String id = "JAVA APT 203";로 하면 밑에 "JAVA APT 203"부분을 id(id+)로 바꾸면 똑같이 출력됨
		
		// Elevator Call
		Elevator myElevator = new Elevator("JAVA APT 203");
		myElevator.callForUp(1);
		
		// Security off   (보안 해제)
		Security mySecurity = new Security("JAVA APT 203");
		mySecurity.off();
		
		//Light on
		Lighting hallLamp = new Lighting("JAVA APT 203 / Hall Lamp");  // JAVA APT 203의 Hall Lamp를 의미
		hallLamp.on();
		
	}

}
