package com.example.jco.android_image_slider_tutorial;

import android.os.Bundle;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class android_image_slider_activity extends AppCompatActivity  {


    TextView descriptionTextView;
    String[] textArray;
    int positionOfImage;

    float x1,x2,y1, y2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_android_image_slider_activity);
        ViewPager mViewPager = (ViewPager) findViewById(R.id.viewPageAndroid);
        AndroidImageAdapter adapterView = new AndroidImageAdapter(this);
        mViewPager.setAdapter(adapterView);



    }





}

