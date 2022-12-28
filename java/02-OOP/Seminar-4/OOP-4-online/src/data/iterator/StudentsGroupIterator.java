package data.iterator;

import data.Student;
import data.StudentGroup;

import java.util.Iterator;
import java.util.List;

public class StudentsGroupIterator implements Iterator<Student> {

    private StudentGroup studentGroup;
//    private Iterator<Student> students;
    private List<Student>  students;
    private int cursor;


    public StudentsGroupIterator(StudentGroup studentGroup) {
        this.studentGroup = studentGroup;
//        this.students = studentGroup.getStudentList().iterator();
        this.students =  studentGroup.getStudentList();
    }

    @Override
    public boolean hasNext() {
//        return this.students.hasNext();
          return cursor<students.size();
    }

    @Override
    public Student next() {
//        return this.students.next();
            return students.get(cursor++);
    }

    @Override
    public void remove() {
//        this.students.remove();
        this.students.remove(cursor);
    }
}
