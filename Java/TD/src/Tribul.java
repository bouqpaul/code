/**
 * 
 */

/**
 * @author bouquepa
 *
 */
import java.util.*; // pour Random 

public class Tribul {
	
	public static int[] Alea(int taille){
		Random rand = new Random ();
		int tab[] = new int[taille];
		for (int i = 0; i < taille; i++) {
			// genere un entier entre 0 et 49 inclus
			tab[i] = rand.nextInt(50);
		}
		return tab;
	}
	
	public static void Tri(int tab[]){
		int n = tab.length;
		for(int j = 1; j < n; j++){
			for(int i = 0; i < n-j; i++){
				if(tab[i] > tab[i+1]){
					int temp = tab[i+1];
					tab[i+1] = tab[i];
					tab[i] = temp;
					}
				}
			}
		}
	
	public static String Affichage(int tab[]){
		int n = tab.length;
		String result = new String();
		for(int i = 0; i < n; i++){
			String temp = Integer.toString(tab[i]);
			result = result + temp + " ";
			
		}
		return result;
		
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] NbrAlea = Alea(20);
		System.out.println("Avant tri : " + Affichage(NbrAlea));
		Tri(NbrAlea);
		System.out.println("Après tri : "+ Affichage(NbrAlea));

	}
	
	
}