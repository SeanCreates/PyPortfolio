#A programme that reads a file and counts the number of words in it
#File I/O
#File Input/Output
def count_words(filename: str):
    """Reads the file, counts the words and brings back the total"""
    try:
        #use with open to ensure safe file handling : ensures the file is automatically closed
        with open(filename, "r") as file:
            #read the entire content into a single string
            text = file.read()
            #handle the empty file case
        if not text:
            return 0

        #3.split the text into a list of words
        #Split sees whitespaces as separators by default
        words =text.split()

        #wordcount
        word_count = len(words)
        return word_count
    except FileNotFoundError:
        print(f"The file {filename} was not found. Check path.")
        return -1

def main():
    input_filename = '/Users/seaniceochieng/PycharmProjects/ML/PyPortfolio/RSRCS/sampletext'
    total_words = count_words(input_filename)

    if total_words >= 0:
        print(f"Successfully counted the words in '{input_filename}'!")
        print (f"The Total Word Count is : {total_words}")

if __name__ == "__main__":
    main()


