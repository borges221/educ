package terminal.executable;

import data.student.Student;
import service.student.StudentSevice;

public class CommandExecutableFactory {

    private StudentSevice studentSevice;

    public CommandExecutableFactory(StudentSevice studentSevice) {
        this.studentSevice = studentSevice;
    }

    public CommandExecutableFactory() {
    }
    public CommandExecutable create(String[] input){
        switch (input[0]){
            case "add":
                new CreateStudentExecutable(studentSevice,  new Student(input[1]));
                break;
            case "delete":
                new DeleteStudentExecutable(studentSevice, new Student(input[1]));
                break;
        }
        return null;

    }
}
