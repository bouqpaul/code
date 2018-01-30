package animationStarter;
import java.awt.*;
import java.awt.geom.QuadCurve2D;

public class Arc extends Figure{

	int X1;
	int Y1;
	int X2;
	int Y2;
	int X3;
	int Y3;
	
	public Arc(int X1, int Y1, int X2, int Y2,int X3, int Y3){
		this.X1 = X1;
		this.Y1 = Y1;
		
		this.X2 = X2;
		this.Y2 = Y2;
		
		this.X3 = X3;
		this.Y3 = Y3;
	}
	
	public Arc(){
		this(0,0,0,0,0,0);
	}
	
	public Arc(String X1, String Y1, String X2, String Y2, String X3, String Y3){
		this(Integer.parseInt(X1), Integer.parseInt(Y1), Integer.parseInt(X2), Integer.parseInt(Y2), Integer.parseInt(X3), Integer.parseInt(Y3));
	}
	
	public void display(Graphics2D g2){
        
        g2.setPaint (Color.RED);
        
		QuadCurve2D.Double curveLine1 = new QuadCurve2D.Double(X1, Y1, X2, Y2, X3, Y3);
	    g2.draw(curveLine1);
		
	}
}
