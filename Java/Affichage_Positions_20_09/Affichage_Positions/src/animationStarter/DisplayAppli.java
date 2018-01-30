package animationStarter;

//-------------------------------------------------
// DisplayAppli
//
// Application pour l'affichage d'une simulation
//
// PhD 28 aout 17
//--------------------------------------------------

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.awt.*;       
import java.io.BufferedReader;

import Tools.FileTools;
import Tools.ParserTools;
import Tools.Global_Var;


public class DisplayAppli 
{	
	AnimationStarter_AffPositions frame;
	//--------------------------------------------------	
	// Variables utiles pour l'application d'affichage 
	//--------------------------------------------------	
	int No_Step_Display;
	public Trajectoire Traj;
	
	//-----------------------------------------------------
	// Constructeur :
	//
	//  ici, initialisation de l'application concernee 
	//  par l'affichage dans le display
	//-----------------------------------------------------
	
	public DisplayAppli (AnimationStarter_AffPositions uneFrame) 
	{
		frame = uneFrame;
		
		displayAppli_init ();
	}

	 // -----------------------------------------------------------
	 //  init de l'appli de parsing d'une liste de positions
	 //
	 //  (methode appelee par le constructeur DisplayAppli () 
	 // -----------------------------------------------------------
	 
	 public void displayAppli_init ()  
	 {		
		String nomFichierPositions = new String ();
		// Evite que les 2 premier tours s'execute, Comportement non souhaite
		No_Step_Display = -2; 

		//--------------------------------------------
		// choix du fichier .trajectoire
		//--------------------------------------------
				
		String nomFichierTraj = new String ();	
		if ((nomFichierTraj = FileTools.fileChoice ("trajectoire")) == null)
		{
			Global_Var.tracer (0, "\nErreur de fileChoice");
			return;
		}
		
		if ((Traj = lireTrajectoire (nomFichierTraj)) == null)
		{
			Global_Var.tracer (0, "\nErreur de lireTraj");
			return;
		}	
		
		Global_Var.tracer (0, "\n " + Traj.getListeFigure().size () + " Figures lues \n");			
		
		
	 } // trace_opb_displayAppli_init
	 
	 public Figure autoFig (String typeFig, String[] args){
		 Figure resFig;
		 switch(typeFig){
		 case "rect":
			 resFig = new Rectangle(args[0], args[1], args[2], args[3]);
			 
			 break;
			 
		 case "line":
			 resFig = new Ligne(args[0], args[1], args[2], args[3]);
			 break;
			 
		 case "arc":
			 resFig = new Arc(args[0], args[1], args[2], args[3], args[4] , args [5]);
			 break;
			 
		 case "text":
			 resFig = new Text(args[0], args[1], args[2]);
			 break;
			 
		 case "oval":
			 resFig = new Ovale(args[0], args[1], args[2], args[3]);
			 break;
			 
		 default:
			 resFig = new Text();
			 System.out.println("type Fig non reconnue: " + typeFig);
		 }
		 
		 return resFig;
	 }
	 
	 public int createFig(String line, Trajectoire Traj){
		 int Etat = 0;
		 if(line != null){
			 
			 if(!(commentaire(line)) && bonType(line)){
				 String[] info = traiterLigne(line);
				 String[] argAuto = Arrays.copyOfRange(info, 1, info.length);
				 Figure F = autoFig(info[0], argAuto);
				 Traj.addFigure(F);
				 Etat = 1;
				 }else{
					 Etat = 1;
					 }
			 }else{
				 Etat = 0;
				 }

		 return Etat;
		 
	 }
	 public Trajectoire lireTrajectoire (String nomFichier){
		 BufferedReader reader = null;
		 try{
			 reader = Tools.FileTools.openReader(nomFichier);
			 }
		 catch(Exception e){
			 System.out.println(e);
			 }
		 
		 Trajectoire Traj = new Trajectoire();
		 String line = new String();
		 int Etat = 1;
		 while(Etat != 0){
			 try{
				 line = reader.readLine();
				 Etat = createFig(line, Traj);
				 }
			 catch(Exception e){
				 System.out.println(e);
				 }
			 }
		 return Traj;
		 }
	 
	 public String[] enleveVide(String[] splt){
		 int eltNonVide = 0;
		for(int i = 0; i < splt.length; i++){
			if(splt[i].length() > 0){
				eltNonVide++;
				}
		}
		
		String[] newSplt = new String[eltNonVide];
		
		int indiceNew = 0;
		for(int i = 0; i < splt.length; i++){
			if(splt[i].length() > 0){
				newSplt[indiceNew] = splt[i];
				indiceNew++;
				}
		}
		return newSplt; 
	 }
	 
	 public String[] traiterLigne(String line){
		String[] splt = line.split(" ");
		String[] newSplt = enleveVide(splt);
		
		int taille = newSplt.length;
		for(int i = 0; i < taille - 1; i++){
			newSplt[i] = newSplt[i].trim();
			newSplt[i] = newSplt[i].substring(0, newSplt[i].length() - 1);
		}
		newSplt[taille - 1] = newSplt[taille - 1].trim();
		
		return newSplt;
	 }
	 
	 public boolean commentaire(String line){
		 boolean tt = line.startsWith("//");
		 return tt;
	 }
	 
	 public boolean bonType(String line){
		 boolean tt = line.startsWith("text") || line.startsWith("rect") || line.startsWith("line") || line.startsWith("oval") || line.startsWith("arc");
		 return tt;
	 }
	 
	 public void displayAppli_Traj_Step (Graphics2D g2){

		 if (No_Step_Display < Traj.getListeFigure().size()){
			 
			 for(int i = 0; i <= No_Step_Display; i++){
				 Figure F = Traj.getListeFigure().get(i);
				 F.display(g2);
				 }
		 }

		 No_Step_Display = (No_Step_Display + 1) % Traj.getListeFigure().size ();
	 }
		
} // DisplayAppli
	



