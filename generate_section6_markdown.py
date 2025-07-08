

import os
import re

# Define paths
section_dir = '/mnt/c/Users/dev/Desktop/dev/FE/vibe_coding_project/section6'
text_file_name = 'section6 바이브코딩을 위한 필수 테크닉(손건).txt'
output_md_file_name = 'section6_강의_요약_통합본_최종.md'
images_dir_name = 'images'

text_file_path = os.path.join(section_dir, text_file_name)
images_path = os.path.join(section_dir, images_dir_name)
output_md_path = os.path.join(section_dir, output_md_file_name)

# Read the text file content
with open(text_file_path, 'r', encoding='utf-8') as f:
    text_content = f.readlines()

# Get sorted list of image files
image_files = sorted([f for f in os.listdir(images_path) if f.startswith('slide-') and f.endswith('.jpg')])

num_slides = len(image_files)
total_lines = len(text_content)
lines_per_slide = total_lines // num_slides

markdown_output = []

current_line_index = 0
for i in range(num_slides):
    slide_number = i + 1
    image_file = image_files[i]
    
    # Extract text for the current slide
    start_line = current_line_index
    end_line = start_line + lines_per_slide
    
    # Ensure the last slide gets all remaining lines
    if i == num_slides - 1:
        slide_text_lines = text_content[start_line:]
    else:
        slide_text_lines = text_content[start_line:end_line]
    
    slide_text = "".join(slide_text_lines).strip()

    # Construct markdown for the slide
    markdown_output.append(f"## Slide {slide_number}")
    markdown_output.append(f"![{image_file}](images/{image_file})")
    markdown_output.append("") # Empty line for spacing
    markdown_output.append("---")
    markdown_output.append("") # Empty line for spacing
    markdown_output.append("**녹취록 내용:**")
    markdown_output.append(f"> {slide_text.replace('\n', '\n> ')}") # Format as blockquote
    markdown_output.append("") # Empty line for spacing

    current_line_index = end_line

# Write the markdown content to the output file
with open(output_md_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(markdown_output))

print(f"Generated markdown file: {output_md_file_name}")

