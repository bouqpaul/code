import java.util.Random;


public class Insecte {
	private int abscisse;
	private int ordonnee;
	private int faim;
	private int dernierRepas;
	private static Random hasard = new Random();
	
	public Insecte(){
		this.abscisse = 0;
		this.ordonnee = 0;
		this.faim = 0;
		this.dernierRepas = 0;
	}
	public Insecte(int faim){
		new Insecte();
		this.faim = faim;
		this.abscisse = Insecte.hasard.nextInt(20);
		this.ordonnee = Insecte.hasard.nextInt(20);
		
	}

	public int getAbscisse() {
		return abscisse;
	}

	public void setAbscisse(int abscisse) {
		this.abscisse = abscisse;
	}

	public int getOrdonnee() {
		return ordonnee;
	}

	public void setOrdonnee(int ordonnee) {
		this.ordonnee = ordonnee;
	}

	public int getFaim() {
		return faim;
	}

	public void setFaim(int faim) {
		this.faim = faim;
	}

	public int getDernierRepas() {
		return dernierRepas;
	}

	public void setDernierRepas(int dernierRepas) {
		this.dernierRepas = dernierRepas;
	}

	@Override
	public String toString() {
		return "Insecte [abscisse=" + abscisse + ", ordonnee=" + ordonnee + ", dernierRepas=" + dernierRepas + ", faim=" + faim + "]";
	}
	
	public void deplace(){
		System.out.println("Méthode deplace pas définit dans les classes filles !");
		
		
	}
	
	public void mange(){
		//this.dernierRepas = this.dernierRepas + 1;
		this.dernierRepas++;
		if(this.dernierRepas > this.faim){
			System.out.println("Je mange !");
			this.dernierRepas = 0;
			}
		}
	

}
