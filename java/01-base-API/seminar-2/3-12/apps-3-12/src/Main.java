import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {

         System.out.println("Enter an mathematical expression ");

        Scanner stringScanner = new Scanner(System.in);
        String expession = stringScanner.next();
        int count = 0;
        //String expession = "[6+(3*3)]";
        char[] ch = expession.toCharArray();
        Set<Character> chars = "[]{}()".chars()
                .mapToObj(c -> (char)c)
                .collect(Collectors.toSet());
        for (int i = 0; i < ch.length; i++) {
            if(chars.contains(ch[i]))
                count++;
        }
        if (count%2==0){
            System.out.print(expession + " - true");
        }
        else System.out.print(expession + " - false");
    }
}