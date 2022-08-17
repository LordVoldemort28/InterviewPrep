package com.low.level.system.LibraryManagement.service;

import org.springframework.stereotype.Service;

@Service
public class LibraryService {
    //There should be a maximum limit of 5 on how many books can be issued to a reader.
    public static final int MAX_BOOKS_PER_READER = 5;

    //There should be maximum limit of 10 on how many days a member can borrow a book.
    public static final int MAX_DAYS_PER_BOOK = 10;

    //The system should be able to collect fines for books returned after the maximum days allowed.
    public static final int FINE_PER_DAY = 1;

    //Member should be able to reserve the books that are not currently available.
    //The system should be able to send notification to the member if the book is available.
    //The system should be able to send notification to the member if the books is not returned within the maximum days allowed.

    public void createBooks() {
    }

    public void notifyLateUsers() {
    }
    
    public void notifyAvailableBooks() {
    }

    public void issueBook() {
    }

    public void returnBook() {
    }

    public void reserveBook() {
    }

    public void searchBook() {
    }
}
