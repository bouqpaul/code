package animationStarter;
import java.awt.*;

public class Ovale extends Figure {

	int posX;
	int posY;
	int largeur;
	int hauteur;
	
	public Ovale(int X, int Y, int larg, int haut){
		this.posX = X;
		this.posY = Y;
		this.largeur = larg;
		this.hauteur = haut;
	}
	public Ovale(){
		this(0,0,0,0);
	}
	
	public Ovale(String X, String Y, String larg, String haut){
		this(Integer.parseInt(X), Integer.parseInt(Y), Integer.parseInt(larg), Integer.parseInt(haut));
	}
	
	public void display(Graphics2D g2){
		
		g2.setPaint (Color.GREEN);
        g2.drawOval(this.posX, this.posY, this.largeur, this.hauteur);
		
	}
}
