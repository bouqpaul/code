//package arbre;


/**
 * Noeud graphique : sous-classe de Node
 * @author R. Moitie
 */
public class GNode extends Node {
	/**
	 * couleur du noeud
	 */
	private int color;
	/**
	 * le noeud est-il actif ? Sert a mettre des noeuds en evidence
	 */
	private boolean active;
	
	/**
	 * Constructeur de noeuds graphiques
	 * @param val valeur du noeud
	 * @param color couleur du noeud (entre 0 et 5 inclus)
	 */
	public GNode(int val, int color) {
		super(val);
		this.color = color;
		this.active = false;
	}

	/**
	 * Cree un noeud graphique pere de 2 fils
	 * @param val valeur du noeud a creer
	 * @param l fils gauche
	 * @param r fils droit
	 */
	public GNode(int val, Node l, Node r) {
		super(val, l, r);
		this.active = false;
	}

	/**
	 * cree un noeud graphique
	 * @param val valeur du noeud
	 */
	public GNode(int val) {
		this(val, null, null);
	}
	
	public int getColor() {
		return color;
	}

	public void setColor(int color) {
		this.color = color;
	}

	public boolean isActive() {
		return active;
	}

	public void setActive(boolean active) {
		this.active = active;
	}
}
