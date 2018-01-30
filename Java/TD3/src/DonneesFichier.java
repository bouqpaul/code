
public class DonneesFichier {
	private double temps;
	private double laser1;
	private double laser2;
	
	public DonneesFichier(String tempsStr, String laser1Str, String laser2Str){
		//System.out.println("Constructeur avec des Strings appelé !");
		this.temps = Double.parseDouble(tempsStr);
		this.laser1 = Double.parseDouble(laser1Str);
		this.laser2 = Double.parseDouble(laser2Str);
	
	}
	
	public DonneesFichier(double tempsFlt, double laser1Flt, double laser2Flt){
		this.temps = tempsFlt;
		this.laser1 = laser1Flt;
		this.laser2 = laser2Flt;
	
	}

	public double getTemps() {
		return temps;
	}

	public void setTemps(double temps) {
		this.temps = temps;
	}
	
	public String toString(){
		String res = "Temps: "+this.temps+"\nLaser1: "+this.laser1+"\nLaser2: "+this.laser2+"\n";
		return res;
	}
	
	public static void main(String[] args) {
		DonneesFichier D = new DonneesFichier(1.0, 1.0, 1.0);
		System.out.println(D);

	}
	
	

}
