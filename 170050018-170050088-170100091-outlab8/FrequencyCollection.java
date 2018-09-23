import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.*;
 
public class  FrequencyCollection
{   
    public static void main(String[] args) 
    {    
         
        HashMap<String, Integer> wordCountMap = new HashMap<String, Integer>();

        ArrayList<String> stop_words= new ArrayList<>(Arrays.asList("and","the","is","in","at","of","his","her","him"));

        ArrayList<String> word_list= new ArrayList<>();

        BufferedReader reader = null;
         
        try
        {
            reader = new BufferedReader(new FileReader(args[0]));
             
            //Reading the first line into currentLine
             
            String currentLine = reader.readLine();
             
            while (currentLine != null)
            {    
                //splitting the currentLine into words
                 
                String[] words = currentLine.toLowerCase().split(" ");
                 
                //Iterating each word
                 
                for (String word : words)
                {

                	 if(word.isEmpty())
	                 {
	                    	continue;
	                 }
                    else if(!stop_words.contains(word))
                    {
                    	word_list.add(word);
                    }
                }
                currentLine = reader.readLine();
            }

            TreeMap<String,Integer> map = new TreeMap<>();

            for(String word : word_list)
            {
            	//if word is already present in wordCountMap, updating its count
            	if(map.containsKey(word))
                {    
                    map.put(word, wordCountMap.get(word)+1);
                }

                else
                {
                	map.put(word,1);
                }

            }
            map.forEach((k,v) -> System.out.println(k + "," + v));
        }     
         
        catch (IOException e) 
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                reader.close();           //Closing the reader
            }
            catch (IOException e) 
            {
                e.printStackTrace();
            }
        }
    }    
}