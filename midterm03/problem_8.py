from bin_id3 import bin_id3

if __name__ == '__main__':
    examples, attribs = bin_id3.parse_csv_file_into_examples('problem_8_1.csv')
    avt = bin_id3.construct_attrib_values_from_examples(examples, attribs)

    print(bin_id3.entropy(examples, 'PlayTennis', avt))


    examples, attribs = bin_id3.parse_csv_file_into_examples('problem_8_2.csv')
    avt = bin_id3.construct_attrib_values_from_examples(examples, attribs)

    print(bin_id3.entropy(examples, 'PlayTennis', avt))


    examples, attribs = bin_id3.parse_csv_file_into_examples('problem_8_1.csv')
    avt = bin_id3.construct_attrib_values_from_examples(examples, attribs)

    print(bin_id3.gain(examples, 'PlayTennis', 'Wind', avt))
    print(bin_id3.gain(examples, 'PlayTennis', 'Humidity', avt))