package com.example.jco.android_image_slider_tutorial;

/**
 * Created by jco on 9/28/2016.
 */

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.drawable.Drawable;
import android.support.v4.view.PagerAdapter;
import android.support.v4.view.ViewPager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.nostra13.universalimageloader.core.ImageLoader;
import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;
import com.nostra13.universalimageloader.core.listener.SimpleImageLoadingListener;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.InputStream;
import java.net.URL;

public class AndroidImageAdapter extends PagerAdapter {
    Context mContext;
    TextView slideShowTextView;
    ImageView slideShowImageView;
    LayoutInflater layoutInflater;
    String jsonStr;

    AndroidImageAdapter(Context context) {

        this.mContext = context;

        //parseJSONData();

    }

    @Override
    public int getCount() {
        return sliderImageURL.length;
    }

    private int[] sliderImagesId = new int[]{
            R.drawable.image1, R.drawable.image2, R.drawable.image3, R.drawable.image4, R.drawable.image5,
    };

    private String[] descriptions = new String[]{
            "1","2", "3","4","The Top of the Rock offers one distinct advantage over the Empire State Building: views of the Empire State Building. Thanks to this — and its three tiers of spacious 360-degree decks — the Top of the Rock Observation Deck has what many consider the finest panoramic vistas in all of New York City. The Top of the Rock crowns the famous GE Building, a 1933 art deco skyscraper that rises an impressive 850 feet, making it the 10th highest in New York City. The view includes most every major sight of New York City, from natural to manmade: the Chrysler Building, the Empire State Building, Grand Central Terminal, the Hudson River, the East River and, on clear days, the Verrazano-Narrows Bridge. Also, Rockefeller Center is closer to Central Park than the Empire State Building, and the view of the iconic park, ringed by skyscrapers, is among the best in the city. The observation deck has windows on the 67th and 69th floors, and is open-air at the 70th floor with only clear glass panels between you and the beautiful view. In other words, it’s ideal for snapping photos. The tour experience is bolstered by various videos and other visual effects, including the Summit Shuttle, the glass-topped elevators that zip to the top in less than a minute. A light show plays across the top of the elevator, through which you can see the elevator shaft hurtling by. 30 Rockefeller Plaza,",
    };

    private String [] sliderImageURL = new String[]{"http://newyorkyimby.com/wp-content/uploads/2016/09/Turkevi-Center_Render-Aerial-looking-west_Courtesy-Perkins-Eastman-777x437.jpg",
            "http://afasiaarchzine.com/wp-content/uploads/2016/02/BIG-.-THE-SPIRAL-tower-.-NEW-YORK-1.jpg",
            "https://cdn0.vox-cdn.com/thumbor/_Zx0CmwWrvO78MVyC2NwdOb-qRA=/1800x0/filters:no_upscale()/cdn0.vox-cdn.com/uploads/chorus_asset/file/7192495/2.jpg",
            "https://static.dezeen.com/uploads/2016/02/the-spiral-big-new-york-skyscraper_dezeen_936_7.jpg"
    };

/*
    public String [] parseJSONData(){


        String jsonStr = getJsonFromSomewhere();
        Gson gson = new Gson();
        Click clicks[] = gson.fromJson(jsonStr, Click[].class);
    }

        try{
        JSONArray jsonarray = new JSONArray(jsonStr);
        for (int i = 0; i < jsonarray.length(); i++) {
            JSONObject jsonobject = jsonarray.getJSONObject(i);
            String name = jsonobject.getString("name");
            String url = jsonobject.getString("url");
        }

    }
        catch (Exception ex){
            System.out.print(ex.getStackTrace());
        }




*/

    @Override
    public boolean isViewFromObject(View v, Object obj) {
        return v == ((View) obj);
    }

    @Override
    public Object instantiateItem(ViewGroup container, int position) {

        ImageLoader imageLoader = ImageLoader.getInstance(); // Get singleton instance

        imageLoader.init(ImageLoaderConfiguration.createDefault(mContext));
        // Load image, decode it to Bitmap and return Bitmap synchronously
        System.out.println(sliderImageURL[position]);





        layoutInflater = (LayoutInflater)mContext.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        View layout = layoutInflater.inflate(R.layout.slideshow, null);

        slideShowTextView = (TextView) layout.findViewById(R.id.slideShowTextView);
        slideShowTextView.setText(descriptions[position]);

        slideShowImageView =(ImageView) layout.findViewById(R.id.slideShowImage);

        imageLoader.displayImage(sliderImageURL[position], slideShowImageView);
        ((ViewPager) container).addView(layout);

        return layout;

    }

    @Override
    public void destroyItem(ViewGroup container, int i, Object obj) {
        ((ViewPager) container).removeView((View) obj);
    }
}