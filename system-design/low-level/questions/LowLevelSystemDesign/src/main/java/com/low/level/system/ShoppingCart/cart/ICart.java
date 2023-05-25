package com.low.level.system.ShoppingCart.cart;

import com.low.level.system.ShoppingCart.models.Product;

public interface ICart {
    
    void addItem(Integer productId);

    void applyDiscount(double discount);

    void checkout();

    void removeItem(Integer productInteger);

    void updateQuantity(Product Id, Integer quantity);

    double calculatePrice();

    void clearCart();

}
