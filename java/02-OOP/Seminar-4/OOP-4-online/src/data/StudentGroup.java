package data;

import java.util.Iterator;
import java.util.List;

public class StudentGroup implements Iterable<Student> , Comparable<StudentGroup> {
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

    @Override
    public Iterator<Student> iterator(){
        return new StudentsGroupIterator(this);
    }

    @Override
    public int compareTo(StudentGroup o) {
        return 0;
    }
}
