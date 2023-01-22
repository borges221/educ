package service;

import data.GroupStream;

import java.util.List;

//public class StreamService {
//
//    public void sortsream (List<GroupStream> groupStreamList){
//
//    }
//}
public interface StreamService<S extends GroupStream, I>{
    void  sortStream(List<S> groupStreamList);
        S save(S entity);
        S findbyID(I id);

    void sortsream(List<GroupStream> groupStreamList);
}