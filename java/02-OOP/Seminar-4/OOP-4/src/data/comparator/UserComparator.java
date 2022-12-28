package data.comparator;

import data.student.Student;

import java.util.Comparator;

public class UserComparator implements Comparator<Student> {


    @Override
    public int compare(Student student1, Student student2) {
        return (student1.getFio().compareTo(student2.getFio()));
    }
};
