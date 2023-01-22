package service.student;
import data.student.StudentGroup;


import java.util.Collections;

public class StudentGroupService {
    public void sortStudent(StudentGroup studentGroup) {
        Collections.sort(studentGroup.getStudentList());

    }
}
