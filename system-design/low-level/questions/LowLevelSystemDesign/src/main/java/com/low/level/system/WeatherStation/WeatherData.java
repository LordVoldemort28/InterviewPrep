package com.low.level.system.WeatherStation;

import java.util.*;

public class WeatherData implements ISubject {

    private List<IObserver> observers;
    private String temp;
    private String pressure;
    private String humidity;

    public WeatherData() {
        observers = new ArrayList<IObserver>();
    }

    public void registerObserver(IObserver observer) {
        observers.add(observer);
    }

    public void removeObserver(IObserver observer) {
        observers.remove(observer);
    }

    public void notifyObserver() {
        for (IObserver observer : observers) {
            observer.update();
        }
    }

    public void measurementChanges() {
        notifyObserver();
    }

    public void setMeasurements(String temp, String pressure, String humidity) {
        this.temp = temp;
        this.pressure = pressure;
        this.humidity = humidity;
        measurementChanges();
    }

    public String getTemperature() {
        return this.temp;
    }

    public String getPressure() {
        return this.pressure;
    }

    public String getHumidity() {
        return this.humidity;
    }

}
