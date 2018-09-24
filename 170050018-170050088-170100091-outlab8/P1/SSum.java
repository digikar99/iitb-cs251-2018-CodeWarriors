import java.util.Arrays;
import java.util.Scanner;

public class SSum{
	
	public static void main(String[] args){
		int debug_level = 0;
		if (args.length > 0) debug_level = Integer.parseInt(args[0]);
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int p = in.nextInt();
		
		int n_ele = (int)Math.pow(p,n);
		int sum=0;
		for(int i=0; i<n_ele; i++) sum += in.nextInt();
		
		System.out.println(sum);
		
	}
}
