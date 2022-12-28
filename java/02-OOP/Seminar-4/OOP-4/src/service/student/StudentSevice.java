package service.student;

import data.student.Student;
import data.User;
import data.student.StudentGroup;
import repository.StudentRepository;
import service.DataService;

public class StudentSevice implements DataService {
    private final StudentRepository studentRepository;

    public StudentSevice(StudentRepository studentRepository){
        this.studentRepository = studentRepository;
    }

    public static Student save(Student entity) {
        return entity;
    }


    public Student saveStudent (Student empty){
        return studentRepository.save(empty);

    }


    public Student findStudentByID(int id){
        return studentRepository.fimdByID(id);
    }


    public Student findStudentByFIO(String fio){
        return studentRepository.findByFIO(fio);
    }


    public void write(User user) {

    }

    @Override
    public StudentGroup getGroup() {
        return null;
    }

    @Override
    public StudentGroup getGroup(int num) {
        return null;
    }

    @Override
    public void findGroup(StudentGroup studentGroup) {

    }

    @Override
    public void usernamesort(StudentGroup studentGroup) {

    }

    @Override
    public void remove(StudentGroup studentGroup) {

    }
}
