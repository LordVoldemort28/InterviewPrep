package com.low.level.system.StarbucksCoffee;

public abstract class Beverage {

    Size size = Size.SMALL; //Default value
    String description = "unknown beverage";


    public String getDescription() {
        return description + " " + this.getSize();
    }

    public Size getSize() {
        return this.size;
    }

    public void setSize(Size size) {
        this.size = size;
    }
    
    abstract float getCost();

}
