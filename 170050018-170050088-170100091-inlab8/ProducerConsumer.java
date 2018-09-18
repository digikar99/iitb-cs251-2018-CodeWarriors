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
			ProducerConsumer.totalStock += updateValue;
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


public class ProducerConsumer{
	static int totalStock=0;
	public static void main(String[] args){
		MarketRunnable producer = new MarketRunnable("producer", 1);
		MarketRunnable consumer = new MarketRunnable("consumer", -1);
		producer.start();
		consumer.start();
		try {
            producer.join();
            consumer.join();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
		System.out.println(totalStock);
	}
}
