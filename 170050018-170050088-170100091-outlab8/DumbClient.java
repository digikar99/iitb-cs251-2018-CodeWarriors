import java.io.*;  
import java.net.*;  
public class DumbClient {  
	public static void main(String[] args) {  
		try{      
			Socket socket = new Socket("localhost",6666);  
			DataOutputStream dout=new DataOutputStream(socket.getOutputStream());  
			dout.writeUTF(args[0]);  
			dout.flush();  
			dout.close();  
			socket.close();  
		}catch(Exception e){System.out.println(e);}  
	}  
}   
