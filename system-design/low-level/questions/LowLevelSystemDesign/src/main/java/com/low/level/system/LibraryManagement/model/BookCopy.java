package com.low.level.system.LibraryManagement.model;

import java.util.UUID;
import java.util.Date;

import lombok.Data;

@Data
public class BookCopy {

    private UUID bookCopyId;
    private String bookId;
    private Date issueDate;
    private Date returnDate;
    private Boolean isAvailable;
    private Member reader;

    public BookCopy(String bookId) {
        this.bookCopyId = UUID.randomUUID();
        this.isAvailable = true;
        this.bookId = bookId;
    }

}