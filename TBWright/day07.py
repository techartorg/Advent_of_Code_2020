"""

"""


def get_chunks(content_list):
    for i in range(0, len(content_list), 4):
        yield content_list[i:i+4]


input_list = [line.rstrip('.').replace('bags', 'bag').replace(' contain ', ' ').replace(',', '') for line in open("inputs/day7_input.txt", "r").read().splitlines()]
input_dicts = []
for _input in input_list:
    inputs = _input.split(' ')
    entry_dict = dict()
    entry_dict['bag type'] = ' '.join(inputs[:3])
    contents = list(get_chunks(inputs[3:]))
    entry_dict['contents'] = [{'quant': content[0], 'content type': ' '.join(content[-3:])} for content in contents if content[0] != 'no']
    input_dicts.append(entry_dict)
# print(input_dicts)

# all_bags = set([bag_type['bag type'] for bag_type in input_dicts])
# print(len(all_bags))


def search_for_bag_type(bags_list, bag_type, container_bags):
    """

    :param bags_list:
    :type bags_list: list[dict]
    :param bag_type:
    :type bag_type: str
    :return: the itr number
    :rtype:
    """
    outer_bags = set()
    for bag_dict in bags_list:  # type: dict
        for content in bag_dict['contents']:
            if content['content type'] == bag_type:
                outer_bags.add(bag_dict['bag type'])
    container_bags.update(outer_bags)
    for outer_bag in outer_bags:
        container_bags.update(search_for_bag_type(bags_list, outer_bag, container_bags))
    return container_bags


def count_all_inner_bags(bag_dict):
    itr = 0
    for content in bag_dict['contents']:
        print(content)
        itr += int(content['quant'])
        inner_bag_dict = [bag_type for bag_type in input_dicts if bag_type['bag type'] == content['content type']][0]
        itr += count_all_inner_bags(inner_bag_dict) * int(content['quant'])
    return itr


shiny_gold_dict = [shiny_gold for shiny_gold in input_dicts if shiny_gold['bag type'] == 'shiny gold bag'][0]
print(len(search_for_bag_type(input_dicts, 'shiny gold bag', set())))
print(count_all_inner_bags(shiny_gold_dict))

