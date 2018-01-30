package animationStarter;
//-------------------------------------------------
// ActionGo
//
// PhD modif 4 sept 16
//--------------------------------------------------

import java.awt.event.*;



//-------------------------------------------------
//  Action liee au Bouton Go
//-------------------------------------------------

class ActionGo implements ActionListener
{
	AnimationStarter_AffPositions frame;
	
	public ActionGo (AnimationStarter_AffPositions uneFrame)
	{
		frame = uneFrame;
	}
	
	//-------------------------------------

	public void actionPerformed (ActionEvent e)
	{
		System.out.println ("Go --> timer.start"); 
		frame.timer.start();  // Start the animation running.
	}
	
} // ActionGo

