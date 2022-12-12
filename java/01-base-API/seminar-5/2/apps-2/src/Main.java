import java.sql.Array;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) {


        class Task3 {



            private Map<Character, Integer> rimToArabic = new HashMap<>();

            Task3() {

                fillMap();
            }

            private void fillMap() {
                rimToArabic.put('I', 1);
                rimToArabic.put('V', 5);
                rimToArabic.put('X', 10);
                rimToArabic.put('L', 50);
                rimToArabic.put('C', 100);
                rimToArabic.put('D', 500);
                rimToArabic.put('M', 1000);
            }


            void tranleterimToArabic(String rim) {
                System.out.println(rim);
                int result = 0;
                for (int i = rim.length() - 1; i >= 0; i--) {
                    int x = rimToArabic.get(rim.charAt(i));
            /*
                   Здесь нужно прописать все проверки на корректность строки содержащей римкое число.
            */
                    if (i - 1 >= 0 &&
                            rimToArabic.get(rim.charAt(i)).toString().charAt(0) == '5' &&
                            rimToArabic.get(rim.charAt(i - 1)).toString().charAt(0) == '5') {
                        System.out.println("Не корректное");
                    /*
                    Начало работы с корректной строкой содержащей римское число.
                    Ожидается корректное число. Числа вида LC IIII IC обрабатываются но их быть не должно.
                     */
                    } else if (i - 1 >= 0) {
                        if (x == rimToArabic.get(rim.charAt(i - 1))) {
                            result += x;
                        } else if (rimToArabic.get(rim.charAt(i)).toString().charAt(0) == '5') {
                            if (x > rimToArabic.get(rim.charAt(i - 1))) {
                                result += x - rimToArabic.get(rim.charAt(i - 1));
                            } else {
                                result += x + rimToArabic.get(rim.charAt(i - 1));
                            }
                            i--;
                        } else if (x > rimToArabic.get(rim.charAt(i - 1))) {
                            result += x - rimToArabic.get(rim.charAt(i - 1));
                            i--;
                        } else {
                            result += x;
                        }
                    } else {
                        result += x;
                    }

                }

                System.out.println(result);

            }

        }
    }

}