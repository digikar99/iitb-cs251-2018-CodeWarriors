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
             
            String currentLine = reader.readLine();
             
            while (currentLine != null)
            {    
                 
                String[] words = currentLine.toLowerCase().split(" |\\t");
                 
                for (String word : words)
                {
                    if(!stop_words.contains(word))
                    {
	                    if(word.isEmpty())
	                    {
	                    	continue;
	                    }
                        else
                        {
                            word_list.add(word);
                        }
                    }
                }

                currentLine = reader.readLine();
            }

            for(String word : word_list)
            {         
                if(wordCountMap.containsKey(word))
                {    
                    wordCountMap.put(word, wordCountMap.get(word)+1);
                }
                 

                else
                {
                    wordCountMap.put(word, 1);
                }
            }


            TreeMap<String,Integer> map = new TreeMap<>(wordCountMap);

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