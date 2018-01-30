/**
 * 
 */

/**
 * @author bouquepa
 *
 */
public class HelloWorld {

	/**
	 * @param args
	 */
	public static void Affichage(String nom){
		System.out.println("Hello "+ nom +" !");		
	}
	
	public static void AffichageLst(String[] LstNom){
		int n =  LstNom.length;
		for(int i = 0;i < n; i++){
			Affichage(LstNom[i]);
			
		}
	}
		
		
		
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String Nom[] = {"Toto", "Tata", "Titi", "Tutu"};
		AffichageLst(Nom);

	}

}
