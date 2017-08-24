import copy
import sys


class Parser():

    def __init__(self, file):
        self.file = file
        self.data = self.get_data_from_file()
        self.number_of_tags = self.get_number_of_tags()
        self.all_tags = self.get_tags()
        self.tag_variables_in_dict = self.get_variables_from_tags()
        self.queries_in_list = self.get_queries_in_list()
        self.answers = self.check_if_queries_exist_in_tags()


    def get_data_from_file(self):
        with open(self.file) as f:
            return [s.strip() for s in f.readlines()]

    def get_tags(self):
        return self.data[1 : self.get_number_of_tags() + 1]

    def get_number_of_tags(self):
        return int(self.data[0][0])

    def get_queries_in_list(self):
        return self.data[self.get_number_of_tags() + 1:]

    def get_variables_from_tags(self):
        tags = {}
        for i in range(len(self.all_tags) - 1):
            if not self.is_opening_tag(self.all_tags[i + 1]):
                tags.update(self.get_not_nested_tags_names_and_variables(i))
            else:
                tags.update(self.get_nested_tags_names_and_variables(i))

        return tags

    def get_not_nested_tags_names_and_variables(self, i):
        return self.get_tag_variables_with_values(self.all_tags[i])


    def get_nested_tags_names_and_variables(self, i):
        tags = {}
        current_tag = ''
        while self.is_opening_tag(self.all_tags[i]):
            if self.is_opening_tag(self.all_tags[i + 1]):
                current_tag += self.get_current_tag_name_as_string(self.all_tags[i])
                tags.update(self.get_tag_variables_with_values(self.all_tags[i]))
                current_tag += '.'
            else:
                variables_names = self.get_tag_variables_with_values(self.all_tags[i])
                temp_v_n = copy.deepcopy(variables_names)
                for k, v in variables_names.items():
                    temp_v_n[current_tag + k] = v
                tags.update(temp_v_n)
            i += 1
        return tags


    def get_current_tag_name_as_string(self, tag):
        return tag.split()[0][1:]

    def get_tag_variables_with_values(self, current_tag):
        current_tag = current_tag.split()
        tag_number = current_tag[0][1:]
        tags_in_dict = {}
        for i in range(1, len(current_tag), 3):
            name = current_tag[i].replace('"', '')
            value = current_tag[i + 2].replace('"', '').replace('>', '')
            tags_in_dict[tag_number + '~' + name] = value

        return tags_in_dict

    def is_opening_tag(self, tag):
        return True if tag[1] != '/' else False

    def check_if_queries_exist_in_tags(self):
        return [self.tag_variables_in_dict[q] if q in self.tag_variables_in_dict else 'Not Found!' for q in self.queries_in_list]



if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'file.txt'

    parser = Parser(filename)
    print(parser.answers)




