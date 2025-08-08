#  Project 1: Word Length Filter (Beginner Level)
# 🎯 Objective:
# From a list of words, filter only those with more than 5 characters using list comprehension.
# 📂 Requirements:
# List of words
# Use list comprehension to:
# Filter words longer than 5 characters
# Count their lengths

class Word:
    def __init__(self , word_list ):
        self.list = word_list 
    
    def filterlen(self):
        longWord = [word for word in self.list if len(word) >= 5]
        lenOfWord = [len(lenWord) for lenWord in longWord]
        return longWord,lenOfWord

handler = Word(["machine", "ai", "data", "analytics", "python", "ml", "learning"])
handler.filterlen()

