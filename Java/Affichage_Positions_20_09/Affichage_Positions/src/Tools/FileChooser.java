/*-------------------------------------------------
 * FileChooser.java
 * 
 * PhD 23 mars 15    
 ---------------------------------------------------*/

package Tools;

import java.io.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.filechooser.*;

/*
 * FileChooserDemo.java uses these files:
 *   images/Open16.gif
 *   images/Save16.gif
 */
public class FileChooser extends JPanel implements ActionListener 
{
	static private final String newline = "\n";
	JButton openButton, saveButton;
	JTextArea log;
	JFileChooser jfc;

	public FileChooser() {
		super(new BorderLayout());

		// Create the log first, because the action listeners
		// need to refer to it.
		log = new JTextArea(5, 20);
		log.setMargin(new Insets(5, 5, 5, 5));
		log.setEditable(false);
		JScrollPane logScrollPane = new JScrollPane(log);

		// Create a file chooser
		jfc = new JFileChooser();

		// Uncomment one of the following lines to try a different
		// file selection mode. The first allows just directories
		// to be selected (and, at least in the Java look and feel,
		// shown). The second allows both files and directories
		// to be selected. If you leave these lines commented out,
		// then the default mode (FILES_ONLY) will be used.
		//
		// fc.setFileSelectionMode (JFileChooser.DIRECTORIES_ONLY);
		// fc.setFileSelectionMode (JFileChooser.FILES_AND_DIRECTORIES);

		// Create the open button. We use the image from the JLF
		// Graphics Repository (but we extracted it from the jar).

		// openButton = new JButton ("Open a File...",
		// createImageIcon ("images/Open16.gif"));
		openButton = new JButton("Open a File...");
		openButton.addActionListener(this);

		// Create the save button. We use the image from the JLF
		// Graphics Repository (but we extracted it from the jar).
		// saveButton = new JButton ("Save a File...",
		// createImageIcon ("images/Save16.gif"));
		// saveButton = new JButton ("Save a File...");
		// saveButton.addActionListener(this);

		// For layout purposes, put the buttons in a separate panel
		JPanel buttonPanel = new JPanel(); // use FlowLayout
		buttonPanel.add(openButton);
		// buttonPanel.add (saveButton);

		// Add the buttons and the log to this panel.
		add(buttonPanel, BorderLayout.PAGE_START);
		add(logScrollPane, BorderLayout.CENTER);
	}

	@Override
	public void actionPerformed(ActionEvent e) {

	}

	/*
	 * public void actionPerformed (ActionEvent e) { String fileName;
	 * 
	 * if (e.getSource() == openButton) {
	 * //----------------------------------------------- // Handle open button
	 * action //----------------------------------------------- int returnVal =
	 * jfc.showOpenDialog (FileChooser.this);
	 * 
	 * if (returnVal == JFileChooser.APPROVE_OPTION) { File file =
	 * jfc.getSelectedFile (); lts_ad.fileName = new String (file.getName ());
	 * System.out.println ("\n FileChooser actionPerformed : file : " + file +
	 * "lts_ad.fileName : " + lts_ad.fileName);
	 * 
	 * //This is where a real application would open the file. log.append
	 * ("actionPerformed : Opening: " + lts_ad.fileName + "." + newline); } else
	 * { log.append ("Open command cancelled by user." + newline); }
	 * log.setCaretPosition (log.getDocument ().getLength ()); }
	 * 
	 * 
	 * else if (e.getSource() == saveButton) {
	 * //----------------------------------------------- // Handle save button
	 * action //-----------------------------------------------
	 * 
	 * int returnVal = fc.showSaveDialog (FileChooser.this); if (returnVal ==
	 * JFileChooser.APPROVE_OPTION) { File file = fc.getSelectedFile (); //This
	 * is where a real application would save the file. log.append ("Saving: " +
	 * file.getName () + "." + newline); } else {
	 * log.append("Save command cancelled by user." + newline); }
	 * log.setCaretPosition (log.getDocument ().getLength ()); }
	 * 
	 * }
	 */

	/** Returns an ImageIcon, or null if the path was invalid. */
	protected static ImageIcon createImageIcon(String path) 
	{
		java.net.URL imgURL = FileChooser.class.getResource(path);
		if (imgURL != null) {
			return new ImageIcon(imgURL);
		} else {
			System.err.println("Couldn't find file: " + path);
			return null;
		}
	}

	/**
	 * Create the GUI and show it. For thread safety, this method should be
	 * invoked from the event dispatch thread.
	 */
	private static void createAndShowGUI() 
	{
		// Create and set up the window.
		JFrame frame = new JFrame("FileChooser");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		// Add content to the window.
		frame.add(new FileChooser());

		// Display the window.
		frame.pack();
		frame.setVisible(true);
	}

}
