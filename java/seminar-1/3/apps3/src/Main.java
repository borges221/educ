import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        System.out.println("\n" + "Hi!!! I am an elementary calculator");
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
            res = Math.pow(a,countexpon);
            bsqr = Math.pow(b, countexpon);
            System.out.println(a + " to power "+countexpon+" = "+res);
            System.out.println(b + " to power "+countexpon+" = "+bsqr);

        }

        if (ans != 5 & ans !=6) {
            System.out.println(res);
        }
        System.out.println("\n" + "See you!!! bye!!");
        }


    }

