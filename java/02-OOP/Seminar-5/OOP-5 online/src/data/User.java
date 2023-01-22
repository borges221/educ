package data;
public class User {
    private String name;
    private String soname;
    private int id;
    private String fio;
    private int dateOfBirth;
    public User(String name, String soname, int id, String fio, int dateOfBirth) {
        this.name = name;
        this.soname = soname;
        this.id = id;
        this.fio = fio;
        this.dateOfBirth = dateOfBirth;
    }

    public User(String fio){
        this.fio = fio;
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

    public String getFio() {
        return fio;
    }

    public void setFio(String fio) {
        this.fio = fio;
    }

    public int getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(int dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
}
