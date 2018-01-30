//package arbre;


/**
 * Noeuds de l'arbre binaire
 * @author R. Moitie
 *
 */
public class Node {
	/** valeur du noeud */
	protected int value;
	/** fils gauche */
	protected Node left;
	/** fils droit */
	protected Node right;
	/** pere */
	protected Node parent;
	/** hauteur de l'arbre sous le noeud courant */
	private int height;
	
	/**
	 * Constructeur avec parametre : initialise la valeur du noeud. Le noeud suivant est initialise a null
	 * @param val valeur du noeud
	 */
	public Node(int val) {
		this(val, null, null);
	}
	
	/**
	 * Constructeur sans parametre : cree un noeud de valeur 0
	 */
	public Node() {
		this(0);
	}

	/**
	 * Constructeur permettant de creer un noeud pere de 2 fils
	 * @param val valeur du noeud a creer
	 * @param l fils gauche
	 * @param r fils droit
	 */
	public Node(int val, Node l, Node r) {
		super();
		this.value = val;
		this.setLeft(l);
		this.setRight(r);;
		setHeight();
		
	}
	
	public int getValue() {
		return value;
	}

	public void setValue(int val) {
		this.value = val;
	}
	
	/**
	 * @return the left
	 */
	public Node getLeft() {
		return left;
	}

	/**
	 * @param n the left to set
	 */
	public void setLeft(Node n) {
		int hr = 1;
		int hl = 1;
		left = n;
		// calculer la nouvelle hauteur
		if (n != null) {
			// hauteur du fils +1
			hl += n.getHeight();
			System.out.println("Setting " + n.value + "'s parent to " + value);
			n.parent = this;
		}
		if (right != null)
			hr += right.getHeight();
		// mise a jour de la hauteur
		height = (hr > hl) ? hr : hl;
	}

	/**
	 * @return the right
	 */
	public Node getRight() {
		return right;
	}

	/**
	 * @param n the right to set
	 */
	public void setRight(Node n) {
		int hr = 1;
		int hl = 1;

		// positionner le fils droit
		right = n;
		// calculer la nouvelle hauteur
		if (n != null) {
			// hauteur du fils droit +1
			hr += n.getHeight();
			System.out.println("Setting " + n.value + "'s parent to " + value);
			n.parent = this;
		}
		if (left != null)
			hl += left.getHeight();
		// mise a jour de la hauteur
		height = (hr > hl) ? hr : hl;
	}

	/**
	 * @return the parent
	 */
	public Node getParent() {
		return parent;
	}

	/**
	 * @param parent the parent to set
	 */
	public void setParent(Node parent) {
		this.parent = parent;
	}

	/**
	 * acces a la hauteur
	 * @return hauteur sous le noeud
	 */
	public int getHeight() {
		return height;
	}

	/**
	 * calcule la hauteur
	 */
	public void setHeight() {
		int hl, hr;
		// hauteur du sous-arbre gauche
		if (left == null)
			hl = 1;
		else
			hl = left.getHeight() + 1;
		// hauteur du sous-arbre droit
		if (right == null)
			hr = 1;
		else
			hr = right.getHeight() + 1;
		// max des deux hauteurs
		height = (hl > hr) ? hl : hr;
	}

	/**
	 * teste si on est une feuille
	 * @return true si le noeud est une feuille
	 */
	public boolean isLeaf() {
		return (left == null) && (right == null);
	}

	/**
	 * teste si on est la racine
	 * @return true si le noeud est la racine
	 */
	public boolean isRoot() {
		return parent == null;
	}

	/**
	 * teste si on est un fils gauche
	 * @return true si le noeud est un fils gauche 
	 */
	public boolean isLeft() {
		return (parent != null) && (parent.left == this);
	}

	/**
	 * teste si on est un fils droit
	 * @return true si le noeud est un fils droit
	 */
	public boolean isRight() {
		return (parent != null) && (parent.right == this);
	}

	/**
	 * teste l'egalite de 2 noeuds
	 * @param n noeud avec qui comparer le noeud courant
	 * @return true si les noeuds sont egaux
	 */
	public boolean equals(Node n) {
		return this.value == n.getValue();
	}
	
	/**
	 * Compare 2 noeuds entre eux
	 * @param n noeud avec qui comparer le noeud courant
	 * @return un nombre negatif si this<n, 0 si this=n et un nombre positif si this>n
	 */
	public int compareTo(Node n) {
		return this.value - n.getValue();
	}
	
	/**
	 * convertir le noeud en chaine de caracteres
	 */
	public String toString() {
		return value+"";
	}
	
	/**
	 * methode toString annexe
	 * @param niv niveau du noeud
	 * @return chaine decrivant le noeud
	 */
	public String toString(int niv) {
		String res = "";
		for (int i = 0; i < niv; i++)
			res += "  ";
		res += "Node " + value + " hauteur " + height + "\n";
		return res;
	}
}
