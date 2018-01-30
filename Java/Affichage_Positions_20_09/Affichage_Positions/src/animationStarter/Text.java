package animationStarter;
import java.awt.*;

public class Text extends Figure {
	private int posX;
	private int posY;
	private String message;
	
	public Text(int X, int Y, String m){
		this.posX = X;
		this.posY = Y;
		this.message = m;
	}
	
	public Text(){
		this(0, 0, "");
		
	}
	
	public Text(String X, String Y, String m){
		this(Integer.parseInt(X), Integer.parseInt(Y), m);
	}
	
	public void display(Graphics2D g2){		
		
		g2.setPaint (Color.RED);
		g2.setFont(new Font("Arial", Font.ITALIC, 12));
		g2.drawString(message, posX, posY);
		
	}
}
