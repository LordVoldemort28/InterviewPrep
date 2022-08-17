package com.low.level.system.NetflixVideoPlayer;

public class MainVideoPlayer {
    
    public static void main(String[] args) {
        
        IResolution resolution = new Resolution1080P();
        IDevice device = new TV();
        
        VideoPlayer tVideoPlayer = new TVVideoPlayer(device, resolution);
        tVideoPlayer.display();
        
    }
}
