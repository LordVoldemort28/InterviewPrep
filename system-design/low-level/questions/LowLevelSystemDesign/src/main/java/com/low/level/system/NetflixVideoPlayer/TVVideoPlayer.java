package com.low.level.system.NetflixVideoPlayer;

import com.low.level.system.NetflixVideoPlayer.VideoPlayer;

public class TVVideoPlayer extends VideoPlayer {

    public TVVideoPlayer(IDevice device, IResolution resolution) {
        this.device = device;
        this.resolution = resolution;
    }

    @Override
    void display() {
        device.getDevice();
        resolution.getResolution();
    }
    

}
