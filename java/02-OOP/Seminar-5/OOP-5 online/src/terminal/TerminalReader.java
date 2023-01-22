package terminal;

import terminal.executable.CommandExecutable;
import terminal.executable.CommandExecutableFactory;

import java.util.Scanner;

public class TerminalReader {

    private static TerminalReader terminalReader;
    private CommandParser commandParser;

    public TerminalReader(CommandParser commandParser) {
        this.commandParser = commandParser;
    }

    public static TerminalReader getInstance(CommandParser commandParser){
        if(terminalReader == null)
            terminalReader = new TerminalReader(commandParser);
        return null;
    }

    public void inputData(int data){
        Scanner dataScanner = new Scanner(System.in);

        while (true){
            String[] parseData = commandParser.parseCommand(dataScanner.nextLine());
            CommandExecutableFactory commandExecutableFactory = new CommandExecutableFactory();
            CommandExecutable commandExecutable = commandExecutableFactory.create(parseData);
            commandExecutable.execute();
        }
    }
}
