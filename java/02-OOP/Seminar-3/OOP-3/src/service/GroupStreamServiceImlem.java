package service;

import data.GroupStream;
import data.comparator.GroupStreamComparator;

import java.util.Collections;
import java.util.List;

public class GroupStreamServiceImlem extends StreamService {

    @Override
    public void sortsream(List<GroupStream> groupStreamList) {
        Collections.sort(groupStreamList, new GroupStreamComparator());
    }
}
