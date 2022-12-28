package repository;

import data.User;

public interface UserRepository <E extends User, I> extends Repository<E,I> {
    E findByFIO(String fio);
}
