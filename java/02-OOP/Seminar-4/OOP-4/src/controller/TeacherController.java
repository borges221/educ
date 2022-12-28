package controller;

import data.Teacher;
import service.TeacherService;

public class TeacherController implements UserController<Teacher, Integer> {

    private final TeacherService teacherService;

    public TeacherController(TeacherService teacherService) {
        this.teacherService = teacherService;
    }


    @Override
    public Teacher save(Teacher teacher) {
        return teacherService.save(teacher);
    }

    @Override
    public Teacher findByID(Integer id) {
        return teacherService.findByID(id);
    }

    @Override
    public Teacher findByFIO(String fio) {
        return teacherService.findByFIO(fio);
    }
}
