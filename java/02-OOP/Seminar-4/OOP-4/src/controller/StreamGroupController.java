package controller;

import data.GroupStream;
import service.StreamService;

import java.util.List;

public class StreamGroupController implements Controller<GroupStream, Integer> {

    private final StreamService<GroupStream, Integer> streamService;

    public StreamGroupController(StreamService<GroupStream, Integer> streamService) {
        this.streamService = streamService;
    }


    void  listStreamSort(List<GroupStream> groupStreamList){
        streamService.sortStream(groupStreamList);
    }


    @Override
    public GroupStream save(GroupStream entity) {
        return streamService.save(entity);
    }

    @Override
    public GroupStream findByID(Integer id) {
        return streamService.findbyID(id);
    }
}
