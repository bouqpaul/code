//-------------------------------------------
// Utilitaires de parsing commun a toutes les applications
//
// PhD 4 mars 16  ******* a integrer dans dev TGM *********
//-------------------------------------------

package Tools;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;



public class ParserTools 
{
	//-------------------------------------------
	// Retourne la position du 1er caractere du pattern 
	// lu dans la chaine ch 
	// (recherche a partir du debut de ch) 
	// (l'index du 1er caractere d'une chaine est 0)
	// retourne -1 si non trouve
	//-------------------------------------------	
	
	public static int searchStringPattern (String ch, String pattern) 
	{
		return ch.indexOf (pattern);  
	}

	//-------------------------------------------
	// Retourne la chaine lue dans ch avant la chaine pattern
	// (recherche a partir du debut de ch) 
	// retourne null si pattern non trouve
	//-------------------------------------------	
	
	public static String searchStringBeforePattern (String ch, String pattern) 
	{
		int indexEnd = ParserTools.searchStringPattern (ch, pattern);
		if (indexEnd == -1) return null;
		return searchString (ch, 0, indexEnd); 
	}
	
	
	//-------------------------------------------
	// Retourne la chaine lue dans ch apres la chaine pattern
	// (recherche a partir du debut de ch) 
	// retourne null si non trouve
	//-------------------------------------------	
	
	public static String searchStringAfterPattern (String ch, String pattern) 
	{
		int indexEnd = ParserTools.searchStringPattern (ch, pattern);
		if (indexEnd == -1) return null;
		if (indexEnd + pattern.length () == ch.length ()) return null;		
		return ParserTools.searchString (ch, indexEnd + pattern.length (), ch.length ()); 
	}
	
	
	//-------------------------------------------	
	// Retourne la position du 1er caractere de pattern 
	// dans la chaine ch a partir de la position offset) 
	// (l'index du 1er caractere d'une chaine est 0)
	// retourne -1 si non trouve
	//-------------------------------------------	
	
	public static int searchStringPatternOffset 
			(String ch, String pattern, int offset) 
	{
		return ch.indexOf (pattern, offset);  
	}

	//-------------------------------------------	
	// Retourne la chaine lue entre
	//      la position indexBeg (incluse)
	//      la position indexEnd (excluse)
	// (l'index du 1er caractere d'une chaine est 0)
	// retourne null si non trouve
	//-------------------------------------------	
	
	public static String searchString (String ch, int indexBeg, int indexEnd) 
	{
		if (indexBeg > indexEnd) return null;
		if (indexEnd > ch.length ()) return null;
		return ch.substring (indexBeg, indexEnd);  
	}

	
	//-------------------------------------------	
	// Retourne la chaine lue entre
	//      la position indexBeg (incluse)
	//      la position indexEnd (excluse)
	// (l'index du 1er caractere d'une chaine est 0)
	// retourne null si non trouve
	//-------------------------------------------	
	
	public static String searchStringIndex (String ch, int indexBeg, int indexEnd) 
	{
		if (indexBeg > indexEnd) return null;
		if (indexEnd > ch.length ()) return null;
		return ch.substring (indexBeg, indexEnd);  
	}
	
	
	
	//-------------------------------------------
	// retourne une chaine lue dans la chaine ch
	// entre le pattern1 et le pattern2
	//--------------------------------------------------------
	// la difference avec la methode searchStringBeforeDblePattern
	// est que la recherche s'effectue a partir de pattern1
	// en allant vers la fin de la chaine.
	// exemple : ch: 1234567231267 pattern1: 23 pattern2: 67 retour : 45
	// retourne null si patterns 1 ou 2 non trouves
	//-------------------------------------------	
	
	public static String searchStringDblePattern 
			(String ch, String pattern1, String pattern2) 
	{		
		int indexDeb, indexFin;
		
		// recherche de la chaine ds les match		
		indexDeb = ParserTools.searchStringPattern (ch, pattern1);  
		if (indexDeb == -1) return null;		
		
		indexDeb = indexDeb +  pattern1.length (); 
		indexFin = ParserTools.searchStringPatternOffset (ch, pattern2, indexDeb);
		if (indexFin == -1) return null;		
		
		// indexDeb : inclus  indexFin : exclus
		return ParserTools.searchString (ch, indexDeb, indexFin);    
		
	} // searchStringDblePattern

	
	
	//-------------------------------------------
	// retourne une chaine lue dans la chaine ch
	// entre le pattern1 et le pattern2
	//--------------------------------------------------------
	// la difference avec la methode searchStringDblePattern
	// est que la recherche s'effectue a partir de pattern1
	// en allant vers la fin de la chaine 
	// Meme si pattern2 n'est pas trouve, rtourne la chine trouve apres pattern1.
	// exemple : ch: 1234567231267 pattern1: 23 pattern2: 99 retour : 4567231267
	// retourne null si pattern 1 non trouve
	//-------------------------------------------	
	
	public static String searchStringDblePatternFin 
			(String ch, String pattern1, String pattern2) 
	{		
		int indexDeb, indexFin;
		
		// recherche de la chaine ds les match		
		indexDeb = ParserTools.searchStringPattern (ch, pattern1);  
		if (indexDeb == -1) return null;	// pattern1 non trouve	
		
		indexDeb = indexDeb +  pattern1.length (); 
		indexFin = ParserTools.searchStringPatternOffset (ch, pattern2, indexDeb);
		if (indexFin == -1) 
			{
				// pattern2 non trouve
				return ParserTools.searchStringAfterPattern (ch, pattern1);
			}
		
		// indexDeb : inclus  indexFin : exclus
		return ParserTools.searchString (ch, indexDeb, indexFin);    
		
	} // searchStringDblePatternFin



	//-------------------------------------------
	// retourne une chaine lue dans la chaine ch
	// entre le pattern1 et le pattern2
	//--------------------------------------------------------
	// la difference avec la methode searchStringDblePattern
	// est que la recherche s'effectue a partir de pattern2
	// en remontant la chaine vers le debut.
	// exemple : ch: 123423567 pattern1: 23 pattern2: 67 retour : 5
	// retourne null si patterns 1 ou 2 non trouves
	//-------------------------------------------	
	
	public static String searchStringBeforeDblePattern 
			(String ch, String pattern1, String pattern2) 
	{		
		int index, indexFin, indexTemp;
		
		// recherche du pattern2 dans la chaine			
		index = ParserTools.searchStringPattern (ch, pattern2);  
		if (index == -1) return null;		
		indexFin = index; 	// se positionner sur le pattern2
		
		// remonter en amont de la chaine a la recherche de pattern1
		while (index != -1)
		{
			index--;
			indexTemp = ParserTools.searchStringPatternOffset (ch, pattern1, index);
			if (indexTemp == -1) continue;
			else
			{
				return (ParserTools.searchStringIndex (ch, indexTemp + pattern1.length(), indexFin));
			}
		}		
		return null;
		
	} // searchStringBeforeDblePattern



	
	//-------------------------------------------
	// retourne le nbre de chaines, separées par
	// l'expression exp, qui sont contenues dans la chaine ch
	// 
	// exemple : ch: 12,345,67 exp: "," 
	// retourne 3 
	//
	// retourne 1 si pattern non trouve
	// exemple : ch: 12 exp: "," 
	// retourne 1 
	//
	// si ch = null  retourne 0
	//-------------------------------------------	
	
	public static int searchNbPatternInString (String ch, String exp) 
	{		
		String tab [];
		
		if (ch == null) return 0;
		
		// exp existe dans ch ?
		if (ParserTools.searchStringPattern (ch, exp) == -1) return 1;
		
		tab =  ch.split (exp); 	
		return (tab.length);
		
	} //searchNbPatternInString

	
	
	//-------------------------------------------
	// retourne le tableau de chaines, separées par
	// l'expression exp, qui sont contenues dans la chaine ch
	// 
	// exemple : ch: 12,345,67 exp: "," 
	// retourne le tableau de String : "12", "345", "56" 
	//
	// retourne un element du tableau = ch si pattern non trouve
	// exemple : ch: 12 exp: "," 
	// retourne le tableau de String : "12" 
	//-------------------------------------------	
	
	public static String [] searchTabStringPattern 
						(String ch, String exp) 
	{		
		return ch.split (exp); 	
		
	} //searchTabStringPattern
	

	
	//-------------------------------------------
	// retourne le nbre de chaines, separées par
	// l'expression exp, qui sont contenues dans la chaine ch
	// 
	// exemple : ch: 12,345,67 exp: "," 
	// retourne 3 
	// exemple : ch: 12 exp: "," 
	// retourne 1 
	// retourne 0 si pattern non trouve
	//-------------------------------------------	
	
	public static int searchNbStringPattern (String ch, String exp) 
	{		
		String tab [];
		
		// exp existe dans ch ?
		if (ParserTools.searchStringPattern (ch, exp) == -1) return 1;
		
		tab =  ch.split (exp); 	
		return (tab.length);
		
	} //searchNbStringPattern

	
	
	
	//-------------------------------------------
	// Autre implementation de la mathode precedente 
	// (a cause des pb du split ...)
	//
	// retourne une liste de chaines, separées par
	// l'expression exp, qui sont contenues dans la chaine ch
	// 
	// exemple : ch: 12,345,67 exp: "," 
	// retourne la liste de chaines : "12", "345", "56" 
	//
	// retourne une liste avec un element = ch si pattern non trouve
	// exemple : ch: 12 exp: "," 
	// retourne la liste de chaine : "12" 
	//-------------------------------------------	
	
	public static List<String> searchListStringPattern 
						 (String ch, String exp) 
	{		
		List<String> stringList = new ArrayList<String>(); 

		// exp existe dans ch ?
		if (ParserTools.searchStringPattern (ch, exp) == -1) 
		{
			// exp n'existe pas dans ch 
			stringList.add (ch);
			return stringList;
		}
		
		while (true)
		{
			String s = searchStringBeforePattern (ch, exp); 
			stringList.add (s);
			ch = searchStringAfterPattern (ch, exp); 

			if (searchStringPattern (ch, exp) == -1) 
			{
				// dernier element de la liste
				stringList.add (ch);
				return stringList;
			}
		}
		
	} //searchListStringPattern 
	

	
	//-------------------------------------------
	// retourne le nbre de chaines, separées par
	// l'expression exp, qui sont contenues dans la chaine ch
	// 
	// exemple : ch: 12,345,67 exp: "," 
	// retourne 3 
	//
	// retourne 1 si pattern non trouve
	// exemple : ch: 12 exp: "," 
	// retourne 1 
	//-------------------------------------------	

	public static int searchNbListStringPattern (String ch, String exp) 
	{	
		List<String> list = searchListStringPattern (ch, exp);
		return (list.size ());
	}
	
	
	

	
	//-------------------------------------------	
	// Retourne la valeur entiere lue dans la chaine ch
	// entre le pattern1 et le pattern2
	// retourne -1 si patterns 1 ou 2 non trouves ou 
	// pb de lecture de l'entier 
	//
	// attention si l'entier lue est egal a -1 !!!
	//-------------------------------------------
	
	public static int searchValueStringDblePattern 
			(String ch, String pattern1, String pattern2) 
	{	
		String chValLue = new String ();
		try
		{
			chValLue = ParserTools.searchStringDblePattern (ch, pattern1, pattern2); 	
			if (chValLue == null) return -1;		

			return Integer.parseInt (chValLue); 	
		}
		catch (NumberFormatException ex) 
		{
			System.out.print (" *** pb de parsing de l'entier: " + chValLue + "*** ");
			return -1;
		} 
	}
	

	
	//-------------------------------------------	
	// Retourne une chaine dont on a supprime dans la chaine s 
	// le caractere c_supp
	//
	//-------------------------------------------

	public static String delete_char_in_string (String s, char c_supp) 
	{	
		String s_new = new String ();
		char c_tmp, c_char;

		if (s.length()== 0)   return s;
		for (int i=0; i < s.length(); i++)
	  	{
			c_char = s.charAt(i);
			int n = (int) c_char;
			c_tmp = c_char;
			// System.out.print 
			//		("\n c_tmp:" + c_tmp + " (int:" + (int) c_tmp + ") ");
			if (c_tmp != c_supp)
				s_new = s_new + c_tmp;
	  	}
		return s_new;
			
	} // delete_char_in_string 


	//-------------------------------------------	
	// Retourne une chaine dont on a supprime dans la chaine s 
	// le caractere c_supp entre le début de la chaine et l'index : index
	//
	//-------------------------------------------

	public static String delete_char_in_string_at_index (String s, char c_supp, int index) 
	{	
		String s_new = new String ();

		if (s.length ()== 0)   return s;
		if (index >= s.length ())   return s;
		if (s.charAt (index) != c_supp)  return s;  // c_supp non trouve a l'index
		
		for (int i = 0; i <index; i++)
				// s_new.charAt (i) = s.charAt (i);
				s_new = s_new + s.charAt (i);
		
		for (int j = index + 1; j < s.length (); j++)
				s_new = s_new + s.charAt (j);
						
		return s_new;
			
	} // delete_char_in_string_at_index


	
	
	//-------------------------------------------	
	// Retourne une chaine dont on a supprime dans la chaine s 
	// les espaces entre le début de la chaine et la fin
	//
	// on laisse un espace apres : beg_str et avant : end_str
	//
	//-------------------------------------------

	public static String delete_space_in_string_between 
						(String s, String beg_str, String end_str) 
	{	
		String new_str = new String ();

		if (s.length ()== 0)   return s;
		
		// recuperer la chaine entre beg_str et end_str	
		new_str = searchStringDblePattern (s, beg_str, end_str);
		if (new_str == null)   return s;
						
		// suprimer les espaces dans tmp_str
		new_str = ParserTools.delete_space_in_string (new_str);

		// remettre le debut et la fin
		new_str = beg_str + " " + new_str + " " + end_str;
		return new_str;
			
	} // delete_space_in_string_between

	

	
	
	//-------------------------------------------	
	// Retourne une chaine dont on a supprime dans la chaine s 
	// la chaine delete_str entre le début de la chaine et la fin
	//
	// *****  Attention a re-verifier qd delete_str = " " PB !!!
	//
	//-------------------------------------------

	public static String delete_str_in_string_between 
						(String s, String delete_str, String beg_str, String end_str) 
	{	
		String tmp_str  = new String ();
		String tmp_str2  = new String ();
		String new_str = new String ();

		if (s.length ()== 0)   return s;
		
		// recuperer la chaine entre beg_str et end_str	
		tmp_str = searchStringDblePattern (s, beg_str, end_str);
		if (tmp_str == null)   return s;
						
		// suprimer les chaines : delete_str dans tmp_str
		
		while (true)
		{
			tmp_str2 = searchStringBeforePattern (tmp_str, delete_str);
			if (tmp_str2 == null)
			{
				new_str = new_str + tmp_str;
				 break;
			}
			new_str = new_str + tmp_str2;
			tmp_str = searchStringAfterPattern (tmp_str, delete_str);
		}

		// remettre le debut et la fin
		new_str = beg_str + " " + new_str + " " + end_str;
		return new_str;
			
	} // delete_str_in_string_between

	

	
	
	
	//-------------------------------------------	
	// Retourne une chaine dont on a supprime 
	// dans la chaine s les espaces (32 ou 160) 
	// et les virgules (",")
	//
	//-------------------------------------------

	public static String delete_space_comma_in_string (String s) 
	{	
		String ch = new String ();
		ch = ParserTools.delete_char_in_string (s, (char) 32);
		ch = ParserTools.delete_char_in_string (ch, (char) 160);
		ch = ParserTools.delete_char_in_string (ch, (char) ',');		
		return ch;	
	
	} // delete_space_comma_in_string 


	//-------------------------------------------	
	// Retourne une chaine dont on a supprime 
	// dans la chaine s les espaces (32 ou 160) 
	//
	//-------------------------------------------

	public static String delete_space_in_string (String s) 
	{	
		String ch = new String ();
		ch = ParserTools.delete_char_in_string (s, (char) 32);
		ch = ParserTools.delete_char_in_string (ch, (char) 160);		
		return ch;	
	
	} // delete_space_in_string 


	//-------------------------------------------	
	// Retourne une chaine dont on a supprime 
	// dans la chaine s les retours a la ligne
	// ********************************************
	//  a mettre dans TGM
	// ********************************************
	//-------------------------------------------

	public static String delete_rc_in_string (String s) 
	{	
		String ch = new String ();
		ch = ParserTools.delete_char_in_string (s, (char) 10);
		return ch;	
	
	} // delete_rc_in_string 


	
	//-------------------------------------------	
	// Retourne la chaine dont on a supprime toutes
	// les chaines comprises entre "//" et RC
	//
	//-------------------------------------------
	
	public static String deleteCommentaires (String ch) 
	{	
		String chRet = new String ();
		String chTmp = new String ();
		boolean fini = false;
		
		while (!fini)
		{
			// 1
			chTmp = ParserTools.searchStringBeforePattern (ch, "//"); 
			if (chTmp == null) 
			{
				chRet = chRet + ch;
			 	return (chRet);
			}
			chRet = chRet + chTmp;
			// 2
			chTmp = ParserTools.searchStringAfterPattern (ch, "//"); 	
			// 3
			ch = ParserTools.searchStringAfterPattern (chTmp, "\n"); 	
			// ch = ParserTools.searchStringAfterPattern (chTmp, "X"); pour debug
			if (ch == null) 
			{
				chRet = chRet + chTmp;
			 	return (chRet);
			}			
		}
		return null;
	}
	

	
	//--------------------------------------------------
	// Lecture dans le fichier d'une chaine de caracteres 
	// située dans une rubrique 
	// delimitee par marqueurDeb et marqueurFin
	// et localisee apres une balise
	//
	// Format de la rubrique :
	//          marqueurDeb 
	// 	        ...	
	// 	        balise chaine
	//     		...	
	// 	        marqueurFin
	//
	// Les lignes de commentaires (commencant par //) 
	// sont supprimees.
	// les espaces sont supprimes.
	//
	// param : String marqueurDeb
	//				String marqueurFin,
	//				String balise
	//				String fichier
	// retour : chaine (la balise est supprimée dans chaine)
	//--------------------------------------------------

	public static String lire_uneString_Deb_Fin_afterBalise 
					(String marqueurDeb, String marqueurFin,
					 String balise, 
					 String fichier) throws Exception
	{		
		String line = new String ();
		String chaine = new String ();
		BufferedReader reader;

		//--------------------------------------------
		//   Lecture  du fichier 
		//--------------------------------------------
		try
		{
			reader = FileTools.openReader (fichier);
		}
		catch (FileNotFoundException e) 
		{
			Global_Var.tracer_console 
					(1, "*** fichier : " + fichier + "\n NON TROUVE ***" );
			return null;
		}
		
		Global_Var.tracer_console (100, "\nlire_string_Deb_Fin_afterBalise : " + 
				marqueurDeb + " " + balise + " " + marqueurFin);

		int Etat = 1;		
		try 
		{
			while (Etat != 0)
			{
				//------- lecture d'une ligne ------
				line = reader.readLine ();
				if (line == null) 
				{
					Etat = 0;
					continue;
				}
				
				// pour enlever les spaces
				// line = line.trim (); 
				line = ParserTools.delete_char_in_string (line, ' ');	
				
				// passer la ligne vide 
				if (line.length () == 0) continue;
				// passer la ligne de commentaire (commence par //)
				if (ParserTools.searchStringPattern (line, "//") != -1) continue; 
				
				switch (Etat)
				{
				case 1 :	// attendre la chaine : marqeurDeb
					if (ParserTools.searchStringPattern 
									(line, marqueurDeb) != -1) 
					{
						Etat = 2;  // marqueurDeb trouve
					}					
					break;
				case 2 :	// lire jusqu'a : marqueurFin
					if (ParserTools.searchStringPattern 
										(line, marqueurFin) != -1) 
					{
						Etat = 0;  // marqueurFin trouve : on sort
					}
					else
					{
						// Global_Var.tracer_console (100, "\n" + line);
						//----- parser la ligne de balise -----
						chaine = ParserTools.searchStringAfterPattern 
															(line, balise);
						if (chaine != null) 	
						{
							reader.close ();
							return chaine;
						}
					}
					break;		
				} // fin switch
			} // fin while
		} // fin try
		
		catch (Exception e)
		{
			java.lang.System.out.println 
				("\nException dans lire_string_Deb_Fin_afterBalise ");
		}						
		return chaine;
		
	} // lire_uneString_Deb_Fin_afterBalise


	
	
	
	//--------------------------------------------------
	// Lecture dans le fichier d'une chaine de caracteres 
	// située localisee apres une balise
	//
	// Format de la rubrique :
	// 	        balise chaine
	//
	// Les lignes de commentaires (commencant par //) 
	// sont supprimees.
	// les espaces sont supprimes.
	//
	// param : String balise
	//		   String fichier
	// retour : chaine (la balise est supprimée dans chaine)
	//--------------------------------------------------

	public static String lire_string_afterBalise 
					(String balise, String fichier) throws Exception
	{		
		String line = new String ();
		String chaine = new String ();
		BufferedReader reader;
		
		//--------------------------------------------
		//   Lecture  du fichier 
		//--------------------------------------------
		try
		{
			reader = FileTools.openReader (fichier);
		}
		catch (FileNotFoundException e) 
		{
			Global_Var.tracer_console 
					(1, "*** fichier : " + fichier + "\n NON TROUVE ***" );
			return null;
		}
		
		Global_Var.tracer_console (100, "\nlire_string_afterBalise: " + 
				 						balise);
		
		int Etat = 1;		
		try 
		{
			while (Etat != 0)
			{
				//------- lecture d'une ligne ------
				line = reader.readLine ();
				if (line == null) 
				{
					Etat = 0;
					continue;
				}
				
				// pour enlever les spaces
				// line = line.trim (); 
				line = ParserTools.delete_char_in_string (line, ' ');	
				
				// passer la ligne vide 
				if (line.length () == 0) continue;
				// passer la ligne de commentaire (commence par //)
				if (ParserTools.searchStringPattern (line, "//") != -1) continue; 
				
				switch (Etat)
				{
				case 1 :	// attendre la chaine : balise
					if (ParserTools.searchStringPattern (line, balise) != -1) 
					{
						//----- parser la ligne de balise -----
						chaine = ParserTools.searchStringAfterPattern 
												(line, balise);
						// balise trouve
						reader.close ();
						if (chaine != null) return (chaine);
					}					
					break;
	
				} // fin switch
			} // fin while
		} // fin try
		
		catch (Exception e)
		{
			java.lang.System.out.println 
				("\nException dans lire_string_afterBalise ");
		}						
		return null;
		
	} // lire_string_afterBalise


	

	// -------------------------------------------------------------
	// Lecture dans le fichier une liste de chaines 
	// localisees dans la rubrique delimitee par 
	// marqueurDeb et marqueurFin
	// et chacune localisee apres une balise.
	//
	// Format des rubriques (exemple) :
	//
	// (marqueurDeb) #Debut
	//				 ...
	// (balise)	 	 Balise chaine1, chaine2, chaine3
	// (balise)	 	 Balise chaineA, chaineB, chaineC, chaineD
	// (balise)	 	 Balise chaineX, chaineY 
	//                ...          
	// (marqueurFin) #Fin
	//----------------------------------------------------
	// Parametre : 
	//        	String marqueurDeb
	//  		String marqueurFin,
	//  		String balise
	//  		String separateur, 
	//  		String fichier   : fichier de lecture
	//
	// retour    : un tableau de chaines : 
	//					tab [] = chaine1, chaine2, chaine3
	// --------------------------------------------------------------

	public static List<String> lire_uneListe_Strings_Deb_Fin_afterBalise 
						(String marqueurDeb, String marqueurFin,
						 String balise, String fichier) 
						 throws Exception
	{	
		String line = new String ();
		String chaine = new String ();
		List<String> listeChaines = new ArrayList<String> (); 	

		BufferedReader reader;

		//--------------------------------------------
		//   Lecture  du fichier 
		//--------------------------------------------
		try
		{
			reader = FileTools.openReader (fichier);
		}
		catch (FileNotFoundException e) 
		{
			Global_Var.tracer_console 
					(1, "*** fichier : " + fichier + "\n NON TROUVE ***" );
			return null;
		}

		Global_Var.tracer_console 
				(100, "\n       lire_uneListe_Strings_Deb_Fin_afterBalise : " + 
						marqueurDeb + " " + balise + " " + marqueurFin);
		int Etat = 1;		
		try 
		{
			while (Etat != 0)
			{
				//------- lecture d'une ligne ------
				line = reader.readLine ();
				if (line == null) 
				{
					Etat = 0;
					continue;
				}
		
				// pour enlever les spaces
				// line = line.trim (); 
				// line = ParserTools.delete_char_in_string (line, ' ');	
		
				// passer la ligne vide 
				if (line.length () == 0) continue;
				// passer la ligne de commentaire (commence par //)
				if (ParserTools.searchStringPattern (line, "//") != -1) continue; 
		
				switch (Etat)
				{
				case 1 :	// attendre la chaine : marqeurDeb
					if (ParserTools.searchStringPattern 
							(line, marqueurDeb) != -1) 
					{
						Etat = 2;  // marqueurDeb trouve
					}					
					break;
				case 2 :	// lire jusqu'a : marqueurFin
					if (ParserTools.searchStringPattern 
								(line, marqueurFin) != -1) 
					{
						Etat = 0;  // marqueurFin trouve : on sort
					}
					else
					{
						// Global_Var.tracer_console (100, "\n" + line);
						// lire la ligne et tester si presence 
						// de la balise (enleve la balise de la chaine lue)

						chaine = ParserTools.searchStringAfterPattern 
													(line, balise);				
						if (chaine != null) 
							// balise trouve et sauver la chaine dans la liste
							listeChaines.add (chaine);
					}
					break;		
				} // fin switch
			} // fin while
		} // fin try

		catch (Exception e)
		{
			Global_Var.tracer_console 
				(1, "\nException dans lire_string_Deb_Fin_afterBalise ");
		}			
		
		reader.close ();
		return listeChaines;
		
	} // lire_uneListe_Strings_Deb_Fin_afterBalise


	
	
	//----------------------------------------------------------------
	// Test des primitives de parsing
	//
	// s : chaine a traiter
	//----------------------------------------------------------------

	public static void essaisParsing (String s) 
	{
		System.out.print ("\n   Traitement de s : " + s);		
		System.out.print ("\n----------------------------------");		

		String chRet = "";
		int ret;

		//-----------------------------------------------------------------
		System.out.print ("\n delete_char_in_string_at_index : " + s + " c_supp : 0  index : 0");
		chRet = ParserTools.delete_char_in_string_at_index (s, '0', 0);
		System.out.print ("\n " + chRet);
		
		//-----------------------------------------------------------------
		System.out.print ("\n delete_char_in_string_at_index : " + s + " c_supp : 0  index : 1");
		chRet = ParserTools.delete_char_in_string_at_index (s, '0', 1);
		System.out.print ("\n " + chRet);
		
		//-----------------------------------------------------------------
		System.out.print ("\n delete_char_in_string_at_index : " + s + " c_supp : 2  index : 2");
		chRet = ParserTools.delete_char_in_string_at_index (s, '2', 2);
		System.out.print ("\n " + chRet);
		
		//-----------------------------------------------------------------
		System.out.print ("\n \n delete_str_in_string_between : " + s + " delete : 12  entre : record et end");
		chRet = ParserTools.delete_str_in_string_between (s, "12", "record", "end");
		System.out.print ("\n " + chRet + "\n");
	
		//-----------------------------------------------------------------
		System.out.print ("\n \n delete_str_in_string_between : " + s + " delete : 2 espaces  entre : record et end");
		chRet = ParserTools.delete_str_in_string_between (s, "  ", "record", "end");
		System.out.print ("\n " + chRet + "\n");
	
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringBeforePattern : " + s + " pattern: abc");
		chRet = ParserTools.searchStringBeforePattern (s, "abc");
		System.out.print ("\n " + chRet);
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringAfterPattern : " + s + " pattern: abc");
		chRet = ParserTools.searchStringAfterPattern (s, "abc");
		System.out.print ("\n " + chRet);

		
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringAfterPattern : " + s + " pattern: d,");
		chRet = ParserTools.searchStringAfterPattern (s, "d,");
		System.out.print ("\n " + chRet);

			
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringPattern : " + s + " pattern: // ");	
		ret =  ParserTools.searchStringPattern (s, "//"); 
		System.out.print ("\n pos: " + ret);	
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringPattern : " + s + " pattern:  45 ");
		ret = ParserTools.searchStringPattern (s, "45");
		System.out.print ("\n pos: " + ret);
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringPattern : " + s + " pattern:  75 ");
		ret = ParserTools.searchStringPattern (s, "75");
		System.out.print ("\n pos: " + ret);
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringPatternOffset : " + s + "  pattern: 45 offset : 1 ");
		ret = ParserTools.searchStringPatternOffset (s, "45", 1);
		System.out.print ("\n  pos: " + ret);
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringPatternOffset : " + s + "  pattern: 45 offset 6 ");
		ret = ParserTools.searchStringPatternOffset (s, "45", 6);
		System.out.print ("\n pos: " + ret);
		//-----------------------------------------------------------------
		System.out.print ("\n searchString : " + s + " 2, 8 --> ");
		chRet = ParserTools.searchStringIndex (s, 2, 8);
		System.out.print ("\n entre pos 2 et pos 8 chRet: " + chRet);
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringDblePattern : " + s + " patterns : 34 et 78 ");	
		chRet = "";
		chRet = ParserTools.searchStringDblePattern 
							(s, "34", "78"); 
		if (chRet != null)
			System.out.print ("\nentre pos 34 et 78 chRet: " + chRet);
		else
			System.out.print ("\nentre pos 34 et pos 78 chRet: null");
			
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringDblePattern : " + s + " patterns : 78, 23 ");		
		chRet = "";
		chRet = ParserTools.searchStringDblePattern 
							(s, "78", "23"); 
		if (chRet != null)
			System.out.print ("\nentre 78 et pos 23 chRet: " + chRet);
		else
			System.out.print ("\nentre 78 et pos 23 chRet: null");
		//-----------------------------------------------------------------
		System.out.print ("\n searchValueStringDblePattern : " + s + "  patterns : 23, 89 ");	
		ret = ParserTools.searchValueStringDblePattern  
							(s, "23", "89"); 
		System.out.print ("\nentre 23 et pos 89 ret: " + ret);
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringBeforeDblePattern : " + s + "  patterns : 34, 78 ");	
		chRet = "";
		chRet = ParserTools.searchStringBeforeDblePattern 
							(s, "34", "78"); 
		if (chRet != null)
			System.out.print ("\nentre 34 et pos 78 chRet: " + chRet);
		else
			System.out.print ("\nentre 34 et pos 78 chRet: null");

		//-----------------------------------------------------------------
		System.out.print ("\n searchStringBeforeDblePattern : " + s + "  patterns : 78, 23 ");	
		chRet = "";
		chRet = ParserTools.searchStringBeforeDblePattern 
							(s, "78", "23"); 
		if (chRet != null)
			System.out.print ("\nentre 78 et pos 23 chRet: " + chRet);
		else
			System.out.print ("\nentre 78 et pos 23 chRet: null");

		//-----------------------------------------------------------------
		System.out.print ("\n searchStringBeforeDblePattern : " + s + "  patterns :  86, 23 ");	
		chRet = "";
		chRet = ParserTools.searchStringBeforeDblePattern 
							(s, "86", "23"); 
		if (chRet != null)
			System.out.print ("\nentre 86 et pos 23 chRet: " + chRet);
		else
			System.out.print ("\nentre 86 et pos 23 chRet: null");

		//-----------------------------------------------------------------
		System.out.print ("\n searchTabStringPattern : " + s + "  pattern : ,");	

		String [] tabCh =  ParserTools.searchTabStringPattern (s, ","); 
		if (tabCh == null)
				System.out.print ("\n , pas trouve ");
		else
		{
			System.out.print ("\nlong tabCh : " + tabCh.length + " : ");
			for (int i=0; i< tabCh.length;i++)
			System.out.print ("\n      " + tabCh [i] + " ");
		}
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchNbStringPattern : " + s + "   pattern : ,");	

		int n =  ParserTools.searchNbStringPattern (s, ","); 
		System.out.print ("\n n : " + n );

		
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchListStringPattern : " + s + "  pattern :  \\},\\{ ");	

		List<String> stringList  =  ParserTools.searchListStringPattern (s, "},{"); 
		if (stringList == null)
				System.out.print ("\n , pas trouve ");
		else
		{
			System.out.print ("\n taille stringList : " + stringList.size () + " : ");
			for (String str : stringList)
							System.out.print ("\n    " + str);
		}
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchNbListStringPattern : " + s + "  pattern :  \\},\\{ ");	

		n =  ParserTools.searchNbListStringPattern (s, "\\},\\{"); 
		System.out.print ("\n nbre d'elements dans la liste : " + n );
	
		//-----------------------------------------------------------------
		System.out.print ("\n delete_char_in_string : space dans " + s);	

		chRet =  ParserTools.delete_char_in_string (s, ' '); //(char) 32); 
		System.out.print ("\n" + chRet);

		//-----------------------------------------------------------------
		System.out.print ("\n searchStringDblePattern : " + s + "  pattern :  from\\{ et  to\\{ ");	
		
		chRet = ParserTools.searchStringDblePattern (s, "from\\{", "to\\{");
		System.out.print ("\n     --> " + chRet);	
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringDblePattern : " + s + "  pattern :  from\\{ et  to\\{ ");	
		
		chRet = ParserTools.searchStringDblePattern (s, "from\\{", "to\\{");
		System.out.print ("\n     --> " + chRet);		
		
		//-----------------------------------------------------------------
		String exp = new String ("from");
		System.out.print ("\n searchNbStringPattern : " + s + "  pattern : " + exp);
		System.out.print ("\ndans : " + s);

		n = ParserTools.searchNbPatternInString (s, exp);
		System.out.print ("\n n : " + n);
		
		tabCh = ParserTools.searchTabStringPattern (s, exp);

		if (tabCh == null)
			System.out.print ("\n tabCh == null ");
		else
		{
			for (int i=0; i< tabCh.length; i++)
				System.out.print ("\n tabCh [" + i + "] : " + tabCh [i]);
		}
		
		//-----------------------------------------------------------------
		exp = new String ("\\},\\{");
		System.out.print ("\n searchNbStringPattern : " + s + "  pattern : " + "\\},\\{");
		System.out.print ("\ndans : " + s);

		n = ParserTools.searchNbPatternInString (s, exp);
		System.out.print ("\n n : " + n);
		
		/* 
		  tabCh = ParserTools.searchTabStringPattern (s, "},{");
		 
		if (tabCh == null)
			System.out.print ("\n tabCh == null ");
		else
		{
			for (int i=0; i< tabCh.length; i++)
				System.out.print ("\n tabCh [" + i + "] : " + tabCh [i]);
		}
		*/
		
		//-----------------------------------------------------------------	
		System.out.print ("\n deleteCommentaires dans : " + s);
		chRet = deleteCommentaires (s);
		System.out.print ("\nchRet : " + chRet);

		//-----------------------------------------------------------------
		System.out.print ("\n searchStringDblePatternFin : " + s + 
							" patterns: laisse1 et laisse2 ");	
		
		chRet = ParserTools.searchStringDblePatternFin (s, "laisse1", "laisse2");
		System.out.print ("\n     --> " + chRet);
		System.out.print ("\n");			
		
		//-----------------------------------------------------------------
		System.out.print ("\n searchStringDblePatternFin : " + s + 
							" pattern1s laisse1 et ZZZ ");	
		
		chRet = ParserTools.searchStringDblePatternFin (s, "laisse1", "ZZZ");
		System.out.print ("\n     --> " + chRet);
		System.out.print ("\n");			
				
	} // essaisParsing
	
	
	
	//----------------------------------
	// Pour lancer le test 
	//----------------------------------
	
	public static void main(String[] args) 
	{
		// 1er test
		System.out.print ("\n-------------- Test 1 ------------");
		String s = new String ("012,34,534678,9abc,d // supp12 X laisse1 // supp2 X laisse2 ");
		ParserTools.essaisParsing (s);

		// 2eme test
		System.out.print ("\n-------------- Test 2 ------------");
		s = new String ("0123 A //8912,");
		ParserTools.essaisParsing (s);
		
		// 3eme test
		System.out.print ("\n-------------- Test 3 ------------");
		s = new String ("012");
		ParserTools.essaisParsing (s);

		// 4eme test  : chaine vide
		System.out.print ("\n-------------- Test 4 ------------");
		s = new String ("");
		ParserTools.essaisParsing (s);

		// 5eme test  
		System.out.print ("\n-------------- Test 5 ------------");
		s = new String ("{Comp}1:Clk([])from{Clock}1to{ProcFor}1;{Comp}12:Clk([])from{Clock}1to{ProcWhile}1;{Comp}1:Clk([])from{Clock}1to{ProcUntil}1;{ProcUntil}1:'TOTOTOTO'");
		ParserTools.essaisParsing (s);
		
		// 6eme test  
		System.out.print ("\n-------------- Test 6 ------------");
		s = new String ("aaaa},{bbbbb},{ccc},{dddd");
		ParserTools.essaisParsing (s);		// 6eme test  
		
		// 7eme test  
		System.out.print ("\n-------------- Test 7 ------------");
		s = new String ("[]");
		ParserTools.essaisParsing (s);
		
		// 8eme test  
		System.out.print ("\n-------------- Test 8 ------------");
		s = new String ("{oper={READ},source={MASTER2},dest={SLAVE2},value=0},{oper={ACK},source={ARB},dest={MASTER2},value=0}");
		ParserTools.essaisParsing (s);
		
		// 9eme test  
		System.out.print ("\n-------------- Test 9 ------------");
		s = new String ("record oper={READ},source={  MASTER121212},dest={SLAVE12},    value=    012},{oper={ACK},12source={ARB},dest={MASTER12121212},value=0}end");
		ParserTools.essaisParsing (s);		
	}

} // ParserTools

