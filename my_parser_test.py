import unittest
from my_parser import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        self.file = 'file.txt'
        self.data = ['4 3', '<tag1 value = "HelloWorld">', '<tag2 name = "Name1">', '</tag2>', '</tag1>',
                     'tag1.tag2~name', 'tag1~name', 'tag1~value']
        self.number_of_tags = 4
        self.number_of_queries = 3

        self.tags = ['<tag1 value = "HelloWorld">', '<tag2 name = "Name1">', '</tag2>', '</tag1>']
        self.tag1_parsed = {'tag1~value': 'HelloWorld'}
        self.tag1_name = 'tag1'

        self.tags_all_parsed = {'tag1~value': 'HelloWorld', 'tag1.tag2~name': 'Name1', 'tag2~name': 'Name1'}

        self.queries = ['tag1.tag2~name', 'tag1~name', 'tag1~value']
        self.queries_answers = ['Name1', 'Not Found!', 'HelloWorld']

        self.Parser = Parser(self.file)


    def test_get_data_from_file(self):
        self.assertEqual(self.data, self.Parser.data)

    def test_get_number_of_tags(self):
        self.assertEqual(self.number_of_tags, self.Parser.number_of_tags)

    def test_get_tags(self):
        self.assertEqual(self.data[1:5], self.Parser.all_tags)

    def test_get_queries(self):
        self.assertEqual(self.data[5:], self.Parser.queries_in_list)

    def test_get_variables_from_tags(self):
        self.assertEqual(self.tags_all_parsed, self.Parser.get_variables_from_tags())

    def test_get_not_nested_tags_names_and_variables(self):
        self.assertEqual(self.tag1_parsed, self.Parser.get_not_nested_tags_names_and_variables(0))

    def test_get_nested_tags_names_and_variables(self):
        self.assertEqual(self.tags_all_parsed, self.Parser.get_nested_tags_names_and_variables(0))

    def test_get_current_tag_name_as_string(self):
        self.assertEqual(self.tag1_name, self.Parser.get_current_tag_name_as_string(self.tags[0]))

    def test_get_tag_variables_with_values(self):
        self.assertEqual(self.tag1_parsed, self.Parser.get_tag_variables_with_values(self.tags[0]))

    def test_is_opening_tag(self):
        self.assertEqual(True, self.Parser.is_opening_tag(self.tags[0]))

    def test_check_if_queries_exist_in_tags(self):
        self.assertEqual(self.queries_answers, self.Parser.check_if_queries_exist_in_tags())


if __name__=='__main__':
    unittest.main(verbosity=2)