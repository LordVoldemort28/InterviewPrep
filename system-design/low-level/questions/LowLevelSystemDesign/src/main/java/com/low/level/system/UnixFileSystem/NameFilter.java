package com.low.level.system.UnixFileSystem;

public class NameFilter implements IFilter {
    
    public boolean isValid(ISearchParams searchParams, File file) {

        if (searchParams.name == null) {
            return true;
        }

        return file.getName().equals(searchParams.name);
    }

}
