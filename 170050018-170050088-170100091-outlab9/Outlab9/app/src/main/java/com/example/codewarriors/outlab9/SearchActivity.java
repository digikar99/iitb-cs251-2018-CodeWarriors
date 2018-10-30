package com.example.codewarriors.outlab9;

import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.JsonReader;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class SearchActivity extends AppCompatActivity {

    private class GetUsers extends AsyncTask<URL, Integer, String> {

        private Context context;;
        public GetUsers(Context c){
            context = c;
        }

        @Override
        public String doInBackground(URL... urls) {
            int count = urls.length;
            for (int i = 0; i < count; i++) {
                try {
                    HttpURLConnection urlConnection;
                    urlConnection = (HttpURLConnection) urls[i].openConnection();
                    InputStream in = new BufferedInputStream(urlConnection.getInputStream());
                    BufferedReader reader = new BufferedReader(new InputStreamReader(in));

                    StringBuffer buffer = new StringBuffer();
                    String line = "";

                    while ((line = reader.readLine()) != null) {
                        buffer.append(line+"\n");
                        Log.d("Response: ", "> " + line);   //here u ll get whole response...... :-)

                    }

                    return buffer.toString();
                } catch(IOException ioe) {

                }



            }
            return "";
        }

        @Override
        protected void onPostExecute(String result) {
            try {
                SearchActivity.jobj = new JSONObject(result);
            } catch (JSONException jse){
                jse.printStackTrace();
            }

            Toast.makeText(context,
                    "Completed Search",
                    Toast.LENGTH_SHORT).show();
            jsonToStringArray();
            ArrayAdapter<String> username_populator = new ArrayAdapter<String>(context, android.R.layout.simple_list_item_1, usernames);
            ListView searchResults = (ListView) findViewById(R.id.searchResults);
            searchResults.setAdapter(username_populator);
        }
    }

    protected static JSONObject jobj;
    protected static List<String> usernames;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);
        ListView searchResults = (ListView) findViewById(R.id.searchResults);
        searchResults.setOnItemClickListener(viewUser);
    }

    public void startSearch(View v){
        EditText searchBox = (EditText)(findViewById(R.id.searchBox));
        String search_term = searchBox.getText().toString();
        URL[] urls = new URL[1];
        try {
            urls[0] = new URL("https://api.github.com/search/users?q=" + search_term + "&sort=repositories");
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        new GetUsers(this).execute(urls);

    }


    protected void jsonToStringArray(){
        try {
            JSONArray jarr = jobj.getJSONArray("items");
            usernames = new ArrayList<String>();
            for (int i=0; i<jarr.length(); i++){
                JSONObject temp = jarr.getJSONObject(i);
               usernames.add(temp.getString("login"));
            }

        } catch (JSONException e) {
            e.printStackTrace();
        }

    }

    protected AdapterView.OnItemClickListener viewUser = new AdapterView.OnItemClickListener(){
        @Override
        public void onItemClick(AdapterView<?> parent, View view,int position, long id){
            Intent intent = new Intent(view.getContext(), UserActivity.class);
            intent.putExtra("login", usernames.get(position));
            startActivity(intent);
            //Toast.makeText(SearchActivity.this, "" + position + usernames.get(position), Toast.LENGTH_SHORT).show();
        }
    };

}
