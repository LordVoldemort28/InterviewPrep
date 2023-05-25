package com.low.level.system.UnixFileSystem;

public interface IEntry {

    public String getName();

    public void setName(String name);

    public boolean isDirectory();

    public Integer getSize();

}
