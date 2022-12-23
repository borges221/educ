package service;

import data.StudentGroup;
import static util.RandW.getTeacherFromFile;
import static util.RandW.getStudentFromFile;

public class StudentGroupServiceImplem extends DataService {

    @Override
    public StudentGroup getGroup() {
        return new StudentGroup(getTeacherFromFile(), getStudentFromFile());

    }
    public StudentGroup getGroup(int num){
        return new StudentGroup(getTeacherFromFile(), getStudentFromFile(), num);
    }

}
