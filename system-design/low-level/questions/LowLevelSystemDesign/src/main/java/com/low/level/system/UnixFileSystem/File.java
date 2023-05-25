package com.low.level.system.UnixFileSystem;

import java.util.List;

public class File extends Entry {

    private byte[] content;

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public void setName(String name) {
        this.name = name;
    }

    public String getFileExtension() {
        return this.name.substring(this.name.indexOf(".") + 1);
    }

    @Override
    public boolean isDirectory() {
        return false;
    }

    public void setContent(byte[] content) {
        this.content = content;
    }
    
    @Override
    public Integer getSize() {
        return content.length;
    }

    @Override
    public String toString() {
        return "File{" +
                "name='" + name + '\'' +
                '}';
    }
}
