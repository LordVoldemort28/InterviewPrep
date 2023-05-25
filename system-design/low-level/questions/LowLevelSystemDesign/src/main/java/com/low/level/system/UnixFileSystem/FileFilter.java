package com.low.level.system.UnixFileSystem;

import java.util.ArrayList;
import java.util.List;

public class FileFilter implements IFilter {

    private List<IFilter> filters = new ArrayList<>();

    public FileFilter() {
        filters.add(new NameFilter());
        filters.add(new ExtensionFilter());
        filters.add(new MaxSizeFilter());
        filters.add(new MinSizeFilter());
    }

    public boolean isValid(ISearchParams searchParams, File file) {

        for (IFilter filter : filters) {
            if (!filter.isValid(searchParams, file)) {
                return false;
            }
        }

        return true;
    }
    
}
