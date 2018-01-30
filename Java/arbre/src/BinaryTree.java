//package arbre;
/**
 * classe arbre binaire
 * 
 */
public class BinaryTree {
	/** Racine de l'arbre */
	protected Node root;
	/** lien vers la classe permettant d'affichier l'arbre */
	private TreePrinter printer;

	/**
	 * constructeur
	 * @param printer afficheur d'arbre
	 * 
	 */
	public BinaryTree(TreePrinter printer) {
		this(null,printer);
	}

	/**
	 * constructeur
	 * 
	 * @param myRoot
	 *            racine de l'arbre
	 * @param printer afficheur d'arbre
	 * 
	 */
	public BinaryTree(Node myRoot,TreePrinter printer) {
		root = myRoot;
		this.printer = printer;
	}

	/**
	 * Modification de la racine
	 * 
	 * @param n
	 *            nouvelle racine
	 * 
	 */
	public void setRoot(Node n) {
		root = n;
		n.setParent(null);
	}

	/**
	 * Recuperation de la racine
	 * 
	 * @return la racine
	 */
	public Node getRoot() {
		return root;
	}

	/** init de l'arbre */
	public void initTree() {
		setHeight();
	}


	/**
	 * @return the printer
	 */
	public TreePrinter getPrinter() {
		return printer;
	}

	/**
	 * recuperation de la hauteur de l'arbre
	 * 
	 * @return hauteur
	 */
	public int getHeight() {
		return root.getHeight();
	}

	/** calcule la hauteur de l'arbre */
	public void setHeight() {
		setHeight(root);
	}

	/**
	 * calcule la hauteur de l'arbre sous un noeud donne
	 * 
	 * @param n
	 *            noeud courant
	 */
	private void setHeight(Node n) {
		if (n != null) {
			setHeight(n.getLeft());
			setHeight(n.getRight());
			n.setHeight();
		}
	}

	/**
	 * convertit l'arbre en chaine de caracteres
	 */
	public String toString() {
		return toString(root, 0);
	}

	/**
	 * convertit l'arbre en chaine de caracteres : methode recursive
	 */
	private String toString(Node n, int niv) {
		if (n == null)
			return "";
		else
			return toString(n.getLeft(), niv + 1) + n.toString(niv)
					+ toString(n.getRight(), niv + 1);
	}

	/**
	 * Fonction iterative de recherche d'element dans un arbre
	 * 
	 * @param value
	 *            valeur a rechercher
	 * @return le premier noeud de la valeur cherchee
	 */
	public Node search(int value) {
		
		// TODO a completer
		int valCourant = this.root.getValue();
		if(valCourant == value){
			return this.root;
		}
		else if(valCourant > value){
			this.search(this.root.getLeft().getValue());
			
		}
		else{
			this.search(this.root.getRight().getValue());
			}
			
			
			
		return null;
	}

	/**
	 * Recherche du plus petit element de l'arbre
	 * 
	 * @return le plus petit element ou null si l'arbre est vide
	 */
	public Node searchMin() {
		
		// TODO a completer

		return null;
	}

	/**
	 * parcours prefixe de l'arbre
	 * 
	 * @return resultat du parcours de l'arbre sous forme de chaine de
	 *         caracteres
	 */
	public String prefix() {
		return prefix(root);
	}

	/**
	 * parcours prefixe de l'arbre
	 * 
	 * @param n
	 *            noeud de depart du parcours
	 * @return la chaine de caracteres contenant les valeurs des noeuds dans
	 *         l'ordre prefixe
	 */
	private String prefix(Node n) {

		// TODO a completer

		return "";
	}

	/**
	 * parcours infixe de l'arbre
	 * 
	 * @return resultat du parcours de l'arbre sous forme de chaine de
	 *         caracteres
	 */
	public String infix() {
		return infix(root);
	}

	/**
	 * parcours infixe de l'arbre
	 * 
	 * @param n
	 *            noeud de depart du parcours
	 * @return la chaine de caracteres contenant les valeurs des noeuds dans
	 *         l'ordre infixe
	 */
	private String infix(Node n) {
		
		// TODO a completer

		return "";
	}

	/**
	 * parcours postfixe de l'arbre
	 * 
	 * @return resultat du parcours de l'arbre sous forme de chaine de
	 *         caracteres
	 */
	public String postfix() {
		return postfix(root);
	}

	/**
	 * parcours postfixe de l'arbre
	 * 
	 * @param n
	 *            noeud de depart du parcours
	 * @return la chaine de caracteres contenant les valeurs des noeuds dans
	 *         l'ordre postfixe
	 */
	private String postfix(Node n) {
		
		// TODO a completer
		
		return "";
	}

	/**
	 * insere une valeur dans l'arbre reequilibre l'arbre apres l'insertion
	 * 
	 * @param value
	 *            valeur a inserer
	 */
	public void insert(int value) {
		Node n = printer.createNode(value);
		insert(n);
	}

	/**
	 * insere un element dans l'arbre
	 * 
	 * @param n
	 *            noeud a inserer
	 */
	public void insert(Node n) {
		// ne pas inserer d'element null
		if (n != null) {
			n.setHeight();
			// premier noeud de l'arbre
			if (root == null)
				root = n;
			else
				// appel de la methode recursive
				insert(root, n);
		}
	}

	/**
	 * insere un element dans l'arbre
	 * 
	 * @param pere
	 *            noeud sous lequel inserer l'element
	 * @param n
	 *            noeud a inserer
	 */
	protected void insert(Node pere, Node n) {
		printer.update(pere);
		
		// TODO a completer

		
		// mise a jour de la hauteur du pere
		pere.setHeight();
	}



	/**
	 * supprime un element de l'arbre
	 * 
	 * @param value
	 *            valeur noeud a supprimer
	 */
	public void suppress(int value) {
		suppress(printer.createNode(value));
	}

	/**
	 * supprime un element de l'arbre
	 * 
	 * @param n
	 *            noeud a supprimer
	 */
	public void suppress(Node n) {
		// ne pas supprimer d'element null
		if (n != null) {
			n.setHeight();
			// premier noeud de l'arbre
			if (root != null)
				suppress(root, n);
		}
	}

	/**
	 * supprime un element de l'arbre
	 * 
	 * @param pere
	 *            noeud sous lequel supprimer l'element
	 * @param n
	 *            noeud a supprimer
	 */
	protected void suppress(Node pere, Node n) {
		printer.update(pere);
		
		// TODO a completer

	}

	public static void main(String args[]) {
		BinaryTree arbre = new BinaryTree(new TTreePrinter());

		// pour chaque valeur passe en parametre
		for (int i = 0; i < args.length; i++) {
			// ajouter un Node dans la liste
			arbre.insert(new Node(Integer.parseInt(args[i])));
		}
		// afficher l'arbre
		System.out.println();
		System.out.println(arbre);

	}

}
