//package arbre;
/**
 @file TreeDisplay.java
 @author Morgan McGuire, morgan@cs.brown.edu
 @created 2002-09-15
 @edited  2002-09-16
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

/**
 * Renders ordered binary trees with nice colors and 3D shading.
 */
class TreeDisplay extends JPanel {
	/**	 */
	private static final long serialVersionUID = -3657653516952272258L;
	private int width;
	private int height;
	/** Radius of nodes when rendered */
	private final static int radius = 20;

	private BinaryTree tree = null;
	private String caption = "";

	/** Used for tracking node positions when handling mouse events. */
	class Position {
		GNode n;
		int x;
		int y;

		Position(GNode n, int x, int y) {
			this.n = n;
			this.x = x;
			this.y = y;
		}
	}

	private ArrayList<Position> position = new ArrayList<Position>();

	public TreeDisplay(BinaryTree tree, String caption) {
		this.caption = caption;
		this.tree = tree;
		setBackground(java.awt.Color.white);

		// taille du panel
		int largEcran = Toolkit.getDefaultToolkit().getScreenSize().width;
		int hautEcran = Toolkit.getDefaultToolkit().getScreenSize().height;
		width = largEcran * 2 / 3;
		height = hautEcran / 2;
		setSize(width, height);
		Dimension dim = new Dimension(width, height);
		setPreferredSize(dim);
		setMinimumSize(dim);
		// utilisation de la souris
		enableEvents(java.awt.AWTEvent.MOUSE_EVENT_MASK);
	}

	protected void processMouseEvent(MouseEvent e) {
		switch (e.getID()) {
		case MouseEvent.MOUSE_PRESSED:
			// Find the node
			GNode node = null;
			for (int n = 0; n < position.size(); ++n) {
				Position pos = (Position) position.get(n);
				if (Math.sqrt(Math.pow(pos.x - e.getX(), 2)
						+ Math.pow(pos.y - e.getY(), 2)) <= radius) {
					node = pos.n;
					break;
				}
			}

			if (node != null) {
				setActive(node);
			}

			break;
		}
	}

	/**
	 * definir un noeud comme etant actif
	 * 
	 * @param n
	 *            le noeud a rendre actif
	 */
	private void setActive(GNode n) {
		tree.getPrinter().setFocus(n);
		repaint();
		System.out.println("Selection: " + n);
		// tree.debugCheckIntegrity();

	}

	synchronized public void paintComponent(Graphics r) {
		super.paintComponent(r);
		Dimension dim = getSize();
		width = dim.width;
		height = dim.height;
		// Java promises to call this method with a Graphics2D
		Graphics2D g = (Graphics2D) r;
		Rectangle bounds = getBounds();

		Node node = tree.getRoot();

		// Enable anti-aliasing
		g.setRenderingHints(new RenderingHints(RenderingHints.KEY_ANTIALIASING,
				RenderingHints.VALUE_ANTIALIAS_ON));

		g.setFont(new Font("Arial", Font.BOLD, 30));
		g.setColor(java.awt.Color.black);
		g.drawString(caption, 5, bounds.height - 10);
		g.drawRect(0, 0, bounds.width - 1, bounds.height - 1);

		g.setFont(new Font("Arial", Font.BOLD, 16));

		position.clear();

		if (node != null) {
			drawShadows(g, node, width / 2, 25, width / 5);
			draw(g, (GNode)node, width / 2, 25, width / 5);
		}
	}

	private void drawShadows(Graphics2D g, Node n, int x, int y, int width) {
		if (n != null) {
			// final int nextY = y + ySpacing - width / 3;
			final int nextY = y + (height - 25 - 2 * radius) / tree.getHeight();

			g.setColor(new java.awt.Color(.85f, .85f, .85f));
			g.fillOval(x - radius + 15, y - radius + 15, (int) (1.8 * radius),
					(int) (1.8 * radius));

			drawShadows(g, n.getLeft(), x - width, nextY, width / 2);
			drawShadows(g, n.getRight(), x + width, nextY, width / 2);
		}
	}

	static public Color computeColor(GNode n, float a, float b) {
		int j = (n.getColor() % 6) + 1;
		int k = (n.getColor() % 6 + 1) + 1;

		// Extract the 0, 1, and 2 bits
		boolean b0 = (j & 1) == 1;
		boolean b1 = (j & 2) == 2;
		boolean b2 = (j & 4) == 4;

		// Extract the 0, 1, and 2 bits
		boolean c0 = (k & 1) == 1;
		boolean c1 = (k & 2) == 2;
		boolean c2 = (k & 4) == 4;

		if (n.isActive())
			return new java.awt.Color(c0 ? a : b, c1 ? a : b, c2 ? a : b);

		return new java.awt.Color(b0 ? a : b, b1 ? a : b, b2 ? a : b);

	}

	private void draw(Graphics2D g, GNode n, int x, int y, int width) {
		position.add(new Position(n, x, y));

		// final int nextY = y + ySpacing - width / 3;
		final int nextY = y + (height - 25 - 2 * radius) / tree.getHeight();
		g.setColor(java.awt.Color.black);
		if (n.getLeft() != null) {
			g.setColor(java.awt.Color.black);
			g.drawLine(x, y, x - width, nextY);
			draw(g, (GNode)n.getLeft(), x - width, nextY, width / 2);
		}

		if (n.getRight() != null) {
			g.setColor(java.awt.Color.black);
			g.drawLine(x, y, x + width, nextY);
			draw(g, (GNode)n.getRight(), x + width, nextY, width / 2);
		}

		// Draw a 3D shaded sphere for the node
		for (int i = radius; i >= 0; --i) {
			float d = (float) Math.cos((Math.PI / 2) * (i / (double) radius)) * .75f + 0.25f;

			g.setColor(computeColor(n, d, 0.0f));

			g.fillOval(x - radius + (radius - i) / 4 + 1, y - radius
					+ (radius - i) / 4 + 1, radius + i, radius + i);
		}

		// Specular highlight
		for (int i = radius; i >= 0; --i) {
			g.setColor(computeColor(n, 1.0f, Math.min(1.0f,
					1.5f * (1.0f - (float) i / radius))));

			g.fillOval(x - radius / 3 + 1 - i / 2, y - radius / 3 + 1 - i / 2,
					i, i);
		}

		// Circle around node
		g.setColor(java.awt.Color.black);

		int dx2 = 0;
		if (n.getValue() > 9) {
			dx2 = -5;
		}

		// Black outline around text
		g.drawOval(x - radius, y - radius, 2 * radius, 2 * radius);
		for (int dx = -1; dx <= 1; ++dx) {
			for (int dy = -1; dy <= 1; ++dy) {
				g.drawString("" + n.getValue(), x - 5 + dx + dx2, y + 5 + dy);
			}
		}

		// Text
		g.setColor(java.awt.Color.white);
		g.drawString("" + n.getValue(), x - 5 + dx2, y + 5);
	}

	/**
	 * reaffichage de la liste
	 */
	public void redrawWindow() {
		// force l'appel a la methode paintComponent
		if (getGraphics()!=null)
			update(getGraphics());
		repaint(0);
	}
}
