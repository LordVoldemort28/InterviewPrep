package com.low.level.system.WeatherStation;

public class WeatherStationMain {

    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();

        PhoneDisplay phoneDisplay = new PhoneDisplay(weatherData);
        HeatIndexDisplay heatIndexDisplay = new HeatIndexDisplay(weatherData);

        weatherData.setMeasurements("2", "45", "0.2");
        weatherData.setMeasurements("34", "45", "0.9");
        weatherData.setMeasurements("44", "45", "0.3");

    }
    
}
