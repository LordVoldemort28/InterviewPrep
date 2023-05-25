package com.low.level.system.ShoppingCart.models;


import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class Product implements Comparable<Product> {
    
    Integer productId;
    String productName;
    ProductCategory productCategory;
    double price;

    public int compareTo(Product product) {
        if (productId == product.productId) {
            return 0;
        }
        return -1;
    }
}
