import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {

        String str1 = new String("Hello World!");
        String str2 = new String("My name is Earl");
        String str3 = new String("I love Java");
        String str4 = new String("I live in Moscow");

        LinkedList<String> ll = new LinkedList<>();
        ll.add(str1);
        ll.add(str2);
        ll.add(str3);
        ll.add(str4);

        System.out.print("Linked List --- " + ll);

        LinkedList<String> llr = new LinkedList<>();
        while (!ll.isEmpty()) {
            String temp = ll.get(ll.size()-1);
            llr.add(temp);
            ll.remove(ll.get(ll.size()-1));
        }

        System.out.println('\n' + "Linked List revers --- " + llr);





    }
}