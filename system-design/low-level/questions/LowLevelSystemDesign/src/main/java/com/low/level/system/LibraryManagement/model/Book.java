package com.low.level.system.LibraryManagement.model;

import java.util.UUID;

import com.low.level.system.LibraryManagement.enums.BookCategory;
import com.low.level.system.LibraryManagement.model.Member;

import lombok.Data;
import lombok.NonNull;

import java.util.List;
import java.util.Date;

@Data
public class Book {

    private UUID bookId;
    private String bookName;
    private String author;
    private String subject;
    private BookCategory category;
    private String publicationDate;
    private Integer rackNumber;

    @NonNull
    private Integer availableCopies;

    private List<BookCopy> availableCopiesList;
    private List<BookCopy> issuedCopiesList;

    public Book(Integer availableCopies) {
        this.bookId = UUID.randomUUID();
        this.availableCopies = availableCopies;

        //Create copies of the book
        for (int i = 0; i < availableCopies; i++) {
            availableCopiesList.add(new BookCopy(bookId.toString()));
        }
    }
    
    public BookCopy checkout(Member reader, Date issueDate, Date returnDate) {
        if (availableCopiesList.size() > 0) {
            BookCopy bookCopy = availableCopiesList.remove(0);
            bookCopy.setReader(reader);
            bookCopy.setIsAvailable(false);
            bookCopy.setIssueDate(issueDate);
            bookCopy.setReturnDate(returnDate);

            issuedCopiesList.add(bookCopy);
            return bookCopy;
        }
        return null;
    }

    public void checkin(BookCopy bookCopy) {

        bookCopy.setReader(null);
        bookCopy.setIsAvailable(true);
        bookCopy.setIssueDate(null);
        bookCopy.setReturnDate(null);
        
        issuedCopiesList.remove(bookCopy);
        availableCopiesList.add(bookCopy);
    }
}
