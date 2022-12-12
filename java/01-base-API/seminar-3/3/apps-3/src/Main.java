import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

        List<Integer> inputlist = new ArrayList<>();
        Random addrndlist = new Random();
        int addlistmin = -4000;
        int addlistmax = 8000;
        int numberinlistmin = 0;
        int numberinlistmax = 0;
        double midleinlist = 0;
        int addtolistiter = 134;

        while (addtolistiter!=0) {
            inputlist.add(addlistmin+Math.abs(addrndlist.nextInt()%addlistmax-addlistmin+1));
            addtolistiter--;
        }
        System.out.println("input" + inputlist);

        for (int i = 0; i < inputlist.size(); i++) {
            if (inputlist.get(i) < numberinlistmin) {
                numberinlistmin = inputlist.get(i);
            } else if (inputlist.get(i) > numberinlistmax) {
                numberinlistmax = inputlist.get(i);
            }
        }
        System.out.println("min = " + numberinlistmin + '\n' + "max = " + numberinlistmax);

        midleinlist = inputlist.stream().reduce(Integer::sum).get();
        System.out.println("sum = " + midleinlist);


        midleinlist  = midleinlist/inputlist.size();
        System.out.println("midl = " + midleinlist);

    }
}