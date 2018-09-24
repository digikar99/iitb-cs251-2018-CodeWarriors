import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.*;
 
public class  FrequencyCollection
{   
    public static void main(String[] args) 
    {    
        //Creating wordCountMap which holds words as keys and their occurrences as values
         
        HashMap<String, Integer> wordCountMap = new HashMap<String, Integer>();

        ArrayList<String> stop_words= new ArrayList<>(Arrays.asList("and","the","is","in","at","of","his","her","him"));
     
        BufferedReader reader = null;
         
        try
        {
            //Creating BufferedReader object
             
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
                    //if word is already present in wordCountMap, updating its count
                    if(!stop_words.contains(word))
                    {
	                    if(word.isEmpty())
	                    {
	                    	continue;
	                    }
	                     
	                    else if(wordCountMap.containsKey(word))
	                    {    
	                        wordCountMap.put(word, wordCountMap.get(word)+1);
	                    }
	                     
	                    //otherwise inserting the word as key and 1 as its value

	                    else
	                    {
	                        wordCountMap.put(word, 1);
	                    }
	                }
                }
                 
                //Reading next line into currentLine
                 
                currentLine = reader.readLine();
            }


            //Set<Entry<String, Integer>> entrySet = wordCountMap.entrySet();

            TreeMap<String,Integer> map = new TreeMap<>(wordCountMap);

            map.forEach((k,v) -> System.out.println(k + "," + v));
             
            // for (Entry<String, Integer> entry : entrySet)
            // {
            //     System.out.println(entry.getKey() + "," + entry.getValue());
            // }
             
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