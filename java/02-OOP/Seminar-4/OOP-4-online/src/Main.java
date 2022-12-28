public class Main {
    public static void main (String[] args) {
        System.out.println("Создать класс GroupStream, содержащий в себе список StudentGroup и реализующий интерфейс Iterable<StudentGroup>\n" +
                "Создать класс GroupStreamComparator<GroupStream>, реализующий сравнение количества групп входящих в GroupStream\n" +
                "Создать класс GroupStreamServiceImpl, добавив в него метод сортировки списка потоков, используя созданный GroupStreamComparator\n" +
                "Модифицировать класс Controller, добавив в него созданный сервис\n" +
                "Модифицировать класс Controller, добавив в него метод, сортирующий список потоков, путем вызова созданного сервиса");
    }
}