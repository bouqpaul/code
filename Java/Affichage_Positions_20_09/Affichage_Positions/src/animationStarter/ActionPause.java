package animationStarter;
//-------------------------------------------------
// ActionPause
//
// PhD modif 4 sept 16
//--------------------------------------------------

import java.awt.event.*;




//-------------------------------------------------
//   Action liee au bouton Pause
//-------------------------------------------------

class ActionPause implements ActionListener
{
	AnimationStarter_AffPositions frame;
	
	public ActionPause (AnimationStarter_AffPositions uneFrame)
	{
		frame = uneFrame;
	}
	
	//-------------------------------------

	public void actionPerformed (ActionEvent e)
	{
		System.out.println ("Pause --> timer.Pause"); 
		frame.timer.stop();  // Start the animation running.
	}
	
} // ActionPause



