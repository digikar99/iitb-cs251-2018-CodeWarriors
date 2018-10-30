package com.example.codewarriors.outlab9;

import android.content.ClipData;
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.text.MessageFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.Period;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.List;

import static com.example.codewarriors.outlab9.SearchActivity.jobj;

public class UserActivity extends AppCompatActivity {


    protected class GetUserDetails extends AsyncTask<URL, Integer, String> {
        Context context;
        public GetUserDetails(Context c){
            context = c;
        }
        @Override
        public String doInBackground(URL... urls) {
            try {
                    HttpURLConnection urlConnection;
                    urlConnection = (HttpURLConnection) urls[0].openConnection();
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
                    ioe.printStackTrace();
                    return "";
                }
            }

        @Override
        public void onPostExecute(String result) {
            try {
                jobj = new JSONObject(result);
                try {
                    new GetRepoDetails(context).execute(new URL(jobj.getString("repos_url")));
                    TextView name = (TextView) findViewById(R.id.name);
                    TextView company = (TextView) findViewById(R.id.company);
                    TextView location = (TextView) findViewById(R.id.location);
                    name.setText(jobj.getString("name"));
                    company.setText(jobj.getString("company"));
                    location.setText(jobj.getString("location"));

                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }
            } catch (JSONException jse){
                jse.printStackTrace();
            }
        }
    }
    protected class GetRepoDetails extends AsyncTask<URL, Integer, String> {
        Context context;
        public GetRepoDetails(Context c){
            context = c;
        }
        @Override
        public String doInBackground(URL... urls) {
            try {
                HttpURLConnection urlConnection;
                urlConnection = (HttpURLConnection) urls[0].openConnection();
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
                ioe.printStackTrace();
                return "";
            }
        }

        @Override
        public void onPostExecute(String result) {
            try {
                repos = new JSONArray(result);
                getDataFromRepos();
                ListView repo_list = (ListView) findViewById(R.id.repo_list);
                RepoAdapter repoAdapter = new RepoAdapter(context, R.layout.repo, repository_list);
                repo_list.setAdapter(repoAdapter);
            } catch (JSONException jse){
                jse.printStackTrace();
            }
        }
    }
    protected class Repo{
        public String name;
        public String age;
        public String description;
    }
    protected class RepoAdapter extends ArrayAdapter<Repo>{
        private int resourceLayout;
        private Context mContext;

        public RepoAdapter(Context context, int resource, List<Repo> items) {
            super(context, resource, items);
            this.resourceLayout = resource;
            this.mContext = context;
        }
        @Override
        public View getView(int position, View convertView, ViewGroup parent) {

            View v = convertView;

            if (v == null) {
                LayoutInflater vi;
                vi = LayoutInflater.from(mContext);
                v = vi.inflate(resourceLayout, null);
            }

            Repo p = getItem(position);

            if (p != null) {
                TextView tt1 = (TextView) v.findViewById(R.id.repo_name);
                TextView tt2 = (TextView) v.findViewById(R.id.repo_age);
                TextView tt3 = (TextView) v.findViewById(R.id.repo_description);

                if (tt1 != null) {
                    tt1.setText(p.name);
                }

                if (tt2 != null) {
                    tt2.setText(p.age);
                }

                if (tt3 != null) {
                    tt3.setText(p.description);
                }
            }

            return v;
        }
    }
    protected JSONObject jobj;
    protected JSONArray repos;
    protected List<Repo> repository_list;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user);

        Intent intent = getIntent();
        String login = intent.getStringExtra("login");
        try {
            URL url = new URL("https://api.github.com/users/" + login);
            new GetUserDetails(this).execute(url);
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }

    }
    protected void getDataFromRepos(){
        repository_list = new ArrayList<Repo>();
        for(int i=0; i<repos.length(); i++){
            try {
                Repo temp = new Repo();
                temp.name = repos.getJSONObject(i).getString("name");
                if (temp.name.length() > 20){
                    temp.name = temp.name.substring(0,17) + "...";
                }

                String string = null;
                string = repos.getJSONObject(i).getString("created_at");
                Date creation_date = (new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssZ")).parse(string.replaceAll("Z$", "+0000"));
                Date current_date = new Date();
                //LocalDate d1 = creation_date.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
                //LocalDate d2 = current_date.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
                //Period diff = Period.between(d1, d2);
                long diff = current_date.getTime() - creation_date.getTime();
                Date diff_date = new Date(diff); // +6307200000L
//                String years = Integer.toString(diff_date.getYear());
//                String months = Integer.toString(diff_date.getMonth());
//                String days = Integer.toString(diff_date.getDate());
                Calendar calendar = new GregorianCalendar();
                calendar.setTime(diff_date);
                String years = Integer.toString(calendar.get(Calendar.YEAR) - 1970);
                String months = Integer.toString(calendar.get(Calendar.MONTH));
                String days = Integer.toString(calendar.get(Calendar.DAY_OF_MONTH));
                //String date_string = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssZ").format(new Date(diff));
                temp.age = MessageFormat.format("{0}y {1}m {2}d", years, months, days);
                temp.description = repos.getJSONObject(i).getString("description");
                repository_list.add(temp);
            } catch (JSONException | ParseException e) {
                e.printStackTrace();
            }
            //Calendar calendar = javax.xml.bind.DatatypeConverter.parseDateTime(repos.getJSONObject(i).getString("name"));

        }
    }

//    protected class UserArrayAdapter extends ArrayAdapter<String> {
//        private final Context context;
//        private final String[] repo_name;
//        private final String[] repo_age;
//        private final String[] repo_description;
//
//        public UserArrayAdapter(Context c,
//                                String repository_name,
//                                String repository_age,
//                                String repository_description) {
//            context = c;
//            repo_age = repository_age;
//            repo_description = repository_description;
//            repo_name = repository_name;
//
//
//        }
//
//    };
}
