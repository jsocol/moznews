CREATE DATABASE moznews CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE DATABASE test_moznews CHARACTER SET utf8 COLLATE utf8_unicode_ci;

GRANT ALL ON moznews.* TO moznews@localhost;
GRANT ALL ON test_moznews.* TO moznews@localhost;
