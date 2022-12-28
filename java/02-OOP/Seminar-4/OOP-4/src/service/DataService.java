package service;

import data.StudentGroup;
import data.User;

public abstract class DataService {
    public StudentGroup getGroup() {
        return null;
    }

    public StudentGroup getGroup(int num) {
        return null;
    }


    public abstract void write(User user);
}
