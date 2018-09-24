import java.io.*;  
import java.net.*;

public class EchoServer{

	public static void main(String[] args){
		try{  
			ServerSocket server = new ServerSocket(8018);
			while(true){
				Socket socket = server.accept();
				DataInputStream dis = new DataInputStream(socket.getInputStream());
				DataOutputStream dous = new DataOutputStream(socket.getOutputStream());
				String msg = (String)dis.readUTF();
				dous.writeUTF(args[0]);
				dous.flush();
				System.out.println(msg);
			}
		}catch(Exception e){System.out.println(e);}  
	}  
}

