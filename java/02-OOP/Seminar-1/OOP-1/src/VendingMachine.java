public class VendingMachine {
    public Product getProduct(String name) {
        return new Product(name);
    }
    public Product getProduct(String name, Double price){
        return new Product(name, price);
    }
    public void productIssued (Product issu){
        System.out.printf("Issued " + issu);
    }
}
