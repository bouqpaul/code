
public class Cigale extends Insecte {
	
	public Cigale(){
		super(3);
		
	}
	
	
	public void deplace(){
		int tempX = this.getAbscisse();
		tempX = tempX +1;
		this.setAbscisse(tempX);
		
		int tempY = this.getOrdonnee();
		tempY = tempY + 1;
		this.setOrdonnee(tempY);
		System.out.println("Nouvelles coordonnees : "+this.getAbscisse()+"  "+this.getOrdonnee());
	}
	
	public String toString(){
		return "Je suis une Cigale "+super.toString();
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Cigale C = new Cigale();
		//C.deplace();
		System.out.println(C);

	}

}
