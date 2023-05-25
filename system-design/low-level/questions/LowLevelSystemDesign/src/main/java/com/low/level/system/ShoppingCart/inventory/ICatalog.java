package com.low.level.system.ShoppingCart.inventory;

import com.low.level.system.ShoppingCart.models.Product;

public interface ICatalog {
    
    void addInCatalog(Product product);

    void printCatalog();

    Product getProduct(String name);

    void removeProduct(String productId);

}
