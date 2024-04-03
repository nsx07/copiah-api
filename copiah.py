import re

def separate_sentences(text):
    '''This function receives a text and returns a list of sentences within the text.'''
    sentences = re.split(r'[.!?]+', text)
    if sentences[-1] == '' or sentences[-1] == None:
        del sentences[-1]
    return sentences

def separate_phrases(sentence):
    '''This function receives a sentence and returns a list of phrases within the sentence.'''
    return re.split(r'[,:;]+', sentence)

def separate_words(phrase):
    '''This function receives a phrase and returns a list of words within the phrase.'''
    return phrase.split()

def count_unique_words(word_list):
    '''This function receives a list of words and returns the number of words that appear only once.'''
    freq = dict()
    unique_words = 0
    for word in word_list:
        p = word.lower()
        if p in freq:
            if freq[p] == 1:
                unique_words -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unique_words += 1

    return unique_words

def count_different_words(word_list):
    '''This function receives a list of words and returns the number of different words used.'''
    freq = dict()
    for word in word_list:
        p = word.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def sentences_words(text):
    '''This function receives a text and returns the number of sentences and words.'''
    n_sentences = separate_sentences(text)
    n_phrases = []
    for sentence in n_sentences:
        n_phrases += (separate_phrases(sentence)) * 1
    n_words = []
    for phrase in n_phrases:
        n_words += (separate_words(phrase)) * 1
    return n_sentences, n_words

def average_word_length(text):
    '''This function receives a text and returns the average word length of the text.'''
    n_words = sentences_words(text)[1]
    count = 0
    for word in n_words:
        count += len(word)
    average = count / len(n_words)
    return average

def type_token_ratio(text):
    '''This function receives a text and returns the Type-Token ratio of the text.'''
    n_words = sentences_words(text)[1]
    ratio = count_different_words(n_words) / len(n_words)
    return ratio

def hapax_legomena_ratio(text):
    '''This function receives a text and returns the Hapax-Legomena ratio of the text.'''
    n_words = sentences_words(text)[1]
    ratio = count_unique_words(n_words) / len(n_words)
    return ratio

def average_sentence_length(text):
    '''This function receives a text and returns the average sentence length.'''
    n_sentences = separate_sentences(text)
    count = 0
    for sentence in n_sentences:
        count += len(sentence)
    average = count / len(n_sentences)
    return average

def sentence_complexity(text):
    '''This function receives a text and returns the sentence complexity.'''
    n_sentences = len(separate_sentences(text))
    n_phrases = len(sentences_words(text)[0])
    ratio = (n_phrases) / (n_sentences)
    return ratio

def average_phrase_length(text):
    '''This function receives a text and returns the average phrase length'''
    n_phrases = sentences_words(text)[0]
    count = 0
    for word in n_phrases:
        count += len(word)
    average = count / len(n_phrases)
    return average
    
def calculate_signature(text):
    '''This function receives a text and returns the signature of the text.'''
    
    average_word_l = average_word_length(text)
    type_token = type_token_ratio(text)
    hapax_legomena = hapax_legomena_ratio(text)
    average_sentence_l = average_sentence_length(text)
    sentence_c = sentence_complexity(text)
    average_phrase_l = average_phrase_length(text)
    
    return [average_word_l, type_token, hapax_legomena, average_sentence_l, sentence_c, average_phrase_l]

def compare_signatures(sig_a, sig_b):
    '''This function receives two text signatures and returns the degree of similarity between the signatures.'''
    count = 0
    for i in range(6):
        count += sig_b[i] - sig_a[i]
    count = abs(count)
    return count / 6
    
def evaluate_texts(texts, reference_signature):
    '''This function receives a list of texts and a reference signature and returns the number (1 to n) of the text with the highest probability of being infected by COH-PIAH.'''
    signatures = []
    for text in texts:
        sig = calculate_signature(text)
        signatures.append(compare_signatures(sig, reference_signature))
    lowest = signatures[0]
    text_id = 0
    for signature in signatures:
        if signature < lowest:
            lowest = signature
            text_id = signatures.index(signature)
    return text_id + 1
