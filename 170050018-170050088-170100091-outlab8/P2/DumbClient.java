import java.io.*;  
import java.net.*;  
public class DumbClient {  
	public static void main(String[] args) {  
		try{      
			Socket socket = new Socket("localhost",8018);  
			DataOutputStream dout=new DataOutputStream(socket.getOutputStream());
			DataInputStream dis = new DataInputStream(socket.getInputStream());
			dout.writeUTF(args[0]);  
			dout.flush();
			String response = (String)dis.readUTF();
			System.out.println(args[0]);
			System.out.println(args[0] + response);
			dout.close();
			socket.close();
		}catch(Exception e){System.out.println(e);}  
	}  
}   
