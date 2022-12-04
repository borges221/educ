import java.util.Arrays;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

        Random rndArray = new Random();

        int[] arrayA = new int[9];
        int[] arrayB = new int[5];
        int min = -9;
        int max = 9;
        int[] arrayC = new int[arrayA.length+arrayB.length];
        int indexA = 0;
        int indexB = 0;

        System.out.print("mas A: [");
        for (int i = 0; i < arrayA.length; i++) {
            arrayA[i] = min+Math.abs(rndArray.nextInt())%(max-min+1);
            if(i == arrayA.length-1){
                System.out.print(arrayA[i] + "");
            }
            else System.out.print(arrayA[i] + ", ");
        }
        System.out.print("]");

        System.out.println(" ");

        System.out.print("mas B: [");

        for (int i = 0; i < arrayB.length; i++) {
            arrayB[i] = min+Math.abs(rndArray.nextInt())%(max-min+1);
            if(i == arrayB.length-1){
                System.out.print(arrayB[i] + "");
            }
            else System.out.print(arrayB[i] + ", ");
        }
        System.out.println("]");


        Arrays.sort(arrayA);
        System.out.println(" ");
        System.out.print(Arrays.toString(arrayA)+ " ");



        Arrays.sort(arrayB);
        System.out.println("");
        System.out.println(Arrays.toString(arrayB) + " ");


        for (int c = 0; c< arrayC.length; c++) {
            if (indexA>arrayA.length-1){
                int temp = arrayB[indexB];
                arrayC[c] = temp;
                indexB++;
            }
            else if (indexB>arrayB.length-1) {
                int temp = arrayA[indexA];
                arrayC[c]= temp;
                indexA++;
            }
            else if (arrayA[indexA]<=arrayB[indexB]) {
               int temp = arrayA[indexA];
                arrayC[c] = temp;
                indexA++;
            }
            else {
                int temp2 = arrayB[indexB];
                arrayC[c] = temp2;
                indexB++;
            }

        }

        System.out.println("concatenated ascending sorted array (array A + array B");
        System.out.print("Array c = " + Arrays.toString(arrayC) + " ");
    }

}