package animationStarter;
//-------------------------------------------------
// ActionTimer
//
// PhD modif 15 sept 16
//--------------------------------------------------

import java.awt.*;        // import statements to make necessary classes available
import java.awt.event.*;
import javax.swing.*;


//-----------------------------------------------------
//Classe ActionTimer 
//-----------------------------------------------------

class ActionTimer implements ActionListener
{
	AnimationStarter_AffPositions uneFrame;

	public ActionTimer (AnimationStarter_AffPositions f)
	{
		uneFrame = f;
	}

	public void actionPerformed (ActionEvent e)
    {
		uneFrame.frameNumber++;
		uneFrame.elapsedTimeMillis = System.currentTimeMillis() - uneFrame.startTime;
       
 		uneFrame.texte.setText 
				(" Period : " + uneFrame.timerPeriod +
				 " frameNumber : " + uneFrame.frameNumber +
				 " Elapsed Time : " + uneFrame.elapsedTimeMillis + " (ms)");

        uneFrame.repaint(); 
        
    } // actionPerformed

} // ActionTimer




