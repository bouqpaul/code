//package arbre;


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.*;


/**
* This code was edited or generated using CloudGarden's Jigloo
* SWT/Swing GUI Builder, which is free for non-commercial
* use. If Jigloo is being used commercially (ie, by a corporation,
* company or business for any purpose whatever) then you
* should purchase a license for each developer using Jigloo.
* Please visit www.cloudgarden.com for details.
* Use of Jigloo implies acceptance of these licensing terms.
* A COMMERCIAL LICENSE HAS NOT BEEN PURCHASED FOR
* THIS MACHINE, SO JIGLOO OR THIS CODE CANNOT BE USED
* LEGALLY FOR ANY CORPORATE OR COMMERCIAL PURPOSE.
*/
/**
 * classe Demo demo permettant de tester l'ajout d'elements dans une liste triee
 */
public class Demo extends JFrame {
	private static final long serialVersionUID = 3247989894263255723L;
	/** arbre a afficher */
	private BinaryTree laListe = null;
	/** zone d'affichage de l'arbre */
	private TreeDisplay listDisplay;
	/** panel contenant un bouton go et une zone de saisie */
	private JPanel panelNord;
	/** panel contenant le bouton exit */
	private JPanel panelSud;
	/** bouton insere elem */
	private JButton boutonGo;
	/** bouton insere elem aleatoire */
	private JButton boutonGoRand;
	/** boite de selection de type d'insersion */
	private JComboBox typeParcours;
	/** bouton recherche */
	private JButton boutonRech;
	/** bouton suppr */
	private JButton boutonSuppr;
	/** zone de saisie de la valeur a inserer */
	private JTextField zoneTexte;
	/** bouton exit */
	private JButton boutonFin;
	/** generateur de nombres aleatoires */
	private Random rand = new Random();

	/** constructeur */
	public Demo() {
		GTreePrinter gd = new GTreePrinter();
		// init de la liste
		laListe = new BinaryTree(gd);
		gd.setMyTree(laListe);
		// creation de la liste
		buildList();

		// recuperation du Container
		Container cont = getContentPane();
		// associer un layout au container
		cont.setLayout(new BorderLayout());

		// creation du panel nord
		panelNord = new JPanel();
		// zone de texte
		zoneTexte = new javax.swing.JTextField();
		// bouton insere elem
		boutonGo = new javax.swing.JButton();
		// bouton insere elem aleatoire
		boutonSuppr = new javax.swing.JButton();

		// creation du panel sud
		panelSud = new javax.swing.JPanel();
		// bouton exit
		boutonFin = new javax.swing.JButton();

		// liste a afficher
		listDisplay = new TreeDisplay(laListe, "Arbre");
		// ajout d'un observer sur la liste
		laListe.getPrinter().initDisplay(listDisplay);

		// ajout d'un grid layout sur le panel nord
		panelNord.setLayout(new GridLayout(1, 4));
		// texte initial dans la zone de saisie
		zoneTexte.setText("0");
		// texte du bouton go
		boutonGo.setText("Ajoute");
		// texte du bouton alea
		boutonSuppr.setText("Supprime");

		// ajout d'un ecouteur sur le bouton go?
		boutonGo.addMouseListener(new java.awt.event.MouseAdapter() {
			public void mouseClicked(java.awt.event.MouseEvent evt) {
				boutonGoMouseClicked(evt);
			}
		});
		// ajout d'un ecouteur sur le bouton recherche
		// ajout d'un ecouteur sur le bouton go alea
		// ajout d'un ecouteur sur le bouton tri
		// ajout d'un ecouteur sur le bouton suppr
		boutonSuppr.addMouseListener(new java.awt.event.MouseAdapter() {
			public void mouseClicked(java.awt.event.MouseEvent evt) {
				boutonSupprMouseClicked(evt);
			}
		});
		// ajout de la zone de texte au panel nord
		panelNord.add(zoneTexte);
		// ajout du bouton go au panel nord
		panelNord.add(boutonGo);
		// ajout du bouton alea au panel nord
		panelNord.add(boutonSuppr);
		{
			boutonRech = new javax.swing.JButton();
			panelNord.add(boutonRech);
			boutonRech.setText("Recherche");
			boutonRech.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent evt) {
					boutonRechMouseClicked(evt);
				}
			});
		}
		{
			boutonGoRand = new javax.swing.JButton();
			panelNord.add(boutonGoRand);
			boutonGoRand.setText("Ajout Aleatoire");
			boutonGoRand.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent evt) {
					boutonGoRandMouseClicked(evt);
				}
			});
		}
		{
			typeParcours = new JComboBox();
			panelNord.add(typeParcours);
			typeParcours.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent evt) {
					typeParcoursActionPerformed(evt);
				}
			});
			// ajout du combobox
			typeParcours.addItem("Parcours prefixe");
			typeParcours.addItem("Parcours infixe");
			typeParcours.addItem("Parcours postfixe");
		}
		
		// texte du bouton exit
		boutonFin.setText("Exit");
		// ajout d'un ecouteur sur le bouton exit
		boutonFin.addMouseListener(new java.awt.event.MouseAdapter() {
			public void mouseClicked(java.awt.event.MouseEvent evt) {
				boutonFinMouseClicked(evt);
			}
		});
		// ajout du bouton dans le panel sud
		panelSud.add(boutonFin);

		// ajout du panel affichage de liste au centre
		cont.add(listDisplay, BorderLayout.CENTER);
		// ajout du panel nord au nord
		cont.add(panelNord, BorderLayout.NORTH);
		// ajout du panel sud au sud
		cont.add(panelSud, BorderLayout.SOUTH);

	}

	/** fin du programme */
	private void boutonFinMouseClicked(java.awt.event.MouseEvent evt) {
		System.exit(0);
	}

	/** ajout d'un element dans la liste */
	private void boutonGoMouseClicked(java.awt.event.MouseEvent evt) {
		try {
			insertData(Integer.parseInt(zoneTexte.getText()));
		} catch (NumberFormatException nfe) {
			System.err.println("Attention, il faut saisir un nombre !");
			zoneTexte.setText("0");
		}
	}

	/** recherche d'un element dans la liste */
	private void boutonRechMouseClicked(java.awt.event.MouseEvent evt) {
		try {
			int val = Integer.parseInt(zoneTexte.getText());
			System.out.println("recherche de " + val);
			System.out.println(laListe.search(val));
		} catch (NumberFormatException nfe) {
			System.err.println("Attention, il faut saisir un nombre !");
			zoneTexte.setText("0");
		}
	}

	
	private void typeParcoursActionPerformed(ActionEvent evt) {
		switch (((JComboBox)evt.getSource()).getSelectedIndex()) {
		case 1:
			System.out.println("Parcours infixe : " + laListe.infix());
			break;
		case 0:
			System.out.println("Parcours prefixe : " + laListe.prefix());
			break;
		case 2:
			System.out.println("Parcours postfixe : " + laListe.postfix());
			break;
		}
	}
	
	/** ajout d'un element dans la liste */
	private void boutonSupprMouseClicked(java.awt.event.MouseEvent evt) {
		try {
			int val = Integer.parseInt(zoneTexte.getText());
			System.out.println("suppression de " + val);
			laListe.suppress(val);
		} catch (NumberFormatException nfe) {
			System.err.println("Attention, il faut saisir un nombre !");
			zoneTexte.setText("0");
		}
	}

	/** ajout d'un element aleatoire dans la liste */
	private void boutonGoRandMouseClicked(java.awt.event.MouseEvent evt) {
		insertData(rand.nextInt(20));
	}

	private void insertData(int val) {
		System.out.println("ajout de " + val);
		laListe.insert(val);
		laListe.getPrinter().update();
	}

	/** creation de la liste initiale */
	private void buildList() {
		laListe.setRoot(new GNode(4, new GNode(2, new GNode(1), new GNode(3)),
				new GNode(5)));
		laListe.initTree();
		/*
		 * for(int i=0;i<5;i++) laListe.insereTri(rand.nextInt(20));
		 * laListe.debut().actif(true);
		 */
	}

	/** lancement de la demo 
	 * @param arg 
	 */
	public static void main(String arg[]) {
		// creation de l'objet demo
		Demo demo = new Demo();
		// dimensionnement des panels
		demo.pack();
		// affichage de la fenetre
		demo.setVisible(true);
	}
}
