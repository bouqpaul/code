package animationStarter;
import java.awt.*;
import java.util.*;

public class Rectangle extends Figure {
	int posX;
	int posY;
	int largeur;
	int hauteur;
	
	public Rectangle(int X, int Y, int larg, int haut){
		this.posX = X;
		this.posY = Y;
		this.largeur = larg;
		this.hauteur = haut;
	}
	
	public Rectangle(){
		this(0, 0, 0, 0);
	}
	
	public Rectangle(String X, String Y, String larg, String haut){
		this(Integer.parseInt(X), Integer.parseInt(Y), Integer.parseInt(larg), Integer.parseInt(haut));
	}
	
	public void display(Graphics2D g2){
		
		g2.setPaint (Color.BLACK);
        g2.drawRect (this.posX, this.posY, this.largeur, this.hauteur);
        }
    }
	
