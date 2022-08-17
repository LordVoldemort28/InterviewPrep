package com.low.level.system.LibraryManagement.model;

import lombok.Data;
import java.util.List;
import java.util.UUID;

@Data
public class Member {
    
    private UUID memberId;
    private String userName;
    private String userEmail;
    private String userPhone;
    private String userAddress;
    private List<BookCopy> books;

    public Member (String userName, String userEmail, String userPhone, String userAddress) {
        this.memberId = UUID.randomUUID();
        this.userName = userName;
        this.userEmail = userEmail;
        this.userPhone = userPhone;
        this.userAddress = userAddress;
    }

}
