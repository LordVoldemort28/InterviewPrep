package com.low.level.system.WeatherStation;

public class PhoneDisplay implements IObserver, IDisplay{
    
    private String temp;
    private String pressure;
    private WeatherData weatherData; 

    public PhoneDisplay(WeatherData weatherData) {
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }

    public void update() {
        this.temp = weatherData.getTemperature();
        this.pressure = weatherData.getPressure();
        display();
    }
    
    public void display() {
        System.out.println("Updated data: Temp = " + this.temp + "; Pressure = " + this.pressure + " from phone display");
    }
}
