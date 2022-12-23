package service;

import data.Student;
import data.StudentGroup;

import java.util.Iterator;

import static util.RandW.getTeacherFromFile;
import static util.RandW.getStudentFromFile;

public class StudentGroupServiceImplem extends DataService  {

    @Override
    public StudentGroup getGroup() {
        return new StudentGroup(getTeacherFromFile(), getStudentFromFile());

    }
    public StudentGroup getGroup(int num){
        return new StudentGroup(getTeacherFromFile(), getStudentFromFile(), num);
    }


    public void remove (Student fio){
        Iterator<Student> studentRemove = getGroup().iterator();
            while (studentRemove.hasNext()) {
                Student student = studentRemove.next();
                if (fio.equals(student.getFio())){
                    studentRemove.remove();
                }
            }
    }
}
