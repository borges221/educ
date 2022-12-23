package controller;

import data.StudentGroup;
import service.DataService;
public class Controler {
    private DataService groupService;

    public Controler(DataService groupService) {
        this.groupService = groupService;
    }
    public StudentGroup newGroup(int groupNumber){
        return groupService.getGroup(groupNumber);
    }
}
