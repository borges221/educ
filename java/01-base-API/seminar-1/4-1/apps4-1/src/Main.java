import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        List<String> list =  new ArrayList<>();
        Scanner file = new Scanner(new File("input.txt"));
        while (file.hasNextLine())
            list.add(file.nextLine());
        String b = list.get(0);
        String a = list.get(1);
        String clearA = a.substring(2);
        String clearB = b.substring(2);
        int numberA = Integer.parseInt(clearA);
        int numberB = Integer.parseInt(clearB);
        double res = Math.pow(numberA,numberB);
        String resw = String.valueOf(res);
        FileWriter write = new FileWriter("output.txt");
        write.write(resw);
        write.close();

    }
}