
public class Fourmi extends Insecte {
	public Fourmi(){
		super(5);
		
	}
	
	public void deplace(){
		int tempAbs = this.getAbscisse();
		tempAbs = tempAbs + 1;
		this.setAbscisse(tempAbs);
	}
	
	public String toString(){
		return "Je suis une Fourmi "+super.toString();
		
	}

}
