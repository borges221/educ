package terminal.executable;

import data.User;
import service.student.StudentSevice;

public class DeleteStudentByFioExecutable implements CommandExecutable{
    private StudentSevice studentSevice;
    private User user;

    public DeleteStudentByFioExecutable(StudentSevice studentSevice, User user) {
        this.studentSevice = studentSevice;
        this.user = user;
    }

    @Override
    public void execute() {
        studentSevice.deleteStudentbyFio(user.getFio());
    }
}
