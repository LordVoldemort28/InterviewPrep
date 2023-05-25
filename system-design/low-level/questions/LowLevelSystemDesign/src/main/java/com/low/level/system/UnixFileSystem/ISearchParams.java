package com.low.level.system.UnixFileSystem;

import lombok.Data;

@Data
public class ISearchParams {

    String name;
    String extension;
    Integer maxSize;
    Integer minSize;
    
}
