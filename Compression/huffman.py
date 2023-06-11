#========================================
# Author     : Jiachen Xu
# Blog       : www.jiachenxu.net
# Time       : 2020-06-22 15:23:04
# Name       : huffman.py
# Version    : V1.0
#========================================


def huffman(str_dict):

    # str_dict = {string: probability}
    assert abs(sum(str_dict.values())-1.0) < 1e-6,  "The sum of probablities is not equal to 1."

    assert len(str_dict) >= 2, "The table contains less than two strings."
    
    # 1. Convergence?
    if len(str_dict) == 2:
        return dict(zip(str_dict.keys(), ['0', '1']))

    merged_str_dict = str_dict.copy()

    # 2. Find the pair of string with lowest probability
    str_1, str_2 = sorted(str_dict, key=str_dict.get)[:2]

    # 3. Merge into new string and compute the probability
    # 4. Update the dictionary (table)
    prob_str_1 = merged_str_dict.pop(str_1)
    prob_str_2 = merged_str_dict.pop(str_2)

    merged_str = str_1 + str_2
    merged_str_dict[merged_str] = prob_str_1 + prob_str_2

    # 5&6. Further construct the huffman tree and retrieve the huffman code for
    # this updated table

    huffman_code = huffman(merged_str_dict)
    
    # 7. Append 0& 1 to the huffman code for the updated table
    code_merged_str = huffman_code.pop(merged_str)
    huffman_code[str_1] = code_merged_str + '0'
    huffman_code[str_2] = code_merged_str + '1'

    return huffman_code


# import pdb;pdb.set_trace()
