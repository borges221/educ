package service;

import data.Teacher;
import repository.TeacherRepository;

public class TeacherService {

    private final TeacherRepository teacherRepository;

    public TeacherService(TeacherRepository teacherRepository) {
        this.teacherRepository = teacherRepository;
    }


    public Teacher save(Teacher teacher){
        return teacherRepository.save(teacher);
    }

    public Teacher findByID(int id){
        return teacherRepository.fimdByID(id);
    }


    public Teacher findByFIO(String fio){
        return teacherRepository.findByFIO(fio);
    }
}
