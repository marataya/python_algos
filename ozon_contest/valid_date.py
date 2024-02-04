from io import StringIO
import sys
from ozon_contest.test_utils import prepare_input, compare_outputs
from time import time

"""
public static boolean has31Days(int month) {
        switch (month) {
            case 1: // January
            case 3: // March
            case 5: // May
            case 7: // July
            case 8: // August
            case 10: // October
            case 12: // December
                return true;
            default:
                return false;
        }
    }

    public static boolean isLeapYear(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }

    public static void main(String[] args) throws IOException {

        String inputDirName = "src/ozon_contest/input/valid_date/";

        var inputFiles = Utils.processFiles(inputDirName);

        for (var f : inputFiles) {
            System.out.println(">>>>>>>>>>>>>>FILE: " + f);
            try (var reader = Files.newBufferedReader(Paths.get(inputDirName + f))) {
                int n = Integer.parseInt(reader.readLine());
                for (int i = 0; i < n; i++) {
                    String result = "YES";
                    String line = reader.readLine();
                    String[] numbers = line.split(" ");
                    int day = Integer.parseInt(numbers[0]);
                    int month = Integer.parseInt(numbers[1]);
                    int year = Integer.parseInt(numbers[2]);
                    if (day > 28) {
                        if (month == 2 && !isLeapYear(year)) {
                            result = "NO";
                        } else if (month == 2 && isLeapYear(year)) {
                            result = day == 29 ? "YES" : "NO";
                        } else if (!has31Days(month)) {
                            result = day > 30 ? "NO" : "YES";
                        }
                    }
                    System.out.println(result);
                }
            }

            Utils.showAnswer(inputDirName, f);
        }

    }
"""


def has_31_days(month) -> bool:
    match month:
        case 1:
            return True
        case 3:
            return True
        case 5:
            return True
        case 7:
            return True
        case 8:
            return True
        case 10:
            return True
        case 12:
            return True
        case _:
            return False


def is_leap_year(year) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


if __name__ == '__main__':
    input_files, output_files = prepare_input('./input/valid_date/*')
    begin = time()
    for idx_file in range(len(input_files)):
        # putting program output into buffer to compare with answer later
        output_buffer = StringIO()
        tmp = sys.stdout
        sys.stdout = output_buffer
        # MAIN LOGIC
        with open(input_files[idx_file], "r") as input_file:
            n = int(input_file.readline())

            for i in range(n):
                result = "YES"
                input = input_file.readline().split()
                day = int(input[0])
                month = int(input[1])
                year = int(input[2])
                if day > 28:
                    if month == 2 and not is_leap_year(year):
                        result = "NO"
                    elif month == 2 and is_leap_year(year):
                        result = "YES" if day == 29 else "NO"
                    elif not has_31_days(month):
                        result = "NO" if day > 30 else "YES"
                print(result, end="\n" if i < n - 1 else "")
        # MAIN LOGIC END
        sys.stdout = tmp

        compare_outputs(output_files[idx_file], output_buffer)
    end = time()
    print(f'{end - begin} sec')
