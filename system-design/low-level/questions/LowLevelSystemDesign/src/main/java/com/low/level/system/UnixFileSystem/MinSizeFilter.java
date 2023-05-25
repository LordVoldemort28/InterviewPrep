package com.low.level.system.UnixFileSystem;

public class MinSizeFilter implements IFilter {
    
    public boolean isValid(ISearchParams searchParams, File file) {
        
        if (searchParams.minSize == null) {
            return true;
        }

        return file.getSize() >= searchParams.minSize;
    }
}
