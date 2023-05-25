package com.low.level.system.MusicPlayer;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class MusicPlayer {

    ArrayList<Song> musicList;
    Queue<Song> playlist;
    Random random;
    int totalSongCount;
    LinkedHashMap<Integer, Integer> songMap;

    public MusicPlayer() {
        this.musicList = new ArrayList<>();
        this.playlist = new LinkedList<>();
        this.random = new Random();
        this.totalSongCount = 0;
        this.songMap = new LinkedHashMap<Integer, Integer>();
    }

    //Implement addSong
    public void addSong(Integer id, String songName, String singerName, Genre genre) {

        if (songMap.containsKey(id)){
            System.out.println("Song already exist in the list");
            return;
        }

        Song song = new Song(songName, singerName, id, genre);
        this.musicList.add(song);

        //Storing id with index in list mapping
        this.songMap.put(id, totalSongCount);

        this.totalSongCount += 1;
    }
    
    //Implement getSong
    public Song getSong(Integer songId) {

        Integer songIdx = this.songMap.get(songId);
        Song song = this.musicList.get(songIdx);

        //Make this song recent
        this.songMap.remove(songId);
        this.songMap.put(songId, songIdx);
        
        return song;
    }

    public void getSongs() {
        System.out.println("=================Songs List================");
        for (Integer songId : this.songMap.keySet()) {
            Integer songIdx = this.songMap.get(songId);
            System.out.printf("Song=%s, SongId=%d, SongIndex=%d\n", this.musicList.get(songIdx).getSongName(), songId, songIdx);
        }
        System.out.println("=================================");
    }
    
    //Play random song

    //Play song
    //Close player
    //Play music from queue
    
}
