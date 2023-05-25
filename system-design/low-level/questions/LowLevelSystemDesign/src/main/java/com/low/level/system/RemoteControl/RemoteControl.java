package com.low.level.system.RemoteControl;

public class RemoteControl {
    private static final int COUNT_COMMANDS = 1;
    private Command[] onCommands;
    private Command[] offCommands;
    private Command undoCommand;

    public RemoteControl() {
        this.onCommands = new Command[COUNT_COMMANDS];
        this.offCommands = new Command[COUNT_COMMANDS];

        Command noCommand = new NoCommand();
        for (int i = 0; i < COUNT_COMMANDS; i++) {
            onCommands[i] = noCommand;
            offCommands[i] = noCommand;
        }
        undoCommand = noCommand;

    }
    
    public void onButtonPressed(Integer slot) {
        this.onCommands[slot].execute();
        this.undoCommand = this.onCommands[slot];
    }

    public void offButtonPressed(Integer slot) {
        this.offCommands[slot].execute();
        this.undoCommand = this.offCommands[slot];
    }

    public void setCommand(int slot, Command onCommand, Command offCommand) {
        this.offCommands[slot] = offCommand;
        this.onCommands[slot] = onCommand;
    }

    public void undoButtonPressed() {
        this.undoCommand.undo();
    }   
}
