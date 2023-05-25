package com.low.level.system.RemoteControl;

public class NoCommand implements Command {
    
    @Override
    public void execute() {
        System.out.println("Do nothing");
    }

    @Override
    public void undo() {
        System.out.println("Do nothing");
    }
}
