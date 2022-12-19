package data;

import java.util.List;

public class StudentGroup {
    private Teacher teacher;
    private List<Student> studentList;
    private int groupNum;

    public StudentGroup(Teacher teacher, List<Student> studentList) {
        this.teacher = teacher;
        this.studentList = studentList;
    }

    public StudentGroup(Teacher teacher, List<Student> studentList, int groupNum) {
        this.teacher = teacher;
        this.studentList = studentList;
        this.groupNum = groupNum;
    }

    public Teacher getTeacher() {
        return teacher;
    }

    public void setTeacher(Teacher teacher) {
        this.teacher = teacher;
    }

    public List<Student> getStudentList() {
        return studentList;
    }

    public void setStudentList(List<Student> studentList) {
        this.studentList = studentList;
    }

    public int getGroupNum() {
        return groupNum;
    }

    public void setGroupNum(int groupNum) {
        this.groupNum = groupNum;
    }
}
