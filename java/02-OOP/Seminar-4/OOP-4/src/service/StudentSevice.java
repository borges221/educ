package service;

import data.Student;
import data.User;
import repository.StudentRepository;

public class StudentSevice extends DataService {
    private final StudentRepository studentRepository;

    public StudentSevice(StudentRepository studentRepository){
        this.studentRepository = studentRepository;
    }


    public void saveStudent (Student empty){
        studentRepository.save(empty);
    }


    public Student findStudentByID(int id){
        return studentRepository.fimdByID(id);
    }


    public Student findStudentByFIO(String fio){
        return studentRepository.findByFIO(fio);
    }

    @Override
    public void write(User user) {

    }
}
