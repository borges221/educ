package repository;

import data.student.Student;

public class StudentRepository implements UserRepository<Student, Integer> {
    @Override
    public Student save(Student empty) {
        return null;
    }

    @Override
    public Student fimdByID(Integer id) {
        return null;
    }

    @Override
    public Student findByFIO(String fio) {
        return null;
    }
}
