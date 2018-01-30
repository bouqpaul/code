/*---------------------------------------------- 
   TestTools.java
   Test des utilitaires de lectured e fichier.
    Choisir un fichier avec extension : ".test"

   PhD 24 oct 15 
-------------------------------------------*/

package Tools;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.FileDialog;
import org.eclipse.swt.widgets.Shell;


public class TestTools 
{

	//-----------------------------------------
	// Tests des methodes
	//-----------------------------------------
	
	public static void main(String[] args) throws Exception
	{		
		String ficName = FileTools.fileChoice ("test");
		testLecture1 (ficName);
		testLecture2 (ficName);
		
	}
		
	public static void testLecture1 (String ficName)  throws Exception
	{		
		System.out.println ("========= fileRead : essai ========");
		System.out.println ("========= fileRead : essai ========");
		System.out.println ("========= fileRead : essai ========");
		System.out.println ("========= fileRead : essai ========");
		String s = FileTools.fileRead (ficName);
		System.out.println (s);
		
	} // testLecture1
	
	public static void testLecture2 (String ficName) throws Exception
	{
		System.out.println ("========= fileReadBis : essai ========");
		System.out.println ("========= fileReadBis : essai ========");
		System.out.println ("========= fileReadBis : essai ========");
		System.out.println ("========= fileReadBis : essai ========");
		System.out.println ("========= fileReadBis : essai ========");

		String s = FileTools.fileReadBis (ficName);
		System.out.println (s);
		
	} // testLecture2
	

} // FileTools

