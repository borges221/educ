package controller;

import data.student.StudentGroup;
import service.implement.StudentGroupServiceImplem;

public class GroupController implements Controller<StudentGroup, Integer> {

    private final StudentGroupServiceImplem studentGroupServiceImplem;


    public GroupController(StudentGroupServiceImplem studentGroupServiceImplem) {
        this.studentGroupServiceImplem = studentGroupServiceImplem;
    }


    public StudentGroup groupCreate(int numGroup){
        return studentGroupServiceImplem.findGroup(numGroup);

    }


    @Override
    public StudentGroup save(StudentGroup entity) {
       return studentGroupServiceImplem.saveGroup(entity);
    }

    @Override
    public StudentGroup findByID(Integer id) {
        return studentGroupServiceImplem.findGroup(id);

    }

}
