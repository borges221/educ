package data;

public class Student extends User implements Comparable<Student>{
    private String department;
    private String course;

    public Student(String name, String soname, int id, String department, String course, String fio, int dataOfBiryh) {
        super(name, soname, id, fio, dataOfBiryh);
        this.department = department;
        this.course = course;
    }
    public int compareTo(Student student){
        if(student.getDateOfBirth()>this.getDateOfBirth()){
            return 1;
        }
        if(student.getDateOfBirth()<this.getDateOfBirth()){
            return -1;
        }
        return 0;
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
