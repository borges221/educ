package repository;

public interface Repository <E, I>{
    E save(E empty);
    E fimdByID(I id);
}
