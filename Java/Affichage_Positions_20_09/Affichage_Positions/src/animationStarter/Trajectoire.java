package animationStarter;
import java.awt.*;
import java.util.*;

import Tools.Global_Var;

public class Trajectoire {
	
	public ArrayList<Figure> listeFigure;
	
	public Trajectoire(){
		this.listeFigure = new ArrayList<Figure>();
	}
	
	public void display(Graphics2D g2){
		for(Figure F: listeFigure){
			F.display(g2);
			}
	}
		
	public ArrayList<Figure> getListeFigure() {
		return listeFigure;
	}

	public void addFigure(Figure Fig){
		this.listeFigure.add(Fig);
		}
	
}
