def getWordCount(s):
    return len(s.split())

if __name__ == '__main__':
    print('Enter a sentence: ', '')
    s = input()
    print('Your sentence contained {} words.'.format(getWordCount(s)))