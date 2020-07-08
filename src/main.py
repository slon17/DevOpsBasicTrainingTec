import extractor
import os
#this only run if the file is executed as python main.py
#won't run when it is imported in other file
if __name__ == "__main__":
    
    #Load the html file to webscrap
    #__file__ is the full path to where the script you are running is located.
    script_dir = os.path.dirname(__file__)
    relative_html_file_path = "Assets/DevOps-Wikipedia.html"
    html_file_path = os.path.join(script_dir, relative_html_file_path)
    f = open(html_file_path,"r")

    html_text = f.read()
    text = extractor.text_from_html(html_text)
    print("html-text----------------------------------------------")
    print(html_text[:100])
    print("raw-text-----------------------------------------------")
    print(text[:100])
    #print("raw-text-len-------------------------------------------")
    #print(len(text))
    print("-------------------------------------------------------")
    print("DevOps count", extractor.count_devops(text))
    print("-------------------------------------------------------")
    image = extractor.create_word_cloud_npArray(text)
    print("Cloud shape: ", image.shape)
    print("-------------------------------------------------------")
    extractor.create_word_cloud_image(text, "devops_word_cloud")
    print("Image saved...")
