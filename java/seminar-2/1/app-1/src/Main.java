import java.io.IOException;
import java.util.Arrays;
import java.util.Random;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;
import java.util.logging.XMLFormatter;

public class Main {
    public static void main(String[] args) throws IOException {
        Random rndArr = new Random();
        int[] array = new int[22];
        int min = -101;
        int max = 101;

        Logger logger = Logger.getLogger(Main.class.getName());
        FileHandler file = new FileHandler("log.xml", 104857600, 200, true);
        logger.addHandler(file);
        XMLFormatter xmlform = new XMLFormatter();
        file.setFormatter(xmlform);

        Logger logtext = Logger.getLogger(Main.class.getName());
        FileHandler filetext = new FileHandler("log.txt", true);
        logtext.addHandler(filetext);
        SimpleFormatter sFormat = new SimpleFormatter();
        filetext.setFormatter(sFormat);


        for (int i = 0; i < array.length; i++) {
            array[i] = min + Math.abs(rndArr.nextInt()) % (max - min + 1);
            System.out.println(array[i] + "");
        }
        boolean sort = false;
        while (!sort) {
            sort = true;
            for (int i = 0; i < array.length - 1; i++) {
                if (array[i] > array[i + 1]) {
                    sort = false;
                    int temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp;

                }

            }
            logtext.info("mas " + Arrays.toString(array));
            logger.info("mas " + Arrays.toString(array));
        }


        System.out.print(Arrays.toString(array));

    }
}