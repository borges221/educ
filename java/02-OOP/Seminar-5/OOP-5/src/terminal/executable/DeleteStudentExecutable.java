package terminal.executable;

import data.student.Student;
import service.student.StudentSevice;

public class DeleteStudentExecutable implements CommandExecutable{

    private StudentSevice studentSevice;
    private Student student;

    public DeleteStudentExecutable(StudentSevice studentSevice, Student student) {
        this.studentSevice = studentSevice;
        this.student = student;
    }

    @Override
    public void execute() {
        studentSevice.deleteStudent(student);

    }
}
