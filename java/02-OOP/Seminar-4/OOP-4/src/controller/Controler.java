package controller;

import data.StudentGroup;
import service.DataService;
import data.GroupStream;
import service.implement.GroupStreamServiceImlem;
import service.StreamService;


import java.util.List;

public class Controler {
    private DataService groupService;
    private StreamService streamService;


    public Controler(DataService groupService) {
        this.groupService = groupService;
    }
    public StudentGroup newGroup(int groupNumber){
        return groupService.getGroup(groupNumber);
    }
    public Controler(GroupStreamServiceImlem streamService) {
        this.streamService = streamService;
    }
    public void sortstreamlist (List<GroupStream> groupStreamList){
        streamService.sortsream(groupStreamList);
    }

}
