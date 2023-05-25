package com.low.level.system.StarbucksCoffee;

public class Whip extends CondimentDecorator {

    private float cost = 0.2f;

    public Whip(Beverage beverage) {
        this.beverage = beverage;
    }

    public String getDescription() {
        return beverage.getDescription() + ", Whip";
    }
    
    public float getCost() {

        float cost = this.cost + beverage.getCost();
        
        if (beverage.getSize() == Size.SMALL) {
            cost += 1;
        } else if (beverage.getSize() == Size.MEDIUM) {
            cost += 2;
        } else if (beverage.getSize() == Size.LARGE) {
            cost += 3;
        }

        return cost;
    }
}
