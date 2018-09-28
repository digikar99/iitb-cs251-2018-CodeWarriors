package com.example.shubhamkar.box8clone;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class OrderReview extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_order_review);

        Intent intent = getIntent();
        String email = intent.getStringExtra("email");
        String pass = intent.getStringExtra("pass");
        String addr = intent.getStringExtra("addr");
        String order = intent.getStringExtra("order");

        TextView email_confirm = (TextView)findViewById(R.id.email_confirm);
        TextView pass_confirm = (TextView)findViewById(R.id.pass_confirm);
        TextView addr_confirm = (TextView)findViewById(R.id.addr_confirm);
        TextView order_confirm = (TextView)findViewById(R.id.order_confirm);

        email_confirm.setText("email: " + email);
        pass_confirm.setText("password: " + pass);
        addr_confirm.setText("postal_address: " + addr);
        order_confirm.setText("selected_option: " + order);
    }
}
