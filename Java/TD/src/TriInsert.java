import java.util.Random;


public class TriInsert {
	
	public static int[] Alea(int taille){
		Random rand = new Random ();
		int tab[] = new int[taille];
		for (int i = 0; i < taille; i++) {
			// genere un entier entre 0 et 49 inclus
			tab[i] = rand.nextInt(50);
		}
		return tab;
	}
	
	/*public static int[] Tri(int[] tab){
		
		
		
	}*/

}
