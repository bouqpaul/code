/*
 * classe Global_Var
 * 
 * PhD 17 avril 15
 * 
 * Classe pour la declaration les parametres globaux
 *     et des fonctions de traces pour le debug
 * 
 * --------------------------------------------------------
 * 
 */

package Tools;

import java.util.List;

public class Global_Var 
{
	// niveau de debug : pour des affichages specifiques
	static int  Debug_LEX = 0;	// voir le niveau dans sdl.lex
	static int  Debug_CUP = 0;	// voir le niveau dans sdl.cup

	// niveau des traces : initialise dans le main
	static public int  Niv_Debug;  


	private static String[] octetUnits = new String[] { "octets", "Ko", "Mo",
			"Go", "To" };


	
	/*----------------------------------------------------
	Converti value en octets, Ko, Mo, Go, etc. 
	--------------------------------------------------*/

	public static String formatOctet(long value) 
	{
		int unit = 0;
		while (value > 1024 && unit < octetUnits.length - 1) 
		{
			value = value / 1024;
			unit++;
		}
		return Long.toString(value) + " " + octetUnits[unit];
	} // formatOctet

	// -----------------------------------------------------
	// Pour evaluation temps de calcul
	// -----------------------------------------------------

	private static long heureDebutCalcul, heureFinCalcul;

	public static void lireStartTimeMillis() 
	{
		heureDebutCalcul = System.currentTimeMillis();
	}

	public static void lireEndTimeMillis() 
	{
		heureFinCalcul = System.currentTimeMillis();
	}

	public static void tracerTempsCalcul() 
	{
		tracer_console (100, "\n tps calcul : " + (heureFinCalcul - heureDebutCalcul)
				+ " ms");
	}

	// -----------------------------------------------------
	// Pour evaluation occupation memoire
	// -----------------------------------------------------

	private static final Runtime runtime = Runtime.getRuntime();
	private static long startTotalMem, endTotalMem;
	private static long startFreeMem, endFreeMem;
	private static long usedMem;

	public static void tracerBusyMemoire() 
	{
		long totalMem = runtime.totalMemory();
		long freeMem = runtime.freeMemory();
		long usedMem = totalMem - freeMem;

		tracer_console (100, "\nmemoire : total: " + formatOctet(totalMem) + " free: "
				+ formatOctet(freeMem) + " used: " + formatOctet(usedMem));
	} // tracerBusyMemoire

	// Garbage Collector

	
	public static void gc() 
	{
		Runtime runtime = Runtime.getRuntime();
		runtime.gc();
	} // gc


	//------------------------------------------------------------------
	// affiche la chaine s dans la console selon le niveau de Debug :
	//------------------------------------------------------------------
	
	public static void tracer_console (int niv, String s) 
	{
		if (Niv_Debug >= niv)
		{
			java.lang.System.out.print (s);
		}
	}	


	//------------------------------------------------------------------
	// affiche la chaine s dans la console selon le niveau de Debug :
	//------------------------------------------------------------------
		
	public static void tracer_liste_console (int niv, List<Object> liste) 
	{
		for (Object o : liste)
		{
			Global_Var.tracer_console (niv, "\n" + o);
		}
	}
	
	

	//------------------------------------------------------------------
	// Ajout d'espaces dans buffer pour le décalage de l'affichage
	//------------------------------------------------------------------
	
	public static void decaler_buffer (StringBuffer buffer, int n) 
	{
		// buffer.append ("\n");
		for (int i = 0; i < n; i++)  buffer.append ("    ");

		
	} // decaler_buffer
	
	
	//------------------------------------------------------------------
	// Ajout d'espaces pour le décalage de l'affichage
	//------------------------------------------------------------------
	
	public static void decaler_console (int niv, int n) 
	{	
		for (int i = 0; i < n; i++)  tracer_console (niv, "    ");		
	} // decaler_buffer
	
	

	//------------------------------------------------------------------
	// afficher s si booleen entre = true
	//------------------------------------------------------------------
	public static void tracer ( boolean niv_debug, String s)
	{
		if ( niv_debug )
		{
			System.out.println (s);
		}

	}
	
	//------------------------------------------------------------------
	public static void tracer(int niv, String s) 
	{
		if (Niv_Debug >= niv)  System.out.print (s);
	}

} // Global_Var

