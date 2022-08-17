package com.low.level.system.NetflixVideoPlayer;

import com.low.level.system.NetflixVideoPlayer.IDevice;
import com.low.level.system.NetflixVideoPlayer.IResolution;

abstract class VideoPlayer {
    
    IDevice device;
    IResolution resolution;

    abstract void display();

    public void getDevice() {
        device.getDevice();
    }

    public void getResolution() {
        resolution.getResolution();;
    }
}
