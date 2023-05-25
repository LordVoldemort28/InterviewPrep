package com.low.level.system.RemoteControl;

public class Light {
    
    private enum LightStateEnums
    {
        ON, OFF
    };

    private LightStateEnums lightState ;

    public Light() {
        this.lightState = LightStateEnums.OFF;
    }

    public void on() {
        System.out.println("Light is on!");
        this.lightState = LightStateEnums.ON;
    }

    public void off() {
        System.out.println("Light is off!");
        this.lightState = LightStateEnums.OFF;
    }
}
