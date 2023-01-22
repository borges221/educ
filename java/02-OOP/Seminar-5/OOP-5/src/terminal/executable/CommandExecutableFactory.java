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
            case "deleteByFIO":
                new DeleteStudentByFioExecutable(studentSevice, new Student(input[1]));
                break;
            case "deleteByGroupAndDateOfBorn":
                new DeleteStudentByGroupAndBorn(studentSevice, new Student(input[1]), new Student(input[2]));
        }
        return null;

    }
}
