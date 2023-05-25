package com.low.level.system.UnixFileSystem;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class FileSearchEngine {

    FileFilter fileFilter = new FileFilter();

    public List<File> searchFile(Directory directory, ISearchParams searchParams) {

        List<File> validFiles = new ArrayList<>();
        Queue<Directory> dirQ = new LinkedList<>();
        dirQ.add(directory);

        while (!dirQ.isEmpty()) {

            Directory currentDirectory = dirQ.poll();

            for (IEntry entry : currentDirectory.entries) {

                if (entry.isDirectory()) {
                    dirQ.add((Directory) entry);
                } else {
                    if (fileFilter.isValid(searchParams, (File)entry)) {
                        validFiles.add((File)entry);
                    }
                }
            }
        }
        
        return validFiles;
    }
}
