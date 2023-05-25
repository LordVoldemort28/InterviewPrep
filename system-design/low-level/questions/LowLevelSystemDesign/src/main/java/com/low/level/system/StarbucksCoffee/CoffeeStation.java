package com.low.level.system.StarbucksCoffee;

public class CoffeeStation {
    
    public static void main(String[] args) {

        Beverage darkRoast = new DarkRoast();
        System.out.println(darkRoast.getDescription() + " $" + darkRoast.getCost());

        Beverage houseBlend = new HouseBlend();
        houseBlend.setSize(Size.LARGE);
        houseBlend = new Whip(houseBlend);
        houseBlend = new Mocha(houseBlend);
        System.out.println(houseBlend.getDescription() + " $" + houseBlend.getCost());
        
    }
}
