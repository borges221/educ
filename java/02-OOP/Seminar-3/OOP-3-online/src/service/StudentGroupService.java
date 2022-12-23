package service;
import data.StudentGroup;
import data.Student;
import data.User;
import data.Teacher;


import java.util.Collections;

public class StudentGroupService {
    public void sortStudent(StudentGroup studentGroup) {
        Collections.sort(studentGroup.getStudentList());

    }
}
