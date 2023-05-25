package com.low.level.system.SQLLibrary;

import java.util.HashMap;

import org.springframework.stereotype.Service;

import com.low.level.system.SQLLibrary.model.Table;

@Service
public class DatabaseService {

    private HashMap<String, Table> tables = new HashMap<>();
    
    public void insert(String tableName, HashMap<String, String> data) {
        HashMap<String, String> items = new HashMap<>();

    }
    
    /*
     * CREATE TABLE <table_name>:
     * data.put(tableName, new HashMap<String, HashMap<String, String>>());
     * 
     * INSERT INTO <Table_name>:
     * HashMap<String, String> item = new HashMap<>();
     * //Put the column info
     * item.put("id", "id1");
     * item.put("name", "user1");
     * item.put("email", "user1@abc.com");
     * data.get(tableName).put("id1", item);
     * 
     * SELECT * FROM <table_name> WHERE ID=:
     * return data.get("tableName").get("id1"); //Or serialize it, or convert to any
     * format we want
     * 
     * UPDATE <table_name> set value= where ID=:
     * data.get("tableName").get("id1").put("value", "actualValue");
     */
    
}
