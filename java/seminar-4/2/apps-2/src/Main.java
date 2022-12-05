import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

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

        Queue<String> qll = new LinkedList<>(ll);
        //qll = ll;
        System.out.println("Q - - - " + qll);
        qadd(ll);
        firstElNotRemove(ll);
        shoowAndRemove(ll);

    }
    static void qadd (Queue<String> addq){
        System.out.print("Enter to add ");
        Scanner sc = new Scanner(System.in);
        String add = sc.next();
        addq.add(add);
        System.out.println(" add q - - - " + addq);
    }
    static void firstElNotRemove (Deque<String> notremove){
        String notr = notremove.getFirst();
        System.out.println("first in q  ---- " + notr);
    }
    static void shoowAndRemove (Deque<String> snv) {
        System.out.println(" q before dell  " + snv);
        System.out.println("dell el --- " + snv.pop());
        System.out.println("q after dell --- " + snv);
    }


}