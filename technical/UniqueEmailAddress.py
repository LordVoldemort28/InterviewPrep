class UniqueEmailAddress:

    def preprocess(self, email):
        localName, domain = email.split("@")

        if '+' in localName:
            localName = localName.split('+')[0]

        if '.' in localName:
            localName = localName.replace('.', '')

        return localName+'@'+domain

    def numUniqueEmails(self, emails) -> int:

        for idx, email in enumerate(emails):
            emails[idx] = self.preprocess(email)

        return len(set(emails))


emails = ["test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

tool = UniqueEmailAddress()
tool.numUniqueEmails(emails)
