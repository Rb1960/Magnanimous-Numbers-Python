
Feature: Run magnanimous_numbers program

    Scenario: Run with default arguments
        Given Eric has a copy of magnanimous_numbers.py in his current directory

        When When Eric enters python magnanimous_numbers.py 45
        And presses the <Enter> key

        Then Eric sees the first 45 Magnanimous "Numbers" displayed

            | Numbers |
            | 0       |
            | 1       |
            | 2       |
            | 3       |
            | 4       |
            | 5       |
            | 6       |
            | 7       |
            | 8       |
            | 9       |
            | 11      |
            | 12      |
            | 14      |
            | 16      |
            | 20      |
            | 21      |
            | 23      |
            | 25      |
            | 29      |
            | 30      |
            | 32      |
            | 34      |
            | 38      |
            | 41      |
            | 43      |
            | 47      |
            | 49      |
            | 50      |
            | 52      |
            | 56      |
            | 58      |
            | 61      |
            | 65      |
            | 67      |
            | 70      |
            | 74      |
            | 76      |
            | 83      |
            | 85      |
            | 89      |
            | 92      |
            | 94      |
            | 98      |
            | 101     |
            | 110     |

    Scenario: list the 241st through 250th Magnanimous Numbers
        Given Eric has a copy of magnanimous_numbers.py in his current directory

        When When Eric enters python magnanimous_numbers.py between 241 250
        And presses the <Enter> key

        Then Eric sees the Magnanimous "Numbers" between 241 and 250 displayed

            | Numbers   |
            | 17992     |
            | 19972     |
            | 20209     |
            | 20261     |
            | 20861     |
            | 22061     |
            | 22201     |
            | 22801     |
            | 22885     |
            | 24407     |

    Scenario: list the 391st to 400th Magnanimous
        Given Eric has a copy of magnanimous_numbers.py in his current directory

        When When Eric enters python magnanimous_numbers.py between 391 400
        And presses the <Enter> key

        Then Eric sees the Magnanimous "Numbers" between 391 and 400 displayed

            | Numbers   |
            | 486685    |
            | 488489    |
            | 515116    |
            | 533176    |
            | 551558    |
            | 559952    |
            | 595592    |
            | 595598    |
            | 600881    |
            | 602081    |