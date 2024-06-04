import java.awt.*;
import java.applet.*;

public class simpleAppletProgram extends Applet{
	public void init(){
		setForeground(Color.white);
		setBackground(Color.blue);
	}
	public void paint(Graphics g){
		g.drawString("Welcome to Java Applet",40,50);
	}
}
