package com.low.level.system.MusicPlayer;

import com.low.level.system.MusicPlayer.Song.SongBuilder;

public class MusicPlayerTest {
    
    public static void main(String args[]) {
        Song song1 = Song.builder(1, "deva deva").build();
        Song song2 = Song.builder(2, "kesaria").build();
        Song song3 = Song.builder(3, "slowly slowly").build();

        MusicPlayer musicPlayer = new MusicPlayer();
        musicPlayer.addSong(1, "deva deva", "Arijit", Genre.POP);
        musicPlayer.addSong(2, "kesaria", "Arijit", Genre.POP);
        musicPlayer.addSong(3, "slowly slowly", "Rahul", Genre.POP);
        musicPlayer.getSongs();

        //Kesaria should be in end of list
        musicPlayer.getSong(2);
        musicPlayer.getSongs();

        musicPlayer.addSong(4, "Go!", "Shivani", Genre.POP);
        musicPlayer.getSongs();

        // Kesaria should be in end of list
        musicPlayer.getSong(1);
        musicPlayer.getSongs();

    }
}
