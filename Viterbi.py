def make_trigrams(string):
        #
        return


class Viterbi(object):
    """Viterbi Model"""
    # @param possibleTags -
    #     set of all possible tags, *, and STOP
    #
    def __init__(self,
                 possible_tags):
        self.possible_tags = possible_tags

    # @param probabilities -
    #
    def learn_probabilities(self,
                            trigram_probabilities,
                            emission_probabilities):
        # TODO: learn this from training data
        self.trigram_probabilities = trigram_probabilities
        self.emission_probabilities = emission_probabilities

    def get_trigram_probability(self, trigram):
        return self.trigram_probabilities[trigram[0]][trigram[1]][trigram[2]]

    def get_emission_probability(self, word, tag):
        return self.emission_probabilities[word]

    def find_likelihood_of_tag_sequence(self, input_sequence, tag_sequence):
        # define probability = 1
        #
        # for each trigram, index in tag sequence,
        #     q_param = this.get_trigram_probability(trigram)
        #     current_word = input_sequence[index]
        #     current_tag = trigram[2]
        #     e_param = this.get_emission_probability(current_word, current_tag)
        #     probability *= q_param * e_param
        return probability

    def viterbify(self,
                  index,
                  tag_at_index,
                  tag_at_previous_index,
                  input):
        # clean input into a list of strings with beginning with *, *, ending with STOP
        # max
        # arg_max
        #
        # while index > 0
        #   for possible_tag in self.possible_tags
        #     trigram = (possible_tag, tag_at_previous_index, tag_at_index)
        #     recurse = viterbify(index - 1, tag_at_previous_index, possible_tag, )
        #     prob = recurse * get_trigram_probability(trigram) * get_emission_probability(input[index])
