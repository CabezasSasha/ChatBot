# chatbot solamente con py que sea una aplicación para pc, table y celu? que la infor la saque de un docx
# Python code for a chatbot application that retrieves information from a docx file
import docx
# Function to read the docx file and return the information
def read_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text
# Main function to run the chatbot
def chatbot():
    file_path = "path/to/docx/file.docx"  # Replace with the actual path to the docx file
    information = read_docx(file_path)
    # Rest of the chatbot logic goes here
    print("Chatbot application for retrieving information from a docx file")
# Entry point of the program
if __name__ == "__main__":
    chatbot()