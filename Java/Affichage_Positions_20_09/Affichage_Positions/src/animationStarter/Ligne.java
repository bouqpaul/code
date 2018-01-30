package animationStarter;
import java.awt.*;

public class Ligne extends Figure {
	int X1;
	int Y1;
	int X2;
	int Y2;
	
	public Ligne(int X1, int Y1, int X2, int Y2){
		this.X1 = X1;
		this.Y1 = Y1;
		this.X2 = X2;
		this.Y2 = Y2;
		
	}
	public Ligne(String X1, String Y1, String X2, String Y2){
		this(Integer.parseInt(X1), Integer.parseInt(Y1), Integer.parseInt(X2), Integer.parseInt(Y2));
	}
	
	public void display(Graphics2D g2){
		g2.setPaint (Color.BLACK);
		g2.drawLine(X1, Y1, X2, Y2);
	}

}
