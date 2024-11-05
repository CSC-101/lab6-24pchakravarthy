import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books1(self):
        books = [data.Book(["Author C"], "Book C"), data.Book(["Author Z"], "Book Z"), data.Book(["Author A"], "Book A")]
        lab6.selection_sort_books(books)
        self.assertEqual(books, [data.Book(['Author A'], 'Book A'), data.Book(['Author C'], 'Book C'), data.Book(['Author Z'], 'Book Z')])

    def test_selection_sort_books2(self):
        books = []
        lab6.selection_sort_books(books)
        self.assertEqual(books, [])


    # Part 2
    def test_swap_case1(self):
        x1 = lab6.swap_case("Hello World234!")
        self.assertEqual(x1, "hELLO wORLD234!")

    def test_swap_case2(self):
        x2 = lab6.swap_case("I LoVE ćS")
        self.assertEqual(x2, "i lOve Ćs")

    # Part 3
    def test_str_translate1(self):
        s1 = lab6.str_translate("help", "e", "a")
        self.assertEqual(s1, "halp")

    def test_str_translate2(self):
        s1 = lab6.str_translate("banana", "a", "e")
        self.assertEqual(s1, "benene")

    def test_str_translate3(self):
        s1 = lab6.str_translate("scream", "p", "a")
        self.assertEqual(s1, "scream")
    # Part 4
    def test_histogram1(self):
        h1 = lab6.histogram("i love the book because it is the best")
        self.assertEqual(h1, {'i': 1, 'love': 1, 'the': 2, 'book': 1, 'because': 1, 'it': 1, 'is': 1, 'best': 1})

    def test_histogram2(self):
        h2 = lab6.histogram("repeat repeat not repeat repeat not repeat")
        self.assertEqual(h2, {'repeat': 5, 'not': 2})






if __name__ == '__main__':
    unittest.main()
