package com.low.level.system.RemoteControl;

public class RemoteControlTest {
    
    public static void main(String args[]) {
        Light light = new Light();
        RemoteControl remoteControl = new RemoteControl();
        
        Command lightOnCommand = new LightOnCommand(light);
        Command lightOffCommand = new LightOffCommand(light);

        remoteControl.setCommand(0, lightOnCommand, lightOffCommand);

        remoteControl.onButtonPressed(0);
        remoteControl.offButtonPressed(0);
        remoteControl.undoButtonPressed();
    }
}
