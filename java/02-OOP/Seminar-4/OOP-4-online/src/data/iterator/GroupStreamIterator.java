package data.iterator;

import data.GroupStream;
import data.StudentGroup;

import java.util.Iterator;
import java.util.List;

public class GroupStreamIterator implements Iterator<StudentGroup> {

    private GroupStream groupStream;
    private List<StudentGroup> studentGroups;
    private int cursor;

    public GroupStreamIterator(GroupStream groupStream) {
        this.groupStream = groupStream;
        this.studentGroups = groupStream.getStudentGroupList();
    }

    @Override
    public StudentGroup next() {
        return studentGroups.get(cursor++);
    }

    @Override
    public boolean hasNext() {
        return cursor<studentGroups.size();
    }

    @Override
    public void remove() {
        this.studentGroups.remove(cursor);
    }
}
