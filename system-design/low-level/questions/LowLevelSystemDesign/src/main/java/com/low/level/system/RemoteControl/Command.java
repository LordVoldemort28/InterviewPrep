package com.low.level.system.RemoteControl;

public interface Command {
    
    public void execute();

    public void undo();
    
}
