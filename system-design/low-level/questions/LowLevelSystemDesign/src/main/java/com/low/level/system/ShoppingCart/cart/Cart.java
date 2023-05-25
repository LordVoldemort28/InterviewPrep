package com.low.level.system.ShoppingCart.cart;

import java.util.ArrayList;
import java.util.List;

import com.low.level.system.ShoppingCart.models.Item;
import com.low.level.system.ShoppingCart.models.Product;

public class Cart implements ICart {
    
    List<Item> items;
    int totalItems;
    double discount;
    
    public Cart() {
        this.items = new ArrayList<>();
        this.totalItems = 0;
        this.discount = 0;
    }

    public void addItem(Product product, int quantity) {
        this.items.add(new Item(totalItems, product, quantity));
        this.totalItems += 1;
    }

    public double calculatePrice() {
        double totalPrice = 0;

        for (Item item : this.items) {
            totalPrice += (item.getProduct().getPrice() * item.getQuantity());
        }

        return totalPrice - discount;
    }

    public void applyDiscount(double discount) {
        this.discount = discount;
        calculatePrice();
    }

    public void checkout() {
        System.out.println("Thanks for checking out!");
        clearCart();
    }
    
    public void clearCart() {
        this.items.clear();
        this.totalItems = 0;
        this.discount = 0;

    }

    public void removeItem(Integer productInteger) {
        
    }

}
