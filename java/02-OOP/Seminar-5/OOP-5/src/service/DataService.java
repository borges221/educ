package service;

import data.student.Student;
import data.student.StudentGroup;
import data.User;

//public abstract class DataService {
//    public StudentGroup getGroup() {
//        return null;
//    }
//
//    public StudentGroup getGroup(int num) {
//        return null;
//    }
//
//
//    public abstract void write(User user);
//}


public interface DataService <D extends User>{
    StudentGroup getGroup();
    StudentGroup getGroup(int num);
    void findGroup(StudentGroup studentGroup);
    void usernamesort(StudentGroup studentGroup);
    void remove(StudentGroup studentGroup);

    void deleteStudent(Student entity);


}
