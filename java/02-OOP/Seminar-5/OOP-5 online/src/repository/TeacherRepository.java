package repository;

import data.Teacher;

public class TeacherRepository implements UserRepository<Teacher, Integer> {

    public TeacherRepository() {
    }


    @Override
    public Teacher save(Teacher empty) {
        return null;
    }

    @Override
    public Teacher fimdByID(Integer id) {
        return null;
    }

    @Override
    public Teacher findByFIO(String fio) {
        return null;
    }
}
