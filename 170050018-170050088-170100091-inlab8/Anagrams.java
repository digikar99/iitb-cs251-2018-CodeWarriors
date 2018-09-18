import java.util.Scanner; 
import java.util.*;  

class Anagrams
{ 
    public static void main(String args[]) 
    { 
        // Using Scanner for Getting Input from User 
        Scanner in = new Scanner(System.in); 
  
        String s1 = in.nextLine(); 
        // System.out.println("You entered string "+s1); 
        String s2 = in.nextLine();        
        // System.out.println("You entered string "+s2);
        String a=s1.toUpperCase();
        String b=s2.toUpperCase();
		// System.out.println(a + b);
        //System.out.println(a.length());



        
        Map<Character,Integer> m = new HashMap<Character,Integer>();
        Map<Character,Integer> n = new HashMap<Character,Integer>();
        m.put(a.charAt(0),1);
        System.out.println(a.length());
        for (Integer i = 1; i < a.length(); ++i){
            if(m.containsKey(a.charAt(i))){
                m.put(a.charAt(i),m.get(a.charAt(i))+1);
            }
            else{
                m.put(a.charAt(i),1);
            }
        }
        n.put(b.charAt(0),1);
        for (int i = 1; i < b.length(); ++i){
            if(n.get(b.charAt(i)) != null){
            n.put(b.charAt(i),n.get(b.charAt(i))+1);
            }
            else{
                n.put(b.charAt(i),1);
            }   
        }
        if(m.equals(n)){
            System.out.println("Anagrams");
        }
        else{
            System.out.println("Not Anagrams");   
        }
    } 
} 
