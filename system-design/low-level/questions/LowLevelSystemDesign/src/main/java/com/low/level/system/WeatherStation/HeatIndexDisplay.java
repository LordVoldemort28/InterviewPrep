package com.low.level.system.WeatherStation;

public class HeatIndexDisplay implements IObserver, IDisplay {

    private float temp;
    private float humidity;
    private WeatherData weatherData;

    public HeatIndexDisplay(WeatherData weatherData) {
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }

    public void update() {
        this.temp = Float.parseFloat(weatherData.getTemperature());
        this.humidity = Float.parseFloat(weatherData.getPressure());
        display();
    }

    public void display() {
        System.out.println("Updated data: HeadIndex = " + (temp/humidity) + "; from Heat Index Display");
    }
    
}
