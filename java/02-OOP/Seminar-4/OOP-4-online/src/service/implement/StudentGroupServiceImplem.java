package service.implement;

import data.Student;
import data.StudentGroup;
import repository.Repository;
import service.DataService;

import java.util.Iterator;

import static util.RandW.getTeacherFromFile;
import static util.RandW.getStudentFromFile;

public class StudentGroupServiceImplem extends DataService {
    private final Repository<StudentGroup, Integer> studentGroupIntegerRepository;

    public StudentGroupServiceImplem(Repository<StudentGroup, Integer> studentGroupIntegerRunnable) {
        this.studentGroupIntegerRepository = studentGroupIntegerRunnable;
    }

    public StudentGroup saveGroup(StudentGroup studentGroup) {
        return studentGroupIntegerRepository.save(studentGroup);
    }

    public StudentGroup findGroup(int groupNumber) {
        return studentGroupIntegerRepository.fimdByID(groupNumber);
    }


    public StudentGroup getGroup(int num) {
        return new StudentGroup(getTeacherFromFile(), getStudentFromFile(), num);
    }


    public void remove(Student fio) {
        Iterator<Student> studentRemove = getGroup().iterator();
        while (studentRemove.hasNext()) {
            Student student = studentRemove.next();
            if (fio.equals(student.getFio())) {
                studentRemove.remove();
            }
        }
    }
}
