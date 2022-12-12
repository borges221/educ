public class Main {
    public static void main(String[] args) {
        int simply = 1000;
        for (int i = 1; i <= simply; i++) {
            boolean flag = true;
            for (int j = 2; j < i && flag == true; j++) {
                if (i % j == 0) {
                    flag = false;
                }
            }
            if (flag == true) {
                System.out.printf("%d "+'\n', i);
            }
        }
    }
    }

