package com.low.level.system.StarbucksCoffee;

public class Mocha extends CondimentDecorator{
    private float cost = 0.2f;

    public Mocha(Beverage beverage) {
        this.beverage = beverage;
    }

    public String getDescription() {
        return beverage.getDescription() + ", Mocha";
    }

    public float getCost() {
        return this.cost + beverage.getCost();
    }
}
