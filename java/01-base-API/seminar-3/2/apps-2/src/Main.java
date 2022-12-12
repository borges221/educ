import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random rndlist = new Random();

        List<Integer> inlist = new ArrayList<>();
        List<Integer> templist = new ArrayList<>();
        int min = -4000;
        int max = 8000;
        int iter = 10;

        while(iter!=0) {
            inlist.add(min+Math.abs(rndlist.nextInt())%max-min+1);
            iter--;

        }
        System.out.println("input list = " + inlist);

        for (int i = 0; i < inlist.size(); i++) {
            if(inlist.get(i)%2==0){
                templist.add(inlist.get(i));
            }

        }

        System.out.println("Even numbers in input list" + templist);

        for (int i = 0; i < templist.size(); i++) {
            inlist.remove(templist.get(i));
        }
        System.out.println("Odd number in input list" + inlist);

    }
}