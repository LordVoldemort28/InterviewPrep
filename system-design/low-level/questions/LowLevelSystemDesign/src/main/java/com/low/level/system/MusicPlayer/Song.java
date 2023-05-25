package com.low.level.system.MusicPlayer;

import lombok.Builder;
import lombok.Data;

@Builder(builderMethodName = "hiddenBuilder")
@Data
public class Song {
    
    private String songName;
    private String singerName;
    private Integer songId;
    private Genre genre;

    public static SongBuilder builder(Integer songId, String songName) {
        return hiddenBuilder().songName(songName).songId(songId);
    }

}
