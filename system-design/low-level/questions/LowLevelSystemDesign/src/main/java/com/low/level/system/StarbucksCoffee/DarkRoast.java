package com.low.level.system.StarbucksCoffee;

public class DarkRoast extends Beverage {
    
    private float cost = 1.4f;
    
    public DarkRoast() {
        description = "Dark Roast Beverage";
    }

    public float getCost() {
        return this.cost;
    }
}
