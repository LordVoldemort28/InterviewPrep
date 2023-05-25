package com.low.level.system.UnixFileSystem;

import java.util.List;

public class FileSystem {

    public static void main(String args[]) {

        ISearchParams searchParams = new ISearchParams();
        searchParams.setExtension("xml");
        searchParams.minSize = 2;
        searchParams.maxSize = 100;

        File xmlFile = new File();
        xmlFile.setContent("aaa.xml".getBytes());
        xmlFile.name = "aaa.xml";

        File txtFile = new File();
        txtFile.setContent("bbb.txt".getBytes());
        txtFile.name = "bbb.txt";

        File jsonFile = new File();
        jsonFile.setContent("ccc.json".getBytes());
        jsonFile.name = "ccc.json";

        File xmlFile1 = new File();
        jsonFile.setContent("ddd.xml".getBytes());
        jsonFile.name = "ddd.xml";

        Directory dir1 = new Directory();
        dir1.addEntry(txtFile);
        dir1.addEntry(xmlFile);
        dir1.addEntry(jsonFile);
        dir1.addEntry(xmlFile1);

        FileSearchEngine fileSearchEngine = new FileSearchEngine();

        List<File> searchResult = fileSearchEngine.searchFile(dir1, searchParams);

        for (File file : searchResult) {
            System.out.println(file.getName());
        }
    }
    
}
