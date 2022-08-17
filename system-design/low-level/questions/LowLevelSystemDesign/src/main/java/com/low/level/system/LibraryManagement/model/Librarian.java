package com.low.level.system.LibraryManagement.model;

import lombok.Data;

@Data
public class Librarian extends Member {

    private String librarianId;

    public Librarian(String librarianId, String userName, String userEmail, String userPhone, String userAddress) {
        super(userName, userEmail, userPhone, userAddress);
        this.librarianId = librarianId;
    }

}