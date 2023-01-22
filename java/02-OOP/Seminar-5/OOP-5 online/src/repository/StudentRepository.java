package repository;

import data.student.Student;

public class StudentRepository implements UserRepository<Student, Integer> {

    public Student delete(Student student){
        return null;
    }

    public Student deleteByGroupAndDateBorn(int groupNum, int born){
        return null;
    }
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
