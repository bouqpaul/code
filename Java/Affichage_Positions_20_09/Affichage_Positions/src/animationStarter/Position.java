package animationStarter;

public class Position 

{
	int X;
	int Y;
	
	Position (int x, int y)
	{
		X = x;
		Y = y;
	}

	public int getX ()
	{
		return X;
	}

	public int getY ()
	{
		return Y;
	}
	
	public String toString ()
	{
		String ch = new String ();
		ch = "X: " + X + " Y: " + Y;
		return ch;
		
	}
}
