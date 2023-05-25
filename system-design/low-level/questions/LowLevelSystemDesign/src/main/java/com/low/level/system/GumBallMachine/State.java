package com.low.level.system.GumBallMachine;

public interface State {
    
    public void dispense();

    public void insertQuarter();

    public void ejectQuarter();

    public void turnCrank();

}
