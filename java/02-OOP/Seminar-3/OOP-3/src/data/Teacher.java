package data;

public class Teacher extends User {
    private String category;

    public Teacher(String name, String soname, int id, String category) {
        super(name, soname, id);
        this.category = category;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
}

