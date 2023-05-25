package com.low.level.system.ShoppingCart.inventory;

import java.util.HashMap;
import java.util.Map;

import com.low.level.system.ShoppingCart.models.Product;

public class Catalog implements ICatalog {

    Map<String, Product> catalog;

    public Catalog() {
        this.catalog = new HashMap<>();
    }

    @Override
    public void addInCatalog(Product product) {
        this.catalog.put(product.getProductName(), product);
    }

    @Override
    public void printCatalog() {
        System.out.println("===========Product List===========");
        for (String productName : this.catalog.keySet()) {
            Product product = this.catalog.get(productName);

            System.out.printf("%d - %s\n", product.getProductId(), product.getProductName());
        }
        System.out.println("==================================");
    }
    
    @Override
    public Product getProduct(String name) {
        return this.catalog.get(name);
    }


    @Override
    public void removeProduct(String name) {
        this.removeProduct(name);
    }

}
