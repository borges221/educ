package terminal.executable;

import data.student.Student;
import data.student.StudentGroup;
import service.student.StudentSevice;

public class DeleteStudentByGroupAndBorn implements CommandExecutable{

    private StudentSevice studentSevice;
    private Student student;

    private StudentGroup studentGroup;


    public DeleteStudentByGroupAndBorn(StudentSevice studentSevice, Student student, Student studentGroup) {
        this.studentSevice = studentSevice;
        this.student = student;
        this.studentGroup = studentGroup;
    }

    @Override
    public void execute() {
        studentSevice.deleteStudeentByGroupAndBorn(studentGroup.getGroupNum(),student.getDateOfBirth());
        System.out.printf("delete studen - %s, number group - %d, date of birth - %d.",
                student.getFio(),studentGroup.getGroupNum(), student.getDateOfBirth());
    }
}
