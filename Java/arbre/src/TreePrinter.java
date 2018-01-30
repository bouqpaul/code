//package arbre;


/**
 * Afficheur abstrait d'arbre
 * 
 * @author R. Moitie
 */
public abstract class TreePrinter implements Cloneable {
	/**
	 * L'afficheur a besoin de l'arbre qu'il decrit
	 */
	protected BinaryTree myTree;

	/**
	 * initialisation de l'interface graphique
	 * 
	 * @param ld
	 *          zone dans laquelle afficher l'arbre
	 */
	public void initDisplay(TreeDisplay ld) {
	}

	/**
	 * change la couleur de l'arbre
	 * 
	 * @param color
	 *          nouvelle couleur
	 */
	public void setColor(int color) {
	}

	/**
	 * Met le focus sur un element de l'arbre
	 * 
	 * @param nod
	 *          element a mettre en evidence
	 */
	public void setFocus(Node nod) {
	}

	/**
	 * supprime le focus de tous les elements de l'arbre
	 */
	public void unFocus() {
	}

	/**
	 * mise a jour de l'affichage
	 */
	public void update() {
	}

	/**
	 * mise a jour de l'affichage, et mise en evidence d'un noeud
	 * @param val noeud a mettre en evidence
	 */
	public void update(Node val) {
	}

	/**
	 * creation d'un noeud connaissant sa valeur
	 * @param val valeur du noeud a creer
	 * @return noeud cree
	 */
	public abstract Node createNode(int val);

	public BinaryTree getMyTree() {
		return myTree;
	}

	public void setMyTree(BinaryTree myTree) {
		this.myTree = myTree;
	}

	@Override
	protected TreePrinter clone() throws CloneNotSupportedException {
		TreePrinter lp = (TreePrinter) super.clone();
		lp.setMyTree(myTree);
		return lp;
	}

}
