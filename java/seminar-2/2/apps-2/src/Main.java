import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class Main {
    public Main() throws IOException {
    }

    public static void main(String[] args) throws IOException {

        Logger logcalc = Logger.getLogger(Main.class.getName());
        FileHandler log = new FileHandler("calc.txt",true);
        logcalc.addHandler(log);
        SimpleFormatter sFormat = new SimpleFormatter();
        log.setFormatter(sFormat);


        System.out.println("\n" + "Hi!!! I am an elementary calculator");
        logcalc.info("Program Started ");

        System.out.print("Enter number A: ");
        Scanner iScannerA = new Scanner(System.in);
        float a = iScannerA.nextInt();

        System.out.print("Enter number B: ");
        Scanner iScannerB = new Scanner(System.in);
        float b = iScannerB.nextInt();

        System.out.println("Choose an arithmetic operation");
        System.out.println("1 - Addition");
        System.out.println("2 - Subtracton");
        System.out.println("3 - Multiplication");
        System.out.println("4 - Division");
        System.out.println("5 - Taking the square root (Number A and number B)");
        System.out.println("6 - Exponentiation");
        System.out.println("7 - Print log to console ");
        Scanner iScanner = new Scanner(System.in);
        int ans = iScanner.nextInt();
        double res = 0;
        double bsqr = 0;
        if (ans == 1) {
            res = a + b;
        }
        else if (ans == 2) {
            res = a - b;
        }
        else if (ans == 3) {
            res = a * b;
        }
        else if (ans==4) {
            if (b == 0) {
                System.out.println("divide by zero is impossible");
                logcalc.log(Level.WARNING,"try to divide by zero");
            }
            else res = a / b;
        }
        else if (ans == 5) {
            res = Math.sqrt(a);
            bsqr = Math.sqrt(b);
            System.out.println("%s square root of a number A: "+ res);
            System.out.println("%s square root of a number B: "+ bsqr);

        }
        else if (ans == 6) {
            System.out.print("Enter the exponent: ");
            Scanner iScanerexpon = new Scanner(System.in);
            int countexpon = iScanerexpon.nextInt();
            logcalc.info("exponentiation is "+ countexpon);
            res = Math.pow(a,countexpon);
            bsqr = Math.pow(b, countexpon);
            System.out.println(a + " to power "+countexpon+" = "+res);
            System.out.println(b + " to power "+countexpon+" = "+bsqr);

        }
        else if (ans == 7){
            List<String> listinglog =  new ArrayList<>();
            Scanner printlog = new Scanner(new File("calc.txt"));
            while (printlog.hasNextLine())
                listinglog.add(printlog.nextLine());
            System.out.println(listinglog);
            logcalc.fine("Sow logs");
        }

        if (ans != 5 & ans !=6) {
            System.out.println(res);
            logcalc.info("result"+res);
        }
        if(ans>0 & ans<=5) {
            logcalc.info("input number A " + a + "input number B " + b + "operation" + ans);
            logcalc.info("result" + res);
            logcalc.info("result" + bsqr);
        }
        System.out.println("\n" + "See you!!! bye!!");
        logcalc.info("program end");

    }

}

