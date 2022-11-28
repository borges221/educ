import java.util.Scanner;
class app1 {
    public static void main(String[] args) {
        System.out.print("Inter number: ");
        Scanner iScanner = new Scanner(System.in);
        int n = iScanner.nextInt();
        int countplus = 0;
        int plus = 0;
        while (countplus<n) {
            plus = countplus+n;
            countplus++;
        }
        int countf = 1;
        int fuck = 1;
        while (countf<=n) {
            fuck = countf * fuck;
            countf++;
        }
        System.out.println("triangular number " + plus);
        System.out.print("factorial " + fuck);
    }
}
