package data;
public class User {
    private String name;
    private String soname;
    private int id;

    public User(String name, String soname, int id) {
        this.name = name;
        this.soname = soname;
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSoname() {
        return soname;
    }

    public void setSoname(String soname) {
        this.soname = soname;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}
