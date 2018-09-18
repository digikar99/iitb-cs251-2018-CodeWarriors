import java.text.SimpleDateFormat;
import java.util.Date;  

class RunnableDemo implements Runnable {
	private Thread t;
	private String threadName;
   
	RunnableDemo( String name) {
		threadName = name;
	}
   
	public void run() {
		//System.out.println("Running " +  threadName );
		try {
			while(true){
				SimpleDateFormat formatter = new SimpleDateFormat("HH:mm:ss");
				Date date = new Date();
				System.out.println(formatter.format(date));
				Thread.sleep(1000);
			}
		} catch (InterruptedException e) {
			System.out.println("Thread " +  threadName + " interrupted.");
		}
		// System.out.println("Thread " +  threadName + " exiting.");
	}
   
	public void start () {
		// System.out.println("Starting " +  threadName );
		if (t == null) {
			t = new Thread (this, threadName);
			t.start ();
		}
	}
}

public class Clock{
	public static void main (String[] args){
		// System.out.println("Program ran!");
		RunnableDemo R = new RunnableDemo("clock");
		R.start();
	}
}
