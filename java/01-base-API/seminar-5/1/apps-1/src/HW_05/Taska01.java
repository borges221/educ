package HW_05;

import java.util.*;

class Taska01 {

    private Map<String, String> phoneBook = new HashMap<>();


    Taska01 (){
//        phoneBook.
        phoneBook.put("Иванов Иван ", " +7 9999 999 99 99, +7 646 644 64 46");
        phoneBook.put("Иванов Колян "," +7 9999 111 11 11, +7 641 222 222 22");
        phoneBook.put("Волчек Александр ", " +7 999 146 14 68, +7 646 222 22 22");
    }

    public String getContact (String name) {
        String contact = phoneBook.get(name);
        return contact;
    }

    public void createContact (String name, String phone) {
        // метод получения данных от пользователя в ТЗ не указан (консольный или другой)
        int sizeBefor = phoneBook.size();
        phoneBook.put(name, phone);
        if (sizeBefor != phoneBook.size()){
            System.out.println(phoneBook);
        } else {
            System.out.println("Контакт с именем " + name + " уже существует!!!");
        }
    }

    public void addPhone (String name, String phone) {
        if (phoneBook.get(name) != null) {
            phoneBook.put(name, phoneBook.get(name) + ", " + phone);
            System.out.println(phoneBook);
        } else {
            System.out.println("Контакт с именем " + name + " не существует!!!");
        }
    }

    public void solution() {
        System.out.println(phoneBook);
    }
}




