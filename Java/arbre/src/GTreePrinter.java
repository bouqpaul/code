//package arbre;


/**
 * Afficheur de type graphique
 * @author R. Moitie
 */
public class GTreePrinter extends TreePrinter {
	/**
	 * zone d'affichage
	 */
	private TreeDisplay myDisplay;
	/** couleur des noeuds de l'arbre  */
	private int color;
	/** delai d'insersion d'element en ms  */
	private int delaiInsert;

	/**
	 * initialise l'afficheur
	 * delai d'insertion par defaut : 300ms
	 */
	public GTreePrinter() {
		this(300);
	}
	
	/**
	 * Initialise l'afficheur avec un certain delai d'affichage
	 * @param delai le delai d'affichage
	 */
	public GTreePrinter(int delai) {
		this.delaiInsert = delai;
	}
	
	@Override
	public void initDisplay(TreeDisplay ld) {
		this.myDisplay = ld;
	}

	@Override
	public void setColor(int color) {
		// les couleurs autorisees vont de 0 a 5 inclus
		color %= 6;
		this.color = color;
		// verifie qu'il s'agit bien d'un GNode
		if (myTree.getRoot() instanceof GNode) {
			// affectation de la couleur a tous les noeuds
			setColor(color,myTree.getRoot());
		}
	}

	/**
	 * Methode recursive d'affectation d'une couleur aux noeuds de l'arbre
	 * @param color couleur a donner aux noeuds
	 * @param cur noeud courant
	 */
	public void setColor(int color, Node cur) {
		if (cur != null) {
			((GNode) cur).setColor(color);
			setColor(color, cur.getLeft());
			setColor(color, cur.getRight());
		}
	}
	
	@Override
	public void update() {
		try {
			// pause de delai ms
			Thread.sleep(delaiInsert);
			// recuperation des exceptions
		} catch (InterruptedException e) {
			// si une exception est levee, l'afficher
			System.err.println(e);
		}
		// reafficher la liste
		if (myDisplay != null)
			myDisplay.redrawWindow();
	}

	@Override
	public void unFocus() {
		// verifie qu'il s'agit bien d'un GNode
		if (myTree.getRoot() instanceof GNode) {
			// suppression du focus sur tous les noeuds
			unFocus(myTree.getRoot());
		}
	}
	
	/**
	 * Methode recursive de suppression du focus sur tous les noeuds
	 * @param cur noeud courant
	 */
	public void unFocus(Node cur) {
		if (cur != null) {
			((GNode) cur).setActive(false);
			unFocus(cur.getLeft());
			unFocus(cur.getRight());
		}		
	}

	@Override
	public void setFocus(Node nod) {
		// verifie qu'il s'agit bien d'un GNode
		if (myTree.getRoot() instanceof GNode && nod instanceof GNode) {
			unFocus();
			((GNode)nod).setActive(true);
		}
	}

	public void setDelaiInsert(int delaiInsert) {
		this.delaiInsert = delaiInsert;
	}

	@Override
	public Node createNode(int val) {
		// le noeud cree est de type GNode
		return new GNode(val, this.color);
	}

	@Override
	public void update(Node val) {
		this.setFocus(val);
		this.update();
	}

	@Override
	protected GTreePrinter clone() throws CloneNotSupportedException {
		GTreePrinter glp = (GTreePrinter)super.clone();
		glp.setColor(color);
		glp.setMyTree(myTree);
		glp.setDelaiInsert(0);
		return glp;
	}
}
