package com.low.level.system.ShoppingCart.models;

import lombok.Getter;

@Getter
public class Item {
    
    private Integer itemId;
    private Product product;
    private int quantity;

    public Item(Integer itemId, Product product, Integer quantity) {
        this.itemId = itemId;
        this.product = product;
        this.quantity = quantity;
    }
    
    public void updateQuantity(int quantity) {
        this.quantity += quantity;
    }

}
