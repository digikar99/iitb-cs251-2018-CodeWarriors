import java.io.*;  
import java.net.*;

public class EchoServer{

	public static void main(String[] args){
		try{  
			ServerSocket server = new ServerSocket(6666);
			while(true){
				Socket socket = server.accept();//establishes connection   
				DataInputStream dis = new DataInputStream(socket.getInputStream());  
				String str = (String)dis.readUTF();  
				System.out.println(str);
				System.out.println(str + args[0]);
			}
		}catch(Exception e){System.out.println(e);}  
	}  
}

