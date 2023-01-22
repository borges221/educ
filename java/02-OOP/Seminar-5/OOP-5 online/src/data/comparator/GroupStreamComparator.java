package data.comparator;

import data.GroupStream;

import java.util.Comparator;

public class GroupStreamComparator implements Comparator<GroupStream> {

    @Override
    public int compare(GroupStream group1, GroupStream group2) {
        int groupsize1 = group1.getStudentGroupList().size();
        int groupsize2 = group2.getStudentGroupList().size();
        return Integer.compare(groupsize1, groupsize2);
    }
}
