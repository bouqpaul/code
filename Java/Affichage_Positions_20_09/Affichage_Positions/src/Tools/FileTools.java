/*---------------------------------------------- 
   FileTools.java
   Utilitaires de gestion de fichiers

   PhD 23 mars 15 
   
   ***************
   Attention : avec fileChoice : 
      un seul fichier ouvert à la fois
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


public class FileTools 
{
	
	// pour memoriser le nom de fichier et repertoire choisi
	static public String nomFichier;
	static public String nomRep;

	// --------------------------------------------------
	// Ouverture d'un fichier et retourne un BufferedReader
	//
	// param : fileName : nom du fichier a lire
	// retourne le BufferedReader
	//  		null si pb
	// --------------------------------------------------

	static public BufferedReader openReader (String fileName) throws Exception 
	{
		FileReader fileReader = null;
		try 
		{
			fileReader = new FileReader(fileName);
		} 
		catch (FileNotFoundException e) 
		{
			System.out.println(e);
			return null;
		}
		BufferedReader bufferedReader = new BufferedReader(fileReader);
		return bufferedReader;
		
	} // openReader

	
	
	// --------------------------------------------------
	// Lecture d'un fichier texte
	//
	// param : fileName : nom du fichier a lire
	// retourne le contenu lu
	//          null si erreur
	// --------------------------------------------------

	static public String fileRead (String fileName)  
	{
		String instring = new String();
		instring = "//--------------------------------";
		instring = instring + "\n//  " + fileName;
		instring = instring + "\n//--------------------------------";

		// --------------------------------------------------
		// Ouverture du fichier
		// --------------------------------------------------
		FileReader fileReader = null;
		try 
		{
			fileReader = new FileReader(fileName);
		} 
		catch (FileNotFoundException e) 
		{
			System.out.println(e);
		     return null;
		}

		BufferedReader bufferedReader = new BufferedReader(fileReader);

		// --------------------------------------------------
		// Lecture ligne par ligne
		// --------------------------------------------------
		String s;
		try 
		{
			// ----- lecture d'une ligne par readLine
			while ((s = bufferedReader.readLine()) != null) 
			{
				instring = instring + "\n" + s;
			}

			fileReader.close();
		} 
		catch (IOException e) 
		{
			System.out.println(e);
			return  null;
		}
		return instring;

	} // fileRead


	// --------------------------------------------------
	// Lecture d'un fichier texte
	//  (maniere alternative par rapport a fileRead () ci dessus)
	//
	// param : fileName : nom du fichier a lire
	// retourne le contenu lu
	// --------------------------------------------------

	static public String fileReadBis (String fileName) throws Exception 
	{
		File file;
		String s;
		
		// --------------------------------------------------
		// Ouverture et lecture du contenudu fichier
		// --------------------------------------------------
		file = new File(fileName);
		s = loadContents (file);		
		return s;
		
	} // fileReadBis
	
	
	
	// --------------------------------------------------
	// Lecture du contenu d'un fichier 
	//
	//   file : Fichier a lire
	//   retour: contenu (String) du fichier
	//---------------------------------------------------

	public static String loadContents (File file) 
	{
		StringBuilder contents = new StringBuilder();
		try 
		{
			BufferedInputStream in = 
					new BufferedInputStream (new FileInputStream(file));
			byte[] buffer = new byte[1024];
			int read = in.read(buffer);
			while ( read >= 0 ) 
			{
				contents.append(new String(buffer, 0, read));
				read = in.read(buffer);
			}
			in.close();
		} 
		catch (Exception e) 
		{
			e.printStackTrace();
			return null;
		}
		return contents.toString();
		
	} // loadContents
	

	
	//--------------------------------------------------
	// Lecture d'un fichier  
	//
	// param : 
	//   fileName : nom du fichier
	//
	// retourne le contenu lu
	//          null si erreur
	//--------------------------------------------------

	static public String fileLoad (String fileName) throws Exception 
	{
		String instring = new String ();
		instring = "";
		// instring = "//--------------------------------" ;
		// instring = instring + "\n //  " + fileName;
		// instring = instring + "\n //--------------------------------";
		
		//--------------------------------------------------
		//     Ouverture du fichier 
		//--------------------------------------------------
		FileReader fileReader = null;
		try 
		{
			fileReader = new FileReader (fileName);
		} 
		catch (FileNotFoundException e) 
		{
			System.out.println(e);
			return null;
		}
    
		BufferedReader bufferedReader = new BufferedReader(fileReader);

		//--------------------------------------------------
		//     Lecture ligne par ligne 
		//--------------------------------------------------
		String s;
		try 
		{
			//----- lecture d'une ligne par readLine
			while((s = bufferedReader.readLine()) != null) 
			{
				instring = instring + s + "\n";
			}

			fileReader.close();
		} 
		catch (IOException e) 
		{
			System.out.println(e);
			return  null;
		} 
		return instring;
    
	} // fileLoad
 

	//----------------------------------------------------
	// Ecriture de la chaine contenu dans le fichier nomFile
	//
	// Param : contenu : la chaine a ecrire
	//		   fichier : nom du fichier a ecrire 
	//----------------------------------------------------	
	
	static public void contentSave 
				(String contenu, String nomFile)
	{
		try
		{
			FileWriter filewriter = new FileWriter (nomFile);
			filewriter.write (contenu);
			filewriter.close ();
			}
		catch (Exception e)
		{
			System.out.println ("\n Erreur contentSave file :" + nomFile);
        	System.out.println (e);			
		}
	} // contentSave


	
	// ----------------------------------------------------
	// Ecriture de la chaine contenu dans le fichier nomFile
	//
	// Param : 	contenu : la chaine a ecrire
	// 			nomFile : nom du fichier a ecrire
	// ----------------------------------------------------

	static public void fileOpenWriteClose 
				(String contenu, String nomFile) 
	{
		try 
		{
			// FileOutputStream fos = new FileOutputStream (nomFile);
			FileWriter filewriter = new FileWriter(nomFile);
			filewriter.write (contenu);
			filewriter.close ();
		} 
		catch (Exception e) 
		{
			System.out.println("\n Erreur fileWrite :" + nomFile);
			System.out.println(e);
		}
	} // fileWrite

	
	
	// --------------------------------------------------
	// Saisie d'un nom de fichier avec l'extension .ch_extension
	//  et le chemin complet (en absolu)
	//
	// param :
	// ch_extension : chaine de caractere indiquant l'extension
	//
	// retourne le nom du fichier avec le chemin complet (en absolu)
	//          avec l'extension .ch_extension
	// --------------------------------------------------


	static public String fileChoice (String ch_extension) 
	{
		Display display = new Display ();
		Shell shell = new Shell (display);
		
		return FileTools.fileChoice (display, shell, ch_extension);
		
	} // fileChoice


	
	//--------------------------------------------------
	// Saisie d'un nom de fichier avec l'extension .ch_extension
	//  et le chemin complet (en absolu)
	//
	// param : 
	//		Display d, 
	//		Shell shell, 
	//   	ch_extension : chaine de caractere indiquant 
	//						l'extension
	//
	// retourne le nom du fichier avec le chemin complet (en absolu)  
	//          avec l'extension .ch_extension
	//--------------------------------------------------
	
	static public String fileChoice 
			(Display d, Shell shell, String ch_extension) 
	{		
		String nomFichier = new String ();
		
		//-----------------------------------------------
		//  choix du fichier .res
		//-----------------------------------------------
		
		FileDialog diag = new FileDialog (shell, 1);
		String[] filtres = {"*." + ch_extension};
		diag.setFilterExtensions (filtres);
		if ( diag.open () == null ) return null;
	
		//------- nom du fichier avec chemin absolu --------
		nomFichier = diag.getFilterPath () + "/"+ diag.getFileName ();
		return nomFichier;
		
	} // fileChoice
	

	
	// --------------------------------------------------
	// Saisie d'un nom de fichier avec l'extension .ch_extension
	//  sans le chemin complet (en relatif)
	//
	// param :
	// ch_extension : chaine de caractere indiquant l'extension
	//
	// retourne le nom du fichier sans le chemin complet (en relatif)
	//          avec l'extension .ch_extension
	// --------------------------------------------------


	static public String fileChoice_relative (String ch_extension) 
	{
		Display d = new Display();
		Shell shell = new Shell(d);
		return FileTools.fileChoice_relative (d, shell, ch_extension);
		
	} // fileChoice_relative



	//--------------------------------------------------
	// Saisie d'un nom de fichier avec l'extension .ch_extension 
	//  sans le chemin complet (en relatif)
	//
	// param : 
	//		Display d, 
	//		Shell shell, 
	//   	ch_extension : chaine de caractere indiquant 
	//						l'extension
	//
	// retourne le nom du fichier sans le chemin complet (en relatif)  
	//          avec l'extension .ch_extension
	//--------------------------------------------------
	
	static public String fileChoice_relative 
			(Display d, Shell shell, String ch_extension) 
	{		
		String nomFichier = new String ();
		
		//-----------------------------------------------
		//  choix du fichier .res
		//-----------------------------------------------
		
		FileDialog diag = new FileDialog (shell, 1);
		String[] filtres = {"*." + ch_extension};
		diag.setFilterExtensions (filtres);
		if ( diag.open () == null ) return null;
	
		//------- nom du fichier avec chemin absolu --------
		nomFichier = diag.getFileName ();
		return nomFichier;
		
	} // fileChoice_relative

} // FileTools

