package controller;

import data.student.Student;
import service.student.StudentSevice;

public class StudentController implements UserController<Student, Integer> {

    private final StudentSevice studentSevice;


    public StudentController(StudentSevice studentSevice) {
        this.studentSevice = studentSevice;
    }


    @Override
    public Student save(Student entity) {
        return studentSevice.saveStudent(entity);
    }

    @Override
    public Student findByID(Integer id) {
        return studentSevice.findStudentByID(id);
    }

    @Override
    public Student findByFIO(String fio) {
        return studentSevice.findStudentByFIO(fio);
    }
}
