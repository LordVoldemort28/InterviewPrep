package com.low.level.system.UnixFileSystem;

public class ExtensionFilter implements IFilter {

    public boolean isValid(ISearchParams searchParams, File file) {

        if (searchParams.extension == null) {
            return true;
        }
        
        return searchParams.extension.equals(file.getFileExtension());
    }
}
