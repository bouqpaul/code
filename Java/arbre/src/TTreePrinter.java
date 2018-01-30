
/**
 * Afficheur de type texte
 * @author R. Moitie
 *
 */
public class TTreePrinter extends TreePrinter {

	/* (non-Javadoc)
	 * @see list.ListPrinter#createNode(int)
	 */
	@Override
	public Node createNode(int val) {
		// le noeud cree est de type Node
		return new Node(val);
	}

}
