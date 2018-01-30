package animationStarter;

//-------------------------------------------------
// AnimationStarter_AffPositions
//
//  Affichage d'une animation (exemple)
//  Version fournie aux etudiants
//
//  PhD  28 aout 17
//--------------------------------------------------

import java.awt.*;        // import statements to make necessary classes available

import javax.swing.*;

import Tools.Global_Var;



/**
 *  This class shows the setup for drawing animated images using Java Graphics2D.
 *  The drawing code goes in the paintComponent() method.  
 *  When the program is run, the drawing is shown in a window on the screen.  
 *  The paintComponent() method will be called about 60 times per second, 
 *  and the value of the global variables frameNumber and elapsedTimeMillis 
 *  will increase.  
 *  These variables can be used in paintComponent(), 
 *  so that the image will change each time it is drawn.
 */
public class AnimationStarter_AffPositions extends JFrame 
{
	public int frameWidth  = 1200;
	public int frameHeight = 800;

	public int frameX;
	public int frameY;
	
	public int displayX  = 20;
	public int displayY  = 80;

	public int displayWidth  = frameWidth - (2 * displayX);
	public int displayHeight = frameHeight - displayY - 20;

	
	public JLabel texte;
	
	public int frameNumber;  		// compteur de rafraichissement
	public long elapsedTimeMillis;  // temps ecoule, en milliseconds

 
	public Timer timer;  
	public long startTime = System.currentTimeMillis ();
     
     
	public int timerPeriod = 500; // periode de rafraichissement

	//---- Application connectee a la simulation  ----
	public DisplayAppli uneDisplayAppli;  

	// Utile pour actionStep. Initialise dans la methode 
	public Graphics2D display_g2;

	
	//------------------------------------------------------------------
	 
	public AnimationStarter_AffPositions ()
	{
		super ("AnimationStarter_AffPositions (PhD - Sept 2017) ");
	
	    //----- Pour la mise en page ---------
		
		Container contentPane = getContentPane();		
		contentPane.setLayout (new FlowLayout ());
		// contentPane.setLayout (new BorderLayout (3,3));

		JPanel panel = new JPanel ();
 
        //---------- size and Center window on screen ------------
		
		pack (); // avant setSize !!!	    
	    setSize (frameWidth, frameHeight);      
	    	    
        Dimension screen = Toolkit.getDefaultToolkit().getScreenSize();	 
        frameX = (screen.width  - frameWidth)  / 2;       
        frameY = (screen.height - frameHeight) / 2;
        setLocation (frameX, frameY);
  
	    // let user resize window. else : false 
        setResizable (true); 

        setBackground (Color.BLUE); // ????
        
	    //--------------------------------------
	    //   Positionnement des boutons et text field
	    // -------------------------------------
 	   
        JButton boutonQuit = new JButton ("Quit");
	    boutonQuit.addActionListener (new ActionQuit ());	   
	    panel.add (boutonQuit);
	    
	    JButton boutonGo = new JButton ("Go");
	    boutonGo.addActionListener (new ActionGo (this));
	    panel.add (boutonGo);
		    
	    JButton boutonStep = new JButton ("Step");
	    boutonStep.addActionListener (new ActionStep (this));
	    panel.add (boutonStep);

	   
	    JButton boutonPause = new JButton ("Pause");
	    boutonPause.addActionListener (new ActionPause (this));
	    panel.add (boutonPause);
	    
	    //------ Ajout d'un champ text field --------
	    texte = new JLabel ("Period : " + timerPeriod);
	    panel.add (texte); 
	    
	    contentPane.add (panel);
	    
	    //------------------------------------------------------
		// A Timer that will emit events to drive the animation.
		//------------------------------------------------------ 
	    
        startTime = System.currentTimeMillis ();
        
        // ----------------------------------------------
        ActionTimer actionTimer = new ActionTimer (this);
        timer = new Timer (timerPeriod, actionTimer);
        
       //------------------------------------------------------
	   // End program when window closes.
       //------------------------------------------------------
	   setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE); 	

	   //-------------------------------------------------
	   //   connexion a une application d'affichage
	   //
	   // c'est ici que l'on indique quelle application
	   // participe à l'affichage dans le display
	   //-------------------------------------------------

	   uneDisplayAppli = new DisplayAppli (this);	   
	   
	} // AnimationStarter_AffPositions
	
	

    /**----------------------------------------------------------------------
     * Point d'entree 
     -------------------------------------------------------------------------
     */
	 
	 public static void main(String[] args) 
	    {   		   
			Global_Var.Niv_Debug = 0;
			
			AnimationStarter_AffPositions frame = new AnimationStarter_AffPositions ();
			frame.show ();
	    }

	 
	   /**------------------------------------------------------------------------------
	     * Rafraichissement de l'affichage associé à 
	     * l'application uneDisplayAppli
	     * 
	     * Cette methode ppaint est appelée à chaque tic du Timer
	     *  (cf methode actionPerformed de la classe ActionTimer)
	     ------------------------------------------------------------------------------
	     */
	 
	    public void paint (Graphics g) 
	    {	        
	    	super.paint (g);   // utile pour l'affichage
	    	
	    	Graphics2D g2 = (Graphics2D)g.create ();	
	    	display_g2 = g2;   // utile pour ActionStep	    	
	    	
	        g2.setRenderingHint
	        		(RenderingHints.KEY_ANTIALIASING, 
	        		 RenderingHints.VALUE_ANTIALIAS_ON);
	                        
	        uneDisplayAppli.displayAppli_Traj_Step(g2);
	        
	    }  // paint
	        	  	   

} // AnimationStarter_AffPositions
	





