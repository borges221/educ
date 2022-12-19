
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Drink> HotDrinks = new ArrayList<>(Arrays.asList(
                new HotDrink("coffe", 120.0, 0.2, 80),
                new HotDrink("tea", 80.0, 0.35, 80),
                new HotDrink("hot chocolate", 100.0, 0.3, 80),
                new Drink("Water", 50.0, 0.5),
                new HotDrink("mulled wine", 450.0, 0.4, 90),
                new Drink("Lemonade", 40.0, 0.2)));


        VendingMachine machine = new HotDrinkVendingMachine();
        HotDrinkVendingMachine machine1 = new HotDrinkVendingMachine();
        HotDrinkVendingMachine machine2 = new HotDrinkVendingMachine();
        HotDrinkVendingMachine machine3 = new HotDrinkVendingMachine();
        machine.productIssued(machine.getProduct("Juce",100.0));
        machine1.productIssued(machine1.getProduct("tea",80.0,0.35,80));
        machine2.productIssued(machine2.getProduct("mulled vine", 450.0, 0.04, 90));
        machine3.productIssued(machine3.getProduct("Water"));


    }

}