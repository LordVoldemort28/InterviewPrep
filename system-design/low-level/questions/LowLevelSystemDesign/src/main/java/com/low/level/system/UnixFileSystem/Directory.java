package com.low.level.system.UnixFileSystem;

import java.util.ArrayList;
import java.util.List;

public class Directory extends Entry {

    protected List<Entry> entries = new ArrayList<>();
    
    @Override
    public boolean isDirectory() {
        return true;
    }

    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public Integer getSize() {
        Integer size = 0;

        for (Entry entry : entries) {
            size += entry.getSize();
        }

        return size;
    }

    public void addEntry(Entry entry) {
        this.entries.add(entry);
    }
}
