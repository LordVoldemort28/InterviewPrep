package com.low.level.system.UnixFileSystem;

public class MaxSizeFilter implements IFilter {
    
    public boolean isValid(ISearchParams searchParams, File file) {
        
        if (searchParams.maxSize == null) {
            return true;
        }

        return file.getSize() <= searchParams.maxSize;
    }
}
