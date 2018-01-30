package animationStarter;
//-------------------------------------------------
// ActionQuit
//
// PhD modif 4 sept 16
//--------------------------------------------------

import java.awt.event.*;


//-------------------------------------------------
//  Action liee au Bouton Quit
//-------------------------------------------------

class ActionQuit implements ActionListener
{
	public void actionPerformed (ActionEvent e)
	{
		System.out.println ("\n bye");   
		System.exit (0);        
	}
	
} // ActionQuit

