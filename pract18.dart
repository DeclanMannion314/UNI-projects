class product {
  String name;
  double price;
  int? clubCardItem;

  product(this.name, this.price, [this.clubCardItem]);

  double calculatePrice(bool hasClubCard) {
    double finalPrice = price;
    if (hasClubCard && clubCardItem != null){
      finalPrice *= 0.85;
    }
    return finalPrice;
  }
}

class shoppingCart {
  List<product> items = [];

  void addToCart(product product){
    items.add(product);
  }

  double calculateOverallPrice(bool hasClubCard) {
    double totalPrice = 0;
    for (var item in items) {
      totalPrice += item.price;
    }
    if (hasClubCard) {
      totalPrice *= 0.85;
    }
    return totalPrice;
  }

  String toString() {
    String output = 'Shopping Cart: \n';
    for (product item in items) {
      output += '${item.name}, ${item.price} \n';
    }
    output += 'Total £${calculateOverallPrice(true).toStringAsFixed(2)}';
    return output;
  }

}

void main() {
  shoppingCart cart = shoppingCart();

  product product1 = product('milk', 1.90);
  product product2 = product('bread', 2.80);

  cart.addToCart(product1);
  cart.addToCart(product2);

  print(cart);

}