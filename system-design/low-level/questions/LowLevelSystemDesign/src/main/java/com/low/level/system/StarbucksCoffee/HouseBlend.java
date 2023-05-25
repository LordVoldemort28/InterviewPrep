package com.low.level.system.StarbucksCoffee;

public class HouseBlend extends Beverage{
    
    private float cost = 0.99f;

    public HouseBlend() {
        description = "House Blend";
    }

    public float getCost() {
        return this.cost;
    }
}
