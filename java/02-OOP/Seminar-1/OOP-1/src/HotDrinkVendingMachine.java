public class HotDrinkVendingMachine extends VendingMachine{
    public Product getPriduct(String name, Double price, Double volume){
        return new Drink(name, price, volume);
    }
    public Product getProduct(String name, Double price, Double volume, int temperature) {
        return new HotDrink(name, price, volume, temperature);
    }
}
