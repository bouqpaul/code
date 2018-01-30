// utilisation d'entrees-sorties

import java.io.*; // pour vector et random
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;

/** classe permettant de convertir un fichier de donnees */
public class ConversionFichier {
	
	/** objet representant le fichier source */
	private File leFichierSource;
	
	/** objet representant le fichier destination */
	private File leFichierDest;
	
	/**
	 * objet permettant de lire plus facilement les fichier : permet de lire une
	 * ligne
	 */
	private BufferedReader lecteur;
	
	/**
	 * objet permettant d'ecrire plus facilement dans un fichier : permet de
	 * faire des print et println
	 */
	private PrintStream ecrivain;
	
	/** collection contenant les donnees */
	private List<DonneesFichier> lesDonnees;
	
	private List<Double> ecart;

	/** constructeur : initialise les variables d'instance */
	public ConversionFichier(String nomFichS, String nomFichD) {
		
		// ouvrir les fichiers source et dest
		leFichierSource = new File(nomFichS);
		leFichierDest = new File(nomFichD);
		
		// initialiser les flots de lecture et d'ecriture
		lecteur = null;
		ecrivain = null;
		
		// initialiser la collection de donnees		
		lesDonnees = new ArrayList<DonneesFichier>();

		try {
			// creer le flot en lecture
			lecteur = new BufferedReader(new FileReader(leFichierSource));
			
			// creer le flot en ecriture
			ecrivain = new PrintStream(new FileOutputStream(leFichierDest));
			
		} catch (FileNotFoundException e) {
			System.out.println(e);
		}
	}

	/**
	 * teste si une ligne est une ligne de donnees une ligne de donnees ne
	 * contient que des chiffres, points, separateurs
	 * 
	 * @return true si s correspond a une ligne de donnees
	 */
	public boolean estLigneDonnees(String s) {
		// \d = digit
		// \s = whitespace character
		return (s != null && s.matches("^\\s*\\d+[\\d\\s.]*$"));
	}

	/**
	 * decode une ligne de donnees la ligne doit avoir passe le test
	 * estLigneDonnee
	 * 
	 * @param s
	 *            contient 3 reels sous forme de chaine de caracteres separes
	 *            par des espaces
	 * @return cree une donnee correspondant a la ligne contenue dans s
	 */
	public DonneesFichier decodeLigne(String s) {
		String s2[];
		
		// decoupe la chaine suivant les separateurs (espace ou tabulation)
		s2 = s.split("\\s");
		
		// creer la donnee correspondant aux chaines de caracteres
		return new DonneesFichier(s2[0], s2[1], s2[2]);
	}
	
	public void lireFichier(){
		try{
			while(lecteur.ready()){
				String ligne = lecteur.readLine();
				if(this.estLigneDonnees(ligne)){
					DonneesFichier D = this.decodeLigne(ligne);
					lesDonnees.add(D);
				}
			}
		}
		
		catch(IOException e){
			System.out.println(e);
			
		}
	}
	
	public void ecrireResultat(){
		int longueur = this.lesDonnees.size();
		for(int i = 0; i < longueur; i++){
			DonneesFichier D = this.lesDonnees.get(i);
			String s = D.toString();
			ecrivain.println(s);
		}
	}
	
	public void close(){
		this.ecrivain.close();
		try{
			this.lecteur.close();
			}
		catch(IOException e){
			System.out.println(e);
		}
		
	}
	
	public double calcEcart(){
		int longueur = this.lesDonnees.size();
		DonneesFichier last = this.lesDonnees.get(longueur-1);
		DonneesFichier first = this.lesDonnees.get(0);
		double moy = (last.getTemps() - first.getTemps()) / longueur;
		double moyTrunc = BigDecimal.valueOf(moy).setScale(10, RoundingMode.HALF_UP).doubleValue();
		
		System.out.println("TEMPS MOY: " + moy);
		System.out.println("TEMPS MOY TRUNC: " + moyTrunc);
		
		return moyTrunc;
	}
	
	public void ajusteTemps(double tempMoy){
		int longueur = this.lesDonnees.size();
		double t0 = this.lesDonnees.get(0).getTemps();
		for(int i = 1; i < longueur; i++){
			double toto = t0 + i*tempMoy;
			this.lesDonnees.get(i).setTemps(toto);
		}
		
		
	}
	
	public static void main(String[] args) {
		
		ConversionFichier F = new ConversionFichier("/home5/bouquepa/Java/TD3/src/bh42.txt", "/home5/bouquepa/Java/TD3/src/resultat.txt");
		F.lireFichier();
		F.ecrireResultat();
		F.close();
		
		ConversionFichier D = new ConversionFichier("/home5/bouquepa/Java/TD3/src/bh42.txt", "/home5/bouquepa/Java/TD3/src/data_diff1.txt");
		D.lireFichier();
		double ecart = D.calcEcart();
		D.ajusteTemps(ecart);
		D.ecrireResultat();
		D.close();
		
		System.out.println("Done.");
		

	}	
	
	

}