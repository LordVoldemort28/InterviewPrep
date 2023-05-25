```python
class ShoppingCart {
public :

  list<items> items;
  bool addItem(item it);
  bool removeItem(item it);
  bool updateItemQuantity(item it, int quantity);
  list<item> getItems();
  bool checkout();
  bool applyCoupon(int couponId);//
};

Customer class can be defined like this.
class Customer {
public :

	  ShoppingCart cart;
	  Order order;
	  ShoppingCart getShoppingCart(); //  Implement this
	  bool addItemToCart(item it);
	  bool removeItemFromCart(item it);
};

An item can be defined as below. Similary we have to define Product, order etc.
class item {
public:

  string prodId;
  int quantity;
  double price;

  bool updateQuantity(int quantity);
};
```