package service.implement;

import data.GroupStream;
import data.comparator.GroupStreamComparator;
import service.StreamService;

import java.util.Collections;
import java.util.List;

public abstract class GroupStreamServiceImlem implements StreamService {

    @Override
    public void sortStream(List groupStreamList) {
        Collections.sort(groupStreamList, new GroupStreamComparator());
    }
}
