Feature: Login

#  Scenario: Login vào hệ thống
#    Given Thực hiện mở trang web
#    When Thực hiện nhập thông tin username và password
#    Then bấn vào nut login
#    And kiểm tra màn hình có chữ login hay không

  Scenario Outline: Login vào hệ thống 2
    Given Thực hiện mở trang web
    When Thực hiện nhập thông tin username "<username>" và password "<password>"
    Then bấn vào nut login
    And kiểm tra màn hình có chữ login hay không

    Examples:
      |   username     |   password    |
      |standard_user   |   secret_sauce|