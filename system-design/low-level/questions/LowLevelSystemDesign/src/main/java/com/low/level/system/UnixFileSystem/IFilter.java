package com.low.level.system.UnixFileSystem;

public interface IFilter {
    
    public boolean isValid(ISearchParams searchParams, File file);

}
