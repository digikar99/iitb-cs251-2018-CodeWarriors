package com.example.shubhamkar.box8clone;

import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

import static android.provider.AlarmClock.EXTRA_MESSAGE;

public class OrderForm extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_order_form);
        Button send_button = findViewById(R.id.send_button);
        send_button.setOnClickListener(onSubmitOrder);
    }

//    public void onRadioButtonClicked(View v){
//        Toast option_changed = Toast.makeText(this, "Option Changed", 1);
//    }

    private View.OnClickListener onSubmitOrder = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            EditText email_field = (EditText) findViewById(R.id.email_field);
            EditText password = (EditText) findViewById(R.id.password);
            EditText post_address = (EditText) findViewById(R.id.post_address);
            RadioGroup order_list = (RadioGroup) findViewById(R.id.order_list);

            int order_id = order_list.getCheckedRadioButtonId();
            RadioButton order_item = (RadioButton) findViewById(order_id);

            String email = email_field.getText().toString();
            String pass = password.getText().toString();
            String addr = post_address.getText().toString();
            String order = order_item.getText().toString();

            Context context = getApplicationContext();
            //CharSequence toast_text = email + "\n" + pass + "\n" + addr + '\n' + order;
            int duration = Toast.LENGTH_SHORT;

            Toast toast = Toast.makeText(context, email, duration);
            toast.show();
            toast = Toast.makeText(context, pass, duration);
            toast.show();
            toast = Toast.makeText(context, addr, duration);
            toast.show();
            toast = Toast.makeText(context, order, duration);
            toast.show();

            Intent intent = new Intent(v.getContext(), OrderReview.class);
            intent.putExtra("email", email);
            intent.putExtra("pass", pass);
            intent.putExtra("addr", addr);
            intent.putExtra("order", order);
            startActivity(intent);
        }
    };
}
