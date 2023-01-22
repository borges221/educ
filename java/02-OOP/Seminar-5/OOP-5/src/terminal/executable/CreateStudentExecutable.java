package terminal.executable;

import data.student.Student;
import service.student.StudentSevice;

public class CreateStudentExecutable implements CommandExecutable{

    private StudentSevice studentSevice;
    private Student student;

    public CreateStudentExecutable(StudentSevice studentSevice, Student student) {
        this.studentSevice = studentSevice;
        this.student = student;
    }

    @Override
    public void execute() {
        studentSevice.saveStudent(student);
    }
}
