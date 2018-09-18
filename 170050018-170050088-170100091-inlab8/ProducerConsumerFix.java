import java.util.concurrent.atomic.AtomicInteger;

class MarketRunnable extends Thread  {
	private Thread t;
	private String threadName;
	private int updateValue;
   
	MarketRunnable(String name, int updateStockValue) {
		threadName = name;
		updateValue = updateStockValue;
	}
   
	public void run() {
		//System.out.println("Running " +  threadName );
		for(int i=0; i<100000; i++){
			ProducerConsumerFix.totalStock.addAndGet(updateValue);
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


public class ProducerConsumerFix{
	static AtomicInteger totalStock=new AtomicInteger(0);
	public static void main(String[] args){
		MarketRunnable producer = new MarketRunnable("producer", 1);
		MarketRunnable consumer = new MarketRunnable("consumer", -1);
		Thread t1 = new Thread(producer, "t1");
		Thread t2 = new Thread(consumer, "t2");
		

		t1.start();
		t2.start();
		try{
			t1.join();
			t2.join();
		}catch(InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
        }
		
		System.out.println(totalStock);
	}
}
