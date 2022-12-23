package data;

public class Student extends User{
    private String department;
    private String course;

    public Student(String name, String soname, int id, String department, String course) {
        super(name, soname, id);
        this.department = department;
        this.course = course;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }
}
