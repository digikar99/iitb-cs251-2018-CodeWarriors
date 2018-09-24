import java.util.Arrays;
import java.util.Scanner;

class Summer implements Runnable{
	int st;
	int ed;
	int id;
	public Summer(int start, int end, int thread_id){
		st = start;
		ed = end;
		id = thread_id;
	}
	
	public void run(){
		int sum=0;
		if (PSum.debug_level>1)
			System.err.println("Summing from " + Integer.toString(st) + " to " + Integer.toString(ed));
		for(int i=st; i<ed; i++){
			sum += PSum.pre_ans[i];
		}
		if (id > -1) {
			PSum.post_ans[id] = sum;
			if (PSum.debug_level>1)
				System.err.println(String.format("Writing %d to post_ans cell %d", sum, id));
		}
		else PSum.final_answer = sum;
	}
}

public class PSum{
	public static int[] pre_ans;
	public static int[] post_ans;
	public static int final_answer;
	static int n_ele, n, p;
	// p - number of elements to sum;
	// n - abstract!
	static Thread[] t;
	public static int debug_level;
	public static void reduce(){
		int n_threads = n_ele / p;
		pre_ans = post_ans;
		post_ans = new int[n_threads];
		t = new Thread[n_threads];
		for(int i=0; i<n_threads; i++){
			post_ans[i] = 0;
			Summer summer = new Summer(i*p, (i+1)*p, i);
			t[i] = new Thread(summer);
			t[i].start();
		}
		try{
			for(int i=0; i<n_threads; i++){
				t[i].join();
			}
		}catch(InterruptedException e) {
			e.printStackTrace();
		}
		n_ele = n_threads;
	}
	
	public static void main(String[] args){
		debug_level = 0;
		if (args.length > 0) debug_level = Integer.parseInt(args[0]);
		Scanner in = new Scanner(System.in);
		n = in.nextInt();
		p = in.nextInt();
		
		n_ele = (int)Math.pow(p,n);
		post_ans = new int[n_ele];
		for(int i=0; i<n_ele; i++) post_ans[i] = in.nextInt();
		if (debug_level > 0) System.err.println("Input taken!");
		
		while(n_ele != 1){
			reduce();
			if (debug_level > 0)
				System.err.println("Reduction step " + Integer.toString(n_ele));
		}

		/*
		Summer summer = new Summer(0, p, -1);
		Thread t_final = new Thread(summer);
		t_final.start();
		try{
			t_final.join();
		}catch(InterruptedException e) {
			e.printStackTrace();
		}
		*/
		System.out.println(post_ans[0]);
		
	}
}
