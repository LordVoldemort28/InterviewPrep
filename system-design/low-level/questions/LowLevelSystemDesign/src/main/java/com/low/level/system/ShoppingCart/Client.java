package com.low.level.system.ShoppingCart;

import com.low.level.system.ShoppingCart.models.Product;
import com.low.level.system.ShoppingCart.models.ProductCategory;

public class Client {
    
    public static void main(String args[]) {
        Catalog catalog = new Catalog();
        catalog.addProduct(new Product.Builder().withID("1").withName("Book-OOPS").withPrice(200)
                .withCategory(ProductCategory.BOOK).build());
        catalog.addProduct(new Product.Builder().withID("2").withName("Book-Python").withPrice(200)
                .withCategory(ProductCategory.BOOK).build());
        catalog.addProduct(new Product.Builder().withID("3").withName("Book-Azure").withPrice(200)
                .withCategory(ProductCategory.BOOK).build());

        Product product = catalog.lookUp("Book-Azure");
        ICart cart = new ShoppingCart();
        cart.addItem(product);
        cart.removeItem(product.getName());

    }
}
