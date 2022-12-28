package service.implement;

import data.GroupStream;
import data.comparator.GroupStreamComparator;
import service.StreamService;

import java.util.Collections;
import java.util.List;

public class GroupStreamServiceImlem extends StreamService {

    @Override
    public void sortsream(List<GroupStream> groupStreamList) {
        Collections.sort(groupStreamList, new GroupStreamComparator());
    }
}
