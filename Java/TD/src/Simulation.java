import java.util.*;

public class Simulation {
	
	private ArrayList<Insecte> collection;
	private int tourSimulation;
	private static Random hasard = new Random();
	
	public Simulation(int nbInsectes, int nbTours){
		this.tourSimulation = nbTours;
		this.collection = new ArrayList<Insecte>();
		for(int i = 0; i < nbInsectes; i++){
		int alea = hasard.nextInt(2);
		//System.out.println(this.collection.size());
		switch(alea){
		case 0:
			this.collection.add(new Cigale());
			break;
		case 1:
			this.collection.add(new Fourmi());
			break;
		default:
			System.out.println("Erreur");
		}
		
			
		}
	}
	
	public void simule(){
		for(int j = 0; j < this.tourSimulation; j++){
			for(int i = 0; i < this.collection.size(); i++){
				Insecte temp = this.collection.get(i);
				System.out.println(temp);
				temp.deplace();
				temp.mange();
				//this.collection.get(i).mange();
				}
			}
		}
		
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Simulation S = new Simulation(20, 50);
		//System.out.println(Simulation.hasard.nextInt(2));
		S.simule();

	}

}
