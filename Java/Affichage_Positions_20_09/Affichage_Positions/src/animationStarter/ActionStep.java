package animationStarter;
//-------------------------------------------------
// ActionStep
//
// PhD modif 22 sept 16
//--------------------------------------------------

import java.awt.Graphics2D;
import java.awt.event.*;



//-------------------------------------------------
//  Action liee au Bouton Step
//-------------------------------------------------

class ActionStep implements ActionListener
{
	AnimationStarter_AffPositions frame;
	
	public ActionStep (AnimationStarter_AffPositions uneFrame)
	{
		frame = uneFrame;
	}
	
	//-------------------------------------

	public void actionPerformed (ActionEvent e)
	{
		System.out.println ("Step"); 
		
		Graphics2D g2 = frame.display_g2;
		
		// 1 pas d'animation : on appelle paint () directement sans le timer
		// frame.uneDisplayAppli.trace_obp_displayAppli_go_aStep (g2);
		frame.paint(g2);
	}
	
} // ActionStep

